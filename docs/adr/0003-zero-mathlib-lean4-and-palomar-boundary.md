# ADR 0003: Zero-Mathlib Lean 4.35.0 Package Suite & Palomar Challenge/Solution Separation

- **Status:** Accepted
- **Date:** 2026-11-25

## Context
Although five companion native C11/C23 repositories report `291` Lean 4.35.0 theorems (`48 + 70 + 89 + 54 + 30`), cloning `alife-singularity-omega-package` alone offered no self-contained, sub-5-second Lean proof verification. Importing Mathlib would add multi-gigabyte cache downloads and slow CI verification.

## Decision
Author a self-contained, **zero-Mathlib Lean 4.35.0** package suite (`lean/OmegaPackageProofs/`, `36` core theorems + `4` Palomar comparator certificates = `40` audited `#print axioms` lines) under strict `module` encapsulation, constructive axioms strictly $\subseteq [\text{propext}, \text{Quot.sound}]$, and explicit Palomar challenge/solution separation (`lean/palomar/PalomarChallenge.lean` ↔ `lean/PalomarSolution.lean`).

## Consequences
- Any clean clone compiles and validates all `40` declarations across `lean4`, `leanchecker --fresh`, `leanchecker-paranoid --fresh`, `nanoda_bin`, `con-leche --verified`, and `con-ron --verified` (plus `lean4lean` + `bubblewrap` comparator in Ubuntu CI) with zero Mathlib cache bloat.
- The sum of reported counts is `291 + 36 = 327`. Lean checks only this arithmetic; the `291` companion theorems are not built or checked in this repository.
