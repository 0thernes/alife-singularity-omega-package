# Zero-Mathlib Lean 4.35.0 Package Invariant Suite (`OmegaPackageProofs`)

This directory contains the self-contained, zero-Mathlib **Lean 4.35.0** formal invariant suite for `alife-singularity-omega-package` (`v3.4.0`), complementing the **244 Pure Lean 4 theorems** verified across the 5 companion native C/C++ ALife engines (`AUTOPHAGE` `42` + `Cellulogonic Mecha` `62` + `Cellular Engine Omega` `72` + `Noetic Organism Omega` `48` + `Asmodensius-Native` `20` = `244`; combined total = **`280` Pure Lean 4 theorems**).

## 5-Second Local Verification

```bash
cd lean
lake build
lake env lean OmegaPackageProofs/VerifyAxioms.lean
lake env leanchecker Solution
lake env leanchecker PalomarSolution
```

## Module Layout

| Module | Theorems | Scope |
|---|---:|---|
| `OmegaPackageProofs/OVBS52Scoring.lean` | 10 | Exact OVBS-52 weights (`=100`), boundedness (`<=10000`), anti-gaming annihilation (`gamma=false -> 0`), Spiegelman & pillar monotonicity, 7-stage escalation classifier monotonicity |
| `OmegaPackageProofs/EscalationAndCube.lean` | 10 | `10x10x10` Hybrid Cube (`661+274+20+45=1000`), `75` substrates, `825` Clean-Slate checks, `78` wired alerts, `244` 5-engine + `36` local = `280` theorem accounting, `11x11=121` coupling, `748` runs |
| `OmegaPackageProofs/CastrationAndRing0.lean` | 10 | `13x13=169` synergy bounds/symmetry/monotonicity, Hardware Ring-0 ACL unconditional write block & kernel-state invariance, `||W||_2 <= 0.99` gate, Pareto order axioms & `SIM07 > SIM03` witness |
| `OmegaPackageProofs/NonVacuity.lean` | 6 | Concrete positive & negative sharp-boundary inhabitants for every hypothesis bundle |
| `PalomarSolution.lean` / `palomar/PalomarChallenge.lean` | 4 | Headline comparator certificates (`m1`–`m4`) for `lake comparator --config comparator.json --paranoid` |

See [`docs/statement-fidelity.md`](../docs/statement-fidelity.md) and [`blueprint/index.html`](../blueprint/index.html) for the full fidelity matrix and interactive proof DAG.
