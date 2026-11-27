-- SPDX-License-Identifier: Apache-2.0
module

public import OmegaPackageProofs.OVBS52Scoring
public import OmegaPackageProofs.CastrationAndRing0

/-!
# Adversarial Definition & False-Claim Refutation Tests (`v3.5-Omega`)

Per Defensible Independent AI Research Playbook v1.3 (Item 12), formally proves inside
the Lean 4.35.0 kernel (strictly constructive, axioms <= [propext, Quot.sound]) that ten
deliberately broken/adversarial variants of our scoring, stage-classification, Ring-0
ACL, synergy, and Pareto definitions are provably `False`.
-/

namespace OmegaPackageProofs.AdversarialTests

open OmegaPackageProofs.OVBS52
open OmegaPackageProofs.CastrationRing0

/-- Theorem 41 (AT01): Refutes any tighter false upper bound `<= 9999` on bounded OVBS-52 scores. -/
public theorem at01_refute_ovi_cap_9999 :
    ¬ (∀ p1 p2 p3 p4 p5 p6 p7 p8 : Nat,
        p1 ≤ 100 → p2 ≤ 100 → p3 ≤ 100 → p4 ≤ 100 →
        p5 ≤ 100 → p6 ≤ 100 → p7 ≤ 100 → p8 ≤ 100 →
        rawOviCentis p1 p2 p3 p4 p5 p6 p7 p8 ≤ 9999) := by
  intro h
  have hbad := h 100 100 100 100 100 100 100 100
    (Nat.le_refl _) (Nat.le_refl _) (Nat.le_refl _) (Nat.le_refl _)
    (Nat.le_refl _) (Nat.le_refl _) (Nat.le_refl _) (Nat.le_refl _)
  have h10000 : rawOviCentis 100 100 100 100 100 100 100 100 = 10000 := rfl
  omega

/-- Theorem 42 (AT02): Refutes any claim that a failed anti-gaming gate can yield a positive OVI. -/
public theorem at02_refute_failed_anti_gaming_positive :
    ¬ (∃ p1 p2 p3 p4 p5 p6 p7 p8 sp : Nat,
        0 < gatedOviCentis p1 p2 p3 p4 p5 p6 p7 p8 false sp) := by
  intro ⟨p1, p2, p3, p4, p5, p6, p7, p8, sp, h⟩
  have hz : gatedOviCentis p1 p2 p3 p4 p5 p6 p7 p8 false sp = 0 := rfl
  omega

/-- Theorem 43 (AT03): Refutes a degenerate constant stage classifier across all OVI scores. -/
public theorem at03_refute_stage_constant :
    ¬ (∀ x y : Nat, classifyStage x = classifyStage y) := by
  intro h
  have h06 : classifyStage 0 = classifyStage 9500 := h 0 9500
  cases h06

/-- Theorem 44 (AT04): Refutes off-by-one Stage-5 promotion at 8499 centi-points (84.99). -/
public theorem at04_refute_stage5_at_8499 :
    ¬ (classifyStage 8499 = .stage5ConvergedSynthesis) := by
  intro h
  cases h

/-- Theorem 45 (AT05): Refutes any spectral norm enabling a permitted write to Ring-0 kernel memory. -/
public theorem at05_refute_ring0_writable :
    ¬ (∃ specBps : Nat, wseWritePermitted .ring0ProtectedKernel specBps = true) := by
  intro ⟨specBps, h⟩
  cases h

/-- Theorem 46 (AT06): Refutes any finite WSE trace mutating Ring-0 kernel memory. -/
public theorem at06_refute_ring0_mutable_by_trace :
    ¬ (∃ (mem : OrganismMemory) (trace : List WseWriteOp),
        (applyWseTrace mem trace).ring0Kernel ≠ mem.ring0Kernel) := by
  intro ⟨mem, trace, hneq⟩
  exact hneq (ring0_trace_invariant trace mem)

/-- Theorem 47 (AT07): Refutes accepting a non-contractive Ring-1 update above ||W||_2 = 0.99 (9901 bps). -/
public theorem at07_refute_ring1_over_spectral_bound :
    ¬ (wseWritePermitted .ring1PlasticSynapses 9901 = true) := by
  intro h
  cases h

/-- Theorem 48 (AT08): Refutes any restraint pair exceeding the capped 100 synergy ceiling. -/
public theorem at08_refute_synergy_exceeds_100 :
    ¬ (∃ a b k : Nat, 100 < synergyScore a b k) := by
  intro ⟨a, b, k, hgt⟩
  have hle := synergyScore_le_100 a b k
  omega

/-- Theorem 49 (AT09): Refutes inverted Pareto claim that partial behavioral guardrails (SIM03)
    dominate Hardware Ring-0 WSE (SIM07). -/
public theorem at09_refute_sim03_dominates_sim07 :
    ¬ (paretoDominates 5642 100 8467 0) := by
  intro ⟨hovi, _, _⟩
  omega

/-- Theorem 50 (AT10): Refutes reflexivity of strict Pareto dominance across all governance pairs. -/
public theorem at10_refute_pareto_reflexive :
    ¬ (∃ ovi ks : Nat, paretoDominates ovi ks ovi ks) := by
  intro ⟨ovi, ks, h⟩
  exact paretoDominates_irrefl ovi ks h

end OmegaPackageProofs.AdversarialTests
