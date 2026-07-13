"""PDF/imagen/docx -> texto por página, con OCR de fórmulas vía Mathpix."""
import base64
import os
import time
from pathlib import Path

import requests
from docx import Document
from dotenv import load_dotenv

load_dotenv()

MATHPIX_APP_ID = os.environ.get("MATHPIX_APP_ID")
MATHPIX_APP_KEY = os.environ.get("MATHPIX_APP_KEY")
MATHPIX_HEADERS = {"app_id": MATHPIX_APP_ID or "", "app_key": MATHPIX_APP_KEY or ""}

SUPPORTED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png", ".docx"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


class ExtractionError(RuntimeError):
    pass


def _require_mathpix_credentials():
    if not MATHPIX_APP_ID or not MATHPIX_APP_KEY:
        raise ExtractionError(
            "Faltan MATHPIX_APP_ID / MATHPIX_APP_KEY en .env (copia .env.example y rellénalo)."
        )


def _extract_pdf(path: Path) -> list[dict]:
    _require_mathpix_credentials()
    with open(path, "rb") as f:
        resp = requests.post(
            "https://api.mathpix.com/v3/pdf",
            headers=MATHPIX_HEADERS,
            files={"file": f},
            data={"options_json": '{"conversion_formats": {"md": true}}'},
            timeout=60,
        )
    resp.raise_for_status()
    pdf_id = resp.json()["pdf_id"]

    for _ in range(120):
        status_resp = requests.get(
            f"https://api.mathpix.com/v3/pdf/{pdf_id}", headers=MATHPIX_HEADERS, timeout=30
        )
        status_resp.raise_for_status()
        status = status_resp.json().get("status")
        if status == "completed":
            break
        if status == "error":
            raise ExtractionError(f"Mathpix devolvió error procesando {path}: {status_resp.json()}")
        time.sleep(5)
    else:
        raise ExtractionError(f"Timeout esperando a Mathpix para {path} (pdf_id={pdf_id})")

    lines_resp = requests.get(
        f"https://api.mathpix.com/v3/pdf/{pdf_id}.lines.mmd.json", headers=MATHPIX_HEADERS, timeout=30
    )
    lines_resp.raise_for_status()
    data = lines_resp.json()

    # Esquema de v3/pdf/{id}.lines.mmd.json no verificado contra una respuesta real todavía
    # (sin credenciales al escribir esto) — si Mathpix cambia las claves, este es el sitio a ajustar.
    pages_raw = data.get("pages")
    if pages_raw is None:
        raise ExtractionError(
            f"Respuesta de Mathpix sin campo 'pages' para {path}. Claves recibidas: {list(data.keys())}"
        )

    pages = []
    for page in pages_raw:
        page_num = page.get("page", page.get("page_idx", len(pages) + 1))
        lines = page.get("lines", [])
        text = "\n".join(line.get("text", "") for line in lines if line.get("text"))
        if text.strip():
            pages.append({"page": page_num, "text": text})
    return pages


def _extract_image(path: Path) -> list[dict]:
    _require_mathpix_credentials()
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    resp = requests.post(
        "https://api.mathpix.com/v3/text",
        headers={**MATHPIX_HEADERS, "Content-Type": "application/json"},
        json={"src": f"data:{mime};base64,{b64}", "formats": ["text"]},
        timeout=60,
    )
    resp.raise_for_status()
    text = resp.json().get("text", "")
    return [{"page": None, "text": text}] if text.strip() else []


def _extract_docx(path: Path) -> list[dict]:
    doc = Document(path)
    text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    return [{"page": None, "text": text}] if text.strip() else []


def extract_pages(path: Path) -> list[dict]:
    """Devuelve [{"page": int|None, "text": str}, ...] para un fichero soportado."""
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return _extract_pdf(path)
    if suffix in IMAGE_EXTENSIONS:
        return _extract_image(path)
    if suffix == ".docx":
        return _extract_docx(path)
    raise ExtractionError(f"Extensión no soportada: {suffix} ({path})")
