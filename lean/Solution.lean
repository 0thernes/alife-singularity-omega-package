-- SPDX-License-Identifier: Apache-2.0
module

public import Challenge

namespace OmegaPackageProofs.Solution

open OmegaPackageProofs.OVBS52
open OmegaPackageProofs.CubeAndPartitions
open OmegaPackageProofs.CastrationRing0
open OmegaPackageProofs.AdversarialTests
open OmegaPackageProofs.Spec

public theorem prove_m1 : M1Statement :=
  ⟨pillar_weights_sum_100,
   fun _ _ _ _ _ _ _ _ _ g h1 h2 h3 h4 h5 h6 h7 h8 hsp =>
     gatedOviCentis_le_10000 h1 h2 h3 h4 h5 h6 h7 h8 hsp g,
   fun _ _ h => classifyStage_monotone h⟩

public theorem prove_m2 : M2Statement :=
  ⟨hybrid_cube_partition_1000.1, hybrid_cube_active_935,
   clean_slate_825_checks_sum, native_5engine_lean_theorems_310,
   ecosystem_total_lean_theorems_360⟩

public theorem prove_m3 : M3Statement :=
  ⟨synergyScore_le_100, synergyScore_comm,
   fun trace mem => ring0_trace_invariant trace mem,
   sim07_pareto_dominates_sim03⟩

public theorem prove_m5 : M5Statement :=
  ⟨at05_refute_ring0_writable,
   at06_refute_ring0_mutable_by_trace,
   at09_refute_sim03_dominates_sim07,
   at10_refute_pareto_reflexive⟩

end OmegaPackageProofs.Solution
