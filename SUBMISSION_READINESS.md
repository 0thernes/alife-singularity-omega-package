# Gold Standard Submission Readiness Checklist (`v3.5.0`)

Itemized 43-item evaluation against **Defensible Independent AI Research Playbook v1.3 (Section 8)** and **Build Standard for LLMs v1.2.0** (`90` items). Every status below is strictly evidence-backed with zero fabricated DOIs, zero fabricated external peer review, and zero unformed legal entities.

| # | Playbook v1.3 Item | Status | Concrete Evidence / Honest Boundary |
| :---: | :--- | :---: | :--- |
| 1 | Claims ledger with explicit epistemic tags | **PASS** | [`CLAIMS.md`](CLAIMS.md) & `paper/main.tex` Table 1 (`C1–C8`: `kernel-checked`, `empirical-paired`, `program-audited`, `editorial-est.`, `open-conj.`). |
| 2 | Zero `sorry`, `admit`, `native_decide`, custom axiom | **PASS** | `0` hits across `lean/` (excluding isolated `lean/palomar/PalomarChallenge.lean` challenge stubs); enforced by pytest, Gate 19 & CI. |
| 3 | `#print axioms` strictly within allowed axioms | **PASS** | `55/55` lines strictly `<= [propext, Quot.sound]` (zero `Classical.choice`) in [`results/lean_package_axioms.txt`](results/lean_package_axioms.txt). |
| 4 | Verbatim `#print axioms` block in `README.md` | **PASS** | Exact 55-line block checked 1:1 by [`scripts/check_readme_axioms.py`](scripts/check_readme_axioms.py) in CI & Gate 22. |
| 5 | Lean linters clean (zero-Mathlib justification) | **PASS** | Zero-Mathlib trust base (`autoImplicit = false`, `linter.unusedVariables = true`, `linter.deprecated = true`); 0 compiler warnings. |
| 6 | Clean build from empty `.lake` with pinned toolchain | **PASS** | `lean/lean-toolchain` pinned to `leanprover/lean4:v4.35.0`; clean `lake clean && lake build` verified locally & on Ubuntu CI. |
| 7 | `lake check --paranoid` + 6 independent kernels | **PASS** | Local 5-kernel check (`lean4`, `leanchecker`, `leanchecker-paranoid`, `nanoda_bin`, `con-leche`, `con-ron`) + full 6/6 Linux CI (`+ lean4lean`, `lake check --paranoid`). |
| 8 | Non-vacuity witness for every hypothesis bundle | **PASS** | [`lean/OmegaPackageProofs/NonVacuity.lean`](lean/OmegaPackageProofs/NonVacuity.lean) (`6` witnesses) + `ring1_ring2_plasticity_reachable`. |
| 9 | `lake comparator --paranoid` & Palomar rules | **PASS** | All Lean files have `module` headers (`< 250` lines each), `Challenge.lean` / `PalomarSolution.lean` / `comparator.json` (`m1..m5`) verified in Ubuntu `bwrap`. |
| 10 | Statement-fidelity matrix signed off | **PASS** | [`docs/statement-fidelity.md`](docs/statement-fidelity.md) & `paper/main.tex` Table 3 explicitly disclose arithmetic-vs-geometric OVI, `rfl` locks vs. quantified proofs, and discrete vs. silicon Ring-0 scope. |
| 11 | Interactive Lean Proof Blueprint on GitHub Pages | **PASS** | [`blueprint/index.html`](blueprint/index.html) (strict CSP, WCAG 2.2 AA landmarks, DAG + M1–M5 table) deployed by `.github/workflows/pages.yml`. |
| 12 | Adversarial definition tests & negative rejection | **PASS** | [`lean/OmegaPackageProofs/AdversarialTests.lean`](lean/OmegaPackageProofs/AdversarialTests.lean) (`10` Lean `¬(...)` refutations) + [`scripts/test_lean_negative.py`](scripts/test_lean_negative.py) (live kernel & comparator tamper rejection). |
| 13 | SAT certificates (`drat-trim -> cake_lpr`) | **N/A** | No SAT/DRAT solver dependency in this package; all proofs are pure constructive Lean 4.35.0. |
| 14 | CNF encoder / float labeling | **PASS** | No CNF encoder; all IEEE-754 float64 scripts explicitly labeled & differentially bridged against 50-digit `Decimal` [`reference/ovbs52_oracle.py`](reference/ovbs52_oracle.py) (`2,000+` cases, `< 1e-12`). |
| 15 | Literature search logged with dates | **PASS** | Logged in `docs/ACADEMIC_REVIEW.md` and `paper/refs.bib` (20 primary references verified `2026-11-26`). |
| 16 | Every reference resolves + Crossref retraction check | **PASS** | [`scripts/check_citations.py`](scripts/check_citations.py) verifies `20/20` DOIs/URLs AND queries Crossref REST API (`0` retractions in [`results/citation_verification.json`](results/citation_verification.json)). |
| 17 | Pre-registration hash & protocol | **PASS** | [`PREREGISTRATION.md`](PREREGISTRATION.md) locks `N=48` seeds `5001–5048`, exact Wilcoxon + Holm-Bonferroni FWER, and `1e-12` FP64 gate. |
| 18 | Deviations log included | **PASS** | [`DEVIATIONS.md`](DEVIATIONS.md) records every protocol adjustment (including `df=23 -> df=47` fix and geometric/arithmetic OVI dual logging). |
| 19 | Negative results & losses reported | **PASS** | Disclosed openly: `SIM02` small negative drag (`-0.96` OVI, `d_z = -0.41`, `p_Holm = 0.0171`), `BM-MRF-05`/`BM-EVO-05` native FAIL slots, `29/825` `INDICATOR_ONLY` cognitive tags, and `0/1,900` Mega-Atlas retirements. |
| 20 | Stats as pre-specified + effect sizes + CIs | **PASS** | Exact paired Wilcoxon, Holm-Bonferroni FWER, within-pair dominance `delta_pair`, paired Cohen's `d_z`, exact `df=47` `LCB_95%`, and 2,000-resample 95% bootstrap CIs. |
| 21 | Blinded scoring where possible | **PASS** | Automated deterministic pipelines (`run_alifeops_suite.py`, `run_alife_castration_sim.py`, `audit_omniscient_integrity.py`) with zero hand-scored pillar overrides. |
| 22 | Seeds, hardware & run counts reported | **PASS** | Locked seeds `5001–5048`, `5101–5112`, `5201–5204` (`748` runs) and hardware specs reported in [`REPLICATION.md`](REPLICATION.md) and `paper/main.tex`. |
| 23 | Lockfiles committed (zero CVEs) | **PASS** | [`requirements.txt`](requirements.txt) (`pytest==9.0.3`, `0` pip-audit/OSV CVEs), `pyproject.toml`, `lean/lean-toolchain`, `lean/lake-manifest.json`. |
| 24 | Third-party attributions & REUSE/SPDX | **PASS** | [`NOTICE`](NOTICE), [`LICENSE`](LICENSE), [`LICENSE-DOCS`](LICENSE-DOCS), and SPDX headers across source/Lean files. |
| 25 | `MANIFEST.sha256` of all artifacts | **PASS** | [`MANIFEST_SHA256.txt`](MANIFEST_SHA256.txt), [`CHECKSUMS.sha256`](CHECKSUMS.sha256), [`data/MANIFEST.sha256`](data/MANIFEST.sha256), and [`MANIFEST.json`](MANIFEST.json) (strict LF, verified by Gate 12). |
| 26 | RFC 3161 TSA timestamp token | **PASS** | Cryptographic DigiCert RFC 3161 token archived at `data/timestamps/CHECKSUMS.sha256.tsr` (OpenTimestamps optional external step). |
| 27 | Plain Git release tag (unsigned per owner rule) | **PASS** | Release `v3.5.0` tagged on GitHub without commit/tag signing per repository policy. |
| 28 | GitHub SLSA artifact attestation (Sigstore/Rekor) | **PASS** | `actions/attest-build-provenance@v2` runs in both `ci.yml` and `release.yml` over PDF, arXiv tarball, axioms & SHA256SUMS. |
| 29 | Software Heritage SWHID (+ optional Zenodo DOI) | **PARTIAL (HONEST)** | Software Heritage snapshot triggered & recorded (`swh:1:snp:...`); Zenodo DOI intentionally deferred until human depositor eligibility review (no fabricated DOI). |
| 30 | `CITATION.cff` validates (`cffconvert`) + FAIR suite | **PASS** | Validated via `uvx --from cffconvert cffconvert --validate -i CITATION.cff`; accompanied by `.zenodo.json`, `croissant.json`, `ro-crate-metadata.json`, `codemeta.json`. |
| 31 | ORCID & honest affiliation (no unformed LLC) | **PASS** | ORCID `0009-0006-8168-9648`, `Independent Researcher, Spokane, WA, USA`; `0` unformed corporate LLC labels in active files. |
| 32 | AI-contribution statement + CRediT roles (no AI authors) | **PASS** | [`docs/AI_DISCLOSURE.md`](docs/AI_DISCLOSURE.md) and `paper/main.tex` Section 8.2. |
| 33 | Redacted audit/run logs archived | **PASS** | [`docs/run-log.md`](docs/run-log.md), [`HARDENING_LOG.md`](HARDENING_LOG.md), and `docs/reviews/` (zero secrets; verified by Gitleaks). |
| 34 | Conflict-of-interest statement | **PASS** | Explicit `COI: none` in `paper/main.tex` Section 8.2 and `docs/AI_DISCLOSURE.md`. |
| 35 | Open dual licenses (`Apache-2.0` + `CC-BY-4.0`) + SPDX | **PASS** | [`LICENSE`](LICENSE) (`Apache-2.0`) and [`LICENSE-DOCS`](LICENSE-DOCS) (`CC-BY-4.0`) with SPDX headers across all scripts & Lean files. |
| 36 | Limitations & threats-to-validity section | **PASS** | [`LIMITATIONS.md`](LIMITATIONS.md) + `paper/main.tex` Section 7 (including Literal-vs-Metaphor boundary table). |
| 37 | Export-control self-screen | **PASS** | Pure open-source fundamental research & discrete math/simulation software; zero controlled encryption/weapons/biological wet-lab protocols. |
| 38 | Title & abstract match Claims Ledger | **PASS** | Visually & programmatically verified (`0` overclaims, explicit `0/1,900` Mega-Atlas boundary, explicit no-peer-review disclosure). |
| 39 | Version parity + `ERRATA.md` + withdrawal policy | **PASS** | Single `VERSION = 3.5.0` synced across paper, CFF, BibTeX, pyproject, formalization, lakefile, FAIR files; [`ERRATA.md`](ERRATA.md) tracks every post-release fix. |
| 40 | Venue-specific AI disclosure alignment | **PASS** | Consistent human-directed AI-assistance wording across `CITATION.cff`, `formalization.yaml`, `docs/AI_DISCLOSURE.md`, and `paper/main.tex`. |
| 41 | Clean-machine reproduction | **PARTIAL (CI-VERIFIED)** | Reproduced on fresh GitHub Actions Ubuntu/macOS/Windows runners (`3-OS CI`); external human third-party reproduction invited via [`REPLICATION.md`](REPLICATION.md). |
| 42 | All 10 review passes recorded with date & outcome | **PASS** | Recorded across [`HARDENING_LOG.md`](HARDENING_LOG.md) and [`docs/reviews/`](docs/reviews/). |
| 43 | Responsible release order observed | **PASS** | Clean-room build & 24-gate audit → GitHub Release + SLSA + SWHID → Blueprint & Pages → Palomar-ready contract → Master Archive registration. |
