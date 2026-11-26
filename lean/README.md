# Zero-Mathlib Lean 4.35.0 Package Invariant Suite (`OmegaPackageProofs`)

This directory contains the self-contained, zero-Mathlib **Lean 4.35.0** formal invariant suite for `alife-singularity-omega-package` (`v3.4.0`), complementing the **291 Pure 6-Kernel Lean 4.35.0 theorems** verified across the 5 companion native C/C++ ALife engines (`AUTOPHAGE v1.4.0` `48` + `Cellulogonic Mecha v1.5.0` `70` + `Cellular Engine Omega v5.2.0` `89` + `Noetic Organism Omega v2.1.0` `54` + `Asmodensius-Native v1.1.0` `30` = `291`; combined ecosystem total = **`327` Pure 6-Kernel Lean 4.35.0 theorems**).

## 5-Second Local 6-Kernel Verification

```bash
cd lean
lake build
lake build PalomarChallenge
lake env lean OmegaPackageProofs/VerifyAxioms.lean
lake env leanchecker --fresh Solution
lake env leanchecker-paranoid --fresh Solution
lake env leanchecker-paranoid --fresh PalomarSolution
```

See [`results/lean4-multi-kernel.txt`](../results/lean4-multi-kernel.txt) for the recorded local 5-checker transcript (`lean4`, `leanchecker`, `leanchecker-paranoid`, `nanoda_bin`, `con-leche`, `con-ron`) and `.github/workflows/ci.yml` for full 6/6 Linux `bubblewrap` CI replay (`lake check --paranoid` + `lake comparator --config comparator.json --paranoid`).

## Module Layout

| Module | Theorems | Scope |
|---|---:|---|
| `OmegaPackageProofs/OVBS52Scoring.lean` | 10 | Exact OVBS-52 weights (`=100`), boundedness (`<=10000`), anti-gaming annihilation (`gamma=false -> 0`), Spiegelman & pillar monotonicity, 7-stage escalation classifier monotonicity |
| `OmegaPackageProofs/EscalationAndCube.lean` | 10 | `10x10x10` Hybrid Cube (`661+274+20+45=1000`), `75` substrates, `825` Clean-Slate checks, `78` wired alerts, `291` 5-engine + `36` local = `327` theorem accounting, `11x11=121` coupling, `748` runs |
| `OmegaPackageProofs/CastrationAndRing0.lean` | 10 | `13x13=169` synergy bounds/symmetry/monotonicity, Hardware Ring-0 ACL unconditional write block & kernel-state invariance, `||W||_2 <= 0.99` gate, Pareto order axioms & `SIM07 > SIM03` witness |
| `OmegaPackageProofs/NonVacuity.lean` | 6 | Concrete positive & negative sharp-boundary inhabitants for every hypothesis bundle |
| `PalomarSolution.lean` / `palomar/PalomarChallenge.lean` | 4 | Headline comparator certificates (`m1`–`m4`) for `lake comparator --config comparator.json --paranoid` |

See [`docs/statement-fidelity.md`](../docs/statement-fidelity.md) and [`blueprint/index.html`](../blueprint/index.html) for the full fidelity matrix and interactive proof DAG.
