# Replication Protocol & Replication Log

## Clean-Clone Replication Protocol (Build Standard B43)

Any independent researcher can verify all local claims (`C1`, `C3`, `C5`, `C6`, `C8`) from a clean clone without external proprietary dependencies:

### Prerequisites
- Git `>= 2.40`
- Python `>= 3.12` and `uv` (`>= 0.5`)
- Lean 4 via `elan` (automatically reads `lean/lean-toolchain` → `leanprover/lean4:v4.35.0`)
- Node.js `>= 20` (for Observatory JS syntax check)
- Chromium / Google Chrome or Edge (for headless PDF generation & Gate 17 live 22-tab DOM stress test)
- Tectonic `>= 0.15` (for AMS-LaTeX white paper & clean-room arXiv tarball verification)

### Step-by-Step Commands

```bash
# 1. Clone and check pinned toolchain
git clone https://github.com/0thernes/alife-singularity-omega-package.git
cd alife-singularity-omega-package

# 2. Verify zero-Mathlib Lean 4.35.0 proofs + independent paranoid kernel (< 5 seconds)
cd lean
lake build
lake env lean OmegaPackageProofs/VerifyAxioms.lean
lake env leanchecker
lake env leanchecker-paranoid
cd ..

# 3. Verify unit, negative, regression, Hypothesis property & 50-digit differential oracle tests
uv run --with pytest --with hypothesis --with openpyxl --with xlwt --with xlrd \
       --with pyyaml --with jsonschema --with scipy --with pypdf pytest tests/ -v

# 4. Verify 6/6 Python semantic mutation kills & verbatim README axiom block
python scripts/run_mutation_audit.py
python scripts/check_readme_axioms.py

# 5. Recompile publication figures, AMS-LaTeX white paper & clean-room arXiv tarball
uv run --with matplotlib --with numpy --with pypdf python scripts/build_paper_and_figures.py

# 6. Optional: re-run full 748-run paired empirical simulation from scratch (~20-40 s)
uv run --with scipy python scripts/run_alife_castration_sim.py

# 7. Run all 22 automated forensic integrity gates
uv run --with openpyxl --with xlwt --with xlrd --with pyyaml --with jsonschema \
       --with scipy --with pypdf python scripts/audit_omniscient_integrity.py

# 8. Run Build Standard v1.2.0 90-item audit (report-only)
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/Audit-Repo.ps1 -Path .
# (or on Linux/macOS: bash scripts/audit-repo.sh .)
```

---

## Replication Log (Build Standard B44)

Independent replications (both successful and failed) are logged verbatim below. Open an issue with the `replication` label to submit an independent run.

| Date | Replicator | Environment | Scope Replicated | Result | Notes / Commit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-11-25 | Alexander Stephen Donahue (Author baseline) | Windows 11 x64, 24C P+E, RTX 5070 Ti, Python 3.12 (`uv 0.12.19`), Lean `v4.35.0`, Tectonic `0.17.0`, Node `v25.8.2` | Full clean rebuild: Lean 4.35.0 (`40/40` axioms + `leanchecker-paranoid`), `748`-run paired sim, `pytest` + Hypothesis + `6/6` mutations, AMS-LaTeX PDF + clean-room `arxiv_submission.tar.gz`, `22/22` forensic gates, `100.0%` Build Standard v1.2.0, `Z: <-> I:` SHA-256 mirror | **PASS** (self-replication baseline; external independent replication invited) | Release `v3.4.0` |
