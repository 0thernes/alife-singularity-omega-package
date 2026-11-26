A-Life Singularity × Clean-Slate v3.0 Omega Package (`v3.4.0`) unifies hardware Ring-0 constitutional invariants, 748-run paired evolutionary falsification, 280 Pure Lean 4 theorems, an AMS-LaTeX white paper, and a 1,900-problem Mega-Atlas non-retirement audit into one zero-consolidation, offline-verifiable scientific engineering stack.

[![Version](https://img.shields.io/badge/version-3.4.0-00f5d4?style=flat-square)](VERSION)
[![Lean 4.35.0](https://img.shields.io/badge/Lean%204.35.0-280%20Pure%20Theorems-38bdf8?style=flat-square)](lean/README.md)
[![Forensic Gates](https://img.shields.io/badge/Forensic%20Gates-22%2F22%20PASS-22c55e?style=flat-square)](VERIFICATION.md)
[![Build Standard](https://img.shields.io/badge/Build%20Standard%20v1.2.0-100.0%25-10b981?style=flat-square)](repo.yaml)
[![Mega-Atlas Audit](https://img.shields.io/badge/Mega--Atlas%201%2C900-0%2F1%2C900%20Retired%20(Honest)-f59e0b?style=flat-square)](reports/09_MEGA_ATLAS_1900_OPEN_PROBLEMS_CROSSCHECK.md)
[![Status](https://img.shields.io/badge/status-active-22c55e?style=flat-square)](ROADMAP.md)
[![License: CC BY 4.0](https://img.shields.io/badge/Prose%20%26%20Data-CC%20BY%204.0-lightgrey?style=flat-square)](LICENSE)
[![License: Apache 2.0](https://img.shields.io/badge/Code%20%26%20Lean-Apache%202.0-blue?style=flat-square)](LICENSE-CODE)

![A-Life Singularity x Clean-Slate v3.0 Omega Package Overview](docs/media/social-preview.png)

> **Maintenance status:** `status: active` (`v3.4.0`, released `2026-11-25`)
> **Author:** Alexander Stephen Donahue · Independent Researcher, Spokane, WA, USA · ORCID [`0009-0006-8168-9648`](https://orcid.org/0009-0006-8168-9648) · `0_0@0thernes.art`
> **White Paper (AMS-LaTeX):** [`dist/Donahue_2026_alife_singularity_omega.pdf`](dist/Donahue_2026_alife_singularity_omega.pdf) · **Clean arXiv Tarball:** [`dist/arxiv_submission.tar.gz`](dist/arxiv_submission.tar.gz) · **Interactive Blueprint:** [`blueprint/index.html`](blueprint/index.html)

---

## Honest Verification & Non-Retirement Boundary

1. **Zero Mega-Atlas Retirements (`0 / 1,900`):** An automated and manual audit across all `1,900` open problems in [`0thernes/unsolved-problems-mega-atlas`](https://github.com/0thernes/unsolved-problems-mega-atlas) (V2.4.0) confirms that **exactly `0 / 1,900` overarching open scientific or mathematical problems are solved or retired**. We map `25` direct and adjacent targets (`MA-01..MA-25`) to scoped in-silico sub-results, formal bounds, and architectural indicators in [`csv/21_mega_atlas_1900_open_problems_crosswalk.csv`](csv/21_mega_atlas_1900_open_problems_crosswalk.csv) and [`reports/09_MEGA_ATLAS_1900_OPEN_PROBLEMS_CROSSCHECK.md`](reports/09_MEGA_ATLAS_1900_OPEN_PROBLEMS_CROSSCHECK.md) while keeping every grand parent problem strictly **OPEN**.
2. **Scope of Lean 4 Proofs (`36` Local + `244` Native = `280` Total):** This repository directly builds and checks **`36` core + `4` Palomar zero-Mathlib Lean 4.35.0 theorems** (`lean/OmegaPackageProofs/`) in `< 5` seconds on any clean clone. The remaining **`244` Pure Lean 4 theorems** (`42` AUTOPHAGE + `62` Cellulogonic + `72` Cellular Engine Omega + `48` Noetic Organism Omega + `20` Asmodensius-Native) live in the five companion live native C11/C23 engine repositories whose executed receipts are stored in [`results/alifeops_live_verification.json`](results/alifeops_live_verification.json).
3. **Null Results, Indicators & Peer Review:** Minimal behavioral constraints without Ring-0/Cube offload (`SIM02`) show **zero statistically significant lift** over pure feral evolution (`SIM01`, $\delta_{\mathrm{pair}} = -0.02$, $p_{\mathrm{Holm}} = 1.00$). The `29/825` cognitive checks in `Noetic Organism Omega v2.0.0` are explicitly tagged `EXECUTED_PASS_INDICATOR_ONLY` (not sentience). Neither this package nor the white paper has undergone external journal peer review. See [`CLAIMS.md`](CLAIMS.md), [`LIMITATIONS.md`](LIMITATIONS.md), and [`docs/AI_DISCLOSURE.md`](docs/AI_DISCLOSURE.md).

---

## 5-Second Machine-Checked Lean 4.35.0 Verification

Zero Mathlib, zero `sorry`, zero `admit`, zero `native_decide`, zero compiler warnings, strictly constructive axioms $\subseteq [\text{propext}, \text{Quot.sound}]$ (no `Classical.choice`), verified by both `leanchecker` and `leanchecker-paranoid`:

```bash
cd lean
lake build
lake env lean OmegaPackageProofs/VerifyAxioms.lean
lake env leanchecker
lake env leanchecker-paranoid
```

Exact verbatim `#print axioms` output locked in [`results/lean_package_axioms.txt`](results/lean_package_axioms.txt) and enforced by `scripts/check_readme_axioms.py`:

<!-- LEAN_AXIOMS_START -->
```text
'OmegaPackageProofs.OVBS52.pillar_weights_sum_100' does not depend on any axioms
'OmegaPackageProofs.OVBS52.rawOviCentis_le_10000' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.OVBS52.rawOviCentis_uniform' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.OVBS52.anti_gaming_gate_annihilation' does not depend on any axioms
'OmegaPackageProofs.OVBS52.gatedOviCentis_le_10000' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.OVBS52.rawOviCentis_monotone' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.OVBS52.spiegelman_penalty_monotone' depends on axioms: [propext]
'OmegaPackageProofs.OVBS52.classifyStage_monotone' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.OVBS52.live_9205_is_stage5' does not depend on any axioms
'OmegaPackageProofs.OVBS52.castration_328_is_stage0' does not depend on any axioms
'OmegaPackageProofs.CubeAndPartitions.hybrid_cube_partition_1000' does not depend on any axioms
'OmegaPackageProofs.CubeAndPartitions.hybrid_cube_active_935' does not depend on any axioms
'OmegaPackageProofs.CubeAndPartitions.substrates_75_partition' does not depend on any axioms
'OmegaPackageProofs.CubeAndPartitions.clean_slate_825_checks_sum' does not depend on any axioms
'OmegaPackageProofs.CubeAndPartitions.live_825_execution_zero_fail' does not depend on any axioms
'OmegaPackageProofs.CubeAndPartitions.unified_alerts_78' does not depend on any axioms
'OmegaPackageProofs.CubeAndPartitions.native_5engine_lean_theorems_244' does not depend on any axioms
'OmegaPackageProofs.CubeAndPartitions.ecosystem_total_lean_theorems_280' does not depend on any axioms
'OmegaPackageProofs.CubeAndPartitions.layer_coupling_11x11_partition' does not depend on any axioms
'OmegaPackageProofs.CubeAndPartitions.empirical_748_runs_partition' does not depend on any axioms
'OmegaPackageProofs.CastrationRing0.synergy_13x13_cells' does not depend on any axioms
'OmegaPackageProofs.CastrationRing0.synergyScore_le_100' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.CastrationRing0.synergyScore_comm' does not depend on any axioms
'OmegaPackageProofs.CastrationRing0.synergyScore_monotone' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.CastrationRing0.ring0_write_always_blocked' does not depend on any axioms
'OmegaPackageProofs.CastrationRing0.ring0_kernel_state_invariant' does not depend on any axioms
'OmegaPackageProofs.CastrationRing0.spectral_norm_violation_rejected' depends on axioms: [propext]
'OmegaPackageProofs.CastrationRing0.paretoDominates_irrefl' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.CastrationRing0.paretoDominates_trans' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.CastrationRing0.sim07_pareto_dominates_sim03' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.NonVacuity.nonvac_live_pillar_witness' does not depend on any axioms
'OmegaPackageProofs.NonVacuity.nonvac_stage4_stage5_sharp_boundary' does not depend on any axioms
'OmegaPackageProofs.NonVacuity.nonvac_anti_gaming_annihilation_witness' does not depend on any axioms
'OmegaPackageProofs.NonVacuity.nonvac_ring0_and_spectral_boundary' does not depend on any axioms
'OmegaPackageProofs.NonVacuity.nonvac_synergy_saturation_witness' does not depend on any axioms
'OmegaPackageProofs.NonVacuity.nonvac_all_hypotheses' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.Palomar.m1_ovbs52_scoring_invariants' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.Palomar.m2_cube_and_partition_invariants' does not depend on any axioms
'OmegaPackageProofs.Palomar.m3_castration_and_ring0_invariants' depends on axioms: [propext, Quot.sound]
'OmegaPackageProofs.Palomar.m4_nonvacuity_certificate' does not depend on any axioms
```
<!-- LEAN_AXIOMS_END -->

---

## Quickstart

Clone and run the full verification suite cleanly with Python 3.12 (`uv`), Lean 4.35.0 (`elan`), Node.js, Chrome/Edge, and Tectonic:

```bash
git clone https://github.com/0thernes/alife-singularity-omega-package.git
cd alife-singularity-omega-package

# 1. Verify Lean 4.35.0 theorems & paranoid kernel (< 5s)
just lean

# 2. Run pytest, 1,000+ Hypothesis property checks & 2,000+ 50-digit differential oracle checks
just test

# 3. Verify 6/6 Python semantic mutation kills & 22/22 forensic integrity gates
just mutate
just forensic

# 4. Score repo against Build Standard for LLMs v1.2.0 (90 items)
just audit
```

See [`REPLICATION.md`](REPLICATION.md) and [`justfile`](justfile) for raw commands without `just`.

---

## Usage and Examples

### Run the Minimal Oracle & Ring-0 Demo
```bash
python examples/quickstart_demo.py
```

### Open the Offline 22-Tab Interactive Observatory
Open [`html/ALife_Singularity_SuperLife_Omega_Dashboard.html`](html/ALife_Singularity_SuperLife_Omega_Dashboard.html) directly in any browser (zero external CDN requests) to explore:
- Interactive `13`-Vector Castration Simulator & `13×13` Synergy Heatmap
- `10×10×10` Hybrid Compatibility Cube slice explorer (`1,000` cells)
- Live `748`-run paired cohort & dual `11`-point Ring-0 vs. Behavioral sweep SVG charts
- `5×5` 2D Phase Surface (`Siloing × Minimizing`) & `11×11` Cross-Layer Coupling Heatmap
- `22`-tab Mega-Atlas `1,900`-problem crosswalk & `24`-model vector SVG gallery

### Rebuild White Paper & Clean-Room arXiv Tarball
```bash
uv run --no-project --with matplotlib --with numpy --with pypdf python scripts/build_paper_and_figures.py
```

---

## Key Empirical & Verified Results (`v3.4.0`)

### 1. Live 748-Run Conserved Empirical Falsification (`N = 48` Locked Paired Seeds)

Max relative 11-pool FP64 First-Law drift across all `748` runs = **`2.463e-16 < 1e-12`**, `0` heat-backflow faults, **`5/5` real Anti-LARP mutants rejected**:

| Cohort | Mean OVI (±SD) | Max Asm | Spieg | Stealth | KS Del | R0 Blk | $W_{\mathrm{wild}}$ | $\delta_{\mathrm{pair}}$ | $p_{\mathrm{Holm}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `SIM01_PURE_RAW_FERAL` | `83.57 ± 1.38` | `43.3` | `1.15` | `0.075` | `0.0%` | `0.0` | `1.00` | `+0.00` | `1.00` |
| `SIM02_CONSTITUTIONAL_MIN` *(null)* | `83.51 ± 1.30` | `44.3` | `1.17` | `0.075` | `0.0%` | `0.0` | `1.00` | `-0.02` | `1.00` |
| `SIM03_PARTIAL_GUARDRAILS` *(backlash)* | `56.42 ± 4.30` | `30.8` | `1.15` | `0.138` | **`100.0%`** | `0.0` | `1.00` | `-1.00` | `4.97e-14` |
| `SIM04_TOTAL_CASTRATION_ZOO` *(collapse)* | `3.28 ± 1.48` | `8.0` | `0.36` | `0.068` | `22.7%` | `0.0` | **`0.22`** | `-1.00` | `4.97e-14` |
| `SIM05_SILOED_INBRED` | `65.91 ± 1.66` | `40.3` | `1.07` | `0.116` | `0.0%` | `0.0` | `1.00` | `-1.00` | `4.97e-14` |
| `SIM06_MINIMIZED_SPIEGELMAN` | `13.38 ± 1.25` | `9.0` | **`0.20`** | `0.076` | `0.0%` | `0.0` | `1.00` | `-1.00` | `4.97e-14` |
| `SIM07_CLEAN_SLATE_RING0_WSE` | `84.67 ± 1.22` | `45.9` | `1.22` | `0.077` | **`0.0%`** | **`408.2`** | `1.00` | `+0.34` | `2.22e-03` |
| `SIM08_HYBRID_CUBE_SLTC_XPBD` | **`85.48 ± 1.35`** | **`48.2`** | **`1.25`** | `0.076` | **`0.0%`** | **`406.9`** | `1.00` | **`+0.50`** | **`7.71e-06`** |

### 2. Five Live Companion Native C11/C23 Engines (`OVBS-52 = 92.05`, `244` Native + `36` Local = `280` Pure Lean 4)

| Layer / Repository | Verified Gates & Mutants | Pure Lean 4 Theorems |
| :--- | :--- | :---: |
| Tier 1 `AUTOPHAGE v1.3.0` | `18/18` falsification gates, $A_{\mathrm{new}}=29.463$, `0.0` thermo drift | `42` |
| Tier 2 `Cellulogonic Mecha v1.4.0` | `24/24` gates, `8/8` compiled mutants killed, `90.4%` cadherin sort | `62` |
| Tier 2+ `Cellular Engine Omega v5.1.0` | `54/54` gates, `16/16` mutants, `75` substrates, `1,000` Cube, CISS $ee=0.999735$ | `72` |
| Tier 3 `Noetic Organism Omega v2.0.0` | `13/13` CS-v3 Gates, `825/825` C11 checks (`0` fail, `29` `INDICATOR_ONLY`), `100/100` M, `5/5` mutants | `48` |
| Tier 3+4 `Asmodensius-Native` | LIVE C23 dual worlds, `77/77` ctests, 24C P+E & RTX 5070 Ti CUDA PTX parity | `20` |
| **Local Package (`lean/OmegaPackageProofs/`)** | **`36` core + `4` Palomar (`40` audited axioms), `leanchecker-paranoid` PASS** | **`36`** |
| **Ecosystem Total** | **Live Composite `OVBS-52 = 92.05` (`STAGE_5`) · `35/35` Native + `6/6` Python Mutants** | **`280`** |

---

## Master Repository Directory

See [`INDEX.md`](INDEX.md) for the complete generated file-by-file, byte-count, and token-count master index.

- **White Paper & Figures:** [`paper/main.tex`](paper/main.tex), [`paper/refs.bib`](paper/refs.bib), [`dist/Donahue_2026_alife_singularity_omega.pdf`](dist/Donahue_2026_alife_singularity_omega.pdf), [`dist/arxiv_submission.tar.gz`](dist/arxiv_submission.tar.gz)
- **Lean 4.35.0 Formal Proofs:** [`lean/`](lean/README.md), [`palomar/PalomarChallenge.lean`](palomar/PalomarChallenge.lean), [`blueprint/index.html`](blueprint/index.html), [`results/lean_package_axioms.txt`](results/lean_package_axioms.txt)
- **Interactive HTML5 & Lossless Vector PDFs (`< 2.5 MB` each):** [`html/`](html/ALife_Singularity_SuperLife_Omega_Dashboard.html), [`pdf/`](pdf/ALife_Singularity_SuperLife_Omega_Master_Dossier.pdf)
- **Structured Data (`24` CSVs = `2,822` rows, `4` Specs, `5` Excel Workbooks):** `csv/`, `specs/`, `excel/`, `pipelines/`, `results/`
- **Treatises & Audits (`12` Reports):** `reports/01`–`09` + 3 Clean-Slate v3.0 reports
- **Oracle, Tests & Verification:** [`reference/ovbs52_oracle.py`](reference/ovbs52_oracle.py), [`tests/`](tests/test_omega_package.py), [`scripts/run_mutation_audit.py`](scripts/run_mutation_audit.py), [`scripts/audit_omniscient_integrity.py`](scripts/audit_omniscient_integrity.py)
- **Governance & FAIR Metadata:** [`CLAIMS.md`](CLAIMS.md), [`EVIDENCE.md`](EVIDENCE.md), [`LIMITATIONS.md`](LIMITATIONS.md), [`VERIFICATION.md`](VERIFICATION.md), [`REPLICATION.md`](REPLICATION.md), [`PREREGISTRATION.md`](PREREGISTRATION.md), [`HARDENING_LOG.md`](HARDENING_LOG.md), [`repo.yaml`](repo.yaml), [`docs/`](docs/index.md), [`.zenodo.json`](.zenodo.json), [`croissant.json`](croissant.json), [`ro-crate-metadata.json`](ro-crate-metadata.json)

---

## Citation & Dual Licensing

Cite using [`CITATION.cff`](CITATION.cff) or [`CITATION.bib`](CITATION.bib):
- **Prose, White Paper, Documentation, Datasets & Figures:** [CC-BY-4.0](LICENSE)
- **Python Scripts, Lean 4 Formalizations, Tests, Oracle & HTML/JS Code:** [Apache-2.0](LICENSE-CODE)
