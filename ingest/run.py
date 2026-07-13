"""Orquesta extract -> chunk -> embed sobre raw/, con manifest incremental.

Uso:
    python3 ingest/run.py                              # ingesta todo raw/, solo lo nuevo/modificado
    python3 ingest/run.py --path "Estudio2carrera/1 cuatri/electrotecnia"   # piloto en una carpeta
    python3 ingest/run.py --force                       # reprocesa todo, ignorando el manifest
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import chunk as chunk_mod
import embed as embed_mod
import extract as extract_mod

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_ROOT = PROJECT_ROOT / "raw"
MANIFEST_PATH = PROJECT_ROOT / "index" / "manifest.json"


def _file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def _load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text())
    return {}


def _save_manifest(manifest: dict) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = MANIFEST_PATH.with_suffix(".json.tmp")
    tmp_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True))
    tmp_path.replace(MANIFEST_PATH)


def _iter_candidate_files(scope: Path):
    for path in sorted(scope.rglob("*")):
        if path.is_file() and path.suffix.lower() in extract_mod.SUPPORTED_EXTENSIONS:
            yield path


def run(scope: Path, force: bool) -> None:
    manifest = _load_manifest()
    nuevos, actualizados, sin_cambios, fallos = [], [], [], []

    for path in _iter_candidate_files(scope):
        key = str(path.relative_to(RAW_ROOT))
        file_hash = _file_hash(path)
        previous = manifest.get(key)

        if not force and previous and previous["hash"] == file_hash:
            sin_cambios.append(key)
            continue

        try:
            pages = extract_mod.extract_pages(path)
            metadata = chunk_mod.derive_metadata(path, RAW_ROOT)
            chunks = chunk_mod.build_chunks(pages, metadata)
            n_chunks = embed_mod.upsert_chunks(chunks, metadata["fuente"])
        except Exception as e:
            print(f"  [FALLO] {key}: {e}")
            fallos.append(key)
            continue

        manifest[key] = {
            "hash": file_hash,
            "indexed_at": datetime.now(timezone.utc).isoformat(),
            "paginas": len(pages),
            "chunks": n_chunks,
        }
        _save_manifest(manifest)

        if previous:
            actualizados.append(key)
            print(f"  [ACTUALIZADO] {key} ({len(pages)} páginas, {n_chunks} chunks)")
        else:
            nuevos.append(key)
            print(f"  [NUEVO] {key} ({len(pages)} páginas, {n_chunks} chunks)")

    print()
    print(f"Nuevos: {len(nuevos)} | Actualizados: {len(actualizados)} | "
          f"Sin cambios: {len(sin_cambios)} | Fallos: {len(fallos)}")
    if fallos:
        print("Ficheros con fallo (revisa .env / conexión / logs arriba):")
        for f in fallos:
            print(f"  - {f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Carpeta dentro de raw/ a la que limitar la ingesta (piloto)")
    parser.add_argument("--force", action="store_true", help="Reprocesa aunque no haya cambiado el hash")
    args = parser.parse_args()

    scope = (RAW_ROOT / args.path) if args.path else RAW_ROOT
    if not scope.exists():
        print(f"No existe la ruta: {scope}")
        sys.exit(1)

    run(scope, args.force)
