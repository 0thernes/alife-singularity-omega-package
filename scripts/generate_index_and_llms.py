#!/usr/bin/env python3
"""Generate complete repository Master INDEX.md (folder/file/bytes/approx-tokens) and llms-full.txt."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", "__pycache__", ".lake", ".venv", "venv", ".pytest_cache", ".ruff_cache", ".mypy_cache", ".hypothesis", "build", "_site", ".v3_source_baseline"}
TEXT_EXTS = {".md", ".py", ".lean", ".tex", ".bib", ".yml", ".yaml", ".json", ".toml", ".txt", ".cff", ".csv", ".tsv", ".sh", ".ps1", ".mdc", ".xml", ".html"}

LLMS_FULL_SOURCES = [
    "README.md",
    "AGENTS.md",
    "CLAIMS.md",
    "EVIDENCE.md",
    "LIMITATIONS.md",
    "VERIFICATION.md",
    "REPLICATION.md",
    "PREREGISTRATION.md",
    "HARDENING_LOG.md",
    "docs/statement-fidelity.md",
    "docs/AI_DISCLOSURE.md",
    "reports/09_MEGA_ATLAS_1900_OPEN_PROBLEMS_CROSSCHECK.md",
    "results/lean_package_axioms.txt",
]


def _should_skip(p: Path) -> bool:
    rel_parts = p.relative_to(ROOT).parts
    if any(part in SKIP_DIRS for part in rel_parts):
        return True
    if p.name.endswith(".zip") or p.name.startswith("_tmp_") or p.name == "audit.json":
        return True
    return False


def main() -> None:
    files = sorted(p for p in ROOT.rglob("*") if p.is_file() and not _should_skip(p))
    by_folder: dict[str, list[Path]] = defaultdict(list)
    total_bytes = 0
    total_tokens_est = 0

    for f in files:
        rel = f.relative_to(ROOT)
        folder = rel.parts[0] if len(rel.parts) > 1 else "(root)"
        by_folder[folder].append(f)
        total_bytes += f.stat().st_size

    lines = [
        "# Master Repository Index & Table of Contents (`v3.4.0`)",
        "",
        "Complete folder-by-folder, file-by-file inventory with exact byte sizes, line counts (text files), and approximate token counts (`~chars / 4`). Regenerate via `python scripts/generate_index_and_llms.py`.",
        "",
        "## Folder Summary",
        "",
        "| Folder | Files | Total Size (KB) |",
        "| :--- | :---: | :---: |",
    ]
    for folder in sorted(by_folder.keys(), key=lambda x: (x != "(root)", x)):
        flist = by_folder[folder]
        fbytes = sum(x.stat().st_size for x in flist)
        lines.append(f"| `{folder}` | `{len(flist)}` | `{fbytes / 1024:.1f}` |")
    lines += [
        f"| **TOTAL** | **`{len(files)}`** | **`{total_bytes / 1024:.1f}`** |",
        "",
        "## Complete File Inventory",
        "",
    ]

    for folder in sorted(by_folder.keys(), key=lambda x: (x != "(root)", x)):
        lines.append(f"### `{folder}`")
        lines.append("")
        lines.append("| File | Size (B) | Lines | Approx Tokens |")
        lines.append("| :--- | :---: | :---: | :---: |")
        for f in by_folder[folder]:
            rel = f.relative_to(ROOT).as_posix()
            sz = f.stat().st_size
            if f.suffix.lower() in TEXT_EXTS or f.name in {"VERSION", "LICENSE", "LICENSE-CODE", "NOTICE", "justfile", ".gitignore", ".gitattributes", ".editorconfig"}:
                try:
                    txt = f.read_text(encoding="utf-8", errors="replace")
                    lc = txt.count("\n") + (1 if txt and not txt.endswith("\n") else 0)
                    tok = max(1, len(txt) // 4)
                    total_tokens_est += tok
                    lines.append(f"| [`{rel}`]({rel}) | `{sz:,}` | `{lc:,}` | `~{tok:,}` |")
                except Exception:
                    lines.append(f"| [`{rel}`]({rel}) | `{sz:,}` | `—` | `binary` |")
            else:
                lines.append(f"| [`{rel}`]({rel}) | `{sz:,}` | `—` | `binary` |")
        lines.append("")

    lines.append(f"---\n*Estimated text corpus tokens across indexable text artifacts: `~{total_tokens_est:,}` tokens.*\n")
    (ROOT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")

    # Build llms-full.txt (concise concatenated context for LLM ingestion)
    full_parts = [
        "# alife-singularity-omega-package (v3.4.0) — Full LLM Context Bundle\n",
        "Author: Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA; ORCID 0009-0006-8168-9648)\n",
    ]
    for rel_src in LLMS_FULL_SOURCES:
        sp = ROOT / rel_src
        if sp.exists():
            full_parts.append(f"\n\n==================== FILE: {rel_src} ====================\n\n")
            full_parts.append(sp.read_text(encoding="utf-8", errors="replace"))
    (ROOT / "llms-full.txt").write_text("".join(full_parts), encoding="utf-8")
    print(f"  [INDEX] Generated INDEX.md ({len(files)} files) and llms-full.txt ({(ROOT / 'llms-full.txt').stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
