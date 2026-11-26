# ADR 0001: Zero-Consolidation Preservation of All 17 Clean-Slate v3.0 Files & Dual-Drive Mirroring

- **Status:** Accepted (`v3.0-Omega` through `v3.4.0`)
- **Date:** 2026-10-28 (reaffirmed 2026-11-25)

## Context
The Clean-Slate v3.0 architecture defines `17` canonical deliverables across HTML, Markdown, PDF, CSV, JSON/YAML/XML/TXT, and Excel (`938` checklist rows, `10x10x10` Hybrid Cube, `160` errata closures). Merging them with the macro Omega Singularity stack risked silently deleting or collapsing legacy files and breaking downstream references.

## Decision
Enforce a strict **Zero-Consolidation Invariant** (Gate 1): all `17` Clean-Slate v3.0 files remain intact as first-class artifacts alongside the Omega deliverables, synchronized programmatically from shared datasets and mirrored atomically between the canonical ReFS Dev Drive (`Z:`) and the secondary SSD Master Folder (`I:`) with Gate 18 SHA-256 verification.

## Consequences
- Every downstream workflow expecting either Clean-Slate v3.0 or Omega filenames continues to work without breakage.
- Build scripts maintain 1:1 parity across all formats (`JSON == YAML`, `26` XML sections, `24` CSVs, `5` workbooks) automatically.
