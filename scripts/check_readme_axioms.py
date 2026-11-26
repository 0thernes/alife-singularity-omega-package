#!/usr/bin/env python3
"""Verify that README.md's verbatim Lean 4.35.0 axiom block matches results/lean_package_axioms.txt 1:1."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
AXIOMS = ROOT / "results" / "lean_package_axioms.txt"

ALLOWED_AXIOMS = {"propext", "Quot.sound"}


def verify_readme_axioms() -> int:
    if not AXIOMS.exists():
        raise FileNotFoundError(f"Missing {AXIOMS}")
    expected_lines = [ln.strip() for ln in AXIOMS.read_text(encoding="utf-8").splitlines() if ln.strip()]
    if len(expected_lines) != 40:
        raise AssertionError(f"Expected 40 audited axiom lines, found {len(expected_lines)}")

    for ln in expected_lines:
        m = re.search(r"depends on axioms:\s*\[([^\]]*)\]", ln)
        if m:
            used = {tok.strip() for tok in m.group(1).split(",") if tok.strip()}
            extra = used - ALLOWED_AXIOMS
            if extra:
                raise AssertionError(f"Disallowed axioms {extra} in line: {ln}")

    readme_txt = README.read_text(encoding="utf-8")
    m_blk = re.search(r"<!-- LEAN_AXIOMS_START -->\s*```text\s*(.*?)\s*```\s*<!-- LEAN_AXIOMS_END -->", readme_txt, re.S)
    if not m_blk:
        raise AssertionError("README.md missing <!-- LEAN_AXIOMS_START --> ... <!-- LEAN_AXIOMS_END --> block")

    readme_lines = [ln.strip() for ln in m_blk.group(1).splitlines() if ln.strip()]
    if readme_lines != expected_lines:
        raise AssertionError(
            f"README axiom block diverged from results/lean_package_axioms.txt "
            f"(readme={len(readme_lines)} lines vs file={len(expected_lines)} lines)"
        )
    print("  [PASS] check_readme_axioms: 40/40 Lean 4.35.0 axiom lines match verbatim (axioms <= [propext, Quot.sound])")
    return len(expected_lines)


if __name__ == "__main__":
    try:
        verify_readme_axioms()
    except Exception as exc:
        print(f"  [FAIL] check_readme_axioms: {exc}", file=sys.stderr)
        sys.exit(1)
