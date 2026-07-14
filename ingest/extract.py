"""PDF/imagen/docx -> texto por página, con OCR de fórmulas vía MinerU (local, gratis)."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from docx import Document

SUPPORTED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png", ".docx"}
MINERU_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}
MINERU_TIMEOUT_SECONDS = 1800


class ExtractionError(RuntimeError):
    pass


def _mineru_bin() -> Path:
    return Path(sys.executable).parent / "mineru"


def _block_text(block: dict) -> str:
    block_type = block.get("type")
    if block_type in ("text", "equation"):
        return block.get("text", "")
    if block_type == "table":
        return block.get("table_body") or block.get("text", "")
    if block_type == "image":
        captions = block.get("img_caption") or block.get("image_caption") or []
        return "\n".join(captions)
    return block.get("text", "")


def _find_content_list(output_dir: Path) -> Path:
    matches = list(output_dir.rglob("*_content_list.json"))
    if not matches:
        raise ExtractionError(f"MinerU no generó content_list.json en {output_dir}")
    return matches[0]


def _run_mineru(path: Path) -> list[dict]:
    with tempfile.TemporaryDirectory() as tmp_dir:
        result = subprocess.run(
            [str(_mineru_bin()), "-p", str(path), "-o", tmp_dir, "-b", "pipeline"],
            capture_output=True,
            text=True,
            timeout=MINERU_TIMEOUT_SECONDS,
        )
        if result.returncode != 0:
            raise ExtractionError(f"MinerU falló procesando {path}: {result.stderr[-2000:]}")

        blocks = json.loads(_find_content_list(Path(tmp_dir)).read_text())

    pages: dict[int, list[str]] = {}
    for block in blocks:
        text = _block_text(block).strip()
        if not text:
            continue
        page_idx = block.get("page_idx", 0)
        pages.setdefault(page_idx, []).append(text)

    return [{"page": idx + 1, "text": "\n\n".join(texts)} for idx, texts in sorted(pages.items())]


def _extract_docx(path: Path) -> list[dict]:
    doc = Document(path)
    text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    return [{"page": None, "text": text}] if text.strip() else []


def extract_pages(path: Path) -> list[dict]:
    """Devuelve [{"page": int|None, "text": str}, ...] para un fichero soportado."""
    suffix = path.suffix.lower()
    if suffix in MINERU_EXTENSIONS:
        return _run_mineru(path)
    if suffix == ".docx":
        return _extract_docx(path)
    raise ExtractionError(f"Extensión no soportada: {suffix} ({path})")
