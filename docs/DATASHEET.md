# Datasheet for Datasets (Gebru et al., 2021)

Following Gebru et al. (2021), *Datasheets for Datasets*, *Communications of the ACM* 64(12):86–92 (`DOI: 10.1145/3458723`), this datasheet documents the `24` canonical CSV tables (`2,822` total rows) and `4`-format Master Specifications shipped in `alife-singularity-omega-package` (`v3.5.0`).

## 1. Motivation
- **Purpose:** Provide an open, machine-readable, cryptographically checksummed scientific engineering corpus spanning A-Life Singularity metrology (`OVBS-52`), 13-vector constraint castration, `748`-run paired empirical falsification, Clean-Slate v3.0 micro-hardware specifications (`938` checklists, `10x10x10` Hybrid Cube, `75` substrates, `160` errata closures), and the `1,900`-problem Mega-Atlas non-retirement crosswalk.
- **Creator:** Alexander Stephen Donahue (`Independent Researcher, Spokane, WA, USA`, ORCID `0009-0006-8168-9648`).
- **Funding:** None (self-funded independent research).

## 2. Composition
- **Instances:** `24` UTF-8 CSV files (`2,822` structured rows total), mirrored identically in `specs/ALife-Framework-v3.0-Master-Spec.{json,yaml,xml,txt}` and `5` Excel workbooks (`excel/`).
- **Exact File Inventory:** Locked with SHA-256 hashes in [`data/MANIFEST.sha256`](../data/MANIFEST.sha256), [`CHECKSUMS.sha256`](../CHECKSUMS.sha256), and [`MANIFEST.json`](../MANIFEST.json).
- **Sensitive / Personal Data:** **None.** Zero human subjects, zero PII, zero confidential/proprietary records.
- **Data Provenance Categories:**
  - *Deterministic Empirical Simulation Output:* `csv/11_empirical_simulation_results.csv`, `results/empirical_sim_summary.json`, `results/ovbs52_scorecard_SIM01..08.json`.
  - *Live Native Engine Receipts:* `results/alifeops_live_verification.json` (`5` C11/C23 engines).
  - *Formalized / Schema-Locked Specifications:* `csv/ALife-Hybrid-Cube-10x10x10.csv` (`1,000` rows), `csv/ALife-Framework-v3.0-Master-Checklists.csv` (`938` rows), `csv/12`, `csv/13`, `csv/14`, `csv/21`.
  - *Declared Engineering Rubrics (`EDITORIAL-ESTIMATE`):* `csv/10` (`13x13` castration synergy), `csv/18` (`11x11` layer impedance), `csv/19` (`15`-substrate comparative scorecard).

## 3. Collection & Generation Process
- Generated reproducibly by `scripts/build_omega_package.py` from `scripts/omega_datasets_part1..6.py`, `scripts/run_alife_castration_sim.py` (locked seeds `5001–5048`), and `scripts/run_alifeops_suite.py`.
- Validated automatically by Gate 2 (exact row counts), Gate 3 (`130/130` FK pointers), Gate 5 (`9/9` JSON Schema Draft 2020-12), Gate 7 (`JSON == YAML == 26-section XML`), and Gate 15 (`24/24` CSV column parity + `78/78` YAML alert FKs).

## 4. Uses, Distribution & Maintenance
- **Recommended Uses:** Reproducible A-Life benchmarking, formal-verification education, governance safety-vs-vitality research, and independent replication.
- **Out-of-Scope Uses:** Treating engineering rubrics (`csv/10`, `csv/18`, `csv/19`) as wet-lab physical constants, or interpreting `INDICATOR_ONLY` cognitive metrics as proof of sentience.
- **License:** `CC-BY-4.0` ([`LICENSE`](../LICENSE)); machine-readable FAIR descriptors in `croissant.json` and `ro-crate-metadata.json`.
- **Maintenance:** Active (`v3.5.0`), versioned via Semantic Versioning (`VERSION`, `CHANGELOG.md`, `ERRATA.md`).
