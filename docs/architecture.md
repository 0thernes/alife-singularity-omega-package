# System Architecture (`v3.4.0`)

## 1. Design Philosophy: Zero-Consolidation Multi-Format Synchronization

`alife-singularity-omega-package` is architected as a **single-source-of-truth generation graph** that preserves every Clean-Slate v3.0 deliverable (`17` canonical files) verbatim alongside the Omega Singularity analytical stack, Lean 4.35.0 formal proof suite, and AMS-LaTeX publication pipeline.

```
Dataset Modules (scripts/omega_datasets_part1..6.py) + Live Receipts (results/*.json)
        │
        ├──▶ scripts/build_omega_package.py
        │       ├──▶ 24 Canonical CSVs (2,822 rows)
        │       ├──▶ 5 Excel Workbooks (Omega 25sh, v3 18sh, Cube 13sh + 2 legacy .xls)
        │       ├──▶ 4-Format Master Spec (JSON == YAML, 26-section XML, TXT)
        │       ├──▶ 3 Standalone HTML5 Apps (22-Tab Observatory, Framework, Blueprint)
        │       ├──▶ 3 Lossless Compressed Chrome Vector PDFs (< 2.5 MB each, 0 U+2611)
        │       └──▶ Cryptographic Manifests (MANIFEST_SHA256.txt, CHECKSUMS.sha256, data/MANIFEST.sha256, MANIFEST.json)
        │
        ├──▶ lean/ (Zero-Mathlib Lean 4.35.0)
        │       ├──▶ OmegaPackageProofs/{OVBS52Scoring,EscalationAndCube,CastrationAndRing0,NonVacuity,VerifyAxioms}.lean
        │       ├──▶ Challenge.lean / Solution.lean / PalomarSolution.lean + palomar/PalomarChallenge.lean
        │       └──▶ results/lean_package_axioms.txt (40 lines, axioms <= [propext, Quot.sound])
        │
        ├──▶ paper/ (AMS-LaTeX + Matplotlib)
        │       ├──▶ scripts/build_paper_and_figures.py -> 4 vector PDFs + docs/media/social-preview.png
        │       └──▶ dist/Donahue_2026_alife_singularity_omega.pdf + dist/arxiv_submission.tar.gz
        │
        └──▶ Verification & Audit
                ├──▶ reference/ovbs52_oracle.py (50-digit Decimal/Fraction oracle)
                ├──▶ tests/ (pytest + Hypothesis + 2,000+ differential + regressions)
                ├──▶ scripts/run_mutation_audit.py (6/6 semantic mutants killed)
                ├──▶ scripts/audit_omniscient_integrity.py (22 Forensic Gates)
                └──▶ scripts/Audit-Repo.ps1 & audit-repo.sh (Build Standard v1.2.0: 90 items)
```

## 2. Directory & Responsibility Map

| Directory | Role |
| :--- | :--- |
| `csv/` | `24` canonical UTF-8 CSV datasets (`2,822` total structured records, zero drift). |
| `specs/` | 4-format synchronized Master Spec (`JSON`, `YAML`, `XML` with `26` fusion sections, `TXT`). |
| `excel/` | `5` Excel workbooks (`3` `.xlsx` with native charts & formulas + `2` binary-verified legacy `.xls`). |
| `html/` | `3` self-contained offline HTML5 applications (including the `22`-tab Observatory with `24` embedded vector SVGs). |
| `pdf/` | `3` lossless-compressed Chrome vector PDFs (`< 2.5 MB` each; `0` `U+2611` in Clean-Slate docs). |
| `reports/` | `12` comprehensive markdown treatises & audit reports (Reports `01–09` + 3 Clean-Slate reports). |
| `lean/` & `palomar/` | Zero-Mathlib Lean 4.35.0 formal proofs (`36` core + `4` Palomar comparator theorems) & interactive DAG (`blueprint/index.html`). |
| `paper/` & `dist/` | AMS-LaTeX white paper (`main.tex`, `refs.bib`, `4` vector PDF figures), compiled PDF, and clean-room `arxiv_submission.tar.gz`. |
| `pipelines/` | `alifeops-master-pipeline.yaml` (`78` alerts, `13` Release Gates) & `benchmark-suite-schema.json` (Draft 2020-12). |
| `results/` | Locked `748`-run simulation JSONs, `8` cohort scorecards, live `5`-engine receipt, `40`-line Lean axiom log, and benchmark history. |
| `reference/` & `tests/` | Independent 50-digit `Decimal` oracle, unit/negative/regression/Hypothesis/differential test suites. |
| `scripts/` | Reproducible build, simulation, mutation, citation, benchmark, indexing, and 22-gate forensic auditing scripts. |
| `docs/` & `examples/` | Governance documentation, 4 ADRs, Datasheet, AI Disclosure, Statement Fidelity, Build Standard v1.2.0, and executable demo. |
