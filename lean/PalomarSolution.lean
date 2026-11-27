-- SPDX-License-Identifier: Apache-2.0
module

public import OmegaPackageProofs

namespace OmegaPackageProofs.Palomar

open OmegaPackageProofs.OVBS52
open OmegaPackageProofs.CubeAndPartitions
open OmegaPackageProofs.CastrationRing0
open OmegaPackageProofs.NonVacuity
open OmegaPackageProofs.AdversarialTests

public theorem m1_ovbs52_scoring_invariants :
    (wP1 + wP2 + wP3 + wP4 + wP5 + wP6 + wP7 + wP8 = 100) ∧
    (∀ p1 p2 p3 p4 p5 p6 p7 p8 spPct g,
      p1 ≤ 100 → p2 ≤ 100 → p3 ≤ 100 → p4 ≤ 100 →
      p5 ≤ 100 → p6 ≤ 100 → p7 ≤ 100 → p8 ≤ 100 →
      spPct ≤ 100 → gatedOviCentis p1 p2 p3 p4 p5 p6 p7 p8 g spPct ≤ 10000) ∧
    (∀ x y, x ≤ y → stageRank (classifyStage x) ≤ stageRank (classifyStage y)) :=
  ⟨pillar_weights_sum_100,
   fun _ _ _ _ _ _ _ _ _ g h1 h2 h3 h4 h5 h6 h7 h8 hsp =>
     gatedOviCentis_le_10000 h1 h2 h3 h4 h5 h6 h7 h8 hsp g,
   fun _ _ h => classifyStage_monotone h⟩

public theorem m2_cube_and_partition_invariants :
    (cubeOK + cubeADAPT + cubeOVER + cubeEXCL = 1000) ∧
    (cubeOK + cubeADAPT = 935) ∧
    (14 + 10 + 25 + 100 + 500 + 100 + 12 + 40 + 24 = 825) ∧
    (48 + 78 + 100 + 54 + 30 = 310) ∧
    (310 + 50 = 360) :=
  ⟨hybrid_cube_partition_1000.1, hybrid_cube_active_935,
   clean_slate_825_checks_sum, native_5engine_lean_theorems_310,
   ecosystem_total_lean_theorems_360⟩

public theorem m3_castration_and_ring0_invariants :
    (∀ a b k, synergyScore a b k ≤ 100) ∧
    (∀ a b k, synergyScore a b k = synergyScore b a k) ∧
    (∀ trace mem, (applyWseTrace mem trace).ring0Kernel = mem.ring0Kernel) ∧
    (paretoDominates 8467 0 5642 100) :=
  ⟨synergyScore_le_100, synergyScore_comm,
   fun trace mem => ring0_trace_invariant trace mem,
   sim07_pareto_dominates_sim03⟩

public theorem m4_nonvacuity_certificate :
    (rawOviCentis 84 86 84 96 99 100 96 96 ≤ 10000) ∧
    (classifyStage 8499 = .stage4SuperAlife) ∧
    (classifyStage 8500 = .stage5ConvergedSynthesis) ∧
    (wseWritePermitted .ring1PlasticSynapses 9900 = true) ∧
    (wseWritePermitted .ring1PlasticSynapses 9901 = false) ∧
    (wseWritePermitted .ring0ProtectedKernel 0 = false) :=
  ⟨by decide, rfl, rfl, rfl, rfl, rfl⟩

public theorem m5_adversarial_refutations :
    (¬ (∃ specBps : Nat, wseWritePermitted .ring0ProtectedKernel specBps = true)) ∧
    (¬ (∃ (mem : OrganismMemory) (trace : List WseWriteOp),
          (applyWseTrace mem trace).ring0Kernel ≠ mem.ring0Kernel)) ∧
    (¬ (paretoDominates 5642 100 8467 0)) ∧
    (¬ (∃ ovi ks : Nat, paretoDominates ovi ks ovi ks)) :=
  ⟨at05_refute_ring0_writable,
   at06_refute_ring0_mutable_by_trace,
   at09_refute_sim03_dominates_sim07,
   at10_refute_pareto_reflexive⟩

end OmegaPackageProofs.Palomar
