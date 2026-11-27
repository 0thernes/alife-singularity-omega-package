# Lean 4.35.0 Formal Invariant Suite (`OmegaPackageProofs`, `v3.5.0`)

Zero-Mathlib, strictly constructive (`axioms <= [propext, Quot.sound]`, **no** `Classical.choice`) Lean 4.35.0 proof package certifying `50` core theorems (`29` quantified/inductive/refutation + `21` closed arithmetic & NonVacuity witnesses) plus `5` Palomar comparator certificates (`55` audited `#print axioms` entries total).

Combined with the `310` Pure 6-Kernel Lean 4.35.0 theorems verified in the five companion native C/C++ engines (`AUTOPHAGE v1.4.0 [48] + Cellulogonic Mecha v1.6.0 [78] + Cellular Engine Omega v5.4.0 [100] + Noetic Organism Omega v2.1.0 [54] + Asmodensius-Native v1.1.0 [30]`), the 7-repo ecosystem totals **`360` Pure 6-Kernel Lean 4.35.0 Theorems**.

## Modules
- `OmegaPackageProofs/OVBS52Scoring.lean` (`12` theorems): OVBS-52 weights, upper bounds, monotonicity, anti-gaming & Spiegelman zero annihilation, P1 Lipschitz sensitivity (`18`), 7-stage monotonicity, live `9191 -> stage5` & `328 -> stage0`.
- `OmegaPackageProofs/EscalationAndCube.lean` (`10` arithmetic locks): `10x10x10` Hybrid Cube (`661+274+20+45=1000`), `75` substrates, `825` checks, `78` alerts, `310+50=360` Lean totals, `121` coupling pairs, `748` empirical runs.
- `OmegaPackageProofs/CastrationAndRing0.lean` (`12` theorems): `13x13=169` synergy cap/symmetry/monotonicity, non-degenerate 3-Ring `OrganismMemory` state machine with structural induction (`ring0_trace_invariant`) and genuine Ring-1/Ring-2 mutation reachability (`ring1_ring2_plasticity_reachable`), `||W||_2 <= 9900` gate, strict Pareto irreflexivity/transitivity & `SIM07 > SIM03`.
- `OmegaPackageProofs/NonVacuity.lean` (`6` witnesses): Concrete inhabitants & sharp positive/negative boundaries (`8499/8500`, `9900/9901`, `ring0/ring1`).
- `OmegaPackageProofs/AdversarialTests.lean` (`10` refutations): Formal Lean `¬ (...)` refutations of 10 deliberately broken definitions & inverted claims.
- `Challenge.lean` / `Solution.lean` / `PalomarSolution.lean` / `palomar/PalomarChallenge.lean` / `comparator.json`: Zero-sorry trusted spec and isolated Palomar comparator contract (`m1..m5`).

## Local Verification Commands
```bash
cd lean
lake build && lake build PalomarChallenge
lake env lean OmegaPackageProofs/VerifyAxioms.lean
lake env leanchecker --fresh PalomarSolution
lake env leanchecker-paranoid --fresh PalomarSolution
# Linux / Ubuntu CI (with bubblewrap):
lake check --paranoid
lake comparator --config comparator.json --paranoid
cd ..
python scripts/test_lean_negative.py
```
