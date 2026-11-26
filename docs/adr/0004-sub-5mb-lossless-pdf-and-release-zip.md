# ADR 0004: Sub-5 MB Git Hygiene via Lossless `pypdf` Compression & Release-Only ZIP Bundling

- **Status:** Accepted
- **Date:** 2026-11-25

## Context
Build Standard for LLMs v1.2.0 (`A24`) forbids committing files larger than `5.00 MB` (`5,242,880` bytes) to Git. In `v3.3-Omega`, `pdf/ALife-Build-Framework-Template.pdf` (`5.54 MB`) and `ALife_Singularity_SuperLife_Omega_Package.zip` (`8.76 MB`) both exceeded this limit.

## Decision
1. Apply lossless level-9 Flate compression plus duplicate/unreferenced object deduplication (`pypdf` `compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)`) automatically at the end of `_render_html_to_pdf` in `scripts/build_v3_unified_artifacts.py`.
2. Remove `ALife_Singularity_SuperLife_Omega_Package.zip` from Git tracking (add to `.gitignore`) while continuing to build it locally via `just build`, mirror it to `I:`, and publish it on GitHub Releases with `SHA256SUMS` and SLSA provenance.

## Consequences
- `ALife-Build-Framework-Template.pdf` shrinks `5.54 MB -> 2.33 MB` (~58% reduction) with `100%` text extraction parity verified by Gate 16.
- Every Git-tracked file stays strictly `< 5.00 MB`, keeping clones fast and `Audit-Repo.ps1` `A24` 100% GREEN.
