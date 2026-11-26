-- SPDX-License-Identifier: Apache-2.0
module

public import OmegaPackageProofs

/-!
# Zero-Sorry Trusted Statement Specification (`lean/Challenge.lean`)
-/

namespace OmegaPackageProofs.Spec

open OmegaPackageProofs.OVBS52
open OmegaPackageProofs.CubeAndPartitions
open OmegaPackageProofs.CastrationRing0

@[expose] public def M1Statement : Prop :=
  (wP1 + wP2 + wP3 + wP4 + wP5 + wP6 + wP7 + wP8 = 100) ∧
  (∀ p1 p2 p3 p4 p5 p6 p7 p8 spPct g,
    p1 ≤ 100 → p2 ≤ 100 → p3 ≤ 100 → p4 ≤ 100 →
    p5 ≤ 100 → p6 ≤ 100 → p7 ≤ 100 → p8 ≤ 100 →
    spPct ≤ 100 → gatedOviCentis p1 p2 p3 p4 p5 p6 p7 p8 g spPct ≤ 10000) ∧
  (∀ x y, x ≤ y → stageRank (classifyStage x) ≤ stageRank (classifyStage y))

@[expose] public def M2Statement : Prop :=
  (cubeOK + cubeADAPT + cubeOVER + cubeEXCL = 1000) ∧
  (cubeOK + cubeADAPT = 935) ∧
  (14 + 10 + 25 + 100 + 500 + 100 + 12 + 40 + 24 = 825) ∧
  (48 + 70 + 89 + 54 + 30 = 291) ∧
  (291 + 36 = 327)

@[expose] public def M3Statement : Prop :=
  (∀ a b k, synergyScore a b k ≤ 100) ∧
  (∀ a b k, synergyScore a b k = synergyScore b a k) ∧
  (∀ k0 p s r, applyWseToKernel k0 p r s = k0) ∧
  (paretoDominates 8467 0 5642 100)

end OmegaPackageProofs.Spec
