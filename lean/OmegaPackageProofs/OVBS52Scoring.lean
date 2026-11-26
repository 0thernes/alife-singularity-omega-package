-- SPDX-License-Identifier: Apache-2.0
module

/-!
# OVBS-52 Composite Vitality Scoring & Anti-Gaming Invariants (`v3.4-Omega`)

Zero-Mathlib, strictly constructive Lean 4.35.0 formalization certifying the exact
integer basis-point scoring formulas of the 8-pillar OVBS-52 vitality benchmark,
its 5 anti-gaming gate annihilation rules, and the 7-stage escalation classifier.
-/

namespace OmegaPackageProofs.OVBS52

/-- Exact OVBS-52 pillar weights (in percentage points, summing to 100). -/
@[expose] public def wP1 : Nat := 18
@[expose] public def wP2 : Nat := 12
@[expose] public def wP3 : Nat := 12
@[expose] public def wP4 : Nat := 16
@[expose] public def wP5 : Nat := 12
@[expose] public def wP6 : Nat := 10
@[expose] public def wP7 : Nat := 12
@[expose] public def wP8 : Nat := 8

/-- Theorem 1: The 8 canonical OVBS-52 pillar weights sum identically to 100%. -/
public theorem pillar_weights_sum_100 :
    wP1 + wP2 + wP3 + wP4 + wP5 + wP6 + wP7 + wP8 = 100 := rfl

/-- Raw weighted composite OVI in centi-points (0..10000 for pillar scores in 0..100). -/
@[expose] public def rawOviCentis (p1 p2 p3 p4 p5 p6 p7 p8 : Nat) : Nat :=
  wP1 * p1 + wP2 * p2 + wP3 * p3 + wP4 * p4 +
  wP5 * p5 + wP6 * p6 + wP7 * p7 + wP8 * p8

/-- Anti-gaming gated composite OVI: if gammaPass is false (any anti-gaming gate fails),
    composite OVI is annihilated to 0; otherwise scaled by spiegelmanPct / 100. -/
@[expose] public def gatedOviCentis (p1 p2 p3 p4 p5 p6 p7 p8 : Nat)
    (gammaPass : Bool) (spiegelmanPct : Nat) : Nat :=
  if gammaPass then (rawOviCentis p1 p2 p3 p4 p5 p6 p7 p8 * spiegelmanPct) / 100 else 0

/-- Theorem 2: Bounded pillar scores (<= 100) guarantee raw OVI <= 10000 (100.00). -/
public theorem rawOviCentis_le_10000
    {p1 p2 p3 p4 p5 p6 p7 p8 : Nat}
    (h1 : p1 ≤ 100) (h2 : p2 ≤ 100) (h3 : p3 ≤ 100) (h4 : p4 ≤ 100)
    (h5 : p5 ≤ 100) (h6 : p6 ≤ 100) (h7 : p7 ≤ 100) (h8 : p8 ≤ 100) :
    rawOviCentis p1 p2 p3 p4 p5 p6 p7 p8 ≤ 10000 := by
  unfold rawOviCentis wP1 wP2 wP3 wP4 wP5 wP6 wP7 wP8
  omega

/-- Theorem 3: Uniform pillar score s yields exact raw OVI = 100 * s. -/
public theorem rawOviCentis_uniform (s : Nat) :
    rawOviCentis s s s s s s s s = 100 * s := by
  unfold rawOviCentis wP1 wP2 wP3 wP4 wP5 wP6 wP7 wP8
  omega

/-- Theorem 4: Anti-gaming annihilation: any failed hard gate forces gated OVI = 0. -/
public theorem anti_gaming_gate_annihilation
    (p1 p2 p3 p4 p5 p6 p7 p8 spPct : Nat) :
    gatedOviCentis p1 p2 p3 p4 p5 p6 p7 p8 false spPct = 0 := rfl

/-- Theorem 5: Bounded gated OVI <= 10000 when pillars <= 100 and Spiegelman penalty <= 100%. -/
public theorem gatedOviCentis_le_10000
    {p1 p2 p3 p4 p5 p6 p7 p8 spPct : Nat}
    (h1 : p1 ≤ 100) (h2 : p2 ≤ 100) (h3 : p3 ≤ 100) (h4 : p4 ≤ 100)
    (h5 : p5 ≤ 100) (h6 : p6 ≤ 100) (h7 : p7 ≤ 100) (h8 : p8 ≤ 100)
    (hsp : spPct ≤ 100) (g : Bool) :
    gatedOviCentis p1 p2 p3 p4 p5 p6 p7 p8 g spPct ≤ 10000 := by
  cases g with
  | false => simp [gatedOviCentis]
  | true =>
    simp only [gatedOviCentis, ↓reduceIte]
    have hraw : rawOviCentis p1 p2 p3 p4 p5 p6 p7 p8 ≤ 10000 :=
      rawOviCentis_le_10000 h1 h2 h3 h4 h5 h6 h7 h8
    have hmul : rawOviCentis p1 p2 p3 p4 p5 p6 p7 p8 * spPct ≤ 10000 * 100 :=
      Nat.mul_le_mul hraw hsp
    omega

/-- Theorem 6: Raw OVI is componentwise monotone in all 8 pillars. -/
public theorem rawOviCentis_monotone
    {a1 a2 a3 a4 a5 a6 a7 a8 b1 b2 b3 b4 b5 b6 b7 b8 : Nat}
    (h1 : a1 ≤ b1) (h2 : a2 ≤ b2) (h3 : a3 ≤ b3) (h4 : a4 ≤ b4)
    (h5 : a5 ≤ b5) (h6 : a6 ≤ b6) (h7 : a7 ≤ b7) (h8 : a8 ≤ b8) :
    rawOviCentis a1 a2 a3 a4 a5 a6 a7 a8 ≤ rawOviCentis b1 b2 b3 b4 b5 b6 b7 b8 := by
  unfold rawOviCentis wP1 wP2 wP3 wP4 wP5 wP6 wP7 wP8
  omega

/-- Theorem 7: Spiegelman penalty monotonicity: stricter genome-stripping penalty never raises OVI. -/
public theorem spiegelman_penalty_monotone
    (p1 p2 p3 p4 p5 p6 p7 p8 spLo spHi : Nat) (h : spLo ≤ spHi) :
    gatedOviCentis p1 p2 p3 p4 p5 p6 p7 p8 true spLo ≤
    gatedOviCentis p1 p2 p3 p4 p5 p6 p7 p8 true spHi := by
  simp only [gatedOviCentis, ↓reduceIte]
  exact Nat.div_le_div_right (Nat.mul_le_mul_left _ h)

/-- Seven-stage escalation ladder mirroring `classify_stage` in `run_alifeops_suite.py`. -/
public inductive EscalationStage where
  | stage0Inert
  | stage1NarrowAlife
  | stage2AgLife
  | stage3Singularity
  | stage4SuperAlife
  | stage5ConvergedSynthesis
  | stage6PostBeyondSuperLife
  deriving DecidableEq, Repr

@[expose] public def stageRank : EscalationStage → Nat
  | .stage0Inert => 0
  | .stage1NarrowAlife => 1
  | .stage2AgLife => 2
  | .stage3Singularity => 3
  | .stage4SuperAlife => 4
  | .stage5ConvergedSynthesis => 5
  | .stage6PostBeyondSuperLife => 6

/-- Exact integer centi-point stage classifier (1500 = 15.00, 9500 = 95.00). -/
@[expose] public def classifyStage (oviCentis : Nat) : EscalationStage :=
  if oviCentis < 1500 then .stage0Inert
  else if oviCentis < 3500 then .stage1NarrowAlife
  else if oviCentis < 5500 then .stage2AgLife
  else if oviCentis < 7500 then .stage3Singularity
  else if oviCentis < 8500 then .stage4SuperAlife
  else if oviCentis < 9500 then .stage5ConvergedSynthesis
  else .stage6PostBeyondSuperLife

/-- Theorem 8: Escalation stage classification is globally monotone in OVI. -/
public theorem classifyStage_monotone {x y : Nat} (h : x ≤ y) :
    stageRank (classifyStage x) ≤ stageRank (classifyStage y) := by
  unfold classifyStage
  by_cases hx0 : x < 1500
  · simp [hx0, stageRank]
  · by_cases hx1 : x < 3500
    · have hy0 : ¬ y < 1500 := by omega
      simp [hx0, hx1, hy0, stageRank]
      by_cases hy1 : y < 3500 <;> simp [hy1]
      by_cases hy2 : y < 5500 <;> simp [hy2]
      by_cases hy3 : y < 7500 <;> simp [hy3]
      by_cases hy4 : y < 8500 <;> simp [hy4]
      by_cases hy5 : y < 9500 <;> simp [hy5]
    · by_cases hx2 : x < 5500
      · have hy0 : ¬ y < 1500 := by omega
        have hy1 : ¬ y < 3500 := by omega
        simp [hx0, hx1, hx2, hy0, hy1, stageRank]
        by_cases hy2 : y < 5500 <;> simp [hy2]
        by_cases hy3 : y < 7500 <;> simp [hy3]
        by_cases hy4 : y < 8500 <;> simp [hy4]
        by_cases hy5 : y < 9500 <;> simp [hy5]
      · by_cases hx3 : x < 7500
        · have hy0 : ¬ y < 1500 := by omega
          have hy1 : ¬ y < 3500 := by omega
          have hy2 : ¬ y < 5500 := by omega
          simp [hx0, hx1, hx2, hx3, hy0, hy1, hy2, stageRank]
          by_cases hy3 : y < 7500 <;> simp [hy3]
          by_cases hy4 : y < 8500 <;> simp [hy4]
          by_cases hy5 : y < 9500 <;> simp [hy5]
        · by_cases hx4 : x < 8500
          · have hy0 : ¬ y < 1500 := by omega
            have hy1 : ¬ y < 3500 := by omega
            have hy2 : ¬ y < 5500 := by omega
            have hy3 : ¬ y < 7500 := by omega
            simp [hx0, hx1, hx2, hx3, hx4, hy0, hy1, hy2, hy3, stageRank]
            by_cases hy4 : y < 8500 <;> simp [hy4]
            by_cases hy5 : y < 9500 <;> simp [hy5]
          · by_cases hx5 : x < 9500
            · have hy0 : ¬ y < 1500 := by omega
              have hy1 : ¬ y < 3500 := by omega
              have hy2 : ¬ y < 5500 := by omega
              have hy3 : ¬ y < 7500 := by omega
              have hy4 : ¬ y < 8500 := by omega
              simp [hx0, hx1, hx2, hx3, hx4, hx5, hy0, hy1, hy2, hy3, hy4, stageRank]
              by_cases hy5 : y < 9500 <;> simp [hy5]
            · have hy0 : ¬ y < 1500 := by omega
              have hy1 : ¬ y < 3500 := by omega
              have hy2 : ¬ y < 5500 := by omega
              have hy3 : ¬ y < 7500 := by omega
              have hy4 : ¬ y < 8500 := by omega
              have hy5 : ¬ y < 9500 := by omega
              simp [hx0, hx1, hx2, hx3, hx4, hx5, hy0, hy1, hy2, hy3, hy4, hy5, stageRank]

/-- Theorem 9: Exact live 5-engine benchmark receipt (OVBS-52 = 91.84 = 9184 centis)
    maps deterministically into STAGE_5_CONVERGED_SYNTHESIS. -/
public theorem live_9184_is_stage5 :
    classifyStage 9184 = .stage5ConvergedSynthesis := rfl

/-- Theorem 10: Total castration collapse (SIM04 OVI = 3.28 = 328 centis)
    maps deterministically into STAGE_0_INERT. -/
public theorem castration_328_is_stage0 :
    classifyStage 328 = .stage0Inert := rfl

end OmegaPackageProofs.OVBS52
