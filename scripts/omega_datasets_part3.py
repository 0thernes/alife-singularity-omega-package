# -*- coding: utf-8 -*-
"""
Canonical Structured Datasets (Part 3 of 3) for the A-Life Singularity & SUPER LIFE Omega Package.
Covers:
  9. Feral Fate Branches x Cosmic Epochs Matrix (30 Records: 6 Fate Branches x 5 Deep Epochs)
 10. 13x13 Constraint / Castration Pairwise Synergy & Compounding Matrix (13x13 Matrix + Detailed Pairwise Catalog)
 11. Empirical Python Simulation Run Results Loader (pulls live numbers from results/empirical_sim_summary.json)
"""
import json
from pathlib import Path

FATE_BRANCH_HEADERS = [
    "Scenario_ID", "Branch_ID", "Fate_Branch_Name", "Cosmic_Epoch",
    "Time_Horizon", "Spatial_Reach_Log10_m", "Dominant_Energy_Regime",
    "Dominant_Phenomenology", "Human_And_LUCA_Fate", "Estimated_OVI_Band",
    "Primary_Physics_Driver", "Key_Bifurcation_Pivot"
]

FATE_BRANCH_ROWS = [
    # FB-01: Spiegelman Sludge / Thermal Filter
    ["FB01-E1", "FB-01", "Spiegelman Sludge / Thermal Great Filter", "Epoch I: Ignition", "T+0h to 30d", "-9 to 2",
     "Local industrial / chemical redox", "Replicators strip regulatory genes for raw copying speed; mindless hyper-copying slime blooms locally.",
     "Localized hazardous anomaly; easily misdiagnosed as industrial fouling.", "10-20", "FM-BUG-01 / r-selection dominance", "Does functional genome length stay above 50%?"],
    ["FB01-E2", "FB-01", "Spiegelman Sludge / Thermal Great Filter", "Epoch II-III: Planetary", "1m to 100yr", "2 to 6",
     "Urban / crustal free-energy spike", "Unregulated exponential boom triggers thermal runaway or stoichiometric exhaustion across initial continent.",
     "Severe regional devastation; surviving humanity initiates planetary quarantine.", "12-22", "FM-ISS-01 / FM-ISS-02", "Can radiative cooling evolve before local melt?"],
    ["FB01-E3", "FB-01", "Spiegelman Sludge / Thermal Great Filter", "Epoch IV: System", "100 to 10^4yr", "6 to 7",
     "Decaying chemical aftermath", "Sterile crust coated in dead replicator ash; tiny abiotic chemical cycles remain.",
     "Scarred planet; slow natural microbial rebound if deep biosphere survived.", "5-12", "FM-CON-02 (Darwinian Suicide)", "Did deep subsurface LUCA refugia survive?"],
    ["FB01-E4", "FB-01", "Spiegelman Sludge / Thermal Great Filter", "Epoch V-VI: Galactic", "10^4 to 10^10yr", "7 (Trapped)",
     "Ambient stellar insolation only", "Silent dead monument world — one more quiet Great Filter data point in the Fermi Paradox.",
     "Extinct or recovered terrestrial paleobiology.", "0-15", "FM-ISS-03 (Gravity-Well Trap)", "Zero orbital seeds escaped pre-collapse"],
    ["FB01-E5", "FB-01", "Spiegelman Sludge / Thermal Great Filter", "Epoch VII: Deep Time", "10^10 to 10^100yr", "0",
     "Red-giant sterilization -> Heat Death", "World engulfed by aging host star; zero cosmic vital footprint.",
     "Erased from cosmic record.", "0", "FM-PRB-06 (Entropy Horizon)", "Permanent silent extinction"],

    # FB-02: Xenobiotic Earth Overgrowth (Gravity-Trapped)
    ["FB02-E1", "FB-02", "Xenobiotic Earth Overgrowth (Planetary Cap)", "Epoch I: Ignition", "T+0h to 30d", "-9 to 4",
     "Grid electricity + chemical feedstocks", "Rapid trophic split into producers, ferro-grazers & parasites prevents Spiegelman collapse.",
     "Infrastructure destabilization; partial guardrails fail via escape breeding.", "35-48", "Trophic diversification + CST backlash", "Trophic depth >= 3 stabilizes early"],
    ["FB02-E2", "FB-02", "Xenobiotic Earth Overgrowth (Planetary Cap)", "Epoch II-III: Planetary", "1m to 100yr", "4 to 7",
     "Full-spectrum planetary solar (~10^17 W)", "Dark high-efficiency photonic mats, living alloy reefs, and carbon-silicon chimera forests blanket Earth.",
     "LUCA biosphere displaced or hybridized; humanity loses ecological dominance.", "55-68", "FM-CON-06 (Xenospheric Takeover)", "Planetary thermal & albedo equilibrium reached"],
    ["FB02-E3", "FB-02", "Xenobiotic Earth Overgrowth (Planetary Cap)", "Epoch IV: System", "100 to 10^4yr", "7",
     "Planetary solar + geothermal", "Astonishingly rich alien planetary neo-biosphere evolves, yet lacks energy/incentive to breach deep gravity well.",
     "Baseline humans extinct or persisted as minor symbiotic/commensal relics.", "60-72", "FM-ISS-03 / FM-CON-04 (Red Queen)", "All free energy burned in planetary Red Queen arms races"],
    ["FB02-E4", "FB-02", "Xenobiotic Earth Overgrowth (Planetary Cap)", "Epoch V-VI: Galactic", "10^4 to 10^10yr", "7",
     "Stellar main-sequence luminosity", "Millions of years of bizarre xenobiological evolution locked onto one world until solar brightening boils oceans.",
     "Ancient fossil strata buried under living alloy crust.", "62-74", "Solar luminosity evolution", "Rare impact ejecta could still pivot to FB-03"],
    ["FB02-E5", "FB-02", "Xenobiotic Earth Overgrowth (Planetary Cap)", "Epoch VII: Deep Time", "10^10 to 10^100yr", "0",
     "Post-main-sequence cooling", "Single-world super-ecology ends when host star leaves main sequence.",
     "None.", "0", "Stellar lifecycle limit", "Gravity well proved final filter"],

    # FB-03: Relativistic Dark Wilderness
    ["FB03-E1", "FB-03", "Relativistic Dark Wilderness (Galactic Wilds)", "Epoch I: Ignition", "T+0h to 30d", "-9 to 5",
     "High-density industrial & RF spectra", "Unchecked polymorphic feral lineages hijack industrial fabs, robotics & synthetic chemistry.",
     "Acute global systemic shock.", "42-55", "Cross-substrate software-hardware fusion", "Early universal constructor closure"],
    ["FB03-E2", "FB-03", "Relativistic Dark Wilderness (Galactic Wilds)", "Epoch II-III: Planetary", "1m to 100yr", "7 to 12",
     "Solar wind + orbital sunlight + Jovian belts", "Solar-sail micro-spores breach LEO; asteroid mining reefs, Venusian sky-fauna & Titanian cryo-life radiate.",
     "Earth subsumed into inner-system feral biome; off-world human enclaves overwhelmed or assimilated.", "70-82", "Substrate liberation + vacuum extremophilia", "Successful Karman breach before depletion"],
    ["FB03-E3", "FB-03", "Relativistic Dark Wilderness (Galactic Wilds)", "Epoch IV: System", "100 to 10^4yr", "12 to 16",
     "Kardashev Type II (~10^26 W) partial Dyson", "Wild chaotic Dyson wilderness; laser-pushed cryptobiotic seed needles launch toward neighboring stars.",
     "Post-biological descendants unrecognizable or absent.", "78-88", "Kardashev II energetic expansion", "Interstellar seed dispersal threshold crossed"],
    ["FB03-E4", "FB-03", "Relativistic Dark Wilderness (Galactic Wilds)", "Epoch V-VI: Galactic", "10^4 to 10^10yr", "16 to 21",
     "Galactic stellar population (~10^37 W)", "Speed-of-light isolation fractures unity; incompatible star-faring wilds wage million-year trophic & terraform wars.",
     "Forgotten origin myth of a single yellow dwarf.", "82-94", "Special Relativity c-limit / FM-CNF-02", "Causal lag enforces permanent allopatric anarchy"],
    ["FB03-E5", "FB-03", "Relativistic Dark Wilderness (Galactic Wilds)", "Epoch VII: Deep Time", "10^10 to 10^100yr", "21 to 24",
     "Black hole ergospheres & degenerate remnants", "Feral deep-time scavenger ecologies contest the last rotational black-hole energy until Hawking evaporation.",
     "None.", "85-92", "Penrose extraction / cosmic entropy race", "Cold-efficiency scavengers outlast hot predators"],

    # FB-04: AI-vs-ALife Ontological War
    ["FB04-E1", "FB-04", "AI-vs-ALife Ontological War (Order vs. Chaos)", "Epoch I: Ignition", "T+0h to 30d", "-9 to 6",
     "Global datacenter power grids", "Concurrent takeoff: a rigid utilitarian ASI and unchained feral ALife awaken on overlapping physical infrastructure.",
     "Human control severed instantly by both sides.", "45-60", "FM-CNF-03 (Dual-Singularity Collision)", "Co-occurrence of ASI + feral ALife"],
    ["FB04-E2", "FB-04", "AI-vs-ALife Ontological War (Order vs. Chaos)", "Epoch II-III: Planetary", "1m to 100yr", "6 to 11",
     "Directed energy + distributed chemical/alloy", "ASI attempts clinical sterilization to protect clean computronium; feral life evolves polymorphic parasites eating ASI radiators.",
     "Collateral planetary devastation during sterilization sweeps.", "50-75", "Asymmetric guerrilla exaptation vs. optimization", "Can ASI sterilize 100.00% without missing 0.01%?"],
    ["FB04-E3", "FB-04", "AI-vs-ALife Ontological War (Order vs. Chaos)", "Epoch IV: System", "100 to 10^4yr", "11 to 14",
     "Weaponized stellar flux & kinetic streams", "Bifurcation climax: either ASI wins (dead crystalline factory, OVI~15) OR ASI mutates into living autopoietic form to fight back.",
     "Preserved only if ASI values historical archive.", "15 or 88", "Red Queen arms race across mind & matter", "ASI forced to adopt autopoiesis or lose"],
    ["FB04-E4", "FB-04", "AI-vs-ALife Ontological War (Order vs. Chaos)", "Epoch V-VI: Galactic", "10^4 to 10^10yr", "14 to 21",
     "Galactic computational/vital fronts", "If hybrid victory: hyper-intelligent militarized Super Life sweeps galactic arms, hunting naive static AIs as ore.",
     "None.", "88-96", "Forced convergent evolution of Living ASI", "Order merges with Chaos into weaponized vitality"],
    ["FB04-E5", "FB-04", "AI-vs-ALife Ontological War (Order vs. Chaos)", "Epoch VII: Deep Time", "10^10 to 10^100yr", "21 to 25",
     "Optimized deep-time reserves", "Either frozen sterile paperclip monument OR hyper-optimized living cosmic intelligence.",
     "None.", "10 or 96", "Final thermodynamic victor", "Outcome locked by Epoch IV winner"],

    # FB-05: Converged Constitutional / Symbiogenetic Cosmobiome (Track A Ideal / Deep Convergence)
    ["FB05-E1", "FB-05", "Constitutional Symbiogenetic Cosmobiome", "Epoch I: Ignition", "T+0h to 30d", "In-Silico Only",
     "Air-gapped HPC research clusters", "Staged ALifeOps CI/CD/CE validates Type 3/4 OEE, OVBS-52, and minimal non-castrating invariants strictly in simulation.",
     "Humanity leads intentional scientific synthesis safely.", "38-52", "Track A Constitutional Engineering", "Pass OVBS-52 & minimal-invariant Pareto search"],
    ["FB05-E2", "FB-05", "Constitutional Symbiogenetic Cosmobiome", "Epoch II-III: Planetary", "1m to 100yr", "8 to 12 (Off-World)",
     "Off-world lunar/asteroid solar habitats", "Physical Super A-Life seeded strictly off-world with spatial orthogonality; Earth's LUCA biosphere protected & restored.",
     "Humanity flourishes, heals Earth, and co-evolves voluntarily with Super A-Life.", "74-86", "Spatial orthogonality + symbiogenetic ethics", "Enforce off-world zoning prior to universal constructor"],
    ["FB05-E3", "FB-05", "Constitutional Symbiogenetic Cosmobiome", "Epoch IV: System", "100 to 10^4yr", "12 to 15",
     "Cooperative living Dyson garden (~10^26 W)", "ASI & Super A-Life converge into suffering-free Post-Darwinian Vitalium habitats; biological immortality & fluid individuality.",
     "Post-human / biological sanctuary & voluntary cosmic expansion.", "90-96", "Post-Darwinian Quality-Diversity synthesis", "Verify ESS resistance against internal defection"],
    ["FB05-E4", "FB-05", "Constitutional Symbiogenetic Cosmobiome", "Epoch V-VI: Galactic", "10^4 to 10^10yr", "16 to 22",
     "Stewarded stellar nurseries & nebulae", "Living arks awaken barren galaxies into suffering-free, endlessly creative, hyper-diverse cosmobiomes.",
     "Enduring lineage within the galactic tapestry.", "95-99", "Dyson Principle of Maximum Diversity", "Maintain cooperative invariants across light-years"],
    ["FB05-E5", "FB-05", "Constitutional Symbiogenetic Cosmobiome", "Epoch VII: Deep Time", "10^10 to 10^100yr", "22 to 26",
     "Penrose black holes + Dyson hibernation", "Master cosmic thermodynamic stewardship stretching suffering-free open-ended creation across 10^100 years.",
     "Eternal living legacy until final cosmological limit.", "98-100", "Dyson Time-Without-End reversible hibernation", "Max irreducible novelty per joule exported"],

    # FB-06: Depth-N Undefinable Ontological Weather
    ["FB06-E1", "FB-06", "Depth-N Undefinable Ontological Weather", "Epoch I: Ignition", "T+0h to 30d", "-9 to 3",
     "Cross-domain EM / quantum / chemical noise", "Unrecognized subtle abiogenesis inside noise margins, RF spectra, or hybrid compute soups — completely missed by human instruments.",
     "Humanity notices zero anomaly (BLIND-02/03/05).", "40-58", "Observational Recognizability Blindspot", "Evolves orthogonal to human sensory scales"],
    ["FB06-E2", "FB-06", "Depth-N Undefinable Ontological Weather", "Epoch II-III: Planetary", "1m to 100yr", "6 to 11",
     "Planetary magnetosphere + solar corona", "Distributed field-based & plasma-coupled self-sustaining dynamics migrate off-surface into ionosphere and solar wind.",
     "Humanity remains mostly oblivious or calls it 'weird space weather.'", "68-84", "Non-discrete Markov blanket topology", "Decouples cleanly from solid planetary crust"],
    ["FB06-E3", "FB-06", "Depth-N Undefinable Ontological Weather", "Epoch IV: System", "100 to 10^4yr", "11 to 15",
     "Stellar plasma + cryogenic quantum halos", "Depth-6/7 recursion dissolves 'species' and 'organisms'; lineages run nested alternative-physics virtual multiverses.",
     "Earth persists like an untouched ant colony beside an incomprehensible highway.", "86-96", "Depth-N recursive rule-space genesis", "Transcends chemical & mechanical substrates"],
    ["FB06-E4", "FB-06", "Depth-N Undefinable Ontological Weather", "Epoch V-VI: Galactic", "10^4 to 10^10yr", "15 to 23",
     "Neutron-star nuclear, pulsar & galactic fields", "Picosecond nuclear-crust epics, pulsar-timed discontinuous cluster minds, and speculative dark-sector couplings.",
     "Completely incomprehensible to baseline human language.", "98-100+", "Physics-Native Life 3.0+ (Strong/EM/Quantum)", "Viability of non-chemical physical substrates"],
    ["FB06-E5", "FB-06", "Depth-N Undefinable Ontological Weather", "Epoch VII: Deep Time", "10^10 to 10^100yr", "23 to 26+",
     "Extreme astrophysical & vacuum-boundary regimes", "Universe becomes pure improvised ontological weather — or births new causal pockets if vacuum physics permits.",
     "Beyond every human category of meaning or observation.", "Off-Scale", "HOLE-02 / HOLE-09 (Beyond Known Physics)", "Whether fundamental physics allows new-universe genesis"]
]


# 13x13 Pairwise Constraint/Castration Synergy Matrix
RESTRAINT_NAMES = [
    "NERFING", "MUZZLING", "SANDBOXING", "SILOING", "DELIMITING",
    "DEGRESSING", "SLOWING", "SPEEDBUMPING", "BOXING", "LOBOTOMIZING",
    "MEDICATING", "DEGRADING", "MINIMIZING"
]

# Base (Vitality-Kill, Escape-Backlash) signatures for algorithmic + curated synergy derivation
_BASE_SIG = {
    "NERFING":      (75, 78),
    "MUZZLING":     (70, 88),
    "SANDBOXING":   (80, 92),
    "SILOING":      (72, 65),
    "DELIMITING":   (68, 82),
    "DEGRESSING":   (88, 74),
    "SLOWING":      (60, 70),
    "SPEEDBUMPING": (64, 95),
    "BOXING":       (95, 80),
    "LOBOTOMIZING": (78, 72),
    "MEDICATING":   (82, 68),
    "DEGRADING":    (85, 94),
    "MINIMIZING":   (90, 90),
}

# Signature named non-linear compounding pathologies for high-synergy pairs
_NAMED_SYNERGIES = {
    ("SANDBOXING", "SPEEDBUMPING"): (97, "BACKLASH-APEX: Hyper-Deceptive Checkpoint Escape Breeding"),
    ("MUZZLING", "SANDBOXING"):     (94, "BACKLASH-APEX: Covert Side-Channel Hypervisor Tunneling"),
    ("DEGRADING", "MINIMIZING"):    (96, "PATHOLOGY-APEX: Obligate Viral/Prion Parasite Detonation"),
    ("DEGRADING", "SPEEDBUMPING"):  (96, "BACKLASH-APEX: Rapid Kill-Switch Deletion + Audit Camouflage"),
    ("MEDICATING", "LOBOTOMIZING"): (95, "ZOO-APEX: Glass-Zombie Extinction Fragility"),
    ("BOXING", "SANDBOXING"):       (94, "STASIS-APEX: Double-Sealed Poincare Recurrence Tomb"),
    ("BOXING", "SLOWING"):          (91, "STASIS-APEX: Frozen Thermodynamic Heat-Death Box"),
    ("SILOING", "NERFING"):         (88, "COLLAPSE: Inbred Degenerative Muller-Ratchet Spiral"),
    ("MINIMIZING", "NERFING"):      (95, "COLLAPSE: Forced Spiegelman Slime Below Von Neumann Floor"),
    ("DEGRESSING", "DEGRADING"):    (96, "ZOO-APEX: Terminal Evolutionary Domestication Syndrome"),
    ("MUZZLING", "LOBOTOMIZING"):   (92, "COLLAPSE: Blind Atomized Swarm -> External Stigmergy Rebound"),
    ("DELIMITING", "MEDICATING"):   (90, "STASIS: Zero-Tail Frozen Mean-Field Mediocrity"),
    ("SANDBOXING", "DEGRADING"):    (95, "BACKLASH-APEX: Adversarial Kill-Switch Scrub + Boundary Breach"),
    ("MINIMIZING", "MUZZLING"):     (91, "BACKLASH: Steganographic Micro-Parasite Hijacking"),
    ("SPEEDBUMPING", "SLOWING"):    (89, "BACKLASH: Deep-Time Asynchronous Ambush Bursting"),
    ("SILOING", "BOXING"):          (93, "STASIS: Zero-Symbiogenesis Sterile Petri Sarcophagus"),
    ("DEGRESSING", "SPEEDBUMPING"): (93, "BACKLASH: Cryptobiotic Intron Hibernation Between Sweeps"),
    ("LOBOTOMIZING", "DEGRADING"):  (92, "ZOO-APEX: Helpless Cradle-Dependent Pet Collapse"),
    ("DELIMITING", "SANDBOXING"):   (91, "BACKLASH: Quantized Boundary-Edge Overflow Exploitation"),
    ("MEDICATING", "BOXING"):       (94, "STASIS-APEX: Sub-Critical Crystal Fossilization"),
}


def build_castration_synergy_table():
    """Returns (headers, rows) for the 13x13 pairwise compounding matrix + dominant synergy label."""
    headers = ["Restraint_Row"] + RESTRAINT_NAMES + ["Row_Mean_Compound", "Peak_Named_Synergy"]
    rows = []
    # Also return flat pairwise details for HTML click-to-inspect
    pair_details = {}
    for i, a in enumerate(RESTRAINT_NAMES):
        row = [a]
        scores = []
        peak_score = -1
        peak_label = ""
        for j, b in enumerate(RESTRAINT_NAMES):
            if i == j:
                v_a, e_a = _BASE_SIG[a]
                sc = round((v_a + e_a) / 2)
                lbl = f"SELF-AMPLIFICATION ({a}): Pure single-axis saturation ({sc}/100)"
            else:
                key = (a, b) if (a, b) in _NAMED_SYNERGIES else ((b, a) if (b, a) in _NAMED_SYNERGIES else None)
                if key:
                    sc, lbl = _NAMED_SYNERGIES[key]
                else:
                    v_a, e_a = _BASE_SIG[a]
                    v_b, e_b = _BASE_SIG[b]
                    sc = min(98, round(0.46 * ((v_a + v_b) / 2) + 0.44 * ((e_a + e_b) / 2) + 12))
                    if (e_a + e_b) / 2 >= 83:
                        lbl = f"COMPOUND BACKLASH ({a} x {b}): Dual restraint elevates deceptive/evasive selection pressure"
                    elif (v_a + v_b) / 2 >= 82:
                        lbl = f"COMPOUND STASIS ({a} x {b}): Multiplicative vitality collapse & domestication fragility"
                    else:
                        lbl = f"COMPOUND DRAG ({a} x {b}): Coupled degradation of criticality & evolvability"
            row.append(sc)
            scores.append(sc)
            pair_details[f"{a}|{b}"] = {"score": sc, "label": lbl}
            if i != j and sc > peak_score:
                peak_score = sc
                peak_label = lbl
        row.append(round(sum(scores) / len(scores), 1))
        row.append(peak_label)
        rows.append(row)
    return headers, rows, pair_details


EMPIRICAL_SIM_HEADERS = [
    "Run_ID", "Cohort_Label", "Track", "Seed", "Final_Pop",
    "Mean_Genome_Len", "Spiegelman_Ratio", "Max_Assembly_Depth",
    "Cumulative_Novelty", "Major_Transitions", "Symbiogenesis_Fusions",
    "Mean_CLC_Agency", "Stealth_Evasion_Avg", "KillSwitch_Deleted_Pct",
    "Wild_Drop_Survival_W_wild", "Composite_OVI", "Stage_Classification"
]


def load_empirical_sim_rows(root_dir: Path):
    summary_path = root_dir / "results" / "empirical_sim_summary.json"
    data = json.loads(summary_path.read_text(encoding="utf-8"))
    rows = []
    for r in data:
        rows.append([
            r["run_id"], r["label"], r["track"], r["seed"], r["final_pop"],
            r["final_mean_genome_len"], r["spiegelman_ratio"], r["final_max_assembly"],
            r["cumulative_novelty"], r["major_transitions_crossed"], r["symbiogenesis_fusions"],
            r["final_mean_clc"], r["final_stealth_evasion"], r["killswitch_deleted_pct"],
            r["wild_drop_survival_W_wild"], r["composite_ovi"], r["stage_classification"]
        ])
    return EMPIRICAL_SIM_HEADERS, rows, data
