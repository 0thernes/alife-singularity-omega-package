# Architecture Overview

See [`docs/architecture.md`](docs/architecture.md) for the complete system architecture, dataflow diagram, module ownership map, and Design Decision Records ([`docs/adr/`](docs/adr/)).

## High-Level Component Stack (`v3.4.0`)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  LAYER 5: PUBLICATION & REPRODUCIBILITY                                      │
│  paper/main.tex (amsart) -> dist/*.pdf & dist/arxiv_submission.tar.gz        │
│  FAIR metadata (.zenodo.json, croissant.json, ro-crate-metadata.json)        │
├──────────────────────────────────────────────────────────────────────────────┤
│  LAYER 4: MULTI-FORMAT ARTIFACT PIPELINE (Zero Consolidation)                │
│  24 CSVs (2,822 rows) | 4 Master Specs (26 XML) | 5 Excel Workbooks          │
│  12 Reports | 3 HTML5 Apps (22-Tab Observatory, 24 SVGs) | 3 Compressed PDFs │
├──────────────────────────────────────────────────────────────────────────────┤
│  LAYER 3: INDEPENDENT VERIFICATION & AUDIT (22 Forensic Gates + 90 Std)      │
│  scripts/audit_omniscient_integrity.py | tests/ (pytest + Hypothesis)        │
│  reference/ovbs52_oracle.py (50-digit Decimal) | scripts/run_mutation_audit  │
├──────────────────────────────────────────────────────────────────────────────┤
│  LAYER 2: FORMAL PROOFS (Zero-Mathlib Lean 4.35.0 + 5 Native Engines)        │
│  lean/OmegaPackageProofs/ (36 core + 4 Palomar = 40 audited axioms)          │
│  + 5 Live Companion Native Engines (42+62+72+48+20 = 244 Lean 4 => 280 tot)  │
├──────────────────────────────────────────────────────────────────────────────┤
│  LAYER 1: CONSERVED SIMULATION & LIVE TELEMETRY                              │
│  scripts/run_alife_castration_sim.py (748 runs, FP64 drift 2.46e-16)         │
│  scripts/run_alifeops_suite.py + pipelines/alifeops-master-pipeline.yaml     │
└──────────────────────────────────────────────────────────────────────────────┘
```
