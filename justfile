# Task runner for alife-singularity-omega-package (v3.5.0) — Build Standard v1.2.0 (A31 / B01)
# No recipe installs git hooks or gates commits/pushes (Hard Rule R1/R4).

set shell := ["bash", "-euo", "pipefail", "-c"]
set windows-shell := ["pwsh", "-NoProfile", "-Command"]

default:
    @just --list

# Install Python verification dependencies via uv or pip
setup:
    uv pip install -r requirements.txt

# Build Lean 4.35.0 proofs (zero-Mathlib), verify axioms & paranoid kernel
lean:
    cd lean && lake build && lake env lean OmegaPackageProofs/VerifyAxioms.lean && lake env leanchecker && lake env leanchecker-paranoid

# Build publication vector figures, AMS-LaTeX white paper PDF & clean-room arXiv tarball
paper:
    uv run --with matplotlib --with numpy --with pypdf python scripts/build_paper_and_figures.py

# Rebuild all 24 CSVs, 4 Specs, 5 Workbooks, 3 HTML5 apps, 3 compressed PDFs, manifests & 24 gates (reusing locked 748-run sim)
build:
    uv run --with openpyxl --with xlwt --with xlrd --with pyyaml --with jsonschema --with scipy --with pypdf python scripts/build_omega_package.py --reuse-sim

# Full empirical 748-run paired simulation + complete rebuild
sim-build:
    uv run --with openpyxl --with xlwt --with xlrd --with pyyaml --with jsonschema --with scipy --with pypdf python scripts/build_omega_package.py

# Run pytest unit, negative, regression, Hypothesis property & 50-digit differential oracle tests
test:
    uv run --with pytest --with hypothesis --with openpyxl --with xlwt --with xlrd --with pyyaml --with jsonschema --with scipy --with pypdf pytest tests/ -v

# Run Python semantic mutation audit (6/6 mutants must be killed)
mutate:
    python scripts/run_mutation_audit.py

# Run report-only linters & strict mypy type checks (never blocks)
lint:
    uv run --with ruff ruff check scripts reference tests examples || true
    uv run --with mypy mypy reference --ignore-missing-imports || true

# Run 10-iteration warmed performance benchmark and refresh docs/benchmarks.md
bench:
    uv run --with scipy python scripts/benchmark_omega.py

# Run 24-gate omniscient forensic integrity audit
forensic:
    uv run --with openpyxl --with xlwt --with xlrd --with pyyaml --with jsonschema --with scipy --with pypdf python scripts/audit_omniscient_integrity.py

# Score repo against Build Standard v1.2.0 (90 items, report-only)
audit:
    pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/Audit-Repo.ps1 -Path . -Json audit.json

# Verify bibliography DOIs/URLs & verbatim README axiom block
check-docs:
    python scripts/check_readme_axioms.py
    python scripts/check_citations.py

# Regenerate INDEX.md and llms-full.txt
index:
    python scripts/generate_index_and_llms.py

# One-command clean-clone reproduction of every headline number (Build Standard B01)
reproduce: lean paper build test mutate bench check-docs forensic audit
    @echo "reproduce: ALL 24 forensic gates, 36+4 Lean 4.35.0 theorems, white paper, pytest/Hypothesis, mutation (6/6) & Build Standard audit PASSED."

# Clean transient build intermediates
clean:
    rm -rf paper/build .pytest_cache .ruff_cache .mypy_cache .hypothesis audit.json _site
