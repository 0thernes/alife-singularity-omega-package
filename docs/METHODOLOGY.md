# Research Methodology (`v3.4.0`)

## 1. Conserved Multi-Island Stochastic A-Life Simulation (`748` Runs)

`scripts/run_alife_castration_sim.py` implements an 8-island stochastic artificial-life simulation over `180` generations per run with strict physical accounting:
- **11-Pool Kahan–Neumaier FP64 Energy Ledger:** Tracks exogenous flux, stored somatic ATP, reproductive investment, synaptic maintenance, stealth-evasion overhead, morphological actuation, and irreversible thermal dissipation. Every step verifies relative First-Law residual $\Delta E_{\mathrm{rel}} < 10^{-12}$ (observed max `2.463e-16`) and Second-Law non-negative dissipation ($\Delta E_{\mathrm{diss,num}} \ge -10^{-15}$, `0` heat-backflow faults).
- **Seed Isolation:** Deterministic locked seeds (`5001..5048`) ensure paired comparisons across identical environmental trajectories.
- **Three Experimental Designs:**
  1. *8-Cohort Paired Comparison (`384` runs):* `SIM01..SIM08` across `N = 48` locked seeds, tested via exact two-sided paired Wilcoxon signed-rank tests (`scipy.stats.wilcoxon`) with Holm–Bonferroni FWER step-down adjustment across all 7 contrasts vs. `SIM01`, plus paired non-parametric dominance effect sizes ($\delta_{\mathrm{pair}}$).
  2. *Dual 11-Point Continuous Gradient Sweep (`264` runs):* Stacked restraint intensity $r \in \{0\%, 10\%, \dots, 100\%\}$ $\times$ `12` locked seeds across both behavioral restraints and Hardware Ring-0 ACL.
  3. *5×5 Two-Dimensional Phase Surface (`100` runs):* Crosses Island Siloing $\{0, 25, 50, 75, 100\%\}$ with Metabolic Minimization $\{0, 25, 50, 75, 100\%\}$ $\times$ `4` locked seeds to quantify super-additive Spiegelman collapse.
- **Anti-LARP Negative Controls (`5/5`):** Injects 5 genuine falsification mutants (AST hardcoded-return check, causal conservation-violation check, Fisher–Yates seed-shuffle control, kill-switch tampering bypass check, and zero-energy phantom-vitality check) verifying every gate catches counterfeit runs.

## 2. Five-Engine Native Verification Harness (`scripts/run_alifeops_suite.py`)

Executes five companion native C11/C23 A-Life engines without hardcoded pillar scores (`AUTOPHAGE v1.3.0`, `Cellulogonic Mecha v1.4.0`, `Cellular Engine Omega v5.1.0`, `Noetic Organism Omega v2.0.0`, `Asmodensius-Native`), aggregates all 52 OVBS-52 submetrics into `results/alifeops_live_verification.json`, and validates the receipt against `pipelines/benchmark-suite-schema.json` (JSON Schema Draft 2020-12).

## 3. Zero-Mathlib Lean 4.35.0 Formalization & 50-Digit Differential Oracle

- **Lean 4.35.0 (`lean/OmegaPackageProofs/`):** Formalizes core OVBS-52 scoring, monotonicity, anti-gaming annihilation, exact corpus partition counts, 13x13 synergy algebra, Hardware Ring-0 ACL write-blocking/state-invariance, spectral-norm gating, Pareto ordering, and non-vacuity inhabitants using zero external libraries (`0` Mathlib, axioms $\subseteq [\text{propext}, \text{Quot.sound}]$).
- **Differential & Mutation Testing:** `reference/ovbs52_oracle.py` independently computes all quantities at 50 decimal digits of precision; `tests/test_properties_and_differential.py` tests `1,000+` Hypothesis examples and `2,000+` differential cases; `scripts/run_mutation_audit.py` kills `6/6` planted semantic mutants.

## 4. Mega-Atlas 1,900-Problem Non-Retirement Screening

Programmatically scanned all `1,900` records in `unsolved-problems-mega-atlas/outputs/MegaAtlas_Unsolved_Problems_V2.json.gz` across five technical keyword clusters (`428` broad matches), manually audited every direct/adjacent candidate into `25` structured rows (`MA-01..MA-25`), and applied a strict binary retirement rule: an overarching parent problem is marked `SOLVED` **if and only if** the full general problem statement (not merely a bounded in-silico proxy) is resolved with peer-reviewed rigor. Result: **`0 / 1,900`** retired.
