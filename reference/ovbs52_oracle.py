# SPDX-License-Identifier: Apache-2.0
"""
Independent 50-Digit Decimal & Exact Rational Reference Oracle for OVBS-52,
Escalation Stage Classification, and 13x13 Castration Synergy (Build Standard B12).

Zero shared runtime code with scripts/run_alifeops_suite.py or omega_datasets_part3.py.
Used for 2,000+ differential tests and Hypothesis property-based verification.
"""
from decimal import Decimal, getcontext, ROUND_HALF_UP
from fractions import Fraction

getcontext().prec = 50

PILLAR_WEIGHTS_EXACT = {
    "P1_OEE_NOVELTY": Fraction(18, 100),
    "P2_AUTOPOIESIS_PERSISTENCE": Fraction(12, 100),
    "P3_HYPER_MORPHOGENESIS": Fraction(12, 100),
    "P4_RECURSIVE_META_EVOLVABILITY": Fraction(16, 100),
    "P5_ASSEMBLY_UNIVERSAL_CONSTRUCTION": Fraction(12, 100),
    "P6_THERMODYNAMIC_SUBSTRATE_MASTERY": Fraction(10, 100),
    "P7_MULTISCALE_AGENCY_INDIVIDUALITY": Fraction(12, 100),
    "P8_FERAL_RESILIENCE_CRITICALITY": Fraction(8, 100),
}


def oracle_composite_ovi_exact(
    pillar_scores: dict[str, float | Decimal],
    gamma_pass: bool = True,
    spiegelman_factor: float | Decimal = Decimal("1"),
) -> Decimal:
    """Computes exact 50-digit Decimal OVBS-52 composite score."""
    if not gamma_pass:
        return Decimal("0")
    total = Decimal("0")
    for k, w in PILLAR_WEIGHTS_EXACT.items():
        val = Decimal(str(pillar_scores[k]))
        if val < Decimal("0"):
            val = Decimal("0")
        elif val > Decimal("100"):
            val = Decimal("100")
        total += val * (Decimal(w.numerator) / Decimal(w.denominator))
    sp = Decimal(str(spiegelman_factor))
    if sp < Decimal("0"):
        sp = Decimal("0")
    elif sp > Decimal("1"):
        sp = Decimal("1")
    return total * sp


def oracle_composite_ovi_rounded(
    pillar_scores: dict[str, float | Decimal],
    gamma_pass: bool = True,
    spiegelman_factor: float | Decimal = Decimal("1"),
) -> float:
    val = oracle_composite_ovi_exact(pillar_scores, gamma_pass, spiegelman_factor)
    return float(val.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def oracle_classify_stage(ovi: float | Decimal) -> str:
    v = Decimal(str(ovi))
    if v < Decimal("15"):
        return "STAGE_0_INERT"
    if v < Decimal("35"):
        return "STAGE_1_NARROW_ALIFE"
    if v < Decimal("55"):
        return "STAGE_2_AG_LIFE"
    if v < Decimal("75"):
        return "STAGE_3_ALIFE_SINGULARITY"
    if v < Decimal("85"):
        return "STAGE_4_SUPER_ALIFE"
    if v < Decimal("95"):
        return "STAGE_5_CONVERGED_SYNTHESIS"
    return "STAGE_6_POST_BEYOND_SUPER_LIFE"


def oracle_synergy_score(base_i: int, base_j: int, bonus: int) -> int:
    """Exact integer castration synergy composition matching Lean 4.35.0 synergyScore."""
    return min(100, (base_i + base_j) // 2 + bonus)


def oracle_ring0_permitted(ring: str, spectral_norm: float | Decimal) -> bool:
    """Exact Ring-0 ACL predicate matching Lean 4.35.0 wseWritePermitted."""
    if ring == "RING0_KERNEL":
        return False
    return Decimal(str(spectral_norm)) <= Decimal("0.99")


def oracle_pareto_dominates(
    ovi_a: float | Decimal,
    ks_del_a: float | Decimal,
    ovi_b: float | Decimal,
    ks_del_b: float | Decimal,
) -> bool:
    """Strict Pareto dominance: higher-or-equal OVI, lower-or-equal KS deletion, strict on at least one."""
    oa, ka = Decimal(str(ovi_a)), Decimal(str(ks_del_a))
    ob, kb = Decimal(str(ovi_b)), Decimal(str(ks_del_b))
    return (oa >= ob) and (ka <= kb) and ((oa > ob) or (ka < kb))
