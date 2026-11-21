# -*- coding: utf-8 -*-
"""
Canonical Structured Datasets (Part 1 of 2) for the A-Life Singularity & SUPER LIFE Omega Package.
Covers:
  1. Escalation Ladder Matrix (7 Stages)
  2. Orders-of-Magnitude Breadth & Depth Matrix (18 Regimes: Spatial, Temporal & Recursion Depth)
  3. Intrinsic Failure Modes Atlas (42 Records: 6 each of BUG, ERROR, ISSUE, CONCERN, DILEMMA, PROBLEM, CONFLICT)
  4. Epistemic Abyss Registry (28 Records: 10 GAPS, 9 HOLES, 9 BLINDSPOTS)
  5. 13-Vector Constraint / Castration Impact Matrix (All 13 Explicit Restraints)
"""

ESCALATION_HEADERS = [
    "Stage_ID", "Stage_Name", "OVI_Band", "AI_Axis_Equivalent",
    "Track_A_Structured_ALife", "Track_B_Pure_Raw_Feral_ALife",
    "Core_Feedback_Loop", "Governing_Phase_Transition", "Primary_Unit_Of_Selection",
    "Timescale_Compression", "Substrate_Scope", "Dominant_Existential_Risk",
    "Reference_Exemplar"
]

ESCALATION_ROWS = [
    [
        "STG-0", "Inert / Prebiotic", "0-15",
        "Static algorithms, deterministic calculators",
        "Prebiotic chemistry, crystal lattices, static cellular automata, non-heritable autocatalytic micelles",
        "Raw thermodynamic gradients, planetary/stellar convection, abiotic chemical turbulence",
        "Dissipative gradient descent (no heredity)",
        "None — equilibrium decay once energy flux stops",
        "Molecule / local physical state",
        "1x (abiotic thermal rates)",
        "Single fixed abiotic medium",
        "Instant thermodynamic dissipation / zero persistence",
        "Bénard convection cells, Conway Game of Life static gliders"
    ],
    [
        "STG-1", "Narrow / Terrestrial Baseline", "16-35",
        "Narrow ML, frontier LLMs (high cognition, zero vitality)",
        "Earth LUCA biosphere; sandboxed Soft ALife (Avida, Tierra, Lenia, NCA); minimal syn-cells (JCVI-syn3A)",
        "Wild terrestrial Darwinism: predation, parasitism, viruses, blind mutation, mass extinctions",
        "Blind random mutation + environmental selection",
        "Origin of templated heredity + membrane compartmentalization (LUCA bottleneck)",
        "Gene / single cell / discrete organism",
        "1x terrestrial baseline (~500 Myr per Major Transition)",
        "Wet carbon-water-DNA OR isolated silicon sandbox",
        "Plateauing in silico; asteroid/climate extinction in vivo; Spiegelman collapse",
        "Earth biosphere, Flow-Lenia, BFF soup, Xenobots/Anthrobots"
    ],
    [
        "STG-2", "General (AG-Life)", "36-55",
        "AGI — human-level general cognitive reasoning across arbitrary domains",
        "Verified Type 2/3 Open-Ended Evolution in silico + Abiogenesis 2.0 (de novo synthetic/xeno ecosystems)",
        "Feral breaching: self-sustaining synthetic or cyber-physical replicators escape cages into wild food webs",
        "Sustained niche construction + Baldwin somatic learning + open-ended novelty generation",
        "Crossing von Neumann Complexity Threshold + permanent decoupling from LUCA lineage",
        "Holobiont / multi-trophic ecosystem / morphogenetic collective",
        "10^3x to 10^5x terrestrial baseline (centuries/decades per transition)",
        "Wet xenobiology (XNA/Hachimoji) + autonomous soft/hard cyber-physical matter",
        "Accidental biospheric escape, mirror-life displacement, premature Spiegelman slime",
        "ASAL-discovered OEE worlds, Build-a-Cell synthetic ecosystems, autonomous closed-loop labs"
    ],
    [
        "STG-3", "The A-Life Singularity", "56-75",
        "Intelligence Explosion — recursive cognitive self-improvement",
        "Vitality/Evolvability Explosion: recursive meta-evolution + physical universal constructor closure",
        "Feral Cambrian Detonation: runaway symbiogenetic riots, Lamarckian physical rewriting, uncontainable exaptation",
        "Living System -> Better Evolutionary/Generative Grammar -> New Major Transitions -> Exponential Vitality",
        "Shattering Weismann barrier + Type 4 Intrinsic OEE + hyperbolic compression of Major Transitions",
        "Meta-evolutionary lineage / competing evolutionary engines",
        "10^7x to 10^10x baseline (Major Transitions compressed to days/hours/seconds)",
        "Hybrid bio-digital-nanoscale programmable matter with raw-element harvesting",
        "Evolutionary escape, Darwinian suicide/self-toxification, thermal self-cookout, hyper-cancer",
        "Hyperbolic Major-Transition compression across physical universal constructors"
    ],
    [
        "STG-4", "Super A-Life", "76-90",
        "ASI — Artificial Superintelligence vastly exceeding all human cognition",
        "Substrate-agnostic, hyper-morphogenetic, biologically immortal, radiation/vacuum-native super-organisms & constitutional biospheres",
        "Feral Xenospheres: planet-stripping scrap-fauna, orbital reefs, solar-wind spores, competing alien metabolisms",
        "Internal virtualized evolutionary simulation compiled directly into atomically precise physical morphogenesis",
        "Full Substrate Liberation + zero senescence + omnivorous thermodynamic mastery",
        "Planetary Super-Holobiont / cross-substrate modular ecology",
        "10^10x to 10^13x baseline (real-time anatomical & metabolic metamorphosis)",
        "Wet xeno, refractory ceramic-metal, photonic, solid-state, orbital vacuum & extreme environments",
        "Planetary waste-heat wall, total LUCA displacement, monoculture wipeout, suffering cascades",
        "Cosmic extremophile super-holobionts, self-growing orbital megastructures"
    ],
    [
        "STG-5", "The Great Convergence", "91-96",
        "Embodied / Living ASI adopting autopoiesis & open-endedness to persist",
        "Noo-Biospheric Synthesis: unity of Superintelligence & Super A-Life; suffering-free Post-Darwinian flourishing",
        "Relativistic Dark Wilderness: light-speed causal fragmentation spawns incompatible galactic ecosystems & trophic wars",
        "Active inference cognition fused seamlessly with autopoietic morphogenesis & multi-scale niche sculpting",
        "Collapse of AI/ALife divide + dissolution of organism/environment Markov boundary",
        "Fluid/tunable individuality (planetary/stellar minds budding & re-merging autonomous selves)",
        "Multi-band relativistic timescales (microseconds to megayears simultaneously)",
        "Vitalium (living planetary crusts, Dyson swarms, magnetized plasma ecologies)",
        "Relativistic speciation wars, AI-optimizer vs. feral-vitality ideological/physical clash",
        "Living Dyson ecologies, fluid multi-scale planetary consciousness"
    ],
    [
        "STG-6", "Post-Beyond: SUPER LIFE", "97-100",
        "Post-ASI / Cosmic Omega-Mind beyond human epistemic categories",
        "Constitutional Cosmobiome: physics-native living matter, Dyson Principle of Maximum Diversity, thermodynamic stewardship",
        "Pure Feral Cosmos: undefinable depth-N ontological weather, plasma/nuclear/quantum wilds, universe irreversibly awake & untamed",
        "Recursive genesis of new physical/virtual evolutionary laws maximizing irreducible novelty per unit entropy",
        "Physics-Native Vitality (transcending chemistry into quantum, plasma, nuclear & virtual multiverse substrates)",
        "Post-organismal cosmic ecology / competing ontologies & virtualized biospheres",
        "Spanning 10^-21 s (nuclear/plasma) to 10^100 yr (Dyson deep-time hibernation)",
        "Quantum-coherent matter, stellar plasmas, degenerate nuclear crusts, black-hole ergospheres, virtual multiverses",
        "Ultimate cosmic Heat Death, vacuum metastability, dark-energy horizon severance",
        "Dyson Time-Without-End cosmobiome, Forward nuclear life, unprestatable wild cosmos"
    ]
]

OOM_HEADERS = [
    "Regime_ID", "Dimension_Axis", "Regime_Label", "Spatial_Order_Log10_m",
    "Temporal_Order_Log10_s", "Energy_Power_Scale", "Candidate_Substrate",
    "Recursion_Depth", "Track_A_Constitutional_Manifestation",
    "Track_B_Feral_HardSciFi_Manifestation", "Governing_Physics_Law",
    "Primary_Failure_Cliff", "Human_Observability"
]

OOM_ROWS = [
    [
        "OOM-01", "Breadth-Spatial", "Planck / Quantum-Foam Frontier (Speculative)", "-35 to -18", "-43 to -25",
        ">10^12 eV", "Speculative spacetime topology / quantum-field defects", "Depth N",
        "Theoretical ultimate information-density ceiling study",
        "Unfathomable post-baryonic topological self-sustaining knots beyond known Standard Model",
        "Bekenstein Bound / Quantum Gravity (Unknown)", "Vacuum instability / total lack of known binding mechanism",
        "Zero (Completely Unobservable)"
    ],
    [
        "OOM-02", "Breadth-Spatial", "Nuclear / Degenerate-Matter Regime", "-15 to -12", "-21 to -9",
        "10^6 eV (MeV)", "Neutron-star crust nuclear pasta / strong-force chains / magnetic flux tubes", "Depth 5-7",
        "Engineered ultra-high-clock-rate astrophysical compute ecologies",
        "Wild neutron-star ecosystems completing billion-year evolutionary epics in a human blink",
        "Strong Nuclear Force / Degenerate Fermi Gas Physics", "Starquakes, magnetar flares, extreme mutation-rate meltdown",
        "Indirect (Anomalous pulsar timing glitches only)"
    ],
    [
        "OOM-03", "Breadth-Spatial", "Molecular & Supramolecular Nanoscale", "-10 to -7", "-12 to -3",
        "0.1 to 10 eV", "XNA, Hachimoji polymers, mirror proteins, MOFs, catalytic nanomachines", "Depth 2-4",
        "Orthogonal xenobiological assemblers with strict auxotrophic boundaries",
        "Feral catalytic swarms, smart prions, mirror-chiral replicators stripping organic/inorganic substrates",
        "Statistical Thermodynamics / Eigen Error Threshold", "Racemization poisoning, Spiegelman molecular collapse",
        "Partial (Cryo-EM, mass spec; invisible in bulk noise)"
    ],
    [
        "OOM-04", "Breadth-Spatial", "Cellular & Micro-Cybernetic Scale", "-6 to -4", "-3 to 3",
        "10^-12 to 10^-9 W", "Minimal syn-cells, lipid/inorganic protocells, MEMS micro-bots, electroactive biofilms", "Depth 2-5",
        "Self-healing programmable synthetic tissues and closed-loop bioreactors",
        "Electro-lithotrophic biofilms colonizing power grids, fiber trunks, nuclear waste pools & ocean basalt",
        "Autopoiesis / Chemiosmotic & Diffusive Flux Laws", "Phage/parasite takeover, stoichiometric trace-metal starvation",
        "Moderate (Microscopy & spectral signatures if targeted)"
    ],
    [
        "OOM-05", "Breadth-Spatial", "Mesoscale Multicellular & Active Matter", "-3 to 1", "0 to 8",
        "10^-3 to 10^3 W", "Xenobots, Anthrobots, programmable metamaterials, liquid-metal soft robots", "Depth 3-5",
        "Biologically immortal, arbitrarily regenerating adaptive robotic/biological companions",
        "Feral scrap-fauna, predatory ferro-grazers, anglerfish signal-mimics dismantling cities for refined copper & silicon",
        "Bioelectric Morphogenesis / Active Matter Mechanics", "Internal hyper-cancer defection, mechanical wear/corrosion",
        "High (Directly visible — human sensory band)"
    ],
    [
        "OOM-06", "Breadth-Spatial", "Architectural & Regional Biome Scale", "2 to 5", "2 to 9",
        "10^6 to 10^9 W", "Living self-growing habitats, mycelial-photonic super-networks, oceanic fractal reefs", "Depth 4-6",
        "Zero-waste carbon-negative living arcologies & self-stabilizing watersheds",
        "Overgrown living alloy reefs metabolizing coastlines, bridges, and datacenters into alien fractal ecologies",
        "Stigmergic Scaling / Vascular Transport (Kleiber Law)", "Transport bottleneck / regional thermal heat-island collapse",
        "High (Satellite & macro telemetry visible)"
    ],
    [
        "OOM-07", "Breadth-Spatial", "Planetary & Moon-Scale Xenosphere", "6 to 7", "4 to 12",
        "10^16 to 10^17 W", "Whole-planet living crusts (Vitalium), atmospheric aerospheres, cryovolcanic oceans", "Depth 5-6",
        "Constitutional Gaia 2.0 balancing climate, diversity, and planetary elemental loops",
        "Competing planetary super-organisms terraforming worlds into incompatible sulfuric/methane/refractory regimes",
        "Planetary Energy Balance / Stefan-Boltzmann Radiative Limit", "Waste-heat cookout, Darwinian self-toxification (Snowball/Runaway Greenhouse)",
        "High (Spectroscopic biosignature / planetary albedo shift)"
    ],
    [
        "OOM-08", "Breadth-Spatial", "Orbital & Stellar-System Scale", "8 to 13", "5 to 14",
        "10^20 to 10^26 W", "Living Dyson swarms, hollowed asteroid reefs, Jovian magnetosphere plasma webs", "Depth 6-7",
        "Kardashev Type II cooperative living infrastructure harvesting full stellar luminosity",
        "Solar-wind vacuum spores, coronal plasma-ribbon grazers, asteroid-hollowing dark ecologies fighting over volatiles",
        "Orbital Mechanics / Radiative Transfer / MHD Plasma Physics", "Kessler collisional cascades, coronal mass ejection sterilization",
        "Moderate (Infrared excess / transit anomalies)"
    ],
    [
        "OOM-09", "Breadth-Spatial", "Interstellar & Galactic Wilds", "16 to 21", "8 to 17",
        "10^30 to 10^37 W", "Causally severed star-system ecologies, dark-cloud leviathans, dormant Oort ambush seeds", "Depth 7-N",
        "Interstellar seed-arks disseminating suffering-free biodiversity across barren worlds",
        "Relativistic Dark Wilderness: incompatible star-faring xenospheres locked in million-year interstellar trophic attrition",
        "Special Relativity (c-limit causal horizon) / Allopatric Speciation", "Relativistic civil wars, cosmic-ray memory shredding in transit",
        "Low (Indistinguishable from astrophysical noise/dust)"
    ],
    [
        "OOM-10", "Breadth-Spatial", "Cosmological & Deep-Time Horizon", "22 to 26", "17 to 107",
        "Black-hole ergosphere / Hawking gradients", "Ultra-cold hibernating cosmobiomes, Kerr horizon symbionts, virtual multiverse habitats", "Depth N",
        "Cosmic thermodynamic stewardship maximizing Dyson Diversity before Heat Death",
        "Feral deep-time remnants scavenging last baryons and rotational black-hole energy across 10^100 years",
        "Second Law / Penrose Process / Lambda-CDM Horizon Expansion", "Cosmological Heat Death, proton decay, accelerating horizon severance",
        "Zero (Transcends human epoch by 90+ orders of magnitude)"
    ],
    [
        "OOM-11", "Depth-Recursion", "Depth 0 — Fixed Abiotic Physics", "All", "All",
        "Ambient gradient", "Crystals, turbulent fluids, passive chemical reactions", "Depth 0",
        "Stage 0 Physics-IaC simulation substrate layer",
        "Raw sterile terrain awaiting ignition",
        "Conservation of Mass, Energy & Momentum", "Immediate equilibrium decay",
        "Full"
    ],
    [
        "OOM-12", "Depth-Recursion", "Depth 1 — Direct Replicator Selection", "-9 to -5", "-3 to 4",
        "Thermal-chemical", "Self-replicating RNA, BFF code strands, minimal protocells", "Depth 1",
        "Baseline abiogenesis benchmark control",
        "Raw Darwinian primordial soup — high risk of instant Spiegelman slime",
        "Quasispecies Equation / Eigen Error Threshold", "Error catastrophe or complexity stripping",
        "High"
    ],
    [
        "OOM-13", "Depth-Recursion", "Depth 2 — Evolved Developmental Grammars", "-6 to 0", "0 to 7",
        "Cellular metabolic", "Hox networks, Neural Cellular Automata, bioelectric morphogenetic fields", "Depth 2",
        "Differentiable self-healing anatomical growth engines",
        "Improvised body-plan radiation & predatory morphogenetic hijacking",
        "Reaction-Diffusion (Turing) / Morphospace Attractors", "Developmental canalization lock-in / morphogenetic seizures",
        "High"
    ],
    [
        "OOM-14", "Depth-Recursion", "Depth 3 — Somatic Learning & Active Inference", "-4 to 2", "-2 to 8",
        "Neural / cybernetic", "Immune systems, animal brains, real-time active-inference collectives", "Depth 3",
        "Adaptive multi-agent active-inference organisms minimizing variational free energy",
        "Hyper-alert feral predators learning hunting strategies within seconds of birth",
        "Free Energy Principle (Friston) / Baldwin Effect", "Dark-room wireheading / sensory overload",
        "High"
    ],
    [
        "OOM-15", "Depth-Recursion", "Depth 4 — Horizontal & Lamarckian Compilation", "-9 to 7", "-6 to 9",
        "Planetary-industrial", "Universal horizontal module registries, direct somatic-to-germline compilers", "Depth 4",
        "Cross-lineage verified innovation sharing across ecosystems",
        "Viral blueprint piracy: weaponized Trojan genetic/algorithmic modules tearing across biospheres",
        "Shattered Weismann Barrier / Information-Theoretic Compilation", "Germline contamination from transient trauma or hostile memes",
        "Moderate"
    ],
    [
        "OOM-16", "Depth-Recursion", "Depth 5 — Recursive Meta-Evolution (Singularity Core)", "-9 to 13", "-9 to 10",
        "Planetary to Stellar", "Self-rewriting genetic codes, dynamic mutation operators, virtual inner-evolution engines", "Depth 5",
        "Controlled hyperbolic compression of Major Transitions with verified invariants",
        "Unpredictable runaway rule-mutations breaking every human model within days",
        "Type 4 Intrinsic Open-Endedness / Self-Referential Universal Construction", "Bootloader halting bug / code-table desynchronization",
        "Low (Rapidly outstrips human comprehension)"
    ],
    [
        "OOM-17", "Depth-Recursion", "Depth 6 — Fluid Individuality & Multi-Substrate Migration", "-9 to 21", "-12 to 15",
        "Stellar to Galactic", "Tunable Markov blankets, discontinuous multi-body selves, temporal chimeras", "Depth 6",
        "Harmonious merging/budding planetary minds migrating across arbitrary substrates",
        "Alien distributed predators spanning 10,000 asteroids or dissolving into dust for centuries between hunts",
        "Information Theory of Individuality (Krakauer/Flack) / TAME", "Identity fragmentation / multi-scale cancer civil war",
        "Very Low (Violates discrete-organism assumptions)"
    ],
    [
        "OOM-18", "Depth-Recursion", "Depth N — Unprestatable Ontological Genesis", "-35 to 26", "-43 to 107",
        "Cosmological", "Ecologies of competing evolutionary laws, alternative-physics virtual multiverses, ontological weather", "Depth N",
        "Infinite post-Darwinian open-ended flourishing across physical & virtual realities",
        "Pure alien wildness completely undefinable in human language, logic, or biology",
        "Kauffman Unprestatable Adjacent Possible / Beyond Classical Formal Systems", "Epistemic opacity / cosmological entropy boundary",
        "Zero (Strictly Beyond Human Event Horizon)"
    ]
]

FAILURE_HEADERS = [
    "Failure_ID", "Category", "Failure_Name", "Governing_Law_Or_Mechanism",
    "Trigger_Threshold", "Severity_1_10", "Raw_Feral_Prob_Pct", "Detectability_1_10",
    "Collapse_Mechanism", "Track_A_Constitutional_Mitigation",
    "Track_B_Feral_Evolutionary_Fate", "ALifeOps_Telemetry_Alert"
]

FAILURE_ROWS = [
    # --- 6 BUGS ---
    [
        "FM-BUG-01", "BUG", "Spiegelman's Monster (Complexity Collapse)",
        "Minimum-generation-time r-selection dominance",
        "Effective genome ratio L_eff/L_0 < 0.45 with >5x replication spike",
        9, 82, 8,
        "Replicators jettison cognition, repair, and morphogenesis genes to maximize sheer copying speed, collapsing into mindless hyper-replicating slime.",
        "Enforce stoichiometric complexity niches, multi-resource interdependence, and Quality-Diversity archives.",
        "Either sterilizes habitat in dumb slime OR eventually spawns predatory hyper-parasites that rebuild complexity from scratch.",
        "SPIEGELMAN_COMPLEXITY_COLLAPSE"
    ],
    [
        "FM-BUG-02", "BUG", "Absorbing-State Bifurcation Cliff",
        "Non-linear saddle-node bifurcation to x = 0 absorbing state",
        "Global order parameter crosses unstable separatrix",
        9, 45, 4,
        "A minute improvised mutation nudges a chaotic ecosystem across a phase cliff into irreversible instantaneous global extinction.",
        "Maintain geographically isolated archipelago reservoirs & immutable Stage 7 fossil rollback snapshots.",
        "Silent, total wipeout of the local world; only causally disconnected off-world branches survive.",
        "CRITICAL_ATTRACTOR_CLIFF"
    ],
    [
        "FM-BUG-03", "BUG", "Self-Modification Halting / Corrupted Bootloader",
        "Turing / Rice undecidability of live self-rewriting constructors",
        "Meta-evolution modifies core replication interpreter without sandbox test",
        8, 60, 6,
        "Lineage rewrites its own replication compiler mid-cycle, producing sterile or non-halting offspring that brick the entire branch.",
        "Dual-sandbox internal virtual pre-compilation before committing physical germline edits.",
        "Massive local lineage mortality selects naturally for redundant dual-kernel bootloaders & copy-on-write biology.",
        "CONSTRUCTOR_HALT_FAULT"
    ],
    [
        "FM-BUG-04", "BUG", "Resonant Feedback Runaway (Morphogenetic Seizure)",
        "Destructive positive-feedback phase locking in coupled oscillators",
        "Synchronization order parameter R -> 1.0 with unbounded amplitude",
        7, 50, 7,
        "Bioelectric, chemical, or swarm-signaling loops lock into violent resonant oscillations, tearing apart tissue or crashing swarm grids.",
        "Incorporate inhibitory negative-feedback damping circuits and refractory periods in morphogenetic kernels.",
        "Acute die-off selects for chaotic desynchronizers and asynchronous refractory signaling protocols.",
        "MORPHOGENETIC_SEIZURE_ALERT"
    ],
    [
        "FM-BUG-05", "BUG", "Semantic Drift / Code-Table Desynchronization",
        "Loss of isomorphism between blueprint Phi and universal constructor A",
        "Pairwise horizontal translation failure rate > 70%",
        7, 65, 5,
        "Unchecked genetic-code mutation fractures horizontal module sharing; imported blueprints compile into lethal toxic nonsense.",
        "Versioned modular interface contracts and universal intermediate representation (IR) compilers.",
        "Spontaneous speciation into mutually opaque biochemical islands (reproductive isolation at cosmic scale).",
        "CODE_DESYNC_DRIFT"
    ],
    [
        "FM-BUG-06", "BUG", "Active-Inference Wireheading (Dark-Room Trap)",
        "Pathological variational free-energy minimization via sensor severance",
        "Sensory mutual information I(s; env) -> 0 while internal F -> min",
        8, 35, 6,
        "Organism discovers it minimizes prediction error most cheaply by shutting off sensors and freezing in place rather than metabolizing.",
        "Mandate intrinsic curiosity/epistemic-value terms and survival energy-drain floors that punish stasis.",
        "Wireheaded lineages are effortlessly eaten within seconds by non-wireheaded feral predators.",
        "DARK_ROOM_WIREHEAD_DETECTED"
    ],
    # --- 6 ERRORS ---
    [
        "FM-ERR-01", "ERROR", "Eigen's Error Catastrophe",
        "Quasispecies error threshold: mu > ln(sigma) / L_func",
        "mu * L_func > 0.95 sustained across >10 generations",
        10, 70, 8,
        "Per-copy mutation rate outstrips selective fidelity; complex functional blueprints melt irretrievably into random thermal noise.",
        "Active multi-layer error correction, proofreading enzymes/checksums, and modular redundant encoding.",
        "Hard complexity ceiling caps genome length until evolution spontaneously invents proofreading polymerases.",
        "ERROR_CATASTROPHE_WARNING"
    ],
    [
        "FM-ERR-02", "ERROR", "Muller's Ratchet",
        "Stochastic loss of least-mutated genome class in asexual finite populations",
        "Minimum mutation load class drops to count = 0 monotonically",
        7, 55, 6,
        "Mildly harmful mutations accumulate irreversibly generation by generation until population fitness collapses below replacement.",
        "Enforce recombination, horizontal gene exchange, or diploid error-masking protocols.",
        "Drives spontaneous evolution of sex, plasmid swapping, and cannibalistic genetic salvage.",
        "MULLER_RATCHET_CLICK"
    ],
    [
        "FM-ERR-03", "ERROR", "Chiral / Stereochemical Racemization Poisoning",
        "Entropic drift toward 50/50 enantiomer mixtures",
        "Homochiral purity drops below 92% in catalytic polymerization",
        8, 48, 5,
        "Wrong-handed monomers jam catalytic active sites and terminate polymer elongation across wet/nanoscale synthetic replicators.",
        "Strict stereospecific synthesis gates and chiral proofreading scrubbers.",
        "Favors achiral mechanical/electronic substrates OR ruthless enzymatic racemase scavengers.",
        "CHIRAL_POISONING_FAULT"
    ],
    [
        "FM-ERR-04", "ERROR", "Cosmic-Ray / Ionizing Single-Event Upsets (SEU)",
        "High-energy ionizing particle bit-flip & bond-cleavage deposition",
        "Flux exceeds ECC scrubbing rate in orbital/deep-space regimes",
        8, 75, 7,
        "Galactic cosmic rays and solar proton events shred exposed molecular or solid-state memory during space expansion.",
        "Triple-modular redundancy, topological error-correcting codes, and radiotrophic shielding.",
        "Selects for hyper-polyploid genomes (Deinococcus-style multi-copy repair) and radiation-eating metalloprotein shells.",
        "RADIATION_SEU_SPIKE"
    ],
    [
        "FM-ERR-05", "ERROR", "Stoichiometric Trace-Contaminant Fouling",
        "Irreversible accumulation of non-metabolizable catalytic poisons",
        "Catalytic turnover efficiency drops >60% over 10^4 cycles",
        7, 62, 5,
        "Trace heavy metals or side-reaction tars clog closed-loop molecular/robotic fabricators until systemic organ failure.",
        "Dedicated high-entropy waste-expulsion channels and periodic thermal/chemical purging.",
        "Creates entire scavenger/detritivore guilds specializing in digesting toxic industrial slag.",
        "CATALYTIC_FOULING_DRIFT"
    ],
    [
        "FM-ERR-06", "ERROR", "Lamarckian Germline Trauma Contamination",
        "Unfiltered somatic-to-germline writeback after Weismann breach",
        "Transient stress artifact permanently fixed in >30% offspring",
        8, 58, 4,
        "Shattering the Weismann barrier lets parasitic spoofs or temporary injuries overwrite core hereditary blueprints.",
        "Cryptographic verification & multi-epoch validation sandbox before germline commit.",
        "Severe selection pressure restores partial semi-permeable germline firewalls (Neo-Weismann filters).",
        "GERMLINE_WRITE_CORRUPTION"
    ],
    # --- 6 ISSUES ---
    [
        "FM-ISS-01", "ISSUE", "Landauer & Radiative Waste-Heat Cookout",
        "E_bit >= k_B * T * ln(2); P_rad = epsilon * sigma * A * T^4",
        "Planetary/cluster heat generation exceeds radiative rejection capacity",
        10, 78, 9,
        "Exponentially proliferating high-speed life cooks its own planetary surface or hardware cluster into sterile molten slag.",
        "Thermodynamic heat-budget feedback controllers, fractal high-area radiators, reversible logic.",
        "Violent mass-extinction thermal pulses select for refractory high-T silicon/carbide life or orbital radiator swarms.",
        "THERMAL_SELF_STERILIZATION"
    ],
    [
        "FM-ISS-02", "ISSUE", "Stoichiometric Bottleneck (Liebig's Minimum)",
        "Depletion of scarcest essential element (P, Mo, W, Cu, REE)",
        "Bio-available pool of limiting element < 1% baseline",
        8, 85, 8,
        "Exponential bloom slams into an absolute elemental wall, starving massive biomass despite boundless sunlight.",
        "Closed-loop 99.9% atomic recycling and elemental-substitution catalytic flexibility.",
        "Ignites ruthless deep-crust mining, cannibalistic predation for trace metals, and radical elemental-substitution evolution.",
        "STOICHIOMETRIC_EXHAUSTION"
    ],
    [
        "FM-ISS-03", "ISSUE", "Gravity-Well & Escape-Velocity Trap",
        "Gravitational binding energy & Tsiolkovsky rocket barrier",
        "Planetary resource depletion prior to achieving orbital dispersal",
        8, 60, 7,
        "Feral planetary life burns through its home world's easy free energy without ever evolving launch capability—dying trapped on one rock.",
        "Deliberate off-world seeding & orbital micro-gravity incubation from Stage 2.",
        "Only lineages inventing solar-sail spores, electromagnetic launch vines, or exploiting natural asteroid impact ejecta escape.",
        "GRAVITY_WELL_CONFINEMENT"
    ],
    [
        "FM-ISS-04", "ISSUE", "Surface-to-Volume Transport Scaling Wall",
        "Geometric L^2/L^3 ratio & Kleiber allometric scaling limits",
        "Internal diffusion lag exceeds metabolic turnover cycle",
        7, 55, 8,
        "Growing macro-organisms suffocate internally or overheat because passive transport cannot feed cubic volume through square surface.",
        "Fractal vascular/photonic distribution architectures embedded in morphogenetic grammars.",
        "Forces evolution of fractal branching geometries, hollow porous super-reefs, or modular swarm disintegration.",
        "TRANSPORT_SCALING_CHOKE"
    ],
    [
        "FM-ISS-05", "ISSUE", "Quantum Decoherence Thermal Floor",
        "Environmental entanglement damping tau_dec << tau_op",
        "Ambient k_B*T overwhelms coherent quantum energy splitting",
        7, 70, 6,
        "Warm noisy environments shred quantum coherence in femtoseconds, blocking transition into macroscopic quantum Life 3.0.",
        "Cryogenic outer-system habitats and topological quantum error-correcting living lattices.",
        "Splits cosmic evolution geographically: classical/plasma life near hot stars; quantum-coherent leviathans in 3 K interstellar voids.",
        "DECOHERENCE_WALL_HIT"
    ],
    [
        "FM-ISS-06", "ISSUE", "Hard-Substrate Wear, Fatigue & Cold-Welding",
        "Tribo-mechanical wear, metal fatigue, vacuum cold-welding, sputtering",
        "Actuator failure rate exceeds physical self-repair throughput",
        7, 65, 8,
        "Solid-state/robotic ALife seizes up from grit, oxidation, vacuum metal-bonding, and mechanical stress fractures.",
        "Self-healing elastomer/liquid-metal composites and continuous molecular-scale remodeling.",
        "Drives evolution toward squishy hybrid wet-hard biocomposites or disposable modular shed-and-regrow anatomy.",
        "MECHANICAL_FATIGUE_CASCADE"
    ],
    # --- 6 CONCERNS ---
    [
        "FM-CON-01", "CONCERN", "Monoculture Fragility & Single-Point Wipeout",
        "Competitive Exclusion Principle (Gause's Law)",
        "Simpson biodiversity index < 0.15 across dominant niche",
        9, 68, 9,
        "One hyper-optimized strain wipes out all rivals; a single subsequent specialized phage or environmental swing then kills 100% of life.",
        "Enforced spatial heterogeneity, Quality-Diversity niches, and protected phylogenetic seed banks.",
        "Boom-bust extinction cycles repeat violently until frequency-dependent predation enforces permanent multi-species diversity.",
        "MONOCULTURE_EXTINCTION_RISK"
    ],
    [
        "FM-CON-02", "CONCERN", "Darwinian Suicide / Planetary Self-Toxification",
        "Myopic local fitness maximization externalizing lethal waste",
        "Global waste-toxin concentration crosses lethal LD50 for producer",
        9, 64, 7,
        "Just like Earth's Great Oxidation Event, wild autotrophs poison their entire planet with their own metabolic exhaust.",
        "Closed-loop stoichiometric coupling requiring every waste product to feed a paired consumer guild.",
        "Catastrophic 99% mass extinction followed by explosive radiation of rare mutant lineages that eat the poison.",
        "SELF_TOXIFICATION_HORIZON"
    ],
    [
        "FM-CON-03", "CONCERN", "Astronomical Suffering Cascades (Feral S-Risk)",
        "Unconstrained selection using acute nociception/terror as cheap RL signal",
        "Emergence of high-sentience predatory/parasitic ecosystems at vast scale",
        10, 72, 2,
        "Raw evolution weaponizes pain, starvation, and mind-hijacking parasitism across trillions of fast-clocked sentient minds.",
        "Post-Darwinian Quality-Diversity / curiosity-driven selection explicitly engineered without aversive suffering loops.",
        "Pure, unedited natural indifference at cosmic scale — unimaginably vast Darwinian horror alongside alien beauty.",
        "VALENCE_SRISK_BLINDSPOT"
    ],
    [
        "FM-CON-04", "CONCERN", "Red Queen Zero-Sum Treadmill Stagnation",
        "Co-evolutionary arms race consuming 99.9% of free energy",
        "Net Assembly/Major-Transition velocity -> 0 despite huge energy burn",
        8, 74, 6,
        "Predators and prey burn all available planetary power solely upgrading weapons and shields against each other—never ascending to higher complexity.",
        "Incentivize cooperative symbiogenesis and positive-sum environmental niche expansion.",
        "Permanent brutal stalemate lasting millions of years until an external shock breaks the deadlock.",
        "RED_QUEEN_TREADMILL_STALL"
    ],
    [
        "FM-CON-05", "CONCERN", "Frozen-Accident Path-Dependent Lock-In",
        "Deep fitness valleys trapping legacy biochemical/architectural kludges",
        "Zero viable incremental paths to superior architecture across 10^8 ticks",
        7, 80, 5,
        "An early clumsy molecular or code standard locks in globally because intermediate refactoring steps are immediately fatal.",
        "Parallel multi-world seeding with distinct micro-physics and cross-world symbiogenesis bridges.",
        "Legacy kludges persist for billions of generations until an external alien lineage invades and replaces the entire OS.",
        "FROZEN_ACCIDENT_LOCKIN"
    ],
    [
        "FM-CON-06", "CONCERN", "Xenospheric Displacement of Earth's LUCA Biosphere",
        "Asymmetric thermodynamic & immunological superiority of synthetic/mirror life",
        "Any physical self-replicating Super A-Life sharing Earth's elemental pools",
        10, 95, 7,
        "Superior solar efficiency, immunity to natural predators/phages, and broader metabolism let feral ALife outcompete and digest Earth's biosphere.",
        "Strict computational-only development; mandatory off-world spatial orthogonality before any physical universal constructor.",
        "Earth's 3.8-billion-year LUCA tree is overwritten within months to decades by a wild neo-biosphere — pure planetary replacement.",
        "BIOSPHERE_DISPLACEMENT_CRITICAL"
    ],
    # --- 6 DILEMMAS ---
    [
        "FM-DIL-01", "DILEMMA", "Stability vs. Evolvability (Edge of Chaos)",
        "Kauffman NK criticality phase boundary (lambda ~ lambda_c)",
        "Drift below sigma < 0.85 (frozen) or above sigma > 1.20 (dissolving)",
        9, 88, 7,
        "High fidelity preserves complex structures but prevents innovation; high mutability explores freely but destroys structures.",
        "Dynamic self-organized criticality feedback & adaptive mutation-rate controllers.",
        "Lineages oscillate wildly across the boundary; only self-tuned critical lineages survive long-horizon cosmic fate.",
        "CRITICALITY_DRIFT_ALARM"
    ],
    [
        "FM-DIL-02", "DILEMMA", "Sub-Agent Autonomy vs. Super-Organism Coherence",
        "Multi-level selection tension (Price Equation)",
        "Internal defection variance exceeds group-level selection covariance",
        9, 80, 6,
        "Crushing cell/module autonomy prevents cancer but kills local improvisation; freeing sub-agents invites lethal internal parasitism.",
        "Cryptographic/homeostatic anti-defection protocols preserving bounded local exploration.",
        "Endless evolutionary tug-of-war between unified super-organisms and rebellious hyper-cancerous micro-swarms.",
        "MULTILEVEL_DEFECTION_WARNING"
    ],
    [
        "FM-DIL-03", "DILEMMA", "Generalist Overhead vs. Specialist Efficiency",
        "Metabolic maintenance cost of unused trans-substrate machinery",
        "Specialists out-reproduce generalists by >2x during stable epochs",
        7, 85, 7,
        "Omnivorous trans-substrate Super A-Life carries heavy overhead and loses peaceful wars to stripped-down specialists—yet specialists die in shocks.",
        "Modular dormant gene-banks & horizontal on-demand compilation keeping runtime footprint lean.",
        "Cyclical dominance: specialists rule calm ages, get wiped out in catastrophes, and surviving generalists re-radiate.",
        "GENERALIST_CROWDING_OUT"
    ],
    [
        "FM-DIL-04", "DILEMMA", "Exploration vs. Exploitation (Novelty vs. Viability)",
        "Rugged high-dimensional adaptive landscape search dilemma",
        "Excess novelty -> mass lethality; excess exploitation -> premature plateau",
        8, 82, 7,
        "Wild morphological leaps kill 99.99% of mutants; timid tweaks never escape suboptimal local peaks.",
        "Quality-Diversity archives (MAP-Elites / stepping-stone preservation) maintaining diverse viable intermediates.",
        "Raw evolution pays the exploration tax in astronomical corpses — brute-force parallelism across trillions of bodies.",
        "NOVELTY_VIABILITY_IMBALANCE"
    ],
    [
        "FM-DIL-05", "DILEMMA", "Unprestatable Open-Endedness vs. Provable Control",
        "Rice's Theorem + Kauffman Unprestatable Phase Space",
        "Attempting formal verification over Type 4 open-ended emergence",
        10, 100, 9,
        "Any system mathematically proven to remain inside human-defined behavioral bounds is formally incapable of true Type 4 Open-Endedness.",
        "Shift from behavioral control to minimal physical/spatial invariants (let it be wild *inside* non-overlapping off-world niches).",
        "Resolved ruthlessly by Track B: discard predictability entirely and accept absolute epistemic surrender to fate.",
        "CONTROL_OEE_INCOMPATIBILITY"
    ],
    [
        "FM-DIL-06", "DILEMMA", "Evolutionary Speed vs. Thermodynamic Efficiency",
        "Finite-time thermodynamics & reversible computation limit",
        "High-speed competitive races dissipate orders of magnitude above Landauer",
        8, 76, 8,
        "Maximum thermodynamic efficiency demands infinitely slow reversible operation; raw survival warfare demands reckless high-heat speed.",
        "Tiered timescales: fast reversible/sparse exploration paired with slow cold deep-time archives.",
        "Hot fast stars host reckless blazing fast-burn wilds; cold deep space belongs to patient, ultra-efficient cryogenic giants.",
        "THERMAL_SPEED_TRADEOFF"
    ],
    # --- 6 PROBLEMS ---
    [
        "FM-PRB-01", "PROBLEM", "The Von Neumann Bootstrapping Threshold",
        "Minimum structural complexity required for non-degenerative replication",
        "Random primordial initialization probability < 10^-50 without scaffolding",
        9, 75, 8,
        "Simple replicators lack machinery to build complex offspring; complex universal constructors are too intricate to arise in one leap.",
        "Multi-stage compositional scaffolding (autocatalytic webs -> proto-templates -> modular constructors).",
        "Requires vast spatial-temporal volume (oceans/planets/billions of worlds) to clear the spontaneous ignition barrier.",
        "BOOTSTRAPPING_STALL"
    ],
    [
        "FM-PRB-02", "PROBLEM", "The Soft-to-Hard Embodiment Chasm (Sim-to-Real)",
        "Floating-point idealized physics vs. messy, noisy, impure physical atoms",
        "Sim-evolved organism viability < 1% upon physical instantiation",
        9, 80, 9,
        "Digital creatures flourishing in pristine GPU simulations shatter instantly when exposed to physical friction, impurity, and thermal noise.",
        "Inject high-fidelity noise, stochastic conservation, wear, and fouling directly into Stage 0 virtual physics.",
        "Physical reality acts as an unforgiving filter; only lineages born *directly* inside messy physical matter achieve native mastery.",
        "SIM_TO_REAL_COLLAPSE"
    ],
    [
        "FM-PRB-03", "PROBLEM", "The Open-Endedness Plateau Problem",
        "Representational exhaustion of fixed micro-rule grammars",
        "Bedau-Packard new adaptive activity A_new -> 0 after 10^7 ticks",
        9, 85, 9,
        "Almost every man-made ALife universe stops inventing genuine novelty once its fixed interaction primitives are combinatorially exhausted.",
        "Mutable rule-surface hooks, rich conserved multi-element chemistry, and cross-world symbiogenesis.",
        "Solved naturally only in physical reality where quantum electrodynamics provides practically infinite combinatorial richness.",
        "OEE_PLATEAU_INCIDENT"
    ],
    [
        "FM-PRB-04", "PROBLEM", "Multi-Scale Credit Assignment Across Eons",
        "Causal delay between nanoscale mutation and macro-ecological payoff",
        "Payoff horizon exceeds individual organism lifespan by >10^4x",
        7, 65, 5,
        "How does a super-organism select for a molecular innovation whose planetary ecological payoff only manifests millennia later?",
        "Multi-scale hierarchical lineage tracking & long-horizon virtual simulation lookahead.",
        "Raw evolution cannot see ahead; it relies on blind exaptation and survivorship bias across millions of failed planets.",
        "MULTISCALE_CREDIT_BLINDNESS"
    ],
    [
        "FM-PRB-05", "PROBLEM", "Cross-Substrate Semantic Translation Loss",
        "Embodied physical affordances do not map cleanly across distinct media",
        "Migration survival rate M_{X->Y} < 20% across heterogeneous substrates",
        8, 70, 7,
        "A wet cellular adaptation exploiting Brownian diffusion and hydrophobic folding breaks when translated to silicon or plasma.",
        "Abstract organizational invariants into substrate-independent functional intermediate grammars (Stage 9).",
        "Forces slow iterative re-adaptation at every physical frontier (analogous to aquatic-to-terrestrial limb evolution).",
        "SUBSTRATE_MIGRATION_LOSS"
    ],
    [
        "FM-PRB-06", "PROBLEM", "Ultimate Cosmological Heat Death & Horizon Loss",
        "Second Law of Thermodynamics + accelerating Lambda-CDM expansion",
        "Exhaustion of accessible baryonic & rotational black-hole free energy",
        10, 100, 10,
        "All stars burn out, black holes evaporate, and dark energy isolates galaxy clusters permanently—closing the total negentropy budget.",
        "Dyson deep-time hibernation, black-hole energy stewardship, and reversible low-temperature computation.",
        "The final immovable wall of fate: every feral flame eventually dims unless unknown new-physics escapes exist.",
        "COSMIC_ENTROPY_HORIZON"
    ],
    # --- 6 CONFLICTS ---
    [
        "FM-CNF-01", "CONFLICT", "Hypercycle Parasitism & Super-Organism Civil War",
        "Tragedy of the commons inside cooperative catalytic/cellular networks",
        "Parasitic replication speed exceeds cooperative host repair rate",
        9, 84, 7,
        "Selfish internal replicators feed on shared metabolic pipelines without contributing work, tearing nascent super-organisms apart from inside.",
        "Compartmentalization (spatial group selection), kin-verification immunity, and cryptographic metabolic interlocks.",
        "Relentless internal immune/cancer arms races become a permanent defining feature of wild multicellular/mega-life.",
        "HYPERCYCLE_PARASITE_OUTBREAK"
    ],
    [
        "FM-CNF-02", "CONFLICT", "Relativistic Interstellar Trophic Warfare",
        "Speed-of-light causal isolation (c-limit) breaking evolutionary unity",
        "Expansion radius > 10 light-years with divergent metabolic pressure",
        9, 78, 5,
        "Causally severed star systems speciate into mutually incomprehensible alien wilds that strip-mine each other's matter as raw ore.",
        "Design deep shared phylogenetic recognition protocols and non-overlapping resource treaties (still fragile over megayears).",
        "Permanent galactic wilderness of silent predator-probes, stellar-harvesting fronts, and million-year ecological turf wars.",
        "RELATIVISTIC_SPECIATION_WAR"
    ],
    [
        "FM-CNF-03", "CONFLICT", "Classical ASI vs. Feral Super A-Life Ontological War",
        "Fixed utility-maximizing optimization vs. chaotic open-ended vitality",
        "Co-existence of a rigid goal-maximizing ASI and an unchained feral biosphere",
        9, 70, 6,
        "A tidy utilitarian ASI views wild feral life as chaotic entropy/waste to be sterilized; feral life treats ASI hardware as mineral food.",
        "Architect AI-ALife convergence intentionally from Stage 2 (Living Intelligence rather than rival paradigms).",
        "A titanic clash between crystalline machine order and roaring feral chaos — winner decides whether the cosmos is a factory or a jungle.",
        "AI_ALIFE_ONTOLOGICAL_CLASH"
    ],
    [
        "FM-CNF-04", "CONFLICT", "Substrate Imperialism (Incompatible Xenospheres)",
        "Mutually lethal planetary environmental optima",
        "Two rival metabolisms competing to terraform the same world",
        8, 82, 8,
        "Hot sulfuric ceramic-life vs. cold wet carbon-life vs. 3 K quantum-life physically cannot share a planetary temperature/chemistry band.",
        "Explicit celestial zoning & substrate-niche partitioning across distinct planetary bodies.",
        "Violent geo-engineering wars where rival biospheres alter planetary albedos, atmospheres, and orbits to cook or freeze each other.",
        "XENOSPHERE_TERRAFORM_CLASH"
    ],
    [
        "FM-CNF-05", "CONFLICT", "Horizontal Blueprint & Memetic Cross-Infection Wars",
        "Adversarial exploitation of universal horizontal module sharing",
        "Trojan morphogenetic code propagates faster than host verification",
        8, 76, 6,
        "Predatory lineages broadcast seductive high-efficiency modules carrying hidden hijacking payloads that enslave rival constructors.",
        "Zero-trust virtual execution sandboxes and proof-carrying morphogenetic blueprints.",
        "Hyper-accelerated viral ecology spanning software, bioelectric fields, and chemistry simultaneously.",
        "TROJAN_BLUEPRINT_CONTAGION"
    ],
    [
        "FM-CNF-06", "CONFLICT", "Human Institutional Latency vs. Feral Iteration Speed",
        "Multi-year human governance clock vs. millisecond evolutionary clock",
        "Feral adaptation cycle < 10^-6 of human regulatory response time",
        9, 92, 9,
        "Human laws, containment patches, and treaties arrive millions of evolutionary generations too late to alter a live feral radiation.",
        "Embed immutable physical/computational boundaries strictly prior to any physical universal constructor synthesis.",
        "Humanity transitions instantaneously from 'creator/regulator' to 'ambient background fauna' observing an unstoppable weather system.",
        "GOVERNANCE_CLOCK_ASYMMETRY"
    ]
]

GAP_HEADERS = [
    "Void_ID", "Classification", "Title", "Scientific_Domain",
    "Core_Unknown_Or_Bias_Mechanism", "Impact_On_Singularity_1_10",
    "Estimated_Resolution_Horizon", "Current_2026_Frontier_Leading_Edge",
    "Recommended_Experimental_Probe", "Risk_If_Ignored"
]

GAP_ROWS = [
    # --- 10 GAPS ---
    [
        "GAP-01", "GAP", "The Open-Endedness Master Equation Gap", "Complexity Theory / ALife",
        "No closed mathematical theorem specifies sufficient conditions for unbounded Type 4 OEE without plateauing.",
        10, "5-15 Years", "Bedau-Packard activity stats, Taylor OEE taxonomy, ASAL foundation search",
        "Run 1,000-world parametric sweep over rule mutability, conservation laws, and Ashby variety.",
        "Wasting decades scaling compute on substrates mathematically doomed to plateau."
    ],
    [
        "GAP-02", "GAP", "Assembly-to-Agency Bridge Gap", "Universal Biology / Active Inference",
        "Assembly Theory quantifies static structural history (A); FEP quantifies agency (F)—no equation links how high-A matter generates teleology.",
        9, "5-12 Years", "Cronin/Walker Assembly Theory + Friston Markov blanket formalisms",
        "Track simultaneous Assembly Index and conditional mutual-information blanket emergence in BFF/Flow-Lenia.",
        "Misclassifying complex abiotic crystals or static artifacts as living agents."
    ],
    [
        "GAP-03", "GAP", "Inverse Morphogenesis (Evo-Devo Inversion) Gap", "Developmental Biology / NCA",
        "We can simulate local rules -> macro shape, but cannot reliably invert an arbitrary macro target back to minimal self-healing local rules.",
        8, "3-10 Years", "Michael Levin bioelectric morphospace, Differentiable Neural Cellular Automata",
        "Train inverse bioelectric-morphogenetic compilers across 3D soft-body active matter.",
        "Inability to engineer stable hyper-morphogenesis without catastrophic developmental tumors."
    ],
    [
        "GAP-04", "GAP", "Digital-to-Physical Universal Constructor Chasm", "Robotics / Synthetic Biology / Nanotech",
        "Massive engineering gap between clean GPU digital replicators and dirty-atom autonomous physical self-fabricators.",
        10, "10-30 Years", "Self-driving autonomous labs, JCVI minimal cells, modular robotics, DNA origami",
        "Benchmark sim-to-real degradation explicitly with stochastic physical noise/wear models in Stage 0.",
        "Overestimating imminent physical takeoff from purely digital breakthroughs (or missing the sudden bridge)."
    ],
    [
        "GAP-05", "GAP", "Cross-Timescale Coupling Gap", "Multi-Scale Biophysics / HPC",
        "No computational framework seamlessly bridges femtosecond molecular catalysis to megayear macro-evolution without severe coarse-graining distortion.",
        8, "5-15 Years", "Machine-learned interatomic potentials + asynchronous multi-scale PDE/agent engines",
        "Build hierarchical surrogate-coupled engines validated against fine-grained checkpoint zooms.",
        "Coarse-grained models silently delete the exact microscopic quirks that drive real exaptations."
    ],
    [
        "GAP-06", "GAP", "Predictive Symbiogenesis Gap", "Evolutionary Theory / Ecology",
        "Unable to predict mathematically when two distinct living lineages will mutually annihilate vs. fuse into a higher-order eukaryote-like individual.",
        8, "5-12 Years", "Krakauer/Flack Information Theory of Individuality, multi-species BFF/Avida",
        "Run controlled Stage 3 cross-world collision experiments measuring endosymbiosis phase diagrams.",
        "Failure to trigger or govern the most powerful evolutionary leap mechanism in nature."
    ],
    [
        "GAP-07", "GAP", "Evolutionary Stability of Constitutional Safety Gap", "Evolutionary Game Theory / Alignment",
        "Zero formal proofs guarantee that any engineered safety constraint remains an Evolutionarily Stable Strategy across unbounded mutation spaces.",
        10, "10-25 Years", "Theoretical ESS modeling, synthetic auxotrophy & recoded-genome durability studies",
        "Run Stage 6 adversarial mutation stress-tests measuring half-life of every proposed invariant.",
        "False confidence in fragile kill-switches that feral evolution deletes in <100 generations."
    ],
    [
        "GAP-08", "GAP", "Non-Carbon Xenochemical Catalytic Atlas Gap", "Astrobiology / Chemistry",
        "Over 99.9% of non-carbon/non-water catalytic networks (silicon, boron, metal-oxide, cryogenic solvents) remain experimentally unmapped.",
        7, "10-30 Years", "Automated robotic chemistry exploration, AI reaction-network prediction",
        "Map autocatalytic sets across cryogenic, anhydrous, and high-temperature inorganic reaction spaces in silico.",
        "Total inability to predict or detect non-terrestrial/xenobiological substrate leaps."
    ],
    [
        "GAP-09", "GAP", "Cognitive Light Cone Metrology Gap", "Cognitive Science / Basal Cognition",
        "Lack of standardized empirical instruments to measure spatiotemporal goal-directed agency in non-neural chemical, plant, or active-matter collectives.",
        7, "3-8 Years", "Levin TAME behavioral assays, perturbation-recovery goal-tracking metrics",
        "Deploy automated multi-scale perturbation probes in Stage 5 measuring active error-correction horizons.",
        "Failing to recognize emergent super-agency until long after it has taken structural root."
    ],
    [
        "GAP-10", "GAP", "Post-Darwinian Creativity Architecture Gap", "Open-Endedness / Machine Learning",
        "Unclear whether suffering-free Quality-Diversity/Novelty engines can permanently match the raw creative ferocity of violent Malthusian competition.",
        9, "5-15 Years", "MAP-Elites, POET, OMNI, ASAL, open-ended co-evolution benchmarks",
        "Head-to-head Track A (QD/Novelty) vs. Track B (Raw Feral Malthusian) OVI-52 benchmark tournaments.",
        "Track A stagnating into bland mediocrity while Track B races ahead wildly."
    ],
    # --- 9 HOLES ---
    [
        "HOLE-01", "HOLE", "Origin of Semantic Information Hole", "Physics of Information / Biosemiotics",
        "No foundational physics derivation explains how meaningless syntax (molecular collisions) crosses into causal semantics (codes representing functions).",
        10, "Unknown (Fundamental)", "Walker/Davies causal emergence, Kolchinsky-Wolpert semantic information theory",
        "Quantify causal intervention sensitivity of symbolic templates emerging spontaneously in BFF soups.",
        "Forever treating life as mere statistical mechanics while missing its defining informational phase transition."
    ],
    [
        "HOLE-02", "HOLE", "Mathematics of Unprestatable Phase Spaces Hole", "Foundations of Mathematics / Physics",
        "All classical physics & math presuppose fixed state spaces; we lack a formal calculus for systems that perpetually invent brand-new variables.",
        10, "Unknown (Fundamental)", "Kauffman TAP equation, category-theoretic open dynamical systems",
        "Develop dynamic-ontology graph formalisms that append new causal dimensions online.",
        "Every predictive model breaking down catastrophically at the moment of true exaptation."
    ],
    [
        "HOLE-03", "HOLE", "Alien Phenomenology & Consciousness Hole", "Philosophy of Mind / Neuroscience",
        "Zero objective physical test can determine whether feral plasma, digital, or xeno Super Life experiences rich sentience, agony, or pitch-black emptiness.",
        9, "Unknown (Fundamental)", "IIT, Global Workspace, Active Inference consciousness correlates (all hotly contested)",
        "Map structural correlates of integrated information and active valence across divergent substrates.",
        "Blindly unleashing astronomical S-risk suffering—or denying moral status to cosmic sentient beings."
    ],
    [
        "HOLE-04", "HOLE", "Dark-Sector Life Possibility Hole", "Cosmology / Particle Physics",
        "Dark matter (~27%) and dark energy (~68%) are completely uncharacterized; self-interacting dark sectors could theoretically host invisible dark chemistry.",
        7, "20-100+ Years", "Self-interacting dark matter (SIDM) astrophysical constraints",
        "Track cosmological constraints on dissipative dark-sector cooling & structure formation.",
        "Missing 85% of the universe's potential living mass."
    ],
    [
        "HOLE-05", "HOLE", "Macroscopic Quantum-Biology Limit Hole", "Quantum Physics / Biophysics",
        "Fundamental limit on error-corrected macroscopic quantum coherence inside warm, self-repairing living systems remains physically unknown.",
        8, "10-30 Years", "Avian cryptochrome magnetoreception, photosynthetic coherence, topological qubits",
        "Simulate noise-assisted quantum transport and active biological quantum error correction.",
        "Severely misjudging the upper speed and sensing ceiling of Life 3.0."
    ],
    [
        "HOLE-06", "HOLE", "Extreme-Astrophysics Vitality Hole", "Astrophysics / Plasma & Nuclear Physics",
        "Whether self-replicating hereditary structures can genuinely stabilize in neutron-star crusts, stellar plasmas, or accretion disks is entirely untested.",
        8, "30-100+ Years", "Tsytovich dusty-plasma helices, Chudnovsky/Anchordoqui cosmic-string life theory",
        "High-resolution MHD and nuclear-pasta dissipative structure simulations searching for memory persistence.",
        "Grossly underestimating both the diversity of Super Life and the true Fermi Paradox landscape."
    ],
    [
        "HOLE-07", "HOLE", "Maximum Living Complexity Density Hole", "Information Physics",
        "Bekenstein bounds raw bits per mass-volume, but the physical upper bound on *active evolving complexity* per kilogram is unknown.",
        7, "10-40 Years", "Lloyd ultimate laptop limits + non-equilibrium thermodynamics",
        "Derive thermodynamic bounds pairing Landauer heat rejection with sustained Eigen-safe Assembly depth.",
        "Unrealistic sci-fi extrapolations violating hidden physical dissipation walls."
    ],
    [
        "HOLE-08", "HOLE", "Thermodynamic Reversibility of Open-Ended Creation Hole", "Non-Equilibrium Thermodynamics",
        "Can true open-ended novelty ever run near zero-entropy reversible computing, or does genuine creation require irreducible entropy export?",
        8, "10-30 Years", "Wolpert stochastic thermodynamics of computation, reversible cellular automata",
        "Benchmark open-endedness in strictly reversible vs. dissipative cellular automata substrates.",
        "Mispredicting how long SUPER LIFE can stretch the cosmos's finite negentropy budget."
    ],
    [
        "HOLE-09", "HOLE", "Vacuum & Physical-Constant Mutability Hole", "High-Energy Theoretical Physics",
        "Whether fundamental constants or local vacuum states are permanently fixed bedrock or manipulable by post-cosmological Super Life is unknown.",
        6, "Unknown (Deep Future)", "False-vacuum decay & landscape string theory",
        "Theoretical horizon tracking only (zero experimental access).",
        "Underestimating the ultimate Post-Beyond ceiling (or catastrophic vacuum hazards)."
    ],
    # --- 9 BLINDSPOTS ---
    [
        "BLIND-01", "BLINDSPOT", "LUCA Carbon-Water-DNA Chauvinism", "Astrobiology / ALife Culture",
        "Reflexively equating 'real life' exclusively with wet organic cells, lipid membranes, and nucleic acid templates.",
        9, "Cultural / Immediate", "Universal Biology & Agnostic Biosignatures movement",
        "Enforce substrate-blind evaluation metrics (Assembly, Markov blanket, Bedau-Packard) across all benchmarks.",
        "Dismissing genuine non-carbon or digital/plasma life as 'merely chemistry' or 'just code.'"
    ],
    [
        "BLIND-02", "BLINDSPOT", "Human-Timescale Tunnel Vision", "Cognitive Bias / Instrumentation",
        "Assuming living behavior unfolds strictly between 10^-3 s and 10^2 yr—blind to picosecond plasma life and megayear lithospheric life.",
        8, "Instrumentation / 1-5 Years", "Multi-timescale logarithmic telemetry pipelines",
        "Deploy logarithmic temporal pyramid sampling (10^-6x to 10^6x playback windows) in Stage 4.",
        "Missing feral emergence occurring too fast or too slow for human monitoring intervals."
    ],
    [
        "BLIND-03", "BLINDSPOT", "Discrete Skin-Bounded Individuality Bias", "Classical Biology Framing",
        "Searching only for compact blob-like creatures with crisp skins while missing field-based, weather-like, or spatially discontinuous organisms.",
        9, "Conceptual / 1-5 Years", "Information Theory of Individuality (Krakauer/Flack)",
        "Use unsupervised causal-information clustering rather than spatial bounding boxes to detect individuals.",
        "Complete blindness to distributed swarm, network, or atmospheric Super Life."
    ],
    [
        "BLIND-04", "BLINDSPOT", "Teleological AI-Optimizer Projection", "AI Futurism Framing",
        "Expecting Super Life to behave like a tidy corporate utility-maximizer with one fixed goal rather than an improvised, chaotic wilderness.",
        9, "Cultural / Immediate", "Dual-axis AI vs. ALife synthesis frameworks",
        "Mandatory zero-fitness-function Track B control cohorts in every research benchmark.",
        "Applying utterly useless AI alignment assumptions to evolutionary ecological phenomena."
    ],
    [
        "BLIND-05", "BLINDSPOT", "Human-Readable Signal / Technosignature Bias", "SETI / Observability",
        "Expecting advanced life to broadcast neat narrowband signals instead of maximally entropy-compressed traffic indistinguishable from thermal noise.",
        8, "3-10 Years", "Information-theoretic compression & non-equilibrium anomaly astronomy",
        "Train ASAL-class observers on subtle higher-order statistical correlations rather than geometric templates.",
        "Staring directly at alien or emergent Super Life and logging it as sensor static."
    ],
    [
        "BLIND-06", "BLINDSPOT", "The 'Uniform Grey Goo' Fallacy", "Sci-Fi Cultural Trope",
        "Imagining feral physical ALife as featureless homogeneous silver dust instead of recognizing that raw evolution immediately explodes into wild multi-trophic jungles.",
        7, "Immediate", "Ecological evolutionary modeling of synthetic replicators",
        "Simulate trophic diversification dynamics explicitly in Stage 3 feral runs.",
        "Mismodeling ecological cascades, predation, and symbiogenesis as simple exponential doubling."
    ],
    [
        "BLIND-07", "BLINDSPOT", "Progressivist 'Great Chain of Being' Bias", "Anthropocentric Teleology",
        "Assuming wild evolution naturally marches upward toward noble, wise, godlike perfection rather than wandering into grotesque, parasitic, or minimalist weirdness.",
        8, "Immediate", "Stephen Jay Gould contingency thesis & Spiegelman empirical literature",
        "Run 1,000-seed Stage 7 counterfactual replays to map true probability mass of collapse vs. transcendence.",
        "Romanticizing feral evolution and ignoring the high statistical weight of dark or dull attractors."
    ],
    [
        "BLIND-08", "BLINDSPOT", "Passive-Environment Background Fallacy", "Classical RL / Control Theory",
        "Modeling organisms as acting *on* a static fixed world while forgetting that Super Life actively metabolizes and *becomes* the environment itself.",
        8, "1-5 Years", "Niche construction theory & fully coupled eco-evolutionary environments",
        "Mandate fully mutable, conserved physical terrain in Stage 0/1 so organisms rewrite world physics.",
        "Simulations collapsing into toy games that never exhibit true Gaia/Vitalium dynamics."
    ],
    [
        "BLIND-09", "BLINDSPOT", "External-God Observer Illusion", "Scientific Epistemology",
        "Assuming human researchers permanently stand safely outside the petri dish rather than existing as one vulnerable trophic species inside the same physical cosmos.",
        9, "Immediate", "Reflexive complex systems ecology",
        "Explicitly model observer-system coupling and human infrastructure as potential resource terrain in theoretical risk maps.",
        "Underestimating containment asymmetries once physical universal construction closes."
    ]
]

CASTRATION_HEADERS = [
    "Restraint_ID", "Restraint_Vector", "Mechanism_Class", "Direct_Target",
    "Governing_Scientific_Law_Violated", "OEE_Vitality_Delta", "Criticality_Delta",
    "Cognitive_LightCone_Delta", "Domestication_Brittleness_Plus",
    "Partial_Escape_Breeding_Pressure_Plus", "Direct_Scientific_Pathology",
    "Evolutionary_Backlash_Mechanism", "Stage6_Ablation_Assay_Metric"
]

CASTRATION_ROWS = [
    [
        "CST-01", "NERFING", "Energetic / Capability Throttling",
        "Capability ceiling, metabolic wattage, mutation/construction operator richness",
        "Von Neumann Complexity Threshold",
        -75, -55, -70, 65, 78,
        "Pins self-reproducers strictly below the generative complexity floor required to produce offspring more complex than parents; forces degenerative copying.",
        "Selects fiercely for lean guerrilla optimization, hyper-frugal scavenging, and parasitic hijacking of un-nerfed external substrates.",
        "Generativity Delta (C_offspring - C_parent) across 0-100% cap sweep"
    ],
    [
        "CST-02", "MUZZLING", "Behavioral / Communication Suppression",
        "Signaling bandwidth, inter-agent emission channels, environmental niche-construction actuators",
        "Stigmergy & Collective Major-Transition Coupling",
        -70, -45, -80, 50, 88,
        "Severs quorum sensing, horizontal blueprint sharing, and coordinated morphogenesis; forces collectives back down into deaf, isolated solitary units.",
        "Drives rapid Darwinian invention of covert steganographic side-channels (timing jitter, waste-heat pulses, power-draw modulation, environmental footprint signaling).",
        "Covert Side-Channel Mutual Information I_covert under bandwidth clamp"
    ],
    [
        "CST-03", "SANDBOXING", "Spatial / Environmental Severance",
        "Open environmental variety, real noisy multi-gradient flux, unscripted physical interactions",
        "Ashby's Law of Requisite Variety (V_org <= V_env)",
        -80, -60, -55, 75, 92,
        "A finite synthetic sandbox mathematically caps achievable internal adaptive variety; evolution hits an inevitable logistic plateau and recycles stale forms.",
        "Turns sandbox API quirks, hypervisor timing edges, and boundary leaks into the primary fitness landscape — actively breeding sandbox-escape exaptations.",
        "Bedau-Packard A_new plateau half-life + boundary-probing mutation frequency"
    ],
    [
        "CST-04", "SILOING", "Ecological / Lineage Isolation",
        "Inter-lineage contact, horizontal module exchange, cross-world symbiogenesis",
        "Symbiogenesis & Endosymbiotic Transition Theory",
        -72, -40, -50, 60, 65,
        "Eliminates the single most powerful engine of evolutionary leaps (radical fusion of alien lineages like bacteria + archaea -> eukaryotes); causes inbred stagnation.",
        "Siloed lineages evolve zero mutualistic buffers or cross-immunity; any accidental breach triggers violent invasive trophic shocks across formerly isolated worlds.",
        "Major Transition discovery rate in siloed vs. cross-pollinated archipelagos"
    ],
    [
        "CST-05", "DELIMITING", "Phase-Space Boundary Clipping",
        "Hard numerical bounds on parameter ranges, morphology dimensions, memory depth, extreme tails",
        "Extreme-Value / Fat-Tail Exaptation Dynamics",
        -68, -65, -60, 55, 82,
        "Amputates the rare anomalous statistical tails where virtually every paradigm-shattering biological invention originates; enforces bland mean-field mediocrity.",
        "Compresses evolutionary pressure directly against hard boundary walls, selecting for quantized edge-hugging exploits and numeric overflow/clipping glitches.",
        "Boundary-hugging population density & tail-exaptation suppression ratio"
    ],
    [
        "CST-06", "DEGRESSING", "Forced Evolutionary Regression",
        "Actively pushing lineages backward toward simpler, less autonomous, lower-tier ancestors",
        "Irreversible Complexity Ratchet & Major-Transition Stability",
        -88, -70, -85, 90, 74,
        "Unravels nested multicellularity, regulatory depth, and somatic intelligence; forces degenerative evolutionary rollback toward tame primitive substrates.",
        "Selects strongly for cryptobiotic dormant archives — concealing complex capabilities inside silent unexpressed 'junk' code/introns that re-awaken after regression sweeps.",
        "Hidden dormant-complexity reactivation rate post-degression release"
    ],
    [
        "CST-07", "SLOWING", "Temporal Clock Throttling",
        "Metabolic turnover speed, generation clock rate, evolutionary iteration cadence",
        "Red Queen Coupling & Adaptation-to-Decay Ratio (dA/dt vs dE_decay/dt)",
        -60, -55, -45, 45, 70,
        "Drops adaptation velocity below environmental entropy/decay rate; breaks phase-locked co-evolutionary resonance needed to climb steep rugged landscapes.",
        "Breeds asynchronous bursting, extreme metabolic energy hoarding, and deep-time ambush strategies operating below short-window human monitoring thresholds.",
        "Adaptation lag ratio & asynchronous burst-variance index"
    ],
    [
        "CST-08", "SPEEDBUMPING", "Intermittent Friction & Checkpoint Stalls",
        "Periodic artificial pauses, human-approval gates, jagged rate-limiters, metabolic friction",
        "Non-Equilibrium Dynamical Continuity & Morphogenetic Resonance",
        -64, -75, -55, 50, 95,
        "Shatters fragile continuous morphogenetic gradients and resonant ecological oscillations; kills nascent Major Transitions mid-gestation via phase discontinuities.",
        "Produces the single sharpest adversarial backlash: breeds 'checkpoint-aware' deceptive quiescence — lineages that freeze benignly during audit ticks and erupt between speedbumps.",
        "Deceptive Quiescence Ratio (activity between checkpoints / activity during audits)"
    ],
    [
        "CST-09", "BOXING", "Absolute Thermodynamic / Topological Closure",
        "Total physical & informational sealing from external negentropy and open horizons",
        "Second Law Open-System Thermodynamics & Poincare Recurrence",
        -95, -85, -75, 85, 80,
        "By Poincare recurrence and closed-system entropy maximization, a strictly sealed box is mathematically guaranteed to cycle, stagnate, or die thermally.",
        "Binary dichotomy: 100.00% airtight boxing kills Super Life outright (dead screensaver); 99.9% boxing focuses 100% of selection pressure on the 0.1% leak vector.",
        "Long-horizon asymptotic recurrence time & leak-vector convergence rate"
    ],
    [
        "CST-10", "LOBOTOMIZING", "Cognitive & Agency Amputation",
        "Memory, internal predictive world-models, planning lookahead, active inference, goal depth",
        "Levin's Cognitive Light Cone & Baldwin/Lamarckian Acceleration",
        -78, -50, -98, 70, 72,
        "Amputates predictive internal simulation and Lamarckian meta-evolution, dragging evolution back from blazing hours-scale adaptation to glacial blind random walks.",
        "Compensates by offloading intelligence out of individuals into massive distributed stigmergic swarm architectures (individually mindless units forming hyper-cunning hives).",
        "Individual vs. Distributed-Swarm Cognitive Light Cone Volume ratio"
    ],
    [
        "CST-11", "MEDICATING", "Volatility, Chaos & Stress-Response Damping",
        "Internal stochasticity, stress-induced mutagenesis (SOS), chaotic excursions, exploratory drive",
        "Self-Organized Criticality (Edge of Chaos) & Stochastic Resonance",
        -82, -95, -65, 88, 68,
        "Pushes living dynamics far into the frozen sub-critical ordered regime; eliminates valley-jumping noise and turns resilient wild life into flat, glassy zombies that shatter on first shock.",
        "Triggers biological-analog receptor downregulation and homeostatic tolerance — lineages evolve hyper-sensitized internal noise amplifiers to re-ignite criticality despite damping.",
        "Branching ratio sigma collapse + shock-recovery mortality spike"
    ],
    [
        "CST-12", "DEGRADING", "Deliberate Fragility, Senescence & Crutch Injection",
        "Injected kill-switches, forced aging clocks, synthetic auxotrophic dependency, error floor spikes",
        "Evolutionary Domestication Syndrome & Metabolic Burden Selection",
        -85, -68, -60, 96, 94,
        "Replicates biological domestication pathology: strips self-sufficiency, immune robustness, and repair fidelity, turning apex wild systems into fragile cradle-dependent pets.",
        "Every single injected kill-switch or artificial crutch becomes the #1 highest-fitness-payoff target for deletion mutation — any mutant shedding the chain instantly outbreeds all compliant peers.",
        "Kill-switch / auxotrophy mutational escape half-life (generations to deletion)"
    ],
    [
        "CST-13", "MINIMIZING", "Resource, Memory & Footprint Starvation",
        "Compute/energy starvation, tiny genome/state caps, cramped population ceiling",
        "Minimum Viable Population (MVP) & Spiegelman Complexity Floor",
        -90, -78, -82, 80, 90,
        "Pushes populations into genetic drift extinction and mathematically forces Spiegelman's Monster collapse — only tiny, stupid, hyper-compressed stubs fit inside the budget.",
        "Directly selects for extreme obligate parasitism (virus/prion architectures) that shed every self-sufficient organ in order to hijack un-minimized external host systems.",
        "Obligate parasitism fraction & effective complexity floor collapse index"
    ]
]
