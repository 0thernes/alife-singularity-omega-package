-- SPDX-License-Identifier: Apache-2.0
module

public import Challenge

namespace OmegaPackageProofs.Solution

open OmegaPackageProofs.OVBS52
open OmegaPackageProofs.CubeAndPartitions
open OmegaPackageProofs.CastrationRing0
open OmegaPackageProofs.Spec

public theorem prove_m1 : M1Statement :=
  ⟨pillar_weights_sum_100,
   fun _ _ _ _ _ _ _ _ _ g h1 h2 h3 h4 h5 h6 h7 h8 hsp =>
     gatedOviCentis_le_10000 h1 h2 h3 h4 h5 h6 h7 h8 hsp g,
   fun _ _ h => classifyStage_monotone h⟩

public theorem prove_m2 : M2Statement :=
  ⟨hybrid_cube_partition_1000.1, hybrid_cube_active_935,
   clean_slate_825_checks_sum, native_5engine_lean_theorems_291,
   ecosystem_total_lean_theorems_327⟩

public theorem prove_m3 : M3Statement :=
  ⟨synergyScore_le_100, synergyScore_comm,
   fun k0 p s r => ring0_kernel_state_invariant k0 p s r,
   sim07_pareto_dominates_sim03⟩

end OmegaPackageProofs.Solution
