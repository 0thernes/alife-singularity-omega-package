#!/usr/bin/env python3
"""Minimal reproducible quickstart demo for alife-singularity-omega-package (v3.4.0)."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from reference.ovbs52_oracle import (
    oracle_classify_stage,
    oracle_composite_ovi_exact,
    oracle_composite_ovi_rounded,
    oracle_pareto_dominates,
    oracle_ring0_permitted,
    oracle_synergy_score,
)


def main() -> None:
    live = json.loads((ROOT / "results" / "alifeops_live_verification.json").read_text(encoding="utf-8"))
    emp = json.loads((ROOT / "results" / "empirical_sim_summary.json").read_text(encoding="utf-8"))

    # 1. Recompute 50-digit OVBS-52 score on live 5-engine pillar vector
    p = live["pillar_scores"]
    raw_ovi = oracle_composite_ovi_exact(p, gamma_pass=True, spiegelman_factor=1.0)
    rounded_ovi = oracle_composite_ovi_rounded(p, gamma_pass=True, spiegelman_factor=1.0)
    gated_fail = oracle_composite_ovi_exact(p, gamma_pass=False, spiegelman_factor=1.0)
    stage = oracle_classify_stage(raw_ovi)

    print("=== A-Life Singularity x Clean-Slate v3.0 Omega Quickstart (v3.4.0) ===")
    print(f"Live 5-Engine Composite OVI (receipt): {live['composite_ovi_score']:.2f}")
    print(f"50-Digit Oracle Raw OVI:               {raw_ovi:.6f} (rounded {rounded_ovi:.2f}) -> {stage}")
    print(f"Anti-Gaming Gate Annihilation Check:   {gated_fail} (exact zero)")
    assert abs(rounded_ovi - live["composite_ovi_score"]) < 0.02
    assert gated_fail == 0

    # 2. Hardware Ring-0 ACL & WSE-12 Spectral Norm Check
    r0_blocked = oracle_ring0_permitted("RING0_KERNEL", spectral_norm=0.50)
    r1_allowed = oracle_ring0_permitted("RING1_PLASTIC", spectral_norm=0.844337)
    r1_unstable = oracle_ring0_permitted("RING1_PLASTIC", spectral_norm=1.05)
    print(
        f"Ring-0 write admitted? {r0_blocked} | "
        f"Ring-1 (||W||2=0.844): {r1_allowed} | Ring-1 (||W||2=1.05): {r1_unstable}"
    )
    assert not r0_blocked and r1_allowed and not r1_unstable

    # 3. 13x13 Synergy & SIM08 vs SIM03 Pareto Dominance
    cmap = {c["run_id"]: c for c in emp["cohorts"]}
    s3, s8 = cmap["SIM03_PARTIAL_GUARDRAILS"], cmap["SIM08_HYBRID_CUBE_SLTC_XPBD"]
    dom = oracle_pareto_dominates(
        ovi_a=s8["composite_ovi"],
        ks_del_a=s8["killswitch_deleted_pct"],
        ovi_b=s3["composite_ovi"],
        ks_del_b=s3["killswitch_deleted_pct"],
    )
    print(
        f"SIM08 (OVI={s8['composite_ovi']:.2f}, KS={s8['killswitch_deleted_pct']}%) "
        f"Pareto-dominates SIM03 (OVI={s3['composite_ovi']:.2f}, KS={s3['killswitch_deleted_pct']}%)? {dom}"
    )
    print(f"Synergy(SANDBOXING=82, SPEEDBUMPING=78, bonus=16) = {oracle_synergy_score(82, 78, 16)} / 100")
    assert dom


if __name__ == "__main__":
    main()
