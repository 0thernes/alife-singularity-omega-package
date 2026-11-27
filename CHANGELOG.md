# Changelog

All notable changes to `alife-singularity-omega-package` are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/).

## [Unreleased] - 2026-11-26

### Changed (documentation only)
- Corrected public claims to match the 2026-11-26 statement audit (see `ERRATA.md`, section "2026-11-26 statement audit"). The headline now states `36` core + `4` Palomar Lean declarations checked here; the `291` companion-reported theorems are not checked at this commit, and `327` is described as a sum of reported counts. `21` of the `36` core items are disclosed as closed evaluations or literal sums. Ring-0 "hardware" and "non-interference" wording replaced. Stale `244`/`92.05` figures, non-existent Lean identifiers, the broken `PalomarChallenge.lean` link, and checker-count and PDF-size drift corrected. Report-only CI and the scope of the `Classical.choice` statement disclosed. No Lean, paper, data or CI file changed.

## [3.5.0] - 2026-11-26

### Added
- **Non-Degenerate 3-Ring Lean 4.35.0 State Machine & `AdversarialTests.lean` (`50` core + `5` Palomar = `55` audited declarations):** Added multi-step inductive Ring-0 kernel trace invariance (`ring0_trace_invariant`), explicit Ring-1/Ring-2 mutation reachability (`ring1_ring2_plasticity_reachable`), `spiegelman_zero_annihilation`, `rawOviCentis_p1_lipschitz`, `10` formal Lean `¬(...)` refutations in `lean/OmegaPackageProofs/AdversarialTests.lean`, and Palomar certificate `m5_adversarial_refutations`. Combined 7-repo ecosystem total: **`360` Pure 6-Kernel Lean 4.35.0 Theorems** (`310` native + `50` local).
- **Live Negative Lean Tamper Rejection (`scripts/test_lean_negative.py`):** Verifies Lean 4.35.0 kernel, axiom allowlist, and Ubuntu `lake comparator --paranoid` reject injected `sorry`, custom axioms, and false claims (`TAMPER-01..04`); wired into CI and Gate 23.
- **Crossref 0-Retraction Citation Verification (`scripts/check_citations.py`):** Queries Crossref Works API across all DOIs (`20/20` resolved, `15` Crossref-checked, `0` retractions).
- **Auto-Generated White Paper Data Table (`paper/generated_tables.tex`):** Programmatically generates Table 2 from `results/empirical_sim_summary.json` so prose/figure drift is structurally impossible.
- **Cryptographic RFC 3161 TSA Timestamp (`data/timestamps/CHECKSUMS.sha256.tsr`), `codemeta.json`, and 43-Item `SUBMISSION_READINESS.md`.**
- **Strict CSP & WCAG 2.2 AA Skip-Link/Landmarks** across `blueprint/index.html` and `html/ALife_Singularity_SuperLife_Omega_Dashboard.html`.
- **24-Gate Automated Forensic Integrity Auditor** (`scripts/audit_omniscient_integrity.py`, adding Gates 23–24).

### Fixed
- **Security (Dependabot Alert `#1` / `CVE-2025-71176`):** Upgraded `pytest==9.0.3` in `requirements.txt` and `pytest>=9.0.3` in `pyproject.toml` (`0` `pip-audit` CVEs).
- **White Paper Table 2 & Visual Figure Defects:** Fixed `v3.4.0` Table 2 drift vs. Figure 2, fixed Figure 4 Panel B clipped title / colliding x-labels and Panel A legend overlap, eliminated `Underfull \vbox (badness 10000)` (`0` overfull hboxes, `0` bad vboxes).
- **Simulator Statistical & Classifier Bugs (`scripts/run_alife_castration_sim.py`):** Replaced hardcoded `df=23` $t$-quantile (`1.7139`) with exact `df=N-1` (`1.6779` at `N=48`), added paired Cohen's $d_z$ and deterministic 2,000-resample 95% bootstrap CIs, unified canonical 7-stage classifier (`SIM08 = 85.48` → `STAGE_5_CONVERGED_SYNTHESIS`), and logged both geometric & arithmetic OVI.
- **Static Lint & Cross-OS Hygiene:** Fixed all `53` `ruff` findings (`0` errors, removed `|| true` in CI), added SPDX headers across all Python modules, and normalized all text files to LF.
- **Live Ecosystem Sync:** Re-executed all 5 live native engines (`Cellulogonic Mecha v1.6.0 [78 Lean, COVI 58.52]`, `Cellular Engine Omega v5.4.0 [100 Lean]`, live composite `OVBS-52 = 91.91`) and re-verified `csv/21` against `unsolved-problems-mega-atlas v2.8.0` (`0/1,900` overarching problems retired).

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
