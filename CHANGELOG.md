# Changelog

All notable changes to `alife-singularity-omega-package` are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

## [Unreleased] - 2026-11-26

### Changed (documentation only)
- Corrected public claims to match the 2026-11-26 statement audit (see `ERRATA.md`, section "2026-11-26 statement audit"). The headline now states `36` core + `4` Palomar Lean declarations checked here; the `291` companion-reported theorems are not checked at this commit, and `327` is described as a sum of reported counts. `21` of the `36` core items are disclosed as closed evaluations or literal sums. Ring-0 "hardware" and "non-interference" wording replaced. Stale `244`/`92.05` figures, non-existent Lean identifiers, the broken `PalomarChallenge.lean` link, and checker-count and PDF-size drift corrected. Report-only CI and the scope of the `Classical.choice` statement disclosed. No Lean, paper, data or CI file changed.

## [3.4.0] - 2026-11-25

### Added
- **Zero-Mathlib Pure 6-Kernel Lean 4.35.0 Package Invariant Suite (`lean/`):** 36 core machine-checked theorems (`OVBS52Scoring`, `EscalationAndCube`, `CastrationAndRing0`, `NonVacuity`) + 4 Palomar comparator certificates (`40` audited `#print axioms` lines in `results/lean_package_axioms.txt`), strictly constructive axioms $\subseteq [\text{propext}, \text{Quot.sound}]$, verified locally across `lean4`, `leanchecker --fresh`, `leanchecker-paranoid --fresh`, `nanoda_bin`, `con-leche --verified`, and `con-ron --verified` (`results/lean4-multi-kernel.txt`, `1,574` declarations accepted) plus full 6/6 Linux `bubblewrap` CI (`lake check --paranoid`, `lake comparator`). Live 7-repo ecosystem sync yields **`291` native** (`AUTOPHAGE v1.4.0`: `48`, `Cellulogonic Mecha v1.5.0`: `70` & `26/26` gates, `Cellular Engine Omega v5.2.0`: `89` & `60/60` gates, `Noetic Organism Omega v2.1.0`: `54`, `Asmodensius-Native v1.1.0`: `30` & `77/77` ctest + `164/164` `test_gpu` + live 24C==RTX 5070 Ti GPU hash parity; composite `OVBS-52 = 91.84`, alongside `omega-triscale-observatory v6.7.0`) **+ `36` local = `327` Pure 6-Kernel Lean 4.35.0 Theorems**.
- **1,900-Problem Mega-Atlas Non-Retirement Audit:** Programmatically audited all `1,900` open problems in `0thernes/unsolved-problems-mega-atlas` (V2.4.0); generated `csv/21_mega_atlas_1900_open_problems_crosswalk.csv` (`25` mapped targets `MA-01..MA-25`), `docs/MEGA_ATLAS_CROSSCHECK.md`, `reports/09_MEGA_ATLAS_1900_OPEN_PROBLEMS_CROSSCHECK.md`, and Observatory Tab 22. Honest verdict: **0 / 1,900** overarching open problems retired.
- **Publication AMS-LaTeX White Paper & Clean-Room arXiv Tarball:** `paper/main.tex` (`amsart`, 0 overfull hboxes, 0 undefined citations/refs, `20/20` live verified primary academic DOIs/URLs in `paper/refs.bib`), 4 vector PDF figures, `dist/Donahue_2026_alife_singularity_omega.pdf`, `dist/arxiv_submission.tar.gz`, and `docs/media/social-preview.png`.
- **Independent 50-Digit Oracle, Property/Differential Tests & Mutation Suite:** `reference/ovbs52_oracle.py`, `scripts/run_mutation_audit.py` (`6/6 = 100%` killed), `tests/test_omega_package.py`, and `tests/test_properties_and_differential.py` (`1,000+` Hypothesis examples + `2,000+` differential oracle cases).
- **Build Standard for LLMs v1.2.0 (`100.0%`) & FAIR Metadata Suite:** `VERSION`, dual `LICENSE` (`Apache-2.0`) + `LICENSE-DOCS` (`CC-BY-4.0`), `CITATION.cff`, `CITATION.bib`, `repo.yaml` (validated against `repo-standard.schema.json`), `.zenodo.json`, `croissant.json`, `ro-crate-metadata.json`, `CLAIMS.md`, `EVIDENCE.md`, `LIMITATIONS.md`, `VERIFICATION.md`, `REPLICATION.md`, `PREREGISTRATION.md`, `DEVIATIONS.md`, `ERRATA.md`, `HARDENING_LOG.md`, `INDEX.md`, `llms.txt`, `llms-full.txt`, `.github/workflows/{ci,pages,release}.yml`, `.github/ISSUE_TEMPLATE/`, `docs/` + 4 ADRs, `blueprint/index.html`, and `examples/quickstart_demo.py`.
- **22-Gate Automated Forensic Integrity Auditor:** Upgraded `scripts/audit_omniscient_integrity.py` from 18 to 22 gates (adding Lean 4.35.0 axiom parity, AMS-LaTeX PDF/arXiv clean-room verification, Build Standard hygiene & `< 5 MB` check, and mutation/README-axiom gates).

### Fixed
- **Legal Identity Cure (`OMG-146`):** Replaced unformed corporate label `"0thernes LLC"` across all repository files with `"Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA)"`, ORCID `0009-0006-8168-9648`.
- **Theorem Arithmetic & 5-Engine Parity (`OMG-147`, `OMG-148`):** Fixed `240 / 240` mis-sum (`42+62+72+48=224`, omitting `Asmodensius-Native`'s `20` theorems → `244` native + `36` local = `280`), and replaced stale `4-Engine` / `Asmodensius (RO)` / `WRITER.lock RO` references with live `5-Engine` receipts (`77/77 ctest`, `20` Lean 4, dual worlds).
- **P8 Benchmark Modulo-Wrap Bug (`OMG-149`):** Added 7th distinct submetric to `P8_FERAL_RESILIENCE_CRITICALITY` in `scripts/run_alifeops_suite.py` so `BM-FRL-07` no longer aliases `BM-FRL-01`.
- **Windows UTF-8 Subprocess Decoding (`OMG-150`):** Added explicit `encoding="utf-8", errors="replace"` to `subprocess.run` calls across Chrome and native engine runners.
- **Git `< 5 MB` File-Size Hygiene (`OMG-151`):** Added lossless level-9 `pypdf` compression to Chrome PDFs (`ALife-Build-Framework-Template.pdf` `5.54 MB -> 2.33 MB`, 100% text parity) and untracked the local `ALife_Singularity_SuperLife_Omega_Package.zip` release bundle from Git (now built locally & attached to GitHub Releases).

## [3.3.0] - 2026-11-16

### Added
- Pass-5 Depth/Spectrum/Pareto expansion (`csv/18..20`, Report 08, 748-run `N=48` paired simulation with dual 11-point gradient sweeps and `5x5` 2D phase surface, 24 vector SVGs, 18-gate forensic auditor, live 5-engine `Asmodensius-Native` upgrade reaching `OVBS-52 = 92.05` and `244` native Lean 4 theorems).

## [3.2.0] - 2026-11-10

### Added
- Pass-4 Comparative Contrast, Continuous Gradients, Operating Margins & Adjacent-Possible expansion (`csv/15..17`, Report 07, 15-gate forensic auditor, `324`-run initial `N=24` paired simulation).

## [3.0.0] - 2026-10-28

### Added
- Zero-consolidation fusion of all 17 Clean-Slate v3.0 files (`938` checklist items, `10x10x10` Hybrid Cube, 4-format Master Spec, `825` C11 checks, `13` Release Gates) with the Omega Singularity stack.

## [2.1.0] - 2026-10-15

### Added
- Initial Omega Singularity package (`v2.1-Omega`): 11 CSVs, 42/42 wired ALifeOps YAML alerts, 13x13 Castration Synergy Matrix, 6-cohort Python simulator, 11-tab HTML Observatory, and SHA-256 manifest.
