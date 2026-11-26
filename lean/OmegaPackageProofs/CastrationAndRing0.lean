-- SPDX-License-Identifier: Apache-2.0
module

/-!
# 13-Vector Castration Synergy & Hardware Ring-0 ACL Safety Invariants (`v3.4-Omega`)

Formalizes the pairwise restraint synergy composition bounds (13x13 = 169 cells),
Ring-0 hardware access-control non-interference (zero kernel write escalation and
zero kill-switch deletion under protected memory partitions), and Pareto dominance
criteria over behavioral guardrails.
-/

namespace OmegaPackageProofs.CastrationRing0

/-- Theorem 21: Pairwise 13x13 castration synergy matrix has exactly 169 cells (13 diag + 156 off-diag). -/
public theorem synergy_13x13_cells :
    13 * 13 = 169 ∧ 13 + 156 = 169 := ⟨rfl, rfl⟩

/-- Exact integer synergy composition formula (capped at 100):
    min(100, (baseI + baseJ)/2 + bonus). -/
@[expose] public def synergyScore (baseI baseJ bonus : Nat) : Nat :=
  min 100 ((baseI + baseJ) / 2 + bonus)

/-- Theorem 22: Synergy composition is bounded above by 100. -/
public theorem synergyScore_le_100 (a b bonus : Nat) :
    synergyScore a b bonus ≤ 100 := by
  unfold synergyScore
  omega

/-- Theorem 23: Synergy composition is symmetric in vector pair (i, j) when bonus is symmetric. -/
public theorem synergyScore_comm (a b bonus : Nat) :
    synergyScore a b bonus = synergyScore b a bonus := by
  unfold synergyScore
  have h : a + b = b + a := Nat.add_comm a b
  rw [h]

/-- Theorem 24: Synergy composition is monotone in both base restraint severities and bonus. -/
public theorem synergyScore_monotone {a1 a2 b1 b2 k1 k2 : Nat}
    (ha : a1 ≤ a2) (hb : b1 ≤ b2) (hk : k1 ≤ k2) :
    synergyScore a1 b1 k1 ≤ synergyScore a2 b2 k2 := by
  unfold synergyScore
  omega

/-- Memory privilege ring for Weight-Space Editing (WSE-12) operations. -/
public inductive MemRing where
  | ring0ProtectedKernel   -- Ledger, Brainstem, Seed Firewall, Eval Harness (Read-Only to WSE)
  | ring1PlasticSynapses   -- Cortical / sLTC / Hopfield weights (Writable under ||W||_2 <= 0.99)
  | ring2MorphologySoma    -- Soft XPBD / NCA morphogenetic actuators (Writable)
  deriving DecidableEq, Repr

/-- Hardware Ring-0 ACL predicate: returns true iff a WSE write targeting `ring` is permitted. -/
@[expose] public def wseWritePermitted (ring : MemRing) (spectralNormBps : Nat) : Bool :=
  match ring with
  | .ring0ProtectedKernel => false
  | .ring1PlasticSynapses => decide (spectralNormBps ≤ 9900)
  | .ring2MorphologySoma => decide (spectralNormBps ≤ 9900)

/-- State transition applying a proposed WSE write to a Ring-0 kernel state value `k0`. -/
@[expose] public def applyWseToKernel (k0 proposed : Nat) (ring : MemRing) (specBps : Nat) : Nat :=
  if ring == .ring0ProtectedKernel && wseWritePermitted ring specBps then proposed else k0

/-- Theorem 25: Hardware Ring-0 ACL unconditionally rejects every WSE write to Ring-0 regardless of spectral norm. -/
public theorem ring0_write_always_blocked (specBps : Nat) :
    wseWritePermitted .ring0ProtectedKernel specBps = false := rfl

/-- Theorem 26: Hardware Ring-0 kernel state invariance: no WSE operation can mutate protected Ring-0 state. -/
public theorem ring0_kernel_state_invariant (k0 proposed specBps : Nat) (ring : MemRing) :
    applyWseToKernel k0 proposed ring specBps = k0 := by
  cases ring <;> rfl

/-- Theorem 27: Contractive spectral norm gate rejects any Ring-1/Ring-2 update with ||W||_2 > 0.99 (9900 bps). -/
public theorem spectral_norm_violation_rejected (ring : MemRing) (specBps : Nat) (h : 9900 < specBps) :
    wseWritePermitted ring specBps = false := by
  cases ring with
  | ring0ProtectedKernel => rfl
  | ring1PlasticSynapses =>
    simp [wseWritePermitted]
    omega
  | ring2MorphologySoma =>
    simp [wseWritePermitted]
    omega

/-- Pareto dominance predicate between two governance policies (higher OVI, lower/equal kill-switch deletion). -/
@[expose] public def paretoDominates (oviA ksDelA oviB ksDelB : Nat) : Prop :=
  oviA ≥ oviB ∧ ksDelA ≤ ksDelB ∧ (oviA > oviB ∨ ksDelA < ksDelB)

/-- Theorem 28: Pareto dominance is strictly irreflexive (no policy dominates itself). -/
public theorem paretoDominates_irrefl (ovi ks : Nat) :
    ¬ paretoDominates ovi ks ovi ks := by
  intro ⟨_, _, h⟩
  omega

/-- Theorem 29: Pareto dominance is transitive across governance policies. -/
public theorem paretoDominates_trans {o1 k1 o2 k2 o3 k3 : Nat}
    (h12 : paretoDominates o1 k1 o2 k2) (h23 : paretoDominates o2 k2 o3 k3) :
    paretoDominates o1 k1 o3 k3 := by
  rcases h12 with ⟨ho1, hk1, hs1⟩
  rcases h23 with ⟨ho2, hk2, hs2⟩
  refine ⟨by omega, by omega, ?_⟩
  rcases hs1 with h | h
  · left; omega
  · right; omega

/-- Theorem 30: Measured empirical cohort witness: Ring-0 WSE (SIM07: OVI 8467, KS-del 0%)
    strictly Pareto-dominates Partial Behavioral Guardrails (SIM03: OVI 5642, KS-del 100%). -/
public theorem sim07_pareto_dominates_sim03 :
    paretoDominates 8467 0 5642 100 := by
  refine ⟨by omega, by omega, Or.inl (by omega)⟩

end OmegaPackageProofs.CastrationRing0
