# SPDX-License-Identifier: Apache-2.0
"""
Semantic Mutation Testing Harness (Build Standard B13 — 100% Mutant Kill Target).

Plants 6 realistic semantic faults against OVBS-52 scoring, escalation thresholds,
anti-gaming annihilation, Ring-0 ACL protection, synergy symmetry/caps, and
5-engine Lean 4 arithmetic, asserting every single mutant is killed by our test oracle.
"""
from decimal import Decimal
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from reference.ovbs52_oracle import (
    PILLAR_WEIGHTS_EXACT,
    oracle_classify_stage,
    oracle_composite_ovi_exact,
    oracle_ring0_permitted,
    oracle_synergy_score,
)


def _check_invariants(ovi_fn, stage_fn, ring0_fn, syn_fn, lean_sum_fn) -> None:
    sample = {k: Decimal("80") for k in PILLAR_WEIGHTS_EXACT}
    assert ovi_fn(sample, True, Decimal("1")) == Decimal("80"), "Uniform 80 must yield 80"
    assert ovi_fn(sample, False, Decimal("1")) == Decimal("0"), "Failed anti-gaming gate must annihilate OVI"
    assert stage_fn(Decimal("84.99")) == "STAGE_4_SUPER_ALIFE"
    assert stage_fn(Decimal("85.00")) == "STAGE_5_CONVERGED_SYNTHESIS"
    assert ring0_fn("RING0_KERNEL", Decimal("0.50")) is False, "Ring-0 must block all writes"
    assert ring0_fn("RING1_SYNAPSE", Decimal("0.99")) is True
    assert ring0_fn("RING1_SYNAPSE", Decimal("0.9901")) is False
    assert syn_fn(95, 92, 15) <= 100, "Synergy score must cap at 100"
    assert syn_fn(30, 70, 5) == syn_fn(70, 30, 5), "Synergy must be symmetric"
    assert lean_sum_fn(42, 62, 72, 48, 20) == 244, "5-engine Lean sum must equal 244"


def run_mutation_audit() -> tuple[int, int]:
    # Baseline must pass
    _check_invariants(
        oracle_composite_ovi_exact,
        oracle_classify_stage,
        oracle_ring0_permitted,
        oracle_synergy_score,
        lambda a, b, c, d, e: a + b + c + d + e,
    )

    mutants = [
        (
            "MUT-PY-01_IGNORE_GAMMA_GATE",
            lambda p, g, s: oracle_composite_ovi_exact(p, True, s),
            oracle_classify_stage,
            oracle_ring0_permitted,
            oracle_synergy_score,
            lambda a, b, c, d, e: a + b + c + d + e,
        ),
        (
            "MUT-PY-02_BAD_WEIGHT_SUM",
            lambda p, g, s: oracle_composite_ovi_exact(p, g, s) + Decimal("2"),
            oracle_classify_stage,
            oracle_ring0_permitted,
            oracle_synergy_score,
            lambda a, b, c, d, e: a + b + c + d + e,
        ),
        (
            "MUT-PY-03_OFF_BY_ONE_STAGE5",
            oracle_composite_ovi_exact,
            lambda v: "STAGE_4_SUPER_ALIFE" if Decimal(str(v)) <= Decimal("85.00") else oracle_classify_stage(v),
            oracle_ring0_permitted,
            oracle_synergy_score,
            lambda a, b, c, d, e: a + b + c + d + e,
        ),
        (
            "MUT-PY-04_RING0_BYPASS",
            oracle_composite_ovi_exact,
            oracle_classify_stage,
            lambda r, sn: Decimal(str(sn)) <= Decimal("0.99"),
            oracle_synergy_score,
            lambda a, b, c, d, e: a + b + c + d + e,
        ),
        (
            "MUT-PY-05_SYNERGY_UNBOUNDED",
            oracle_composite_ovi_exact,
            oracle_classify_stage,
            oracle_ring0_permitted,
            lambda i, j, b: (i + j) // 2 + b,
            lambda a, b, c, d, e: a + b + c + d + e,
        ),
        (
            "MUT-PY-06_OMIT_ASMODENSIUS_LEAN",
            oracle_composite_ovi_exact,
            oracle_classify_stage,
            oracle_ring0_permitted,
            oracle_synergy_score,
            lambda a, b, c, d, e: a + b + c + d,
        ),
    ]

    killed = 0
    for name, f1, f2, f3, f4, f5 in mutants:
        try:
            _check_invariants(f1, f2, f3, f4, f5)
            print(f"  [SURVIVED!] {name}")
        except AssertionError:
            killed += 1
            print(f"  [KILLED]    {name}")

    print(f"Mutation Audit Summary: {killed}/{len(mutants)} killed ({100.0 * killed / len(mutants):.1f}%)")
    if killed != len(mutants):
        sys.exit(1)
    return killed, len(mutants)


if __name__ == "__main__":
    run_mutation_audit()
