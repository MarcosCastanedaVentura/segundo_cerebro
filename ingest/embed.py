"""Embeddings de chunks (OpenAI) + upsert a la colección única de Chroma en index/."""
import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

INDEX_DIR = Path(__file__).resolve().parent.parent / "index"
COLLECTION_NAME = "segundo_cerebro"
EMBEDDING_MODEL = "text-embedding-3-small"
BATCH_SIZE = 100

_openai_client = None


def _get_openai_client() -> OpenAI:
    global _openai_client
    if _openai_client is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("Falta OPENAI_API_KEY en .env (copia .env.example y rellénalo).")
        _openai_client = OpenAI(api_key=api_key)
    return _openai_client


def get_collection():
    client = chromadb.PersistentClient(path=str(INDEX_DIR))
    return client.get_or_create_collection(COLLECTION_NAME)


def _embed_texts(texts: list[str]) -> list[list[float]]:
    client = _get_openai_client()
    vectors = []
    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i : i + BATCH_SIZE]
        resp = client.embeddings.create(model=EMBEDDING_MODEL, input=batch)
        vectors.extend(item.embedding for item in resp.data)
    return vectors


def upsert_chunks(chunks: list[dict], fuente: str) -> int:
    """Borra los chunks previos de `fuente` (si los había) e inserta los nuevos."""
    collection = get_collection()
    collection.delete(where={"fuente": fuente})
    if not chunks:
        return 0

    ids = [f"{c['fuente']}::p{c['pagina']}::c{c['chunk_index']}" for c in chunks]
    texts = [c["text"] for c in chunks]
    metadatas = [
        {
            "asignatura": c["asignatura"] or "",
            "curso": c["curso"] or "",
            "tema": c["tema"] or "",
            "fuente": c["fuente"],
            "pagina": c["pagina"] if c["pagina"] is not None else -1,
        }
        for c in chunks
    ]
    embeddings = _embed_texts(texts)
    collection.add(ids=ids, embeddings=embeddings, documents=texts, metadatas=metadatas)
    return len(chunks)
