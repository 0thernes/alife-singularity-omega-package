# Verification Architecture & Automated Gate Suite

This repository enforces defense-in-depth verification across **six independent verification layers**:

1. **Layer 1 — Pure Lean 4.35.0 Kernel & Paranoid Checker (`lean/`):**
   - Zero-Mathlib `OmegaPackageProofs` (`50` core + `5` Palomar comparator certificates = `55` audited `#print axioms` lines).
   - Strict `module` encapsulation, `0` warnings, `0` `sorry` outside the `5` intentional challenge stubs in `lean/palomar/PalomarChallenge.lean`, `0` `native_decide`, axioms strictly $\subseteq [\text{propext}, \text{Quot.sound}]$.
   - Independently validated by `leanchecker --fresh`, `leanchecker-paranoid --fresh`, `nanoda_bin`, `con-leche --verified`, and `con-ron --verified` locally (`results/lean4-multi-kernel.txt`, `rc=0`), plus full 6/6 Linux `bubblewrap` CI replay (`lake check --paranoid` & `lake comparator --config comparator.json --paranoid`).
2. **Layer 2 — Independent 50-Digit Arithmetic Oracle & Hypothesis Property Testing (`reference/`, `tests/`):**
   - `reference/ovbs52_oracle.py` re-implements OVBS-52, 7-stage classification, 13x13 synergy, and Ring-0 ACL using 50-digit `Decimal` and exact `Fraction` arithmetic.
   - `tests/test_properties_and_differential.py` verifies `1,000+` Hypothesis property examples and `2,000+` randomized differential checks against runtime & Lean integer formulas.
3. **Layer 3 — Semantic Mutation & Anti-LARP Testing (`scripts/run_mutation_audit.py`, `scripts/run_alife_castration_sim.py`):**
   - `6/6` (`100.0%`) planted Python semantic mutants killed (weight perturbation, anti-gaming gate bypass, Ring-0 ACL leak, spectral norm leak, symmetry violation, stage-boundary off-by-one).
   - `5/5` (`100.0%`) real AST/causal/Fisher–Yates Anti-LARP simulation mutants rejected.
   - `35/35` compiled native C/C++ mutants killed across companion engines.
4. **Layer 4 — 24-Gate Omniscient Forensic Integrity Auditor (`scripts/audit_omniscient_integrity.py`):**
   - Gates 1–18: Zero-consolidation parity, 24 CSVs (`2,822` rows), `130/130` checklist FK integrity, `78/78` YAML alerts & `13/13` Release Gates, `9/9` JSON Schema Draft 2020-12 scorecards, `748`-run FP64 drift `< 1e-12`, 4-format Master Spec parity (`26` XML sections), 5 Excel workbooks + `xlrd` binary `.xls` readback, 3 HTML5 apps (`24/24` SVGs, `0` raw LaTeX, `0` `U+2611`), Node.js JS syntax check, 3 compressed `< 5 MB` Chrome PDFs, bijective SHA-256 manifests, zero stale-version drift, all-24-SVG geometry bounds, CSV column & YAML FK audit, `pypdf` deep PDF text audit, live headless Chrome 22-tab DOM click-through stress test, and dual-drive `Z: <-> I:` SHA-256 parity.
   - Gates 19–24 (`v3.5.0`): Gate 19 Lean 4.35.0 axiom parity & zero `sorry` (`55/55` + `AdversarialTests.lean`), Gate 20 AMS-LaTeX white paper PDF (`0` overfull hboxes, auto-generated Table 2 parity) + clean-room `arxiv_submission.tar.gz`, Gate 21 Build Standard v1.2.0 hygiene (`< 5 MB` tracked, `0` R4 banned files, valid `repo.yaml`, `VERSION`/`CHANGELOG`/`CITATION.cff` parity, `0` fake LLC), Gate 22 `6/6` Python mutation audit + verbatim README axiom parity (`55/55`), Gate 23 live negative Lean tamper rejection + Blueprint CSP/WCAG/M5 parity + Crossref 0-retraction citation receipt, and Gate 24 RFC 3161 TSA timestamp + FAIR CodeMeta + 43-item submission readiness + strict LF hygiene.
5. **Layer 5 — Publication Typesetting & Bibliography Resolution (`scripts/build_paper_and_figures.py`, `scripts/check_citations.py`):**
   - Tectonic compilation verified with `0` overfull hboxes, `0` undefined refs/citations, plus clean-room extraction and recompilation of `dist/arxiv_submission.tar.gz` in an isolated temporary directory.
   - Live DOI/URL resolution over every bibliographic entry in `paper/refs.bib`.
6. **Layer 6 — Build Standard for LLMs v1.2.0 Audit (`scripts/Audit-Repo.ps1` / `scripts/audit-repo.sh`):**
   - `100.0%` Structure, `100.0%` Completion, `100.0%` Core, `0` placeholder files, `0` R4 banned files.
