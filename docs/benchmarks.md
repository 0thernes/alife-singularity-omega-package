# Performance Benchmarks & Runtime Budgets (Build Standard A37 / B26 / B27)

- **Version:** `3.4.0` · **Measured (UTC):** `2026-11-26T03:23:09Z`
- **Host:** `Windows 11 / Python 3.12.10`
- **Protocol:** `2` warmup iterations + `10` timed iterations (`time.perf_counter`), reporting median, IQR, and p95 in milliseconds. Historical runs are appended to [`results/bench-history.csv`](../results/bench-history.csv).

## Core Verification Micro-Benchmarks

| Benchmark | Workload | Median (ms) | IQR (ms) | p95 (ms) | Budget (ms) | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `oracle_ovi_1000_calls` | 1,000 × 50-digit Decimal OVBS-52 + stage calls | `6.461` | `0.165` | `6.589` | `< 100.0` | **PASS** |
| `ring0_acl_10000_checks` | 10,000 × Ring-0 ACL + spectral-norm gate evaluations | `2.039` | `0.013` | `2.048` | `< 50.0` | **PASS** |
| `synergy_13x13_100_sweeps` | 100 × full 13×13 (16,900 cell) synergy matrix sweeps | `3.628` | `0.133` | `3.754` | `< 50.0` | **PASS** |

## End-to-End Pipeline Budgets (`A37`)

| Workflow Stage | Command | Runtime Budget | Observed Tier |
| :--- | :--- | :---: | :--- |
| Zero-Mathlib Lean 4.35.0 full check + `leanchecker-paranoid` | `just lean` | `< 10 s` | Warm `< 5 s` |
| `pytest` + Hypothesis (`1,000+`) + 50-digit differential oracle (`2,000+`) | `just test` | `< 30 s` | ~`5–12 s` |
| Python semantic mutation suite (`6/6` mutants) | `just mutate` | `< 5 s` | `< 0.5 s` |
| AMS-LaTeX white paper + 4 figures + clean-room arXiv tarball | `just paper` | `< 60 s` | ~`10–18 s` |
| Full 748-run conserved paired empirical simulation | `python scripts/run_alife_castration_sim.py` | `< 120 s` | ~`20–45 s` |
| Complete 22-Gate Omniscient Forensic Audit (incl. Chrome DOM stress) | `just forensic` | `< 90 s` | ~`15–30 s` |
