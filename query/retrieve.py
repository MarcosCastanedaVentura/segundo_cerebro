"""Búsqueda semántica sobre la colección única de Chroma (todo raw/, filtrable por metadata).

Uso:
    python3 query/retrieve.py "¿qué es el ciclo de Krebs?"
    python3 query/retrieve.py "triángulo de potencias" --asignatura electrotecnia --top-k 8
    python3 query/retrieve.py "..." --json
"""
import argparse
import json
import os
import sys
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

INDEX_DIR = Path(__file__).resolve().parent.parent / "index"
COLLECTION_NAME = "segundo_cerebro"
EMBEDDING_MODEL = "text-embedding-3-small"


def _get_collection():
    client = chromadb.PersistentClient(path=str(INDEX_DIR))
    return client.get_or_create_collection(COLLECTION_NAME)


def _embed_query(text: str) -> list[float]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Falta OPENAI_API_KEY en .env (copia .env.example y rellénalo).")
    client = OpenAI(api_key=api_key)
    resp = client.embeddings.create(model=EMBEDDING_MODEL, input=[text])
    return resp.data[0].embedding


def retrieve(query: str, asignatura: str | None = None, tema: str | None = None, top_k: int = 6) -> list[dict]:
    collection = _get_collection()
    where = None
    conditions = []
    if asignatura:
        conditions.append({"asignatura": asignatura.lower().replace(" ", "-")})
    if tema:
        conditions.append({"tema": tema})
    if len(conditions) == 1:
        where = conditions[0]
    elif len(conditions) > 1:
        where = {"$and": conditions}

    query_embedding = _embed_query(query)
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where=where,
    )

    hits = []
    for text, meta, distance in zip(
        result["documents"][0], result["metadatas"][0], result["distances"][0]
    ):
        hits.append({
            "text": text,
            "asignatura": meta.get("asignatura"),
            "curso": meta.get("curso"),
            "tema": meta.get("tema"),
            "fuente": meta.get("fuente"),
            "pagina": meta.get("pagina"),
            "distance": distance,
        })
    return hits


def _format_citation(hit: dict) -> str:
    pagina = hit["pagina"]
    pagina_str = f"p.{pagina}" if pagina not in (None, -1) else "sin página"
    tema = f" · {hit['tema']}" if hit.get("tema") else ""
    return f"{hit['asignatura']}{tema} · {hit['fuente']} · {pagina_str}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--asignatura", default=None)
    parser.add_argument("--tema", default=None)
    parser.add_argument("--top-k", type=int, default=6)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        hits = retrieve(args.query, args.asignatura, args.tema, args.top_k)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(hits, indent=2, ensure_ascii=False))
    else:
        if not hits:
            print("Sin resultados.")
        for hit in hits:
            print(f"--- {_format_citation(hit)} (distancia {hit['distance']:.3f}) ---")
            print(hit["text"])
            print()
