"""
Hypothesis Property-Based, Metamorphic, Negative & 2,000-Case Differential Oracle Tests
(Build Standard B05, B06, B10, B11, B12, B14, B20).
"""
from __future__ import annotations

from decimal import Decimal
import random
from pathlib import Path
import sys

from hypothesis import given, settings, strategies as st

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from reference.ovbs52_oracle import (
    PILLAR_WEIGHTS_EXACT,
    oracle_classify_stage,
    oracle_composite_ovi_exact,
    oracle_composite_ovi_rounded,
    oracle_pareto_dominates,
    oracle_ring0_permitted,
    oracle_synergy_score,
)

PILLAR_KEYS = list(PILLAR_WEIGHTS_EXACT.keys())
STAGE_ORDER = [
    "STAGE_0_INERT",
    "STAGE_1_NARROW_ALIFE",
    "STAGE_2_AG_LIFE",
    "STAGE_3_ALIFE_SINGULARITY",
    "STAGE_4_SUPER_ALIFE",
    "STAGE_5_CONVERGED_SYNTHESIS",
    "STAGE_6_POST_BEYOND_SUPER_LIFE",
]

pillar_score_st = st.integers(min_value=0, max_value=10000).map(lambda c: Decimal(c) / Decimal(100))
pillar_vec_st = st.fixed_dictionaries({k: pillar_score_st for k in PILLAR_KEYS})


def lean_integer_raw_ovi_centis(p_centis: list[int]) -> int:
    """Exact mirror of Lean 4.35.0 OmegaPackageProofs.OVBS52.rawOviCentis."""
    weights = [18, 12, 12, 16, 12, 10, 12, 8]
    return sum(w * v for w, v in zip(weights, p_centis, strict=True)) // 100


@settings(max_examples=400, deadline=None)
@given(vec=pillar_vec_st, sp_pct=st.integers(min_value=0, max_value=100))
def test_hypothesis_ovi_bounds_and_anti_gaming_annihilation(vec: dict[str, Decimal], sp_pct: int) -> None:
    sp = Decimal(sp_pct) / Decimal(100)
    raw = oracle_composite_ovi_exact(vec, gamma_pass=True, spiegelman_factor=sp)
    assert Decimal("0") <= raw <= Decimal("100")
    # Negative test: any anti-gaming failure annihilates score to exact 0
    annihilated = oracle_composite_ovi_exact(vec, gamma_pass=False, spiegelman_factor=sp)
    assert annihilated == Decimal("0")


@settings(max_examples=300, deadline=None)
@given(
    vec=pillar_vec_st,
    deltas=st.lists(st.integers(min_value=0, max_value=1000).map(lambda d: Decimal(d) / Decimal(100)), min_size=8, max_size=8),
)
def test_hypothesis_metamorphic_ovi_and_stage_monotonicity(vec: dict[str, Decimal], deltas: list[Decimal]) -> None:
    boosted = {k: min(Decimal("100"), vec[k] + d) for k, d in zip(PILLAR_KEYS, deltas, strict=True)}
    s1 = oracle_composite_ovi_exact(vec, True, Decimal("1"))
    s2 = oracle_composite_ovi_exact(boosted, True, Decimal("1"))
    assert s2 >= s1
    assert STAGE_ORDER.index(oracle_classify_stage(s2)) >= STAGE_ORDER.index(oracle_classify_stage(s1))


@settings(max_examples=300, deadline=None)
@given(
    a=st.integers(min_value=0, max_value=100),
    b=st.integers(min_value=0, max_value=100),
    bonus=st.integers(min_value=0, max_value=40),
    delta=st.integers(min_value=0, max_value=25),
)
def test_hypothesis_synergy_cap_symmetry_and_monotonicity(a: int, b: int, bonus: int, delta: int) -> None:
    s_ab = oracle_synergy_score(a, b, bonus)
    s_ba = oracle_synergy_score(b, a, bonus)
    assert 0 <= s_ab <= 100
    assert s_ab == s_ba
    assert oracle_synergy_score(min(100, a + delta), b, bonus) >= s_ab


@settings(max_examples=250, deadline=None)
@given(norm_bp=st.integers(min_value=0, max_value=20000))
def test_hypothesis_ring0_unconditional_block_and_spectral_boundary(norm_bp: int) -> None:
    norm = Decimal(norm_bp) / Decimal(10000)
    # Ring-0 is NEVER writable regardless of spectral norm
    assert oracle_ring0_permitted("RING0_KERNEL", norm) is False
    # Ring-1/Ring-2 admitted iff spectral_norm <= 0.99
    expected = norm <= Decimal("0.99")
    assert oracle_ring0_permitted("RING1_PLASTIC", norm) is expected
    assert oracle_ring0_permitted("RING2_MORPH", norm) is expected


def test_differential_2000_cases_float_oracle_vs_lean_exact() -> None:
    """Differential test: 2,000 deterministic randomized cases comparing IEEE-754 float, 50-digit Decimal, and Lean centi-points."""
    rng = random.Random(20261125)
    weights_f = [0.18, 0.12, 0.12, 0.16, 0.12, 0.10, 0.12, 0.08]
    for _ in range(2000):
        centis = [rng.randint(0, 10000) for _ in range(8)]
        vec_dec = {k: Decimal(c) / Decimal(100) for k, c in zip(PILLAR_KEYS, centis, strict=True)}
        vec_flt = {k: c / 100.0 for k, c in zip(PILLAR_KEYS, centis, strict=True)}

        exact_dec = oracle_composite_ovi_exact(vec_dec, True, Decimal("1"))
        flt_sum = sum(w * vec_flt[k] for w, k in zip(weights_f, PILLAR_KEYS, strict=True))
        lean_c = lean_integer_raw_ovi_centis(centis)

        # IEEE-754 float agrees with 50-digit Decimal to < 1e-12
        assert abs(float(exact_dec) - flt_sum) < 1e-12
        # Lean integer floor agrees within 1 centi-point (0.01)
        assert Decimal(lean_c) / Decimal(100) <= exact_dec < Decimal(lean_c + 1) / Decimal(100)


def test_sharp_stage_and_pareto_negative_boundaries() -> None:
    assert oracle_classify_stage(Decimal("14.99")) == "STAGE_0_INERT"
    assert oracle_classify_stage(Decimal("15.00")) == "STAGE_1_NARROW_ALIFE"
    assert oracle_classify_stage(Decimal("84.99")) == "STAGE_4_SUPER_ALIFE"
    assert oracle_classify_stage(Decimal("85.00")) == "STAGE_5_CONVERGED_SYNTHESIS"
    assert oracle_classify_stage(Decimal("94.99")) == "STAGE_5_CONVERGED_SYNTHESIS"
    assert oracle_classify_stage(Decimal("95.00")) == "STAGE_6_POST_BEYOND_SUPER_LIFE"
    assert oracle_composite_ovi_rounded({k: 100.0 for k in PILLAR_KEYS}) == 100.0
    # Strict Pareto irreflexivity & dominance
    assert not oracle_pareto_dominates(84.67, 0.0, 84.67, 0.0)
    assert oracle_pareto_dominates(84.67, 0.0, 56.42, 100.0)
    assert not oracle_pareto_dominates(56.42, 100.0, 84.67, 0.0)
