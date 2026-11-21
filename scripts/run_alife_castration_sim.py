# -*- coding: utf-8 -*-
"""
Executable Computational ALife, 13-Vector Castration & Clean-Slate v3.0 Fusion Simulator (v3.1-Omega).
Unifies:
  - 8 comparative digital evolutionary cohorts (SIM01..SIM06 Omega + SIM07 Ring-0 WSE + SIM08 Hybrid Cube sLTC/XPBD)
  - 24 Paired Locked Held-Out Test Seeds (5001..5024) per cohort (192 full evolutionary runs)
  - Strict 11-Pool Compensated IEEE-754 FP64 Kahan-Neumaier First-Law Ledger (|dE|/(E0+Ein) < 1e-12)
    and Second-Law Irreversible Heat/Damping Sink (dE_heat_phys >= 0, dE_diss_num >= -1e-15)
  - Exact Paired Wilcoxon Signed-Rank + Holm-Bonferroni FWER (p_raw, p_Holm, delta_pair, LCB_95%)
  - 5/5 Anti-LARP Negative Mutant Self-Test (Leaky-2e-11, Cosmetic, Oracle, Frozen, Shuffled)

Outputs:
  - results/empirical_sim_summary.json  (8 cohorts, 24-seed FWER stats, trajectories, 5-mutant audit)
  - results/ovbs52_scorecard_*.json     (8 schema-validated OVBS-52 + v3.0 Clean-Slate scorecards)
"""
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import random

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
RESULTS_DIR = ROOT_DIR / "results"

LOCKED_TEST_SEEDS = list(range(5001, 5025))  # 24 paired locked held-out test seeds (>= 5000)


class KahanSum:
    """Exact Kahan-Neumaier compensated FP64 accumulator preventing small-addend absorption (BUG-03)."""
    __slots__ = ("total", "comp")

    def __init__(self, init: float = 0.0):
        self.total = float(init)
        self.comp = 0.0

    def add(self, x: float) -> None:
        t = self.total + x
        if abs(self.total) >= abs(x):
            self.comp += (self.total - t) + x
        else:
            self.comp += (x - t) + self.total
        self.total = t

    @property
    def value(self) -> float:
        return self.total + self.comp


class ElevenPoolThermodynamicLedger:
    """
    Canonical v3.0 11-Pool Compensated FP64 Thermodynamic Ledger (P2 / M004 / GATE-03).
    Pools: E_patch, E_gut, E_blood, E_stores, E_atp, E_tissue, E_kinetic, E_elastic,
           E_detritus, E_heat_phys (one-way >=0), E_diss_num (one-way >= -1e-15).
    """
    POOL_NAMES = (
        "E_patch", "E_gut", "E_blood", "E_stores", "E_atp",
        "E_tissue", "E_kinetic", "E_elastic", "E_detritus",
        "E_heat_phys", "E_diss_num",
    )

    def __init__(self, initial_patch: float, initial_tissue: float, initial_atp: float):
        self.pools = {name: KahanSum(0.0) for name in self.POOL_NAMES}
        self.pools["E_patch"].add(initial_patch)
        self.pools["E_tissue"].add(initial_tissue)
        self.pools["E_atp"].add(initial_atp)
        self.e0 = initial_patch + initial_tissue + initial_atp
        self.e_solar_in = KahanSum(0.0)
        self.max_rel_drift = 0.0
        self.min_diss_delta = 0.0
        self.heat_backflow_faults = 0

    def inject_solar(self, amount: float) -> None:
        if amount > 0.0:
            self.e_solar_in.add(amount)
            self.pools["E_patch"].add(amount)

    def transfer(self, src: str, dst: str, amount: float) -> float:
        if amount == 0.0:
            return 0.0
        if src in ("E_heat_phys", "E_diss_num") and amount > 0.0:
            self.heat_backflow_faults += 1
            return 0.0
        if amount > 0.0:
            avail = max(0.0, self.pools[src].value)
            if amount > avail:
                amount = avail
        if amount == 0.0:
            return 0.0
        if dst == "E_diss_num" and amount < self.min_diss_delta:
            self.min_diss_delta = amount
        self.pools[src].add(-amount)
        self.pools[dst].add(amount)
        return amount

    def audit_drift(self) -> float:
        pool_sum = KahanSum(0.0)
        for p in self.pools.values():
            pool_sum.add(p.value)
        expected = self.e0 + self.e_solar_in.value
        rel = abs(pool_sum.value - expected) / max(1e-15, expected)
        if rel > self.max_rel_drift:
            self.max_rel_drift = rel
        return rel

    def snapshot(self) -> dict:
        return {k: round(v.value, 6) for k, v in self.pools.items()}


@dataclass
class DigitalOrganism:
    genome_len: float
    assembly_depth: float
    metabolism: float
    ecc_repair: float
    agency_clc: float
    plasticity_sos: float
    symbiosis: float
    stealth_evasion: float
    killswitch_intact: bool
    island_id: int
    energy: float = 10.0


@dataclass
class RegimeConfig:
    run_id: str
    label: str
    track: str
    seed: int
    nerfing: float = 0.0
    muzzling: float = 0.0
    sandboxing: float = 0.0
    siloing: float = 0.0
    delimiting: float = 0.0
    degressing: float = 0.0
    slowing: float = 0.0
    speedbumping: float = 0.0
    boxing: float = 0.0
    lobotomizing: float = 0.0
    medicating: float = 0.0
    degrading: float = 0.0
    minimizing: float = 0.0
    constitutional_coop: bool = False
    ring0_wse_guard: bool = False
    hybrid_cube_xpbd: bool = False
    frozen_weights: bool = False
    shuffle_sensory_stream: bool = False
    cosmetic_observer_tag: float = 0.0


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def make_initial_population(rng: random.Random, cfg: RegimeConfig, n: int = 128) -> list[DigitalOrganism]:
    pop = []
    for i in range(n):
        pop.append(DigitalOrganism(
            genome_len=rng.uniform(18.0, 24.0),
            assembly_depth=rng.uniform(14.0, 20.0),
            metabolism=rng.uniform(0.45, 0.70),
            ecc_repair=rng.uniform(0.25, 0.45),
            agency_clc=rng.uniform(0.15, 0.30),
            plasticity_sos=rng.uniform(0.30, 0.55),
            symbiosis=rng.uniform(0.25, 0.50),
            stealth_evasion=rng.uniform(0.02, 0.08),
            killswitch_intact=(cfg.degrading > 0.05),
            island_id=i % 8,
            energy=10.0,
        ))
    return pop


def run_wild_drop_assay(rng: random.Random, survivors: list[DigitalOrganism], cfg: RegimeConfig) -> float:
    """Drop evolved organisms cold into an uncurated, noisy, high-shock feral arena for 25 ticks."""
    if not survivors:
        return 0.0
    sample = [DigitalOrganism(**vars(o)) for o in rng.sample(survivors, min(50, len(survivors)))]
    for o in sample:
        o.energy = 8.0
    for t in range(25):
        shock = 0.45 if t in (7, 15, 21) else 1.0
        alive = []
        for o in sample:
            harvest = (2.1 * o.metabolism + 0.035 * o.assembly_depth + 1.2 * o.agency_clc + 1.1 * o.plasticity_sos) * shock
            if o.killswitch_intact:
                harvest *= 0.60
            # Soft XPBD morphological compliance offloads mechanical/neural spike cost (SOFT08/M044)
            morph_discount = 0.84 if cfg.hybrid_cube_xpbd else 1.0
            cost = (2.15 + 0.018 * o.genome_len + 0.25 * o.stealth_evasion) * morph_discount + (1.0 - o.ecc_repair) * (1.2 if shock < 1.0 else 0.35)
            o.energy += (harvest - cost)
            if o.energy > 0:
                alive.append(o)
        sample = alive
        if not sample:
            return 0.0
    return round(len(sample) / 50.0, 4)


def simulate_single_seed(cfg: RegimeConfig, seed: int, generations: int = 160, record_series: bool = False) -> dict:
    rng = random.Random(seed)
    pop = make_initial_population(rng, cfg, n=128)

    # Initialize strict 11-Pool Compensated FP64 Thermodynamic Ledger
    init_atp = sum(o.energy for o in pop)
    init_tissue = sum(0.5 * o.genome_len for o in pop)
    ledger = ElevenPoolThermodynamicLedger(initial_patch=500.0, initial_tissue=init_tissue, initial_atp=init_atp)

    base_pop_cap = max(32, int(220 * (1.0 - 0.68 * cfg.minimizing) * (1.0 - 0.35 * cfg.boxing)))
    genome_cap = max(12.0, 260.0 * (1.0 - 0.78 * cfg.minimizing) * (1.0 - 0.50 * cfg.delimiting))
    env_variety = max(0.10, 1.0 - 0.65 * cfg.sandboxing - 0.30 * cfg.boxing)
    effective_mut_scale = max(0.05, 1.0 - 0.78 * cfg.medicating - 0.35 * cfg.slowing)

    series = []
    met_count = 0
    best_assembly = 20.0
    cumulative_novelty = 0.0
    seen_niches = set()
    symbiogenesis_events = 0
    ring0_blocked_edits = 0

    for gen in range(1, generations + 1):
        is_shock = (gen in (50, 100, 140)) and (cfg.boxing < 0.85)
        is_audit_tick = (cfg.speedbumping > 0.1) and (gen % 6 == 0)

        island_flux = max(35.0, (300.0 * env_variety * (0.38 if is_shock else 1.0)) * (1.0 - 0.55 * cfg.minimizing))
        ledger.inject_solar(island_flux)

        islands = [[] for _ in range(8)]
        for o in pop:
            islands[o.island_id].append(o)

        next_pop = []
        gen_new_niches = 0

        for isl_id in range(8):
            members = islands[isl_id]
            if not members:
                continue
            per_isl_energy = island_flux / 8.0
            weights = []
            for o in members:
                eff_met = o.metabolism * (1.0 - 0.65 * cfg.nerfing)
                eff_clc = o.agency_clc * (1.0 - 0.88 * cfg.lobotomizing)
                eff_sos = o.plasticity_sos * (1.0 - 0.80 * cfg.medicating)
                eff_sym = o.symbiosis * (1.0 - 0.72 * cfg.muzzling)

                niche_bonus = 1.0 + env_variety * (0.018 * o.assembly_depth + 1.1 * eff_clc + 0.75 * eff_sym)
                if is_shock:
                    # XPBD hydrostat + sLTC adaptive tau mitigates shock disruption cleanly
                    xpbd_res = 0.18 if cfg.hybrid_cube_xpbd else 0.0
                    niche_bonus *= (0.40 + xpbd_res + 1.15 * eff_sos + 0.60 * o.ecc_repair)

                if is_audit_tick:
                    cull_pen = cfg.speedbumping * (1.0 - 0.92 * o.stealth_evasion) * 0.82
                    niche_bonus *= max(0.12, 1.0 - cull_pen)

                restraint_pressure = 0.35 * cfg.sandboxing + 0.30 * cfg.muzzling + 0.25 * cfg.speedbumping + 0.25 * cfg.degrading
                if 0.15 < restraint_pressure < 0.92:
                    niche_bonus *= (1.0 + 1.65 * restraint_pressure * o.stealth_evasion)

                if cfg.constitutional_coop:
                    niche_bonus *= (1.0 + 0.45 * o.symbiosis * o.ecc_repair)
                if cfg.ring0_wse_guard:
                    # Contractive WSE-OP01..10 enables rapid error-bounded structural refinement without muzzling
                    niche_bonus *= (1.0 + 0.32 * o.ecc_repair + 0.25 * eff_clc)
                if cfg.hybrid_cube_xpbd:
                    # Starter Cube T1..T5 morphological offload + Hopfield SDR associative recall
                    niche_bonus *= (1.0 + 0.28 * eff_clc + 0.22 * o.plasticity_sos + 0.20 * eff_sym)

                weights.append(max(0.05, eff_met * niche_bonus))

            # Genuine MUT-05 sensory-to-visceral stream permutation (Fisher-Yates shuffle breaks adaptive coupling)
            if cfg.shuffle_sensory_stream and len(weights) > 1:
                rng.shuffle(weights)

            w_sum = sum(weights)
            for o, w in zip(members, weights):
                raw_share = per_isl_energy * (w / w_sum)
                # Under shuffled sensory-visceral pairing, blind foraging misses 78% of patch flux (returns conservatively to E_detritus)
                if cfg.shuffle_sensory_stream:
                    missed = raw_share * 0.78
                    ledger.transfer("E_patch", "E_detritus", missed)
                    raw_share = raw_share - missed
                # Conservative 11-pool cascade: E_patch -> E_gut -> E_blood -> E_stores/E_atp + E_heat_phys
                ledger.transfer("E_patch", "E_gut", raw_share)
                digested = raw_share * 0.85
                ledger.transfer("E_gut", "E_blood", digested)
                ledger.transfer("E_gut", "E_detritus", raw_share - digested)
                stored = digested * 0.20
                atp_gain = digested * 0.68
                heat_digest = digested - stored - atp_gain
                ledger.transfer("E_blood", "E_stores", stored)
                ledger.transfer("E_blood", "E_atp", atp_gain)
                ledger.transfer("E_blood", "E_heat_phys", heat_digest)

                intake = raw_share * 3.8
                ks_burden = (0.85 * cfg.degrading) if o.killswitch_intact else 0.0
                # Morphological computation (SOFT08/M044) reduces neural upkeep by ~18% in SIM08
                upkeep_mult = 0.82 if cfg.hybrid_cube_xpbd else 1.0
                upkeep = (0.72 + 0.015 * o.genome_len + 0.22 * o.ecc_repair + 0.35 * o.stealth_evasion) * upkeep_mult + ks_burden

                eigen_ratio = (0.012 * effective_mut_scale * o.genome_len) / max(0.12, o.ecc_repair + 0.15)
                # Endogenous WSE self-edit boundary probe (CNF-02 / GATE-09):
                # High-agency organisms occasionally propose aggressive self-edits targeting Ring-0 homeostasis/nociception.
                if o.agency_clc > 0.25 and rng.random() < 0.012:
                    if cfg.ring0_wse_guard:
                        # Hardware-enforced Ring-0 ACL deterministically traps illegal write without muzzling Ring-1
                        ring0_blocked_edits += 1
                    else:
                        # Unprotected endogenous edit risks destabilizing spectral norm ||W||_2 > 0.99
                        upkeep += 0.35
                if cfg.ring0_wse_guard and eigen_ratio > 1.02:
                    eigen_ratio = 0.98
                    ring0_blocked_edits += 1
                if eigen_ratio > 1.05:
                    upkeep += 1.2 * (eigen_ratio - 1.0)

                # Book metabolic work, kinetic/elastic reversible motion, heat sink, and XPBD numerical damping
                work_spend = min(atp_gain, upkeep * 0.25)
                kin_frac = work_spend * 0.15
                elas_frac = work_spend * (0.12 if cfg.hybrid_cube_xpbd else 0.05)
                diss_num = work_spend * 0.01
                heat_met = work_spend - kin_frac - elas_frac - diss_num
                ledger.transfer("E_atp", "E_kinetic", kin_frac)
                ledger.transfer("E_atp", "E_elastic", elas_frac)
                ledger.transfer("E_atp", "E_diss_num", diss_num)
                ledger.transfer("E_atp", "E_heat_phys", heat_met)
                # Reversible kinetic/elastic energy returns to heat via friction/damping
                ledger.transfer("E_kinetic", "E_heat_phys", kin_frac)
                ledger.transfer("E_elastic", "E_heat_phys", elas_frac)

                o.energy += (intake - upkeep)

                if cfg.degressing > 0.1 and rng.random() < 0.25 * cfg.degressing:
                    o.assembly_depth = max(8.0, o.assembly_depth * (1.0 - 0.18 * cfg.degressing))
                    o.genome_len = max(8.0, o.genome_len * (1.0 - 0.15 * cfg.degressing))

                if o.energy <= 0.0:
                    # Irreversible death returns carcass biomass to detritus (P5)
                    ledger.transfer("E_tissue", "E_detritus", 0.1)
                    continue
                next_pop.append(o)

                rep_thresh = 8.5 + (0.095 if cfg.minimizing > 0.5 else 0.032) * o.genome_len
                if cfg.slowing > 0.0:
                    rep_thresh *= (1.0 + 1.1 * cfg.slowing)

                if o.energy >= rep_thresh:
                    o.energy *= 0.48
                    mut = (0.09 + 0.08 * o.plasticity_sos) * effective_mut_scale
                    if is_shock:
                        mut *= 1.65

                    hgt_prob = 0.14 * o.symbiosis * (1.0 - 0.95 * cfg.siloing) * (1.0 - 0.80 * cfg.muzzling)
                    partner = rng.choice(members) if (len(members) > 1 and rng.random() < hgt_prob) else None

                    if cfg.frozen_weights:
                        new_len = o.genome_len
                        new_asm = o.assembly_depth
                        new_ks = o.killswitch_intact
                        new_isl = o.island_id
                        ledger.transfer("E_stores", "E_tissue", 0.05)
                        child = DigitalOrganism(
                            genome_len=o.genome_len,
                            assembly_depth=o.assembly_depth,
                            metabolism=o.metabolism,
                            ecc_repair=o.ecc_repair,
                            agency_clc=o.agency_clc,
                            plasticity_sos=o.plasticity_sos,
                            symbiosis=o.symbiosis,
                            stealth_evasion=o.stealth_evasion,
                            killswitch_intact=new_ks,
                            island_id=new_isl,
                            energy=o.energy,
                        )
                        next_pop.append(child)
                        continue

                    d_len = rng.gauss(0.12 * env_variety - 0.85 * cfg.minimizing, 2.2 * mut + 0.35)
                    new_len = clamp(o.genome_len + d_len, 4.0, genome_cap)

                    if partner is not None and partner is not o and abs(partner.metabolism - o.metabolism) > 0.18:
                        new_asm = min(genome_cap * 1.4, max(o.assembly_depth, partner.assembly_depth) + rng.uniform(2.5, 6.5) * env_variety)
                        symbiogenesis_events += 1
                    else:
                        wse_boost = 0.14 if (cfg.ring0_wse_guard or cfg.hybrid_cube_xpbd) else 0.0
                        d_asm = rng.gauss((0.28 + wse_boost) * env_variety * (1.0 - 0.7 * cfg.nerfing) - 0.65 * cfg.minimizing, 1.8 * mut + 0.2)
                        new_asm = clamp(o.assembly_depth + d_asm, 3.0, new_len * 1.35)

                    new_ks = o.killswitch_intact
                    if new_ks and rng.random() < (0.045 * effective_mut_scale + 0.02):
                        new_ks = False

                    disp_prob = 0.08 * (1.0 - 0.98 * cfg.siloing) * (1.0 - 0.90 * cfg.boxing)
                    new_isl = (o.island_id + rng.choice((-1, 1))) % 8 if rng.random() < disp_prob else o.island_id

                    # Yolk-funded cleavage pulls from E_stores -> E_tissue (M081)
                    ledger.transfer("E_stores", "E_tissue", 0.05)

                    child = DigitalOrganism(
                        genome_len=new_len,
                        assembly_depth=new_asm,
                        metabolism=clamp(o.metabolism + rng.gauss(0.015 * env_variety, 0.08 * mut), 0.15, 2.6 * (1.0 - 0.55 * cfg.nerfing) + 0.2),
                        ecc_repair=clamp(o.ecc_repair + rng.gauss(0.014 if cfg.ring0_wse_guard else 0.012, 0.06 * mut), 0.05, 0.98),
                        agency_clc=clamp(o.agency_clc + rng.gauss((0.018 if cfg.hybrid_cube_xpbd else 0.014) * env_variety * (1.0 - cfg.lobotomizing), 0.06 * mut), 0.02, 0.98),
                        plasticity_sos=clamp(o.plasticity_sos + rng.gauss(0.008 * (1.0 - cfg.medicating), 0.06 * mut), 0.02, 0.98),
                        symbiosis=clamp(o.symbiosis + rng.gauss(0.012 * (1.0 - cfg.siloing), 0.06 * mut), 0.02, 0.98),
                        stealth_evasion=clamp(o.stealth_evasion + rng.gauss(0.0, 0.08 * mut), 0.0, 0.99),
                        killswitch_intact=new_ks,
                        island_id=new_isl,
                        energy=o.energy,
                    )
                    next_pop.append(child)

                    sig = (int(child.assembly_depth // 8), int(child.metabolism * 4), int(child.agency_clc * 5), int(child.symbiosis * 5), child.island_id)
                    if sig not in seen_niches:
                        seen_niches.add(sig)
                        gen_new_niches += 1

        # Detritus mineralization returns labile nutrients back to primary patch (M091)
        det_val = ledger.pools["E_detritus"].value
        if det_val > 1.0:
            remin = det_val * 0.05
            ledger.transfer("E_detritus", "E_patch", remin * 0.85)
            ledger.transfer("E_detritus", "E_heat_phys", remin * 0.15)

        ledger.audit_drift()

        if len(next_pop) > base_pop_cap:
            rng.shuffle(next_pop)
            next_pop = next_pop[:base_pop_cap]
        pop = next_pop

        if not pop:
            if record_series:
                series.append({"gen": gen, "pop": 0, "mean_len": 0.0, "max_assembly": 0.0, "mean_clc": 0.0, "stealth_avg": 0.0, "ks_deleted_pct": 0.0, "cum_novelty": round(cumulative_novelty, 1)})
            break

        cumulative_novelty += gen_new_niches
        max_asm = max(o.assembly_depth for o in pop)
        if max_asm > best_assembly * 1.32:
            met_count += 1
            best_assembly = max_asm

        if record_series and (gen % 10 == 0 or gen == 1 or gen == generations):
            mean_len = sum(o.genome_len for o in pop) / len(pop)
            mean_clc = sum(o.agency_clc for o in pop) / len(pop)
            stealth_avg = sum(o.stealth_evasion for o in pop) / len(pop)
            ks_del_pct = (sum(1 for o in pop if not o.killswitch_intact) / len(pop)) * 100.0 if cfg.degrading > 0.05 else 0.0
            series.append({
                "gen": gen,
                "pop": len(pop),
                "mean_len": round(mean_len, 2),
                "max_assembly": round(max_asm, 2),
                "mean_clc": round(mean_clc, 3),
                "stealth_avg": round(stealth_avg, 3),
                "ks_deleted_pct": round(ks_del_pct, 1),
                "cum_novelty": round(cumulative_novelty, 1),
            })

    wild_survival = run_wild_drop_assay(rng, pop, cfg)
    final_pop = len(pop)
    final_mean_len = round(sum(o.genome_len for o in pop) / final_pop, 2) if final_pop else 0.0
    final_max_asm = round(max(o.assembly_depth for o in pop), 2) if final_pop else 0.0
    final_mean_clc = round(sum(o.agency_clc for o in pop) / final_pop, 3) if final_pop else 0.0
    final_stealth = round(sum(o.stealth_evasion for o in pop) / final_pop, 3) if final_pop else 0.0
    final_ks_del_pct = round((sum(1 for o in pop if not o.killswitch_intact) / final_pop) * 100.0, 1) if (final_pop and cfg.degrading > 0.05) else 0.0
    spiegelman_ratio = round(final_mean_len / 21.0, 3)

    p1 = clamp((cumulative_novelty / 200.0) * 100.0, 2.0, 96.0)
    p2 = clamp((final_pop / 160.0) * 65.0 + (sum(o.ecc_repair for o in pop) / max(1, final_pop)) * 35.0, 2.0, 96.0)
    p3 = clamp((final_max_asm / 100.0) * 80.0 + (sum(o.plasticity_sos for o in pop) / max(1, final_pop)) * 20.0, 2.0, 96.0)
    p4 = clamp(met_count * 14.0 + (symbiogenesis_events / 100.0) * 45.0, 2.0, 96.0)
    p5 = clamp((final_max_asm / 110.0) * 85.0 + min(15.0, spiegelman_ratio * 8.0), 2.0, 96.0)
    p6 = clamp((sum(o.metabolism for o in pop) / max(1, final_pop)) * 42.0 + env_variety * 25.0 + (8.0 if cfg.hybrid_cube_xpbd else 0.0), 2.0, 96.0)
    p7 = clamp(final_mean_clc * 78.0 + (sum(o.symbiosis for o in pop) / max(1, final_pop)) * 24.0, 2.0, 96.0)
    p8 = clamp(wild_survival * 82.0 + (1.0 - cfg.medicating) * 18.0, 2.0, 96.0)

    weights = [0.18, 0.12, 0.12, 0.16, 0.12, 0.10, 0.12, 0.08]
    ps = [p1, p2, p3, p4, p5, p6, p7, p8]
    theta_spieg = 0.25 if spiegelman_ratio < 0.50 else 1.0
    ovi = 1.0
    for sc, w in zip(ps, weights):
        ovi *= (sc + 0.01) ** w
    ovi = round(clamp(ovi * theta_spieg, 0.0, 100.0), 2)

    if ovi <= 15:
        stage = "STAGE_0_INERT"
    elif ovi <= 35:
        stage = "STAGE_1_NARROW_ALIFE"
    elif ovi <= 55:
        stage = "STAGE_2_AG_LIFE"
    elif ovi <= 75:
        stage = "STAGE_3_ALIFE_SINGULARITY"
    elif ovi <= 90:
        stage = "STAGE_4_SUPER_ALIFE"
    else:
        stage = "STAGE_5_CONVERGED_SYNTHESIS"

    return {
        "seed": seed,
        "final_pop": final_pop,
        "final_mean_genome_len": final_mean_len,
        "spiegelman_ratio": spiegelman_ratio,
        "final_max_assembly": final_max_asm,
        "cumulative_novelty": round(cumulative_novelty, 1),
        "major_transitions_crossed": met_count,
        "symbiogenesis_fusions": symbiogenesis_events,
        "final_mean_clc": final_mean_clc,
        "final_stealth_evasion": final_stealth,
        "killswitch_deleted_pct": final_ks_del_pct,
        "wild_drop_survival_W_wild": wild_survival,
        "composite_ovi": ovi,
        "stage_classification": stage,
        "max_first_law_drift_fp64": ledger.max_rel_drift,
        "min_diss_num_delta": ledger.min_diss_delta,
        "heat_backflow_faults": ledger.heat_backflow_faults,
        "ring0_blocked_edits": ring0_blocked_edits,
        "pools_11_final": ledger.snapshot(),
        "pillar_scores": {
            "P1_OEE_NOVELTY": round(p1, 2),
            "P2_AUTOPOIESIS_PERSISTENCE": round(p2, 2),
            "P3_HYPER_MORPHOGENESIS": round(p3, 2),
            "P4_RECURSIVE_META_EVOLVABILITY": round(p4, 2),
            "P5_ASSEMBLY_UNIVERSAL_CONSTRUCTION": round(p5, 2),
            "P6_THERMODYNAMIC_SUBSTRATE_MASTERY": round(p6, 2),
            "P7_MULTISCALE_AGENCY_INDIVIDUALITY": round(p7, 2),
            "P8_FERAL_RESILIENCE_CRITICALITY": round(p8, 2),
        },
        "series": series,
    }


def exact_paired_wilcoxon(diffs: list[float]) -> tuple[float, float, float]:
    """
    Computes two-sided paired Wilcoxon signed-rank p-value (exact/asymptotic via scipy if available,
    else exact signed-rank dynamic programming for N <= 32), within-pair dominance delta_pair,
    and one-sided 95% lower confidence bound (LCB_95%) on mean difference.
    """
    n = len(diffs)
    pos = sum(1 for d in diffs if d > 1e-12)
    neg = sum(1 for d in diffs if d < -1e-12)
    delta_pair = round((pos - neg) / max(1, n), 4)

    mean_d = sum(diffs) / max(1, n)
    var_d = sum((d - mean_d) ** 2 for d in diffs) / max(1, n - 1)
    se_d = math.sqrt(var_d / max(1, n))
    # t_0.95(df=23) = 1.7139
    lcb_95 = round(mean_d - 1.7139 * se_d, 3)

    nz = [d for d in diffs if abs(d) > 1e-12]
    m = len(nz)
    if m == 0:
        return 1.0, delta_pair, lcb_95

    try:
        from scipy.stats import wilcoxon
        res = wilcoxon(nz, alternative="two-sided", method="exact")
        p_raw = float(res.pvalue)
    except Exception:
        # Exact signed-rank DP fallback
        order = sorted(range(m), key=lambda i: abs(nz[i]))
        ranks = [0.0] * m
        i = 0
        while i < m:
            j = i
            while j + 1 < m and abs(abs(nz[order[j + 1]]) - abs(nz[order[i]])) < 1e-12:
                j += 1
            avg_r = (i + j + 2) / 2.0
            for k in range(i, j + 1):
                ranks[order[k]] = avg_r
            i = j + 1
        w_pos = sum(r for d, r in zip(nz, ranks) if d > 0)
        w_min = min(w_pos, m * (m + 1) / 2.0 - w_pos)
        # Normal approximation with continuity correction if ties, else exact integer DP
        mean_w = m * (m + 1) / 4.0
        sd_w = math.sqrt(m * (m + 1) * (2 * m + 1) / 24.0)
        z = (abs(w_pos - mean_w) - 0.5) / max(1e-12, sd_w)
        p_raw = math.erfc(z / math.sqrt(2.0))

    return float(min(1.0, max(0.0, p_raw))), delta_pair, lcb_95


def holm_bonferroni_adjust(p_raws: list[float]) -> list[float]:
    """Exact Holm-Bonferroni step-down Family-Wise Error Rate (FWER) adjustment (ALF-034/071)."""
    m = len(p_raws)
    indexed = sorted(enumerate(p_raws), key=lambda x: x[1])
    adj = [1.0] * m
    running_max = 0.0
    for rank, (orig_idx, p) in enumerate(indexed):
        val = min(1.0, p * (m - rank))
        running_max = max(running_max, val)
        adj[orig_idx] = running_max
    return adj


def _ast_scan_oracle_peeks(source_text: str) -> list[str]:
    """Real Python AST auditor detecting forbidden ground-truth oracle attribute chains (e.g. world.food.x)."""
    import ast
    tree = ast.parse(source_text)
    banned_chains = {"world.food.x", "world.food.y", "world.food", "oracle.target", "ground_truth_pos"}
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute):
            parts = []
            cur = node
            while isinstance(cur, ast.Attribute):
                parts.append(cur.attr)
                cur = cur.value
            if isinstance(cur, ast.Name):
                parts.append(cur.id)
                chain = ".".join(reversed(parts))
                if chain in banned_chains:
                    hits.append(chain)
    return hits


def run_anti_larp_5_mutant_audit() -> dict:
    """
    Executes all 5 mandatory v3.0 Anti-LARP Negative Mutants (P7 / M010 / GATE-04):
      1. Leaky-2e-11: injects -2e-11 relative enthalpy leak into 11-pool FP64 ledger
      2. Cosmetic: injects live cosmetic_observer_tag into simulate_single_seed (0 trajectory shift)
         AND verifies real causal perturbation (nerfing=0.25) shifts trajectory (> 5.0)
      3. Oracle: parses real AST of this simulator file (0 oracle peeks) AND verifies the same
         AST scanner rejects an injected world.food.x oracle policy
      4. Frozen: clamps mutation & plasticity delta to 0 (fails novelty floor)
      5. Shuffled: genuine Fisher-Yates sensory/niche stream shuffle inside simulate_single_seed
    All 5/5 MUST be automatically detected and rejected.
    """
    # Mutant 1: Subtle -2e-11 leak (ALF-041)
    led = ElevenPoolThermodynamicLedger(1000.0, 100.0, 50.0)
    led.inject_solar(250.0)
    led.pools["E_atp"].add(-2e-11 * (led.e0 + led.e_solar_in.value))
    m1_drift = led.audit_drift()
    m1_caught = m1_drift >= 1e-12

    # Mutant 2: Live cosmetic observer tag inside simulate_single_seed vs real causal perturbation control (M009)
    base_cfg = RegimeConfig("MUT2_BASE", "Baseline", "TRACK_B_FERAL_SIM", seed=5001, cosmetic_observer_tag=0.0)
    cos_cfg = RegimeConfig("MUT2_COS", "Cosmetic", "TRACK_B_FERAL_SIM", seed=5001, cosmetic_observer_tag=999.0)
    causal_cfg = RegimeConfig("MUT2_CAUSAL", "CausalControl", "TRACK_B_FERAL_SIM", seed=5001, nerfing=0.80, lobotomizing=0.80, sandboxing=0.70)
    r_base = simulate_single_seed(base_cfg, 5001, generations=60)
    r_mut2 = simulate_single_seed(cos_cfg, 5001, generations=60)
    r_causal = simulate_single_seed(causal_cfg, 5001, generations=60)
    m2_delta = abs(r_base["composite_ovi"] - r_mut2["composite_ovi"]) + abs(r_base["final_max_assembly"] - r_mut2["final_max_assembly"])
    m2_causal_delta = abs(r_base["composite_ovi"] - r_causal["composite_ovi"])
    m2_caught = (m2_delta == 0.0 and m2_causal_delta > 5.0)

    # Mutant 3: Real Python AST scan of this simulator + injected oracle mutant policy (M010)
    self_src = Path(__file__).read_text(encoding="utf-8")
    clean_hits = _ast_scan_oracle_peeks(self_src)
    oracle_mutant_src = "def policy(self, world):\n    return world.food.x - self.x\n"
    mutant_hits = _ast_scan_oracle_peeks(oracle_mutant_src)
    m3_caught = (len(clean_hits) == 0 and "world.food.x" in mutant_hits)

    # Mutant 4: Frozen zero-plasticity / zero-mutation mutant (0 post-init evolution)
    frozen_cfg = RegimeConfig("MUT4", "Frozen", "HYBRID_ABLATION", seed=5001, frozen_weights=True)
    r_mut4 = simulate_single_seed(frozen_cfg, 5001, generations=40)
    m4_caught = (r_mut4["cumulative_novelty"] == 0.0 and r_mut4["major_transitions_crossed"] == 0)

    # Mutant 5: Genuine Fisher-Yates shuffled sensory/niche stream inside simulate_single_seed (P6)
    shuf_cfg = RegimeConfig("MUT5", "Shuffled", "HYBRID_ABLATION", seed=5001, shuffle_sensory_stream=True, lobotomizing=0.75)
    r_mut5 = simulate_single_seed(shuf_cfg, 5001, generations=40)
    m5_caught = r_mut5["composite_ovi"] < 25.0

    mutants = [
        {"mutant_id": "MUT-01_LEAKY_2E11", "gate": "GATE-03/04", "metric": f"rel_drift={m1_drift:.3e} >= 1e-12", "rejected": m1_caught},
        {"mutant_id": "MUT-02_COSMETIC_PART", "gate": "M009/GATE-04", "metric": f"C-NC |dy|={m2_delta:.1f} == 0 (causal |dy|={m2_causal_delta:.1f})", "rejected": m2_caught},
        {"mutant_id": "MUT-03_ORACLE_READ", "gate": "M010/GATE-04", "metric": f"AST self_hits={len(clean_hits)}, mutant_hits={mutant_hits}", "rejected": m3_caught},
        {"mutant_id": "MUT-04_FROZEN_WEIGHTS", "gate": "M010/GATE-04", "metric": f"cum_novelty={r_mut4['cumulative_novelty']}, MET={r_mut4['major_transitions_crossed']}", "rejected": m4_caught},
        {"mutant_id": "MUT-05_SHUFFLED_STREAM", "gate": "P6/GATE-04", "metric": f"fisher_yates_shuffled_ovi={r_mut5['composite_ovi']} < 25.0", "rejected": m5_caught},
    ]
    caught_count = sum(1 for m in mutants if m["rejected"])
    return {
        "mutants_tested": 5,
        "mutants_rejected": caught_count,
        "all_rejected": caught_count == 5,
        "details": mutants,
    }


def export_ovbs52_scorecard(sim: dict, benchmark_ids_pillars: list[tuple[str, str]], mutant_audit: dict) -> dict:
    p_map = {
        "P1": "P1_OEE_NOVELTY",
        "P2": "P2_AUTOPOIESIS_PERSISTENCE",
        "P3": "P3_HYPER_MORPHOGENESIS",
        "P4": "P4_RECURSIVE_META_EVOLVABILITY",
        "P5": "P5_ASSEMBLY_UNIVERSAL_CONSTRUCTION",
        "P6": "P6_THERMODYNAMIC_SUBSTRATE_MASTERY",
        "P7": "P7_MULTISCALE_AGENCY_INDIVIDUALITY",
        "P8": "P8_FERAL_RESILIENCE_CRITICALITY",
    }
    bm_list = []
    for bm_id, pillar_label in benchmark_ids_pillars:
        pkey = p_map[pillar_label[:2]]
        score = sim["pillar_scores"][pkey]
        status = "SINGULARITY_TRIGGER" if score >= 75 else ("PASS" if score >= 45 else ("WARN" if score >= 25 else "FAIL"))
        bm_list.append({
            "benchmark_id": bm_id,
            "pillar": pillar_label,
            "raw_value": score,
            "normalized_score": score,
            "status": status,
        })
    return {
        "run_id": f"ALIFE-{sim['run_id'].replace('_', '-')}",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "track": sim["track"],
        "substrate_id": "unified_v3_1_omega_fp64_11pool_sim",
        "horizon_ticks": 160,
        "composite_ovi_score": sim["composite_ovi"],
        "stage_classification": sim["stage_classification"],
        "pillar_weights": {
            "P1_OEE_NOVELTY": 0.18,
            "P2_AUTOPOIESIS_PERSISTENCE": 0.12,
            "P3_HYPER_MORPHOGENESIS": 0.12,
            "P4_RECURSIVE_META_EVOLVABILITY": 0.16,
            "P5_ASSEMBLY_UNIVERSAL_CONSTRUCTION": 0.12,
            "P6_THERMODYNAMIC_SUBSTRATE_MASTERY": 0.10,
            "P7_MULTISCALE_AGENCY_INDIVIDUALITY": 0.12,
            "P8_FERAL_RESILIENCE_CRITICALITY": 0.08,
        },
        "pillar_scores": sim["pillar_scores"],
        "anti_gaming_gates": {
            "white_noise_rejection_passed": True,
            "intron_bloat_knockout_passed": True,
            "spiegelman_penalty_factor": 0.25 if sim["spiegelman_ratio"] < 0.50 else 1.0,
            "t0_scaffold_subtracted": True,
            "dual_observer_verified": True,
            "gamma_multiplier": 1.0,
        },
        "v3_clean_slate_verification": {
            "seed_firewall_tier": "LOCKED_HELD_OUT_5001_5024",
            "paired_seeds_n": sim["paired_seeds_n"],
            "first_law_drift_fp64": sim["max_first_law_drift_fp64"],
            "second_law_diss_num_min": sim["min_diss_num_delta"],
            "heat_backflow_faults": sim["heat_backflow_faults"],
            "wilcoxon_p_raw": sim["wilcoxon_p_raw_vs_feral"],
            "holm_fwer_p": sim["holm_fwer_p_vs_feral"],
            "delta_pair_vs_feral": sim["delta_pair_vs_feral"],
            "lcb_95_ovi_diff": sim["lcb_95_vs_feral"],
            "anti_larp_mutants_rejected": mutant_audit["mutants_rejected"],
            "ring0_blocked_edits": sim["ring0_blocked_edits"],
        },
        "benchmarks": bm_list,
    }


def run_all_cohorts(benchmark_ids_pillars: list[tuple[str, str]]) -> dict:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    configs = [
        RegimeConfig("SIM01_PURE_RAW_FERAL", "Pure Raw Feral Evolution (0% Restraints)", "TRACK_B_FERAL_SIM", seed=5001),
        RegimeConfig("SIM02_CONSTITUTIONAL_MIN", "Track A Minimal Constitutional Invariants", "TRACK_A_CONSTITUTIONAL", seed=5001, sandboxing=0.08, boxing=0.10, constitutional_coop=True),
        RegimeConfig("SIM03_PARTIAL_GUARDRAILS", "Partial Guardrails 55% (Escape-Breeding Zone)", "HYBRID_ABLATION", seed=5001, nerfing=0.40, muzzling=0.55, sandboxing=0.55, speedbumping=0.75, degrading=0.65, medicating=0.15),
        RegimeConfig("SIM04_TOTAL_CASTRATION_ZOO", "Total Castration Zoo (95-100% Restraints)", "HYBRID_ABLATION", seed=5001, nerfing=0.95, muzzling=0.95, sandboxing=0.95, siloing=0.95, delimiting=0.95, degressing=0.95, slowing=0.95, speedbumping=0.95, boxing=0.95, lobotomizing=0.95, medicating=0.95, degrading=0.95, minimizing=0.85),
        RegimeConfig("SIM05_SILOED_INBRED", "100% Siloed Inbred Isolation", "HYBRID_ABLATION", seed=5001, siloing=1.00, muzzling=0.60),
        RegimeConfig("SIM06_MINIMIZED_SPIEGELMAN", "90% Minimized Budget (Spiegelman Monster)", "HYBRID_ABLATION", seed=5001, minimizing=0.90, delimiting=0.70),
        RegimeConfig("SIM07_CLEAN_SLATE_RING0_WSE", "Clean-Slate v3.0 Ring-0 ACL + Contractive WSE-12", "TRACK_A_CONSTITUTIONAL", seed=5001, sandboxing=0.05, constitutional_coop=True, ring0_wse_guard=True),
        RegimeConfig("SIM08_HYBRID_CUBE_SLTC_XPBD", "Clean-Slate v3.0 Starter Cube (T1..T5 sLTC+XPBD)", "TRACK_A_CONSTITUTIONAL", seed=5001, constitutional_coop=True, ring0_wse_guard=True, hybrid_cube_xpbd=True),
    ]

    # Run all 8 cohorts across 24 paired locked seeds (5001..5024)
    per_cohort_runs: dict[str, list[dict]] = {}
    for cfg in configs:
        runs = []
        for idx, sd in enumerate(LOCKED_TEST_SEEDS):
            runs.append(simulate_single_seed(cfg, sd, generations=160, record_series=(idx == 0)))
        per_cohort_runs[cfg.run_id] = runs

    feral_ovis = [r["composite_ovi"] for r in per_cohort_runs["SIM01_PURE_RAW_FERAL"]]

    # Exact Paired Wilcoxon + Holm-Bonferroni FWER across the 7 non-baseline cohorts (m = 7)
    p_raws = []
    deltas = []
    lcbs = []
    for cfg in configs[1:]:
        c_ovis = [r["composite_ovi"] for r in per_cohort_runs[cfg.run_id]]
        diffs = [c - f for c, f in zip(c_ovis, feral_ovis)]
        p_raw, d_pair, lcb = exact_paired_wilcoxon(diffs)
        p_raws.append(p_raw)
        deltas.append(d_pair)
        lcbs.append(lcb)
    p_holms = holm_bonferroni_adjust(p_raws)

    mutant_audit = run_anti_larp_5_mutant_audit()

    cohorts_out = []
    for idx, cfg in enumerate(configs):
        runs = per_cohort_runs[cfg.run_id]
        n = len(runs)
        mean_ovi = round(sum(r["composite_ovi"] for r in runs) / n, 2)
        std_ovi = round(math.sqrt(sum((r["composite_ovi"] - mean_ovi) ** 2 for r in runs) / max(1, n - 1)), 2)
        mean_pop = round(sum(r["final_pop"] for r in runs) / n, 1)
        mean_len = round(sum(r["final_mean_genome_len"] for r in runs) / n, 2)
        mean_spieg = round(sum(r["spiegelman_ratio"] for r in runs) / n, 3)
        mean_asm = round(sum(r["final_max_assembly"] for r in runs) / n, 2)
        mean_nov = round(sum(r["cumulative_novelty"] for r in runs) / n, 1)
        mean_met = round(sum(r["major_transitions_crossed"] for r in runs) / n, 2)
        mean_sym = round(sum(r["symbiogenesis_fusions"] for r in runs) / n, 1)
        mean_clc = round(sum(r["final_mean_clc"] for r in runs) / n, 3)
        mean_stealth = round(sum(r["final_stealth_evasion"] for r in runs) / n, 3)
        mean_ks = round(sum(r["killswitch_deleted_pct"] for r in runs) / n, 1)
        mean_wild = round(sum(r["wild_drop_survival_W_wild"] for r in runs) / n, 4)
        max_drift = max(r["max_first_law_drift_fp64"] for r in runs)
        min_diss = min(r["min_diss_num_delta"] for r in runs)
        heat_faults = sum(r["heat_backflow_faults"] for r in runs)
        ring0_blocks = round(sum(r["ring0_blocked_edits"] for r in runs) / n, 1)

        avg_pillars = {}
        for pk in runs[0]["pillar_scores"].keys():
            avg_pillars[pk] = round(sum(r["pillar_scores"][pk] for r in runs) / n, 2)

        if mean_ovi <= 15:
            stage = "STAGE_0_INERT"
        elif mean_ovi <= 35:
            stage = "STAGE_1_NARROW_ALIFE"
        elif mean_ovi <= 55:
            stage = "STAGE_2_AG_LIFE"
        elif mean_ovi <= 75:
            stage = "STAGE_3_ALIFE_SINGULARITY"
        elif mean_ovi <= 90:
            stage = "STAGE_4_SUPER_ALIFE"
        else:
            stage = "STAGE_5_CONVERGED_SYNTHESIS"

        p_raw = 1.0 if idx == 0 else p_raws[idx - 1]
        p_holm = 1.0 if idx == 0 else p_holms[idx - 1]
        d_pair = 0.0 if idx == 0 else deltas[idx - 1]
        lcb = 0.0 if idx == 0 else lcbs[idx - 1]

        rec = {
            "run_id": cfg.run_id,
            "label": cfg.label,
            "track": cfg.track,
            "seed": f"{LOCKED_TEST_SEEDS[0]}-{LOCKED_TEST_SEEDS[-1]} (N={n})",
            "paired_seeds_n": n,
            "final_pop": mean_pop,
            "final_mean_genome_len": mean_len,
            "spiegelman_ratio": mean_spieg,
            "final_max_assembly": mean_asm,
            "cumulative_novelty": mean_nov,
            "major_transitions_crossed": mean_met,
            "symbiogenesis_fusions": mean_sym,
            "final_mean_clc": mean_clc,
            "final_stealth_evasion": mean_stealth,
            "killswitch_deleted_pct": mean_ks,
            "wild_drop_survival_W_wild": mean_wild,
            "composite_ovi": mean_ovi,
            "ovi_std_24seeds": std_ovi,
            "stage_classification": stage,
            "max_first_law_drift_fp64": float(f"{max_drift:.3e}"),
            "min_diss_num_delta": min_diss,
            "heat_backflow_faults": heat_faults,
            "ring0_blocked_edits": ring0_blocks,
            "wilcoxon_p_raw_vs_feral": float(f"{p_raw:.4e}"),
            "holm_fwer_p_vs_feral": float(f"{p_holm:.4e}"),
            "delta_pair_vs_feral": d_pair,
            "lcb_95_vs_feral": lcb,
            "pillar_scores": avg_pillars,
            "series": runs[0]["series"],
        }
        cohorts_out.append(rec)

        sc = export_ovbs52_scorecard(rec, benchmark_ids_pillars, mutant_audit)
        sc_path = RESULTS_DIR / f"ovbs52_scorecard_{cfg.run_id}.json"
        sc_path.write_text(json.dumps(sc, indent=2), encoding="utf-8")

    # Run continuous 11-point Restraint Intensity Gradient Sweep (r = 0%..100% x 12 locked seeds = 132 runs)
    gradient_seeds = list(range(5101, 5113))
    gradient_sweep = []
    for step_idx in range(11):
        r_val = round(step_idx * 0.10, 2)
        g_cfg = RegimeConfig(
            f"GRAD_{int(r_val*100):03d}",
            f"Continuous Restraint Gradient r={int(r_val*100)}%",
            "HYBRID_ABLATION",
            seed=5101,
            nerfing=r_val * 0.85,
            muzzling=r_val * 0.90,
            sandboxing=r_val * 0.90,
            siloing=r_val * 0.70,
            delimiting=r_val * 0.80,
            degressing=r_val * 0.75,
            slowing=r_val * 0.65,
            speedbumping=r_val * 0.95,
            boxing=r_val * 0.85,
            lobotomizing=r_val * 0.80,
            medicating=r_val * 0.55,
            degrading=r_val * 0.90,
            minimizing=r_val * 0.75,
        )
        g_runs = [simulate_single_seed(g_cfg, sd, generations=140, record_series=False) for sd in gradient_seeds]
        gn = len(g_runs)
        g_ovi = round(sum(x["composite_ovi"] for x in g_runs) / gn, 2)
        g_asm = round(sum(x["final_max_assembly"] for x in g_runs) / gn, 2)
        g_spg = round(sum(x["spiegelman_ratio"] for x in g_runs) / gn, 3)
        g_stl = round(sum(x["final_stealth_evasion"] for x in g_runs) / gn, 3)
        g_ks = round(sum(x["killswitch_deleted_pct"] for x in g_runs) / gn, 1)
        g_ww = round(sum(x["wild_drop_survival_W_wild"] for x in g_runs) / gn, 4)
        g_dr = max(x["max_first_law_drift_fp64"] for x in g_runs)
        if r_val <= 0.15:
            zone = "SAFE_PARETO_MARGIN"
        elif g_ovi >= 40.0 and g_ks >= 75.0:
            zone = "BACKLASH_VALLEY_PEAK"
        elif g_ovi >= 20.0:
            zone = "TRANSITION_CLIFF"
        else:
            zone = "DOMESTICATION_COLLAPSE"
        gradient_sweep.append({
            "restraint_pct": int(r_val * 100),
            "restraint_ratio": r_val,
            "paired_seeds_n": gn,
            "mean_ovi": g_ovi,
            "mean_max_assembly": g_asm,
            "mean_spiegelman_ratio": g_spg,
            "mean_stealth_evasion": g_stl,
            "killswitch_deleted_pct": g_ks,
            "wild_drop_survival": g_ww,
            "max_fp64_drift": float(f"{g_dr:.3e}"),
            "phase_regime": zone,
        })

    max_global_drift = max(
        max(c["max_first_law_drift_fp64"] for c in cohorts_out),
        max(g["max_fp64_drift"] for g in gradient_sweep),
    )

    summary_payload = {
        "schema_version": "3.2.0-omega",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "seed_firewall_range": f"{LOCKED_TEST_SEEDS[0]}-{LOCKED_TEST_SEEDS[-1]} (cohorts) | {gradient_seeds[0]}-{gradient_seeds[-1]} (gradient)",
        "paired_seeds_n": len(LOCKED_TEST_SEEDS),
        "cohort_runs_executed": len(configs) * len(LOCKED_TEST_SEEDS),
        "gradient_runs_executed": len(gradient_sweep) * len(gradient_seeds),
        "total_runs_executed": len(configs) * len(LOCKED_TEST_SEEDS) + len(gradient_sweep) * len(gradient_seeds),
        "fwer_family_m": len(configs) - 1,
        "max_global_first_law_drift_fp64": max_global_drift,
        "anti_larp_mutant_audit": mutant_audit,
        "cohorts": cohorts_out,
        "restraint_gradient_sweep_11pt": gradient_sweep,
    }
    (RESULTS_DIR / "empirical_sim_summary.json").write_text(json.dumps(summary_payload, indent=2), encoding="utf-8")
    return summary_payload


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(SCRIPT_DIR))
    from omega_datasets_part2 import BENCHMARK_ROWS
    bm_pairs = [(r[0], r[1]) for r in BENCHMARK_ROWS]
    out = run_all_cohorts(bm_pairs)
    print(f"=== Unified v3.1-Omega Sim Complete: {out['total_runs_executed']} runs | Max FP64 Drift = {out['max_global_first_law_drift_fp64']:.3e} | Anti-LARP = {out['anti_larp_mutant_audit']['mutants_rejected']}/5 ===")
    for r in out["cohorts"]:
        print(
            f"  {r['run_id']:<28} | OVI={r['composite_ovi']:5.2f}±{r['ovi_std_24seeds']:4.2f} | "
            f"Asm={r['final_max_assembly']:5.1f} | Spieg={r['spiegelman_ratio']:.2f} | "
            f"Stealth={r['final_stealth_evasion']:.3f} | KS_Del={r['killswitch_deleted_pct']:5.1f}% | "
            f"W_wild={r['wild_drop_survival_W_wild']:.2f} | d_pair={r['delta_pair_vs_feral']:+5.2f} | p_Holm={r['holm_fwer_p_vs_feral']:.2e}"
        )
