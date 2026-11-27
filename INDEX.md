# Master Repository Index & Table of Contents (`v3.5.0`)

Complete folder-by-folder, file-by-file inventory with exact byte sizes, line counts (text files), and approximate token counts (`~chars / 4`). Regenerate via `python scripts/generate_index_and_llms.py`.

## Folder Summary

| Folder | Files | Total Size (KB) |
| :--- | :---: | :---: |
| `(root)` | `51` | `393.9` |
| `.cursor` | `1` | `0.8` |
| `.github` | `9` | `13.2` |
| `blueprint` | `1` | `10.1` |
| `csv` | `24` | `1324.3` |
| `data` | `2` | `10.8` |
| `dist` | `2` | `455.2` |
| `docs` | `25` | `299.4` |
| `examples` | `2` | `3.3` |
| `excel` | `5` | `2701.9` |
| `html` | `3` | `3926.9` |
| `lean` | `17` | `48.4` |
| `paper` | `7` | `184.0` |
| `pdf` | `3` | `4919.4` |
| `pipelines` | `2` | `31.6` |
| `reference` | `1` | `3.4` |
| `reports` | `12` | `725.3` |
| `results` | `14` | `183.1` |
| `scripts` | `24` | `924.2` |
| `specs` | `4` | `5433.1` |
| `tests` | `2` | `16.9` |
| **TOTAL** | **`211`** | **`21609.2`** |

## Complete File Inventory

### `(root)`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`.editorconfig`](.editorconfig) | `363` | `23` | `~90` |
| [`.env.example`](.env.example) | `729` | `—` | `binary` |
| [`.gitattributes`](.gitattributes) | `411` | `26` | `~102` |
| [`.gitignore`](.gitignore) | `671` | `39` | `~167` |
| [`.gitleaks.toml`](.gitleaks.toml) | `391` | `15` | `~97` |
| [`.zenodo.json`](.zenodo.json) | `2,141` | `40` | `~535` |
| [`AGENTS.md`](AGENTS.md) | `4,100` | `40` | `~1,020` |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | `2,982` | `29` | `~490` |
| [`AUTHORS.md`](AUTHORS.md) | `1,264` | `18` | `~315` |
| [`CHANGELOG.md`](CHANGELOG.md) | `9,612` | `64` | `~2,401` |
| [`CHECKSUMS.sha256`](CHECKSUMS.sha256) | `20,268` | `—` | `binary` |
| [`CITATION.bib`](CITATION.bib) | `682` | `10` | `~170` |
| [`CITATION.cff`](CITATION.cff) | `1,925` | `37` | `~481` |
| [`CLAIMS.md`](CLAIMS.md) | `9,425` | `35` | `~2,352` |
| [`CLAUDE.md`](CLAUDE.md) | `11` | `1` | `~2` |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | `1,273` | `20` | `~318` |
| [`codemeta.json`](codemeta.json) | `2,001` | `59` | `~500` |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | `1,803` | `25` | `~449` |
| [`croissant.json`](croissant.json) | `2,249` | `60` | `~562` |
| [`DEVIATIONS.md`](DEVIATIONS.md) | `3,234` | `15` | `~807` |
| [`ERRATA.md`](ERRATA.md) | `11,701` | `55` | `~2,924` |
| [`EVIDENCE.md`](EVIDENCE.md) | `3,078` | `14` | `~768` |
| [`GEMINI.md`](GEMINI.md) | `13` | `1` | `~3` |
| [`HANDOFF.md`](HANDOFF.md) | `3,329` | `31` | `~832` |
| [`HARDENING_LOG.md`](HARDENING_LOG.md) | `14,043` | `61` | `~3,506` |
| [`INDEX.md`](INDEX.md) | `24,454` | `351` | `~6,103` |
| [`justfile`](justfile) | `3,162` | `70` | `~790` |
| [`LICENSE`](LICENSE) | `6,039` | `117` | `~1,509` |
| [`LICENSE-DOCS`](LICENSE-DOCS) | `9,774` | `200` | `~2,443` |
| [`LIMITATIONS.md`](LIMITATIONS.md) | `7,717` | `31` | `~1,927` |
| [`llms-full.txt`](llms-full.txt) | `122,348` | `887` | `~30,521` |
| [`llms.txt`](llms.txt) | `3,344` | `36` | `~835` |
| [`MANIFEST.json`](MANIFEST.json) | `34,691` | `1,039` | `~8,672` |
| [`MANIFEST_SHA256.txt`](MANIFEST_SHA256.txt) | `23,421` | `210` | `~5,854` |
| [`NOTICE`](NOTICE) | `603` | `11` | `~150` |
| [`PREREGISTRATION.md`](PREREGISTRATION.md) | `3,735` | `19` | `~929` |
| [`pyproject.toml`](pyproject.toml) | `1,677` | `62` | `~419` |
| [`README.md`](README.md) | `19,527` | `206` | `~4,872` |
| [`REPLICATION.md`](REPLICATION.md) | `3,415` | `69` | `~853` |
| [`repo-standard.schema.json`](repo-standard.schema.json) | `5,417` | `245` | `~1,354` |
| [`repo.yaml`](repo.yaml) | `11,919` | `117` | `~2,979` |
| [`requirements.txt`](requirements.txt) | `381` | `15` | `~95` |
| [`ro-crate-metadata.json`](ro-crate-metadata.json) | `2,497` | `49` | `~624` |
| [`ROADMAP.md`](ROADMAP.md) | `1,932` | `19` | `~481` |
| [`SECURITY.md`](SECURITY.md) | `1,040` | `20` | `~260` |
| [`SUBMISSION_READINESS.md`](SUBMISSION_READINESS.md) | `9,502` | `49` | `~2,370` |
| [`SUPPORT.md`](SUPPORT.md) | `589` | `9` | `~147` |
| [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) | `2,340` | `19` | `~584` |
| [`UPGRADING.md`](UPGRADING.md) | `2,520` | `20` | `~630` |
| [`VERIFICATION.md`](VERIFICATION.md) | `3,582` | `23` | `~891` |
| [`VERSION`](VERSION) | `6` | `1` | `~1` |

### `.cursor`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`.cursor/rules/build-standard.mdc`](.cursor/rules/build-standard.mdc) | `775` | `11` | `~193` |

### `.github`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`.github/ISSUE_TEMPLATE/academic-review.yml`](.github/ISSUE_TEMPLATE/academic-review.yml) | `1,117` | `32` | `~277` |
| [`.github/ISSUE_TEMPLATE/bug.yml`](.github/ISSUE_TEMPLATE/bug.yml) | `1,923` | `52` | `~480` |
| [`.github/ISSUE_TEMPLATE/config.yml`](.github/ISSUE_TEMPLATE/config.yml) | `456` | `8` | `~114` |
| [`.github/ISSUE_TEMPLATE/feature.yml`](.github/ISSUE_TEMPLATE/feature.yml) | `605` | `25` | `~151` |
| [`.github/ISSUE_TEMPLATE/question.yml`](.github/ISSUE_TEMPLATE/question.yml) | `429` | `17` | `~107` |
| [`.github/labels.tsv`](.github/labels.tsv) | `1,122` | `17` | `~280` |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | `5,193` | `117` | `~1,297` |
| [`.github/workflows/pages.yml`](.github/workflows/pages.yml) | `1,162` | `44` | `~290` |
| [`.github/workflows/release.yml`](.github/workflows/release.yml) | `1,512` | `42` | `~378` |

### `blueprint`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`blueprint/index.html`](blueprint/index.html) | `10,380` | `126` | `~2,594` |

### `csv`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`csv/01_escalation_ladder_ai_vs_alife_matrix.csv`](csv/01_escalation_ladder_ai_vs_alife_matrix.csv) | `7,161` | `8` | `~1,787` |
| [`csv/02_orders_of_magnitude_breadth_depth_matrix.csv`](csv/02_orders_of_magnitude_breadth_depth_matrix.csv) | `10,877` | `19` | `~2,713` |
| [`csv/03_failure_modes_bugs_errors_conflicts_matrix.csv`](csv/03_failure_modes_bugs_errors_conflicts_matrix.csv) | `28,020` | `43` | `~7,000` |
| [`csv/04_gaps_holes_blindspots_registry.csv`](csv/04_gaps_holes_blindspots_registry.csv) | `16,734` | `29` | `~4,177` |
| [`csv/05_constraint_castration_impact_matrix.csv`](csv/05_constraint_castration_impact_matrix.csv) | `9,666` | `14` | `~2,413` |
| [`csv/06_alifeops_devops_pipeline_stages.csv`](csv/06_alifeops_devops_pipeline_stages.csv) | `21,212` | `41` | `~5,302` |
| [`csv/07_master_operational_checklist.csv`](csv/07_master_operational_checklist.csv) | `38,580` | `131` | `~9,644` |
| [`csv/08_super_life_benchmarks_suite.csv`](csv/08_super_life_benchmarks_suite.csv) | `22,196` | `53` | `~5,548` |
| [`csv/09_feral_fate_branches_cosmic_epochs.csv`](csv/09_feral_fate_branches_cosmic_epochs.csv) | `14,761` | `31` | `~3,688` |
| [`csv/10_castration_13x13_synergy_matrix.csv`](csv/10_castration_13x13_synergy_matrix.csv) | `1,583` | `14` | `~395` |
| [`csv/11_empirical_simulation_results.csv`](csv/11_empirical_simulation_results.csv) | `2,316` | `9` | `~578` |
| [`csv/12_v3_substrates_75_and_wse_10_matrix.csv`](csv/12_v3_substrates_75_and_wse_10_matrix.csv) | `29,562` | `86` | `~7,355` |
| [`csv/13_v3_forensic_36_and_release_gates_13_matrix.csv`](csv/13_v3_forensic_36_and_release_gates_13_matrix.csv) | `17,862` | `50` | `~4,417` |
| [`csv/14_omniscient_cross_corpus_traceability_matrix.csv`](csv/14_omniscient_cross_corpus_traceability_matrix.csv) | `15,031` | `49` | `~3,757` |
| [`csv/15_gradients_margins_and_phase_spectrums_matrix.csv`](csv/15_gradients_margins_and_phase_spectrums_matrix.csv) | `9,229` | `25` | `~2,306` |
| [`csv/16_comparative_contrast_layers_taxonomies_matrix.csv`](csv/16_comparative_contrast_layers_taxonomies_matrix.csv) | `21,496` | `37` | `~5,373` |
| [`csv/17_adjacent_possible_and_substrate_adjacencies_matrix.csv`](csv/17_adjacent_possible_and_substrate_adjacencies_matrix.csv) | `13,617` | `31` | `~3,403` |
| [`csv/18_layer_11x11_coupling_impedance_matrix.csv`](csv/18_layer_11x11_coupling_impedance_matrix.csv) | `1,983` | `12` | `~495` |
| [`csv/19_substrate_spectrum_comparative_scorecard.csv`](csv/19_substrate_spectrum_comparative_scorecard.csv) | `3,632` | `16` | `~907` |
| [`csv/20_pareto_frontiers_and_dilemmas_matrix.csv`](csv/20_pareto_frontiers_and_dilemmas_matrix.csv) | `9,182` | `21` | `~2,295` |
| [`csv/21_mega_atlas_1900_open_problems_crosswalk.csv`](csv/21_mega_atlas_1900_open_problems_crosswalk.csv) | `15,076` | `26` | `~3,768` |
| [`csv/ALife-Framework-v3.0-Master-Checklists.csv`](csv/ALife-Framework-v3.0-Master-Checklists.csv) | `500,506` | `939` | `~123,834` |
| [`csv/ALife-Hybrid-Cube-10x10x10.csv`](csv/ALife-Hybrid-Cube-10x10x10.csv) | `343,407` | `1,001` | `~85,696` |
| [`csv/ALife-v3.0-Errata-Closure-Register.csv`](csv/ALife-v3.0-Errata-Closure-Register.csv) | `202,413` | `161` | `~50,484` |

### `data`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`data/MANIFEST.sha256`](data/MANIFEST.sha256) | `5,073` | `—` | `binary` |
| [`data/timestamps/CHECKSUMS.sha256.tsr`](data/timestamps/CHECKSUMS.sha256.tsr) | `5,996` | `—` | `binary` |

### `dist`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`dist/arxiv_submission.tar.gz`](dist/arxiv_submission.tar.gz) | `147,608` | `—` | `binary` |
| [`dist/Donahue_2026_alife_singularity_omega.pdf`](dist/Donahue_2026_alife_singularity_omega.pdf) | `318,487` | `—` | `binary` |

### `docs`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`docs/ACADEMIC_REVIEW.md`](docs/ACADEMIC_REVIEW.md) | `2,831` | `25` | `~706` |
| [`docs/adr/0001-zero-consolidation-dual-drive-fusion.md`](docs/adr/0001-zero-consolidation-dual-drive-fusion.md) | `1,199` | `14` | `~299` |
| [`docs/adr/0002-ring0-acl-vs-behavioral-castration.md`](docs/adr/0002-ring0-acl-vs-behavioral-castration.md) | `1,425` | `14` | `~355` |
| [`docs/adr/0003-zero-mathlib-lean4-and-palomar-boundary.md`](docs/adr/0003-zero-mathlib-lean4-and-palomar-boundary.md) | `1,366` | `14` | `~341` |
| [`docs/adr/0004-sub-5mb-lossless-pdf-and-release-zip.md`](docs/adr/0004-sub-5mb-lossless-pdf-and-release-zip.md) | `1,231` | `15` | `~307` |
| [`docs/adr/README.md`](docs/adr/README.md) | `703` | `8` | `~175` |
| [`docs/AI_DISCLOSURE.md`](docs/AI_DISCLOSURE.md) | `2,802` | `27` | `~700` |
| [`docs/architecture.md`](docs/architecture.md) | `4,120` | `51` | `~982` |
| [`docs/benchmarks.md`](docs/benchmarks.md) | `1,801` | `24` | `~447` |
| [`docs/build-standard.md`](docs/build-standard.md) | `109,226` | `1,742` | `~27,283` |
| [`docs/configuration.md`](docs/configuration.md) | `1,554` | `17` | `~388` |
| [`docs/DATASHEET.md`](docs/DATASHEET.md) | `3,301` | `28` | `~824` |
| [`docs/faq.md`](docs/faq.md) | `3,590` | `22` | `~896` |
| [`docs/glossary.md`](docs/glossary.md) | `4,096` | `35` | `~1,023` |
| [`docs/index.md`](docs/index.md) | `2,281` | `26` | `~559` |
| [`docs/media/social-preview.png`](docs/media/social-preview.png) | `122,787` | `—` | `binary` |
| [`docs/MEGA_ATLAS_CROSSCHECK.md`](docs/MEGA_ATLAS_CROSSCHECK.md) | `9,437` | `45` | `~2,349` |
| [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) | `4,061` | `25` | `~1,013` |
| [`docs/operations.md`](docs/operations.md) | `1,719` | `28` | `~429` |
| [`docs/PRESERVATION.md`](docs/PRESERVATION.md) | `1,803` | `16` | `~450` |
| [`docs/reviews/2026-11-25-three-cycle-redteam-hardening.md`](docs/reviews/2026-11-25-three-cycle-redteam-hardening.md) | `3,989` | `28` | `~995` |
| [`docs/reviews/2026-11-26-round2-3-cycle-hardening-audit.md`](docs/reviews/2026-11-26-round2-3-cycle-hardening-audit.md) | `7,622` | `25` | `~1,899` |
| [`docs/run-log.md`](docs/run-log.md) | `3,879` | `19` | `~968` |
| [`docs/statement-fidelity.md`](docs/statement-fidelity.md) | `6,991` | `22` | `~1,746` |
| [`docs/threat-model.md`](docs/threat-model.md) | `2,756` | `20` | `~689` |

### `examples`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`examples/quickstart_demo.py`](examples/quickstart_demo.py) | `2,894` | `69` | `~723` |
| [`examples/README.md`](examples/README.md) | `526` | `11` | `~131` |

### `excel`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`excel/ALife-Framework-v3.0-Master-Workbook.xls`](excel/ALife-Framework-v3.0-Master-Workbook.xls) | `1,198,592` | `—` | `binary` |
| [`excel/ALife-Framework-v3.0-Master-Workbook.xlsx`](excel/ALife-Framework-v3.0-Master-Workbook.xlsx) | `417,271` | `—` | `binary` |
| [`excel/ALife-Hybrid-Cube-10x10x10.xlsx`](excel/ALife-Hybrid-Cube-10x10x10.xlsx) | `101,139` | `—` | `binary` |
| [`excel/ALife_Singularity_SuperLife_Omega_Workbook.xls`](excel/ALife_Singularity_SuperLife_Omega_Workbook.xls) | `732,160` | `—` | `binary` |
| [`excel/ALife_Singularity_SuperLife_Omega_Workbook.xlsx`](excel/ALife_Singularity_SuperLife_Omega_Workbook.xlsx) | `317,630` | `—` | `binary` |

### `html`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`html/ALife-Build-Framework-Template.html`](html/ALife-Build-Framework-Template.html) | `791,859` | `3,026` | `~196,632` |
| [`html/ALife_Singularity_SuperLife_Omega_Dashboard.html`](html/ALife_Singularity_SuperLife_Omega_Dashboard.html) | `2,547,441` | `3,292` | `~634,788` |
| [`html/Clean-Slate-Creature-Blueprint-Checklist.html`](html/Clean-Slate-Creature-Blueprint-Checklist.html) | `681,876` | `2,915` | `~169,181` |

### `lean`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`lean/Challenge.lean`](lean/Challenge.lean) | `1,670` | `44` | `~394` |
| [`lean/comparator.json`](lean/comparator.json) | `517` | `16` | `~129` |
| [`lean/formalization.yaml`](lean/formalization.yaml) | `6,579` | `131` | `~1,644` |
| [`lean/lake-manifest.json`](lean/lake-manifest.json) | `150` | `6` | `~37` |
| [`lean/lakefile.toml`](lean/lakefile.toml) | `492` | `26` | `~123` |
| [`lean/lean-toolchain`](lean/lean-toolchain) | `25` | `—` | `binary` |
| [`lean/OmegaPackageProofs/AdversarialTests.lean`](lean/OmegaPackageProofs/AdversarialTests.lean) | `3,986` | `94` | `~975` |
| [`lean/OmegaPackageProofs/CastrationAndRing0.lean`](lean/OmegaPackageProofs/CastrationAndRing0.lean) | `7,583` | `165` | `~1,877` |
| [`lean/OmegaPackageProofs/EscalationAndCube.lean`](lean/OmegaPackageProofs/EscalationAndCube.lean) | `2,939` | `63` | `~731` |
| [`lean/OmegaPackageProofs/NonVacuity.lean`](lean/OmegaPackageProofs/NonVacuity.lean) | `2,926` | `59` | `~719` |
| [`lean/OmegaPackageProofs/OVBS52Scoring.lean`](lean/OmegaPackageProofs/OVBS52Scoring.lean) | `9,169` | `206` | `~2,264` |
| [`lean/OmegaPackageProofs/VerifyAxioms.lean`](lean/OmegaPackageProofs/VerifyAxioms.lean) | `4,274` | `68` | `~1,068` |
| [`lean/OmegaPackageProofs.lean`](lean/OmegaPackageProofs.lean) | `291` | `8` | `~72` |
| [`lean/palomar/PalomarChallenge.lean`](lean/palomar/PalomarChallenge.lean) | `2,476` | `62` | `~593` |
| [`lean/PalomarSolution.lean`](lean/PalomarSolution.lean) | `2,801` | `65` | `~669` |
| [`lean/README.md`](lean/README.md) | `2,534` | `27` | `~633` |
| [`lean/Solution.lean`](lean/Solution.lean) | `1,128` | `36` | `~278` |

### `paper`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`paper/figures/fig01_dual_sweep_pareto.pdf`](paper/figures/fig01_dual_sweep_pareto.pdf) | `38,276` | `—` | `binary` |
| [`paper/figures/fig02_8cohort_ovi_fwer.pdf`](paper/figures/fig02_8cohort_ovi_fwer.pdf) | `32,507` | `—` | `binary` |
| [`paper/figures/fig03_2d_phase_surface.pdf`](paper/figures/fig03_2d_phase_surface.pdf) | `34,770` | `—` | `binary` |
| [`paper/figures/fig04_5engine_pillars_lean.pdf`](paper/figures/fig04_5engine_pillars_lean.pdf) | `36,839` | `—` | `binary` |
| [`paper/generated_tables.tex`](paper/generated_tables.tex) | `1,620` | `16` | `~405` |
| [`paper/main.tex`](paper/main.tex) | `36,332` | `270` | `~9,083` |
| [`paper/refs.bib`](paper/refs.bib) | `8,052` | `196` | `~2,013` |

### `pdf`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`pdf/ALife-Build-Framework-Template.pdf`](pdf/ALife-Build-Framework-Template.pdf) | `2,316,145` | `—` | `binary` |
| [`pdf/ALife_Singularity_SuperLife_Omega_Master_Dossier.pdf`](pdf/ALife_Singularity_SuperLife_Omega_Master_Dossier.pdf) | `538,849` | `—` | `binary` |
| [`pdf/Clean-Slate-Creature-Blueprint-Checklist.pdf`](pdf/Clean-Slate-Creature-Blueprint-Checklist.pdf) | `2,182,441` | `—` | `binary` |

### `pipelines`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`pipelines/alifeops-master-pipeline.yaml`](pipelines/alifeops-master-pipeline.yaml) | `27,019` | `402` | `~6,754` |
| [`pipelines/benchmark-suite-schema.json`](pipelines/benchmark-suite-schema.json) | `5,305` | `133` | `~1,326` |

### `reference`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`reference/ovbs52_oracle.py`](reference/ovbs52_oracle.py) | `3,511` | `97` | `~877` |

### `reports`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`reports/01_MASTER_DEEP_DIVE_REPORT.md`](reports/01_MASTER_DEEP_DIVE_REPORT.md) | `53,615` | `408` | `~13,091` |
| [`reports/02_DEVOPS_ALIFEOPS_PIPELINE_ARCHITECTURE.md`](reports/02_DEVOPS_ALIFEOPS_PIPELINE_ARCHITECTURE.md) | `29,311` | `214` | `~7,032` |
| [`reports/03_FAILURE_MODES_GAPS_AND_CASTRATION_ATLAS.md`](reports/03_FAILURE_MODES_GAPS_AND_CASTRATION_ATLAS.md) | `38,438` | `206` | `~9,577` |
| [`reports/04_BENCHMARKS_CHECKLISTS_AND_MATRICES_MANUAL.md`](reports/04_BENCHMARKS_CHECKLISTS_AND_MATRICES_MANUAL.md) | `20,627` | `159` | `~5,125` |
| [`reports/05_HARD_SCIFI_FERAL_COSMOS_SCENARIOS_AND_CHRONICLES.md`](reports/05_HARD_SCIFI_FERAL_COSMOS_SCENARIOS_AND_CHRONICLES.md) | `22,551` | `146` | `~5,588` |
| [`reports/06_OMNISCIENT_UNIFIED_ARCHITECTURE_AND_SYSTEMS_SYNTHESIS.md`](reports/06_OMNISCIENT_UNIFIED_ARCHITECTURE_AND_SYSTEMS_SYNTHESIS.md) | `17,845` | `118` | `~4,430` |
| [`reports/07_PASS4_COMPARATIVE_CONTRAST_GRADIENTS_MARGINS_AND_ADJACENTS_AUDIT.md`](reports/07_PASS4_COMPARATIVE_CONTRAST_GRADIENTS_MARGINS_AND_ADJACENTS_AUDIT.md) | `31,821` | `170` | `~7,901` |
| [`reports/08_PASS5_LAYER_COUPLING_SUBSTRATE_SPECTRUMS_PARETO_AND_2D_PHASE_AUDIT.md`](reports/08_PASS5_LAYER_COUPLING_SUBSTRATE_SPECTRUMS_PARETO_AND_2D_PHASE_AUDIT.md) | `27,256` | `159` | `~6,769` |
| [`reports/09_MEGA_ATLAS_1900_OPEN_PROBLEMS_CROSSCHECK.md`](reports/09_MEGA_ATLAS_1900_OPEN_PROBLEMS_CROSSCHECK.md) | `15,282` | `81` | `~3,806` |
| [`reports/ALife-Build-Framework-Template.md`](reports/ALife-Build-Framework-Template.md) | `249,049` | `1,613` | `~61,267` |
| [`reports/ALife-v3.0-Errata-Closure-Report.md`](reports/ALife-v3.0-Errata-Closure-Report.md) | `44,751` | `188` | `~11,150` |
| [`reports/Clean-Slate-Creature-Blueprint-Checklist.md`](reports/Clean-Slate-Creature-Blueprint-Checklist.md) | `192,174` | `1,199` | `~47,155` |

### `results`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`results/alifeops_live_verification.json`](results/alifeops_live_verification.json) | `15,925` | `541` | `~3,981` |
| [`results/bench-history.csv`](results/bench-history.csv) | `726` | `7` | `~181` |
| [`results/citation_verification.json`](results/citation_verification.json) | `6,605` | `226` | `~1,651` |
| [`results/empirical_sim_summary.json`](results/empirical_sim_summary.json) | `63,142` | `2,307` | `~15,785` |
| [`results/lean4-multi-kernel.txt`](results/lean4-multi-kernel.txt) | `3,101` | `44` | `~774` |
| [`results/lean_package_axioms.txt`](results/lean_package_axioms.txt) | `5,275` | `55` | `~1,318` |
| [`results/ovbs52_scorecard_SIM01_PURE_RAW_FERAL.json`](results/ovbs52_scorecard_SIM01_PURE_RAW_FERAL.json) | `11,706` | `416` | `~2,926` |
| [`results/ovbs52_scorecard_SIM02_CONSTITUTIONAL_MIN.json`](results/ovbs52_scorecard_SIM02_CONSTITUTIONAL_MIN.json) | `11,745` | `416` | `~2,936` |
| [`results/ovbs52_scorecard_SIM03_PARTIAL_GUARDRAILS.json`](results/ovbs52_scorecard_SIM03_PARTIAL_GUARDRAILS.json) | `11,461` | `416` | `~2,865` |
| [`results/ovbs52_scorecard_SIM04_TOTAL_CASTRATION_ZOO.json`](results/ovbs52_scorecard_SIM04_TOTAL_CASTRATION_ZOO.json) | `11,165` | `416` | `~2,791` |
| [`results/ovbs52_scorecard_SIM05_SILOED_INBRED.json`](results/ovbs52_scorecard_SIM05_SILOED_INBRED.json) | `11,653` | `416` | `~2,913` |
| [`results/ovbs52_scorecard_SIM06_MINIMIZED_SPIEGELMAN.json`](results/ovbs52_scorecard_SIM06_MINIMIZED_SPIEGELMAN.json) | `11,531` | `416` | `~2,882` |
| [`results/ovbs52_scorecard_SIM07_CLEAN_SLATE_RING0_WSE.json`](results/ovbs52_scorecard_SIM07_CLEAN_SLATE_RING0_WSE.json) | `11,722` | `416` | `~2,930` |
| [`results/ovbs52_scorecard_SIM08_HYBRID_CUBE_SLTC_XPBD.json`](results/ovbs52_scorecard_SIM08_HYBRID_CUBE_SLTC_XPBD.json) | `11,731` | `416` | `~2,932` |

### `scripts`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`scripts/audit-checks.tsv`](scripts/audit-checks.tsv) | `8,356` | `107` | `~2,089` |
| [`scripts/Audit-Repo.ps1`](scripts/Audit-Repo.ps1) | `17,136` | `249` | `~4,283` |
| [`scripts/audit-repo.sh`](scripts/audit-repo.sh) | `14,011` | `204` | `~3,502` |
| [`scripts/audit_omniscient_integrity.py`](scripts/audit_omniscient_integrity.py) | `46,065` | `730` | `~11,503` |
| [`scripts/benchmark_omega.py`](scripts/benchmark_omega.py) | `5,492` | `123` | `~1,369` |
| [`scripts/build_html_dashboard.py`](scripts/build_html_dashboard.py) | `147,014` | `1,974` | `~36,737` |
| [`scripts/build_omega_package.py`](scripts/build_omega_package.py) | `48,282` | `786` | `~12,068` |
| [`scripts/build_paper.py`](scripts/build_paper.py) | `319` | `11` | `~79` |
| [`scripts/build_paper_and_figures.py`](scripts/build_paper_and_figures.py) | `19,831` | `418` | `~4,953` |
| [`scripts/build_v3_unified_artifacts.py`](scripts/build_v3_unified_artifacts.py) | `87,074` | `1,325` | `~21,727` |
| [`scripts/check_citations.py`](scripts/check_citations.py) | `5,888` | `149` | `~1,472` |
| [`scripts/check_readme_axioms.py`](scripts/check_readme_axioms.py) | `2,239` | `53` | `~559` |
| [`scripts/generate_index_and_llms.py`](scripts/generate_index_and_llms.py) | `4,914` | `115` | `~1,227` |
| [`scripts/omega_datasets_part1.py`](scripts/omega_datasets_part1.py) | `73,671` | `1,041` | `~18,402` |
| [`scripts/omega_datasets_part2.py`](scripts/omega_datasets_part2.py) | `79,211` | `581` | `~19,802` |
| [`scripts/omega_datasets_part3.py`](scripts/omega_datasets_part3.py) | `86,338` | `857` | `~21,581` |
| [`scripts/omega_datasets_part4.py`](scripts/omega_datasets_part4.py) | `64,814` | `634` | `~16,203` |
| [`scripts/omega_datasets_part5.py`](scripts/omega_datasets_part5.py) | `36,254` | `307` | `~9,062` |
| [`scripts/omega_datasets_part6.py`](scripts/omega_datasets_part6.py) | `32,805` | `280` | `~8,200` |
| [`scripts/run_alife_castration_sim.py`](scripts/run_alife_castration_sim.py) | `52,945` | `1,086` | `~13,236` |
| [`scripts/run_alifeops_suite.py`](scripts/run_alifeops_suite.py) | `37,046` | `661` | `~9,261` |
| [`scripts/run_mutation_audit.py`](scripts/run_mutation_audit.py) | `4,240` | `117` | `~1,059` |
| [`scripts/svg_architecture_models.py`](scripts/svg_architecture_models.py) | `63,043` | `878` | `~15,685` |
| [`scripts/test_lean_negative.py`](scripts/test_lean_negative.py) | `9,354` | `202` | `~2,334` |

### `specs`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`specs/ALife-Framework-v3.0-Master-Spec.json`](specs/ALife-Framework-v3.0-Master-Spec.json) | `2,408,522` | `47,761` | `~600,384` |
| [`specs/ALife-Framework-v3.0-Master-Spec.txt`](specs/ALife-Framework-v3.0-Master-Spec.txt) | `337,428` | `1,572` | `~82,985` |
| [`specs/ALife-Framework-v3.0-Master-Spec.xml`](specs/ALife-Framework-v3.0-Master-Spec.xml) | `758,616` | `3,615` | `~188,401` |
| [`specs/ALife-Framework-v3.0-Master-Spec.yaml`](specs/ALife-Framework-v3.0-Master-Spec.yaml) | `2,058,917` | `42,314` | `~502,404` |

### `tests`

| File | Size (B) | Lines | Approx Tokens |
| :--- | :---: | :---: | :---: |
| [`tests/test_omega_package.py`](tests/test_omega_package.py) | `11,586` | `246` | `~2,896` |
| [`tests/test_properties_and_differential.py`](tests/test_properties_and_differential.py) | `5,765` | `130` | `~1,441` |

---
*Estimated text corpus tokens across indexable text artifacts: `~3,363,282` tokens.*
