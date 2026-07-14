"""Auditoría mecánica de higiene del wiki: wikilinks sin resolver, notas sin fuente,
posibles duplicados y carpetas sobrecargadas. Solo detecta — no corrige ni borra nada.

Uso: .venv/bin/python tools/wiki_health.py
"""
import re
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

import yaml

WIKI_ROOT = Path(__file__).resolve().parent.parent / "wiki"
EXCLUDED_DIRS = {"_templates"}
CONCEPTO_TYPES = {"concepto", "formula", "procedimiento", "practica"}
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
DUPLICATE_THRESHOLD = 0.6


def iter_notes():
    for path in sorted(WIKI_ROOT.rglob("*.md")):
        if EXCLUDED_DIRS & set(path.relative_to(WIKI_ROOT).parts):
            continue
        yield path


def parse_note(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        frontmatter = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        frontmatter = {}
    return frontmatter, parts[2]


def extract_links(frontmatter: dict, body: str) -> set[str]:
    links = set(WIKILINK_RE.findall(body))
    links.update(frontmatter.get("relacionado") or [])
    return links


def build_stem_index() -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = defaultdict(list)
    for path in iter_notes():
        index[path.stem].append(path)
    return index


def resolve_link(target: str, source_path: Path, stem_index: dict) -> bool:
    target = target.strip()
    if target.split("/")[-1] in stem_index:
        return True
    if (WIKI_ROOT / f"{target}.md").exists():
        return True
    candidate = (source_path.parent / f"{target}.md").resolve()
    try:
        candidate.relative_to(WIKI_ROOT.resolve())
    except ValueError:
        return False
    return candidate.exists()


def check_broken_links() -> list[tuple[str, str]]:
    stem_index = build_stem_index()
    findings = []
    for path in iter_notes():
        frontmatter, body = parse_note(path)
        for link in sorted(extract_links(frontmatter, body)):
            if not resolve_link(link, path, stem_index):
                findings.append((str(path.relative_to(WIKI_ROOT)), link))
    return findings


def check_missing_fuente() -> list[str]:
    findings = []
    for path in iter_notes():
        frontmatter, _ = parse_note(path)
        if frontmatter.get("tipo") not in CONCEPTO_TYPES:
            continue
        if not frontmatter.get("fuente"):
            findings.append(str(path.relative_to(WIKI_ROOT)))
    return findings


def check_duplicates() -> list[tuple[str, str, float]]:
    notes = [(path, parse_note(path)[1]) for path in iter_notes()]
    findings = []
    for i in range(len(notes)):
        path_a, body_a = notes[i]
        for path_b, body_b in notes[i + 1 :]:
            if path_a.parent != path_b.parent:
                continue
            ratio = SequenceMatcher(None, body_a, body_b).ratio()
            if ratio >= DUPLICATE_THRESHOLD:
                findings.append((str(path_a.relative_to(WIKI_ROOT)), str(path_b.relative_to(WIKI_ROOT)), ratio))
    return findings


def check_oversized_folders() -> list[tuple[str, int]]:
    counts: dict[str, int] = defaultdict(int)
    for path in iter_notes():
        parts = path.relative_to(WIKI_ROOT).parts
        if len(parts) > 1:
            counts[parts[0]] += 1
    if not counts:
        return []
    values = sorted(counts.values())
    median = values[len(values) // 2]
    threshold = max(median * 2, median + 8)
    return sorted((f, n) for f, n in counts.items() if n > threshold)


def main() -> None:
    print("=== Wikilinks sin resolver (huecos / posibles temas por crear) ===")
    broken = check_broken_links()
    print("Ninguno." if not broken else "")
    for source, link in broken:
        print(f"  {source} -> [[{link}]]")

    print("\n=== Notas de tipo concepto sin frontmatter 'fuente' ===")
    missing = check_missing_fuente()
    print("Ninguna." if not missing else "")
    for note in missing:
        print(f"  {note}")

    print(f"\n=== Posibles duplicados (misma carpeta, similitud >= {DUPLICATE_THRESHOLD:.0%}) ===")
    dups = check_duplicates()
    print("Ninguno." if not dups else "")
    for a, b, ratio in dups:
        print(f"  {a} <-> {b} ({ratio:.0%})")

    print("\n=== Carpetas con muchas más notas que la mediana ===")
    oversized = check_oversized_folders()
    print("Ninguna." if not oversized else "")
    for folder, n in oversized:
        print(f"  {folder}: {n} notas")


if __name__ == "__main__":
    main()
