"""Trocea texto extraído en chunks semánticos con metadata de asignatura/tema/página."""
from pathlib import Path

TARGET_CHUNK_CHARS = 1200


def derive_metadata(path: Path, raw_root: Path) -> dict:
    rel_parts = path.relative_to(raw_root).parts
    # raw/Estudio2carrera/<cuatri>/<asignatura>/[.../]<archivo>
    cuatri = rel_parts[1] if len(rel_parts) > 1 else None
    asignatura_raw = rel_parts[2] if len(rel_parts) > 2 else None
    asignatura = asignatura_raw.lower().replace(" ", "-") if asignatura_raw else None
    tema = rel_parts[-2] if len(rel_parts) > 4 else None
    return {
        "asignatura": asignatura,
        "curso": cuatri,
        "tema": tema,
        "fuente": str(path.relative_to(raw_root)),
    }


def _split_paragraphs(text: str) -> list[str]:
    return [p.strip() for p in text.split("\n\n") if p.strip()]


def chunk_page(text: str) -> list[str]:
    """Agrupa párrafos de una página en chunks de ~TARGET_CHUNK_CHARS, sin partir párrafos."""
    paragraphs = _split_paragraphs(text)
    if not paragraphs:
        return []

    chunks, current = [], ""
    for para in paragraphs:
        if current and len(current) + len(para) + 2 > TARGET_CHUNK_CHARS:
            chunks.append(current)
            current = para
        else:
            current = f"{current}\n\n{para}" if current else para
    if current:
        chunks.append(current)
    return chunks


def build_chunks(pages: list[dict], base_metadata: dict) -> list[dict]:
    """pages: [{"page": int|None, "text": str}, ...] -> lista de chunks con metadata completa."""
    chunks = []
    for page in pages:
        for i, chunk_text in enumerate(chunk_page(page["text"])):
            chunks.append({
                "text": chunk_text,
                "pagina": page["page"],
                "chunk_index": i,
                **base_metadata,
            })
    return chunks
