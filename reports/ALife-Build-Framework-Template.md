# Artificial Life Clean-Slate Build Framework & Architecture Template (v3.0)

- **Status:** FINAL CANONICAL SPECIFICATION (`0 / 825` Clean-Slate Initialized)
- **Author:** Alex Donahue · **Date:** 2026-11-11
- **Ordered Visual Architecture Models:** `Model 1` through `Model 14` (strictly ascending in companion PDF/HTML)

## 1. Ten Clean-Slate Architectural Invariants (`P1–P10`)

| ID | Invariant | Operational Engineering Contract |
| --- | --- | --- |
| P1 | Clean-Room Originality (Principles Only, Never Copies) | Transfer mathematical, biophysical, neurological, and ecological principles from peer-reviewed biology and A-Life literature, while engineering 100% original parametric morphologies, body silhouettes, connectomes, shaders, and source code. Zero copied meshes, sprites, weight dumps, or repositories. |
| P2 | Compensated FP64 First-Law Closure & Second-Law Sink | Conserve mass and enthalpy across all 11 pools (`E_patch..E_heat_phys + E_diss_num`) in IEEE `FP64` with Kahan-Neumaier compensation (`\|ΔE\| / (E_0 + E_in,cum) < 1e-12`; never `Q16.16`). Enforce Second-Law irreversibility (`0` heat-to-ATP backflow) and book XPBD numerical damping explicitly (`ΔE_diss_num ≥ -1e-15`). |
| P3 | Causal Wiring & Zero Cosmetic Parts (`C-NC`) | Every declared organ, neural sub-circuit, soft hydrostatic chamber, neuromodulator, and transducer must causally alter internal state and downstream behavior within its active ecological regime. Display-only variables, dead matrices, and scripted animations fail conformance. |
| P4 | Seed Firewall, Domain-Isolated PRNG & Two-Tier Reproducibility | Separate `Practice (100–999)`, `Tuning (2000–2999)`, and `Locked Held-Out Test (≥5000, burn-on-fail)` seeds. Key `Philox4x32-10` counters by `(ver, seed, domain, entity_id, organ_id, tick, purpose, draw_idx)` with `WORLD_EXOG` isolated from `ENTITY_INT`. Tier-1 CPU/WASM uses core-shipped `exp_det`/`log_det` and `.alifebin` snapshots for bit-exact SHA-256 hashes; Tier-2 GPU/surrogate bulk mode verifies preregistered observable distribution parity. |
| P5 | Soft Embodied Allostasis, Chemoton Chemistry & Real Mortality | Ground survival in deformable XPBD hydrostatic boundaries (`\|ΔV\|/V_0 < 1%`), Gánti's 3-cycle Chemoton (`A`, membrane `T`, template polymer `pV_n`), Michaelis-Menten saturation, 3-phase fasting, clotting/regeneration, and irreversible death returning carcass mass to dome detritus. |
| P6 | Controlled Multi-Arm Causal & FWER Statistical Proof | Evaluate claims across `1. Intact`, `2. Passive Soft-Body (0-Brain)`, `3. Shuffled Stream`, `4. Targeted Lesion`, plus `Size-Matched Sham Lesion` (for ablations) and `Competent Simple Baseline` (for complex substrates). Use power-sized paired locked seeds (`N ≥ 24` large effects; `N = 64–120` moderate effects), exact paired Wilcoxon/sign-flip tests with **Holm-Bonferroni FWER (`α ≤ 0.05`)**, within-pair dominance `δ_pair ≥ 0.33`, and one-sided non-inferiority (`LCB_95% > -Δ_NI`) on prior floors. |
| P7 | Neutral Operational Framing & Static/Mutant Anti-LARP Guard | Treat `Butlin-14`, `F1–F10`, and forked-snapshot `PCI*` strictly as operational computational-dynamics indicators—never metaphysical claims of subjective sentience. Enforce AST/symbol-import oracle bans and reject all 5 negative mutants (`Leaky-2e-11, Cosmetic, Oracle, Frozen, Shuffled`). |
| P8 | Multicellular Ontogeny, Metamorphosis & Open-Ended Biosphere | Grow bodies and brains from yolk-funded founder cells via GRN cleavage, differential adhesion, apoptosis, and size-proportional juvenile sleep pruning; preserve learned aversions across holometabolous metamorphosis inside an `O(N_pop + C_pairs)` closed trophic dome. |
| P9 | Strict Observer Independence & Bounded Telemetry | In Tier-1 canonical runs, camera pose, open UI tabs, exports, and the Frame-Time Governor adjust **render & lossy UI decimation ONLY**—never physics meshes, ray counts, or `WSE` timing (`UI-open hash == headless hash`). Scope zero-copy strictly to Sim-Worker ↔ UI-Worker `SharedArrayBuffer` (`SeqLock` 3-retry bound + double-buffer fallback). |
| P10 | Hardware Frugality, Explicit Arena Accounting & Multirate Clocks | Use flat `SoA` `TypedArray` arenas (`0` post-warmup heap allocations across `10,000` ticks), tiled sparse `CSR` / 32-synapse packed `int4`/`b1.58` blocks with separate plasticity/queue budgets, the `5-Gear Deterministic Multirate Scheduler`, `0 ≤ Q ≤ 10` qubit caps, and contiguous hysteresis Governor bands. |


## 2. Clean-Room Principle Transfer Matrix

| Domain | Principles & Equations to Transfer | Strictly Banned Shortcuts / Copies |
| --- | --- | --- |
| 1. Autopoietic Chemistry & Metabolism | Gánti Chemoton (`A`, lipid `T`, polymer `pV_n`), Michaelis-Menten saturation, positive-orthant antithetic integral control, 3-phase starvation, Cori cycle. | Scalar `energy -= 0.1` counters; negative chemical concentrations; copying external parameter tables. |
| 2. Soft Continuum Mechanics & Gaits | Hydrostatic `\|ΔV\|/V_0 < 1%` cavities, XPBD viscoelastic cuticles, biotensegrity webs, passive compliance offload, peristaltic/undulatory/ciliary gaits. | Copying any external creature's 3D mesh, limb rig, body silhouette, or visual appearance. |
| 3. Omnimodal Active Sensorium | Motion-parallax peering, saccadic foveation, bilateral plume chemotaxis, log-spaced cochlea, lateral-line wake shear, continuum skin strain sheet. | Passing ground-truth `food.x - self.x` coordinates or unmediated object-class enums to policy. |
| 4. Spiking, Liquid & Dendritic Compute | LIF/AdEx sparse spikes, bounded closed-form `CfC` & spiking `sLTC` adaptive `τ(x)`, two-compartment apical `dCaAP` XOR, autonomous peripheral ganglia. | Unbounded dense `FP32` `N²` matrices where sparse `CSR` fits, or cosmetic spikes with zero motor gain. |
| 5. Plasticity, Glia & Sleep Homeostasis | 3-factor `pre × post × mod` eligibility, BTSP plateau tagging, astrocyte `Ca²⁺` gates, SCN circadian pacemaker, size-scaled NREM `SHY` & REM replay. | Backpropagating gradients through world physics or running positive Hebbian loops without `iSTDP`/BCM. |
| 6. Associative & World-Model Memory | Kenyon-inspired `2%` SDR expansion, theta-gamma 4-slot WM, Modern Hopfield + VSA binding, latent world rollouts, source/reality monitoring. | Unbounded `.push()` episode arrays causing OOM; conflating REM rollouts with experienced counts. |
| 7. Global Workspace, HOT & Planning | Capacity-limited ignition + lags 2–5 blink (lag-1 sparing), Attention Schema (`AST`), calibrated `HOT` belief/confidence, danger-geodesic detours. | Hardcoded `if (conf < 0.5) scan()` heuristics bypassing learned internal second-order monitors. |
| 8. Affective Interior & Self-Agency | 4-timescale affect (`emotions → moods → attitudes → temperament`), efference-copy forward model (`AE-2`), trajectory-curvature caution, famine triage. | Naming random variables `'joy'` or `'grief'` without causal feedback into policy and visceral state. |
| 9. Ontogeny, Metamorphosis & Heredity | Yolk-funded zygote cleavage, Steinberg cell sorting, apoptosis, Kleiber `M^0.75` scaling, Blackiston-assay metamorphosis retention, Baldwin effect. | Spawning full-grown adult clones at zero enthalpy cost or claiming Lamarckian weight copy by accident. |
| 10. Biosphere, Culture & Trophic Webs | Solar-detritus nutrient closure, ATP-priced acoustic/chromatophore calls, dialect drift, conformable-grip stone tools, 3-guild coevolving food webs. | `O(N_pop²)` pairwise social loops; zero-cost telepathic state sharing bypassing physical fields. |


## 3. Disambiguated Complexity Legend & 11-Pool Compensated FP64 Thermodynamics

| Symbol | Scope, Cardinality & Reference Tier Anchor |
| --- | --- |
| N_units | Neural units / compartments per creature brain (reference Tier-W focal = 50,000; Tier-L laptop = 8,192). |
| E_syn | Directed stored synaptic edges per creature brain (reference focal = 10^8 at density ρ = 4.0%; Tier-L = 500,000). |
| k | Active spiking fraction per Gear-1 (5 ms) step; biological sparse regime k ≈ 0.01–0.04 (2–8 Hz mean firing rate). |
| N_pop | Active organisms in dome/biosphere; broad-phase spatial hash is O(N_pop + C_pairs), where C_pairs = local candidate contacts. |
| V_mesh | Soft-body viscoelastic mesh vertices per organism (fixed per experiment in Tier-1 canonical runs: e.g. 24, 32, or 64). |
| R_rays | Active sensory rays / plume sample probes per organism step; B_bands = cochlear / lateral-line spectral filter bands. |
| D_lat | Latent world-model, working-memory, or VSA hypervector dimension (typically 128–4,096). |
| M_pat / M_mod | M_pat = stored Modern Hopfield episodic patterns; M_mod = parallel specialist modules competing for workspace ignition. |
| G_sp / G_plan | G_sp = spline intervals per KAN edge; G_plan = nodes in internal Riemannian planning graph. |
| K_iter | Bounded inner solver iterations per step (e.g., XPBD constraint sweeps K=4..8, implicit chemistry Newton steps K=2..4). |
| Q | Coherent qubits in optional internal quantum register; integer-clamped 0 ≤ Q ≤ 10 (statevector = 2^(Q+4) bytes ≤ 16 KiB). |


- **Representation:** IEEE-754 FP64 with Kahan-Neumaier compensated summation (or int64 1-microjoule integer quanta); NEVER Q16.16 fixed-point.
- **Relative Drift Gate:** `|(Sum_11(E_pools(t)) + E_export_out_cum(t)) - (E_0 + E_solar_in_cum(t) + E_import_in_cum(t))| / (E_0 + E_solar_in_cum(t)) < 1e-12`
- **Second-Law Sink Rule:** Heat sinks (E_heat_phys, E_diss_num) are strictly one-way irreversible sinks (dE_heat_phys/dt ≥ 0, zero back-conversion to E_atp, E_stores, or mechanical work; ΔE_diss_num < -1e-15 triggers anti-free-energy fault).

| Slot | Pool ID | Physical Meaning & Sign Invariant |
| --- | --- | --- |
| Pool 01 | E_patch | Primary producer / substrate chemical enthalpy standing stock (kJ) |
| Pool 02 | E_gut | Unabsorbed chyme enthalpy inside organism digestive lumen (kJ) |
| Pool 03 | E_blood | Circulating glucose, free fatty acids, amino acids & beta-HB ketones (kJ) |
| Pool 04 | E_stores | Hepatic glycogen + adipose triacylglycerol reserve pools (kJ) |
| Pool 05 | E_atp | Immediate high-energy phosphate currency gating spikes, pumps & motors (kJ) |
| Pool 06 | E_tissue | Structural somatic & neural biomass enthalpy (kJ) |
| Pool 07 | E_kinetic | Macroscopic translational & rotational soft-body kinetic energy (kJ) |
| Pool 08 | E_elastic | Reversible XPBD viscoelastic membrane & tendon strain potential energy (kJ) |
| Pool 09 | E_detritus | Excreted urea/feces + post-mortem carcass labile organic pools (kJ) |
| Pool 10 | E_heat_phys | Irreversible metabolic, frictional & spike-dissipation thermal sink (kJ; monotone non-decreasing) |
| Pool 11 | E_diss_num | Explicit XPBD / implicit-integrator numerical damping sink (kJ; must satisfy ΔE_diss_num ≥ -1e-15 per step) |


## 4. Eight Orthogonal System Dimensions (`D1–D8`)

| ID | Dimension | Tagline | Soft A-Life & Wet Biology Scope | Hardware Rule |
| --- | --- | --- | --- | --- |
| D1 ⚙ | Computational | What Math, Precision Contracts & Information Transformations Execute Inside the Entity | In Soft A-Life & wet biology, computation spans sparse spiking events, adaptive liquid conductances, reaction-diffusion PDEs, apical calcium XOR plateaus, and passive viscoelastic strain fields—each governed by an explicit storage/accumulator/rounding contract. | Use tiled sparse CSR O(k·E_syn) + 32-synapse packed blocks; clamp coherent quantum registers to integer 0 ≤ Q ≤ 10. |
| D2 ⏱ | Operational | How the Simulation Schedules, Allocates, Streams & Stays Deterministic on Real Silicon | Coupling deformable bodies, spiking cortices, and ecosystems stalls CPUs/GPUs if everything steps at 0.5 ms in GC-allocated objects. Operational engineering enforces multirate clocks, flat SoA arenas, deterministic math, and render-only frame governance. | Zero allocations & zero BigInt conversions in tick(); verify crossOriginIsolated before enabling SharedArrayBuffer. |
| D3 🎯 | Functional | What Adaptive Viability Problem Each Mechanism Solves ('Why It Pays Its ATP Rent') | Biological organs persist because they solve concrete survival, homeostatic, or reproductive problems under energetic scarcity. Functional contracts define input-to-consequence lift independent of substrate, supporting degeneracy. | Every module must beat Passive-Body, Shuffled, Targeted-Lesion, and Size-Matched Sham-Lesion controls on locked seeds. |
| D4 🔄 | Systems | Closed-Loop Cybernetics, First/Second-Law Conservation & Push-Pull Organ Coupling | A living creature is not a feedforward `sense -> think -> act` pipe; it is a closed thermodynamic knot where visceral chemistry modulates neural gain, action reshapes resource patches, and heat exits one-way under First- and Second-Law constraints. | Enforce single-writer double-buffered state updates (`prev -> next`) and explicit cross-gear flux accumulators. |
| D5 📐 | Design | Parametric Bauplan Geometry, Compliance Gradients, Connectome Wiring & Protection Rings | Design governs the creature's 100% original physical bauplan, viscoelastic compliance distribution, active sensor geometry, 3D wiring cost, and write-protection rings—making mechanical and metabolic trade-offs evolvable. | Fix soft-mesh vertex count per experiment in Tier-1 canonical mode; reserve multi-fidelity mesh swapping for Tier-2 crowds. |
| D6 🪜 | Orders | Orthogonal Spatial Scales (O0–O7) × Cybernetic Control Orders (0th–4th Order) | Separating physical spatial scale (ions to biospheres) from cybernetic control depth (passive compliance to lineage evolution) eliminates 'Orders' ambiguity and assigns every variable a clear clock gear and state width. | Coarsen integration rate and aggregate spatial representations at higher O-levels so host step time stays bounded. |
| D7 🌊 | Processes | Continuous & Event-Driven Biophysical Fluxes Unfolding Across Time | Living matter is never static at rest: ion pumps counter osmotic leak, metabolic intermediates turn over, eligibility traces decay, adenosine accumulates, and soil detritus mineralizes continuously. | Use exact exponential-Euler for linear decay and bounded implicit backward-Euler/TR-BDF2 for stiff nonlinear chemistry. |
| D8 🏁 | Stages | Discrete Phase Regimes Across Ontogeny, Arousal/Sleep, Fasting & Verification Gates | Continuous biological processes reorganize across sharp regime transitions—zygote hatching, critical-period closure, pupal metamorphosis, NREM/REM flips, cryptobiotic vitrification, and strict CI promotion gates. | Block promotion to Stage k+1 until Stage k passes 100% of thermodynamic, memory-arena, and causal-control gates. |


## 5. 36-Item Forensic Triage Registry & Exact Statistical Protocol

| ID | Class | Title | Layer | Failure Mode / Hazard | Mandatory v3.0 Resolution |
| --- | --- | --- | --- | --- | --- |
| PRB-01 | ◆ PROB | Rigid-Sphere Embodiment Gap | L2 Soft Body | Modeling organisms as rigid circles/spheres eliminates compliant gripping, narrow-gap squeezing, peristalsis, and passive terrain damping. | Build 2D/3D XPBD viscoelastic membrane + `\|ΔV\|/V_0 < 1%` hydrostatic coelom (`SOFT01–SOFT10`). |
| PRB-02 | ◆ PROB | Missing Wet Autopoietic Core | L1 Chemoton | Single scalar `energy` counters lack stoichiometric coupling between metabolism, membrane surface area, and template replication. | Implement Gánti Chemoton (`A`, lipid `T`, polymer `pV_n`) + Michaelis-Menten saturation (`SOFT21–SOFT25`). |
| PRB-03 | ◆ PROB | Missing Sensorimotor Forward Model | L3/L7 Agency | Without an internal efference-copy predictor, self-generated soft-body deformation triggers false external threat/obstacle reflexes. | Wire motor-to-sensory forward predictor (`AE-2`, `M073`) subtracting expected self-reafference. |
| PRB-04 | ◆ PROB | No Metamorphosis / Cell Sorting | L8 Ontogeny | Scalar mass growth omits embryonic cell sorting, apoptotic sculpting, and larval-to-adult body remodeling with memory survival. | Implement Steinberg adhesion, apoptosis, and Blackiston-assay pupal remodeling (`SOFT32–35`, `M084`). |
| PRB-05 | ◆ PROB | Missing Sham & Passive Controls | Sec 5.4 Eval | Comparing Intact only against uncalibrated cuts conflates passive body physics and random damage size with true circuit function. | Require 4 core arms + `Size-Matched Sham Lesion` + `Competent Simple Baseline` (`P6`). |
| PRB-06 | ◆ PROB | Unseparated Weight vs Plasticity RAM | Sec 9 Arena | Counting only packed weight bits hides eligibility queues, consolidation cascades, masks, neuron states, and GPU staging buffers. | Enforce full-process memory inventory separating packed weights from bounded `+0.40 B/syn` plasticity rings (`ALF-004`). |
| ISS-01 | ◈ ISSU | SharedArrayBuffer Origin Isolation | Web Runtime | Browsers disable `SharedArrayBuffer` unless top-level `COOP: same-origin` + `COEP: require-corp` headers establish `crossOriginIsolated`. | Assert `self.crossOriginIsolated === true` at boot (`HW14`); fall back cleanly to double-buffered `postMessage` transfer. |
| ISS-02 | ◈ ISSU | Mobile/Laptop Thermal Throttling | Host Silicon | Sustained SIMD/WebGPU bursts push mobile silicon past 90°C, dropping host clocks and desynchronizing wall-clock assumptions. | Decouple integer `sim_tick` from `wall_time`; drive contiguous Frame-Time Governor (`HW21`) via EMA `ms/frame`. |
| ISS-03 | ◈ ISSU | Spreadsheet 1,048,576-Row Ceiling | Data Export | Dumping raw spike rasters or synapse tables directly into `.xlsx`/`.xls` crashes writers or silently truncates past `1,048,576` rows. | Route full tensors to `Parquet`/`HDF5`; auto-shard `.xls`/`.xlsx` into `≤ 500K`-row summary sheets + manifests. |
| ISS-04 | ◈ ISSU | Multi-Artifact Specification Drift | Governance | Editing PDFs, CSVs, JSON, and workbooks by hand causes IDs, byte totals, and Cube cells to diverge across files. | Generate all 9 output formats (`PDF, JSON, MD, XML, TXT, YAML, HTML, CSV, XLS`) from one canonical v3.0 schema + audit script. |
| ISS-05 | ◈ ISSU | Lossy UI Ring vs Lossless Audit | Data Ops | Sharing one circular buffer between a 60 Hz UI sparkline and scientific benchmark logging drops audit events under burst load. | Separate overwrite-allowed UI telemetry rings (with explicit `gap_count`) from backpressure-safe lossless Export/Audit streams. |
| ISS-06 | ◈ ISSU | Broken Git Worktree Provenance | Repo Hygiene | Copied directories containing broken `.git` pointer files lack object stores, invalidating commit SHA provenance in test manifests. | Gate Stage 0 (`M003`, `GATE-01`) on `git rev-parse --verify HEAD` + clean working-tree manifest hash. |
| DIL-01 | ⚖ DILM | Continuum FEM Fidelity vs Evo Speed | Physics × Evo | High-element 3D continuum FEM (`~50 ms/step`) precludes multi-generation evolutionary sweeps on single workstations. | Ruling: Evolve on fixed-mesh XPBD hydrostats (`0.5 ms` Gear 0); validate selected genotypes in high-resolution continuum. |
| DIL-02 | ⚖ DILM | Cross-OS Bit-Exactness vs GPU Speed | Compute × Lab | Parallel WebGPU/CUDA float reductions are non-associative, preventing bit-identical hashes against sequential CPU code. | Ruling: Tier-1 CPU/WASM canonical mode enforces bit-exact hashes; Tier-2 GPU bulk mode verifies preregistered observable tolerances. |
| DIL-03 | ⚖ DILM | Open-Ended Speciation vs Fixed Floors | Evo × Testing | Locomotor foraging floors unfairly penalize lineages evolving into sessile filter-feeders, ambushers, or decomposers. | Ruling: Enforce universal First-Law + autopoietic viability globally; score behavioral competence per MAP-Elites guild cell. |
| DIL-04 | ⚖ DILM | Compact Indirect GRN vs Mutational Lethality | Devo × Evo | Indirect developmental GRN/NCA encodings compress genomes dramatically but risk catastrophic embryonic instability under point mutation. | Ruling: Canalize embryogenesis via bioelectric polarity clamping (`SOFT37`) and homeostatic `iSTDP`/synaptic scaling (`M045`). |
| DIL-05 | ⚖ DILM | Per-Agent Retina/Cochlea vs Crowd Scale | Senses × HW | Full 2D RGBD retinas for 500 crowd organisms saturate integrated GPU bandwidth, yet changing rays alters Tier-1 trajectory hashes. | Ruling: Keep sensor config fixed for all agents in Tier-1 canonical runs; enable salience-scheduled crowd LOD strictly in Tier-2. |
| DIL-06 | ⚖ DILM | Live Hardware Sensors vs Repeatability | Omnisensor | Live webcam/microphone/IMU inputs provide genuine open-world entropy but cannot repeat deterministically across CI runs. | Ruling: Explore live in Practice mode while recording immutable timestamped `.sensorlog` streams replayed bit-exactly in Test gates. |
| ERR-01 | ⚠ ERR | 24 GB/s Naive Live Synapse Streaming | Telemetry Spec | Streaming `10^8 × 4 B × 60 Hz = 24 GB/s` across threads violates memory-bus budgets and stalls simulation workers. | Corrected: Stream `O(1)` statistical sketches (`≤ 32 KB/fr`) globally; pull subgraph slices on demand (`2 Hz`) for inspected organs. |
| ERR-02 | ⚠ ERR | Full 825-Suite Per Online WSE Edit | WSE-10 Spec | Running full held-out benchmark suites on every millisecond in-life `WSE` plasticity edit freezes runtime execution. | Corrected: 3-Tier WSE Gate—Tier-0 `O(1)` induced-norm `‖W‖_2 ≤ 0.99` + ATP check online, Tier-1 sleep shadow rollout, Tier-2 promotion. |
| ERR-03 | ⚠ ERR | Underpowered & Mislabeled FDR Stats | Scoreboard | Conflating Holm-Bonferroni FWER with FDR `q`-values or claiming `N=16` powers 100-item medium-effect families invites false claims. | Corrected: Exact paired Wilcoxon/sign-flip + **Holm-Bonferroni FWER (`α ≤ 0.05`)**, power-sized `N` (`24..120`), `δ_pair`, and `LCB_95% > -Δ_NI`. |
| ERR-04 | ⚠ ERR | Z-Blind 2D Cube Compatibility | Sec 7.5 Cube | Scoring `Model × Precision` while ignoring `Geometry Z` misses hyperbolic (`Z4`), attractor (`Z5`), and steerable (`Z6`) low-bit failures. | Corrected: Full 3-axis `evaluateCubeCell(X, Y, Z)` with grayscale-safe `[OK] / [OVER] / [ADAPT] / [EXCL]` synced across PDF & CSV/XLS. |
| ERR-05 | ⚠ ERR | Shared PRNG & World-Entity Coupling | Lesion Method | Drawing random numbers sequentially or failing to isolate world weather from creature organs scrambles trajectories upon ablation. | Corrected: `Philox4x32-10` keyed by `(ver, seed, domain, entity, organ, tick, purpose, idx)` isolating `WORLD_EXOG` from `ENTITY_INT`. |
| ERR-06 | ⚠ ERR | Circular Parameter Count & Exact-Φ Claims | Anti-LARP | Equating parameter count with competence or claiming exact `O(2^N)` IIT `Φ` on large brains is scientifically invalid. | Corrected: Require forked-snapshot perturbational `PCI*` (`F2`), `C-NC` causal divergence, and Competent Simple Baselines. |
| BUG-01 | ✖ BUG | Cross-OS libm Transcendental ULP Drift | L0 Determinism | Host `Math.exp`/`Math.log`/`Math.tanh` implementations vary by `1–2 ULP` across OS/browser engines, breaking bit-exact hashes. | Ship core-owned versioned deterministic minimax/LUT `exp_det`, `log_det`, `pow_det`, and `tanh_det` in Tier-1 runtime. |
| BUG-02 | ✖ BUG | Explicit Euler Soft-Spring Explosion & Free Energy | Soft Physics | Explicit Euler explodes on stiff membranes, while unmonitored XPBD constraint projections can inject or dissipate unbooked energy. | Use XPBD (`α̃ = α/dt²`) + book positive solver damping to `E_diss_num ≥ 0` and fault on `ΔE_diss_num < -1e-15`. |
| BUG-03 | ✖ BUG | FP32 Small-Addend Absorption in Ledger | First-Law Pool | Adding `1e-6 kJ` spike heat to a `1e5 kJ` dome heat accumulator in `FP32` (`24` mantissa bits) rounds the increment completely to `0`. | Accumulate all 11 enthalpy/mass pools in `FP64` with Kahan-Neumaier compensation (`\|ΔE\|/(E0+Ein) < 1e-12`). |
| BUG-04 | ✖ BUG | JS 32-Bit Shift Wraparound (`1 << 32 === 1`) | Quantum Organ | In JS/C-style 32-bit shifts, `1 << Q` masks `Q & 31` (`Q=32` allocates 2 floats instead of guarding, while `Q=30` overflows signed int32!). | Validate `Number.isInteger(Q) && Q >= 0 && Q <= 10` first, then allocate `2 * (2 ** Q)` `Float64` values (`≤ 16 KiB`). |
| BUG-05 | ✖ BUG | Per-Tick Closures, BigInt Box & WASM Grow | Runtime Loop | Temporary closures, `BigInt` boxing in JS PRNGs, or dynamic WASM `memory.grow` inside `tick()` trigger latency spikes and view invalidation. | Pre-allocate fixed SoA arenas; use `Math.imul` 32-bit `Philox4x32-10`; assert `0` allocs & `0` page grows across `10,000` ticks. |
| BUG-06 | ✖ BUG | Lesion Toggle Resurrecting Pruned Wires | Ablation Code | Restoring a reversible lesion by setting mask bits to `1` overwrites `0`s created by developmental or sleep pruning. | Maintain orthogonal `structuralMask` (ontogeny/sleep) and `lesionMask` (assay), applying `effectiveMask = structuralMask & lesionMask`. |
| CNF-01 | ⚡ CONF | Epistemic Curiosity vs Starvation Urgency | Drive Arbiter | Additive novelty bonuses overpower homeostatic error when fuel runs low, causing starving organisms to inspect noisy traps. | Multiplicative Urgency Gate: weight epistemic value by sigmoid survival margin `σ((TTC - TTC_crit)/τ)`. |
| CNF-02 | ⚡ CONF | In-Life WSE Surgery vs Autonomic Survival | WSE / Brainstem | Self-editing operators optimizing short-horizon reward silence nociceptors, cardiac pacemakers, or metabolic accounting. | Hardware-enforced Protection Rings: `Ring-0` (`brainstem, nociception, ledger, harness`) uses frozen read-only views. |
| CNF-03 | ⚡ CONF | Cuticle Armor Stiffening vs Squeeze/Speed | Soft Bauplan | Inducible cuticle thickening shields against toxins/bites but raises bending energy, mass, and narrow-aperture failure. | Expose as regulated endocrine/catch-state trade-off (`SOFT04`) modulated by predator/toxin threat cues. |
| CNF-04 | ⚡ CONF | Fast Hebbian LTP vs Recurrent Runaway | Spiking Cortex | Positive Hebbian loops without rapid counterbalance saturate firing rates or collapse into epileptic synchrony. | Couple 3-factor LTP with fast inhibitory `iSTDP`, sliding BCM threshold, `‖W‖_2 ≤ 0.99` guard, and NREM `SHY`. |
| CNF-05 | ⚡ CONF | Exotic Field Senses vs Anti-LARP Physics | World Boundary | Simulated bioelectric or distant-sensing channels degenerate into zero-cost oracle cheats if unattenuated. | Mediate every exotic sense through inverse-distance noisy in-world fields with strict per-bit ATP debit and shuffle controls. |
| CNF-06 | ⚡ CONF | Concurrent Multi-Organ State Write Races | Coupling Bus | Sleep flip-flop, HPA cortisol, and workspace writing shared `arousal` in arbitrary order produce order-dependent oscillations. | Single-writer variable ownership + canonical deterministic reducer over double-buffered `prevTick -> nextTick` state. |


- **Primary Paired Test:** Two-sided or preregistered directional exact paired Wilcoxon signed-rank / 2^N sign-flip permutation test on locked seed pairs d_i = Y_intact(s_i) - Y_ctrl(s_i).
- **Effect Size:** Within-pair dominance δ_pair = (count(d_i > 0) - count(d_i < 0)) / N_pairs (reported alongside unpaired Cliff's δ for archival cross-lineage comparisons); default threshold δ_pair ≥ 0.33 (medium) or ≥ 0.50 (structural gates).
- **Multiplicity Control:** Holm-Bonferroni step-down Family-Wise Error Rate (FWER) control at α_FWER ≤ 0.05 within each checklist family (reports p_raw and p_Holm; never mislabeled as false-discovery rate).
- **Burn-on-Fail Hygiene:** Any Locked Held-Out Test seed block evaluated on a failed promotion attempt is permanently retired to `Historical-Audit` and replaced by a fresh unseen seed block (`≥ 5000 + offset`) before re-testing.

| Checklist Family Tier | Paired Seeds | Power & Resolution Rule |
| --- | --- | --- |
| Small Suite / Large Effect (m ≤ 25: WSE-12, Butlin-14, F10, HW-24, CQM-25) | N_pairs ≥ 24 | Min achievable two-sided sign-flip p = 1.19e-7; clears Holm α/25 = 0.002 at ≥85% power for δ_pair ≥ 0.55. |
| Medium Suite / Strong Effect (m = 40–100: SOFT-40, FREAK-100, NOVEL-100) | N_pairs ≥ 48–64 | Clears Holm α/100 = 0.0005 for strong physiological/ablation effects (δ_pair ≥ 0.50). |
| Large Suite / Moderate Behavioral Effect (m = 100–500: subtle cognition/ecology) | N_pairs = 96–120 | Sample-size set from Tuning-seed variance pilot; underpowered tests report `Inconclusive ◌` (never Fail or Pass). |


## 6. 19-Tab Master Center, WSE Algebra, 75 Substrates & 10×10×10 Hybrid Cube

| Tab | Panel Name | Telemetry & Read-Only Tier-1 Scope | Transport · Hz · Budget |
| --- | --- | --- | --- |
| Tab 01 | Executive Overview & Vital Signs | Dome population, FPS/Governor band, First-Law residual `\|ΔE\|/(E0+Ein)`, active seed range (`Practice 100–999`), and `0/825` clean-slate scoreboard. | SAB SeqLock · 10 Hz · 0.5 KB/fr |
| Tab 02 | 2D / 3D Biosphere & Field Map | Interactive dome viewport with solar, thermal, odor plume, acoustic wake, slime trail, and detritus grid overlays. | SAB Decimated · 30 Hz · 16 KB/fr |
| Tab 03 | Soft Body, Strain & Morphology | Focal organism XPBD viscoelastic mesh, chamber pressures `P_1..P_k`, catch-state stiffness, tear/clot plugs, and compliance metrics. | Focal Pull · 30 Hz · 4.0 KB/fr |
| Tab 04 | Live Brain Activity & Wave Sheet | Topographic spike raster, somatic `V_m`, `sLTC` time-constant map `τ(x)`, traveling waves, and PV+ gamma phase coherence. | Focal Slice · 20 Hz · 8.0 KB/fr |
| Tab 05 | 3D Connectome & Precision Inspector | On-demand 3D wiring subgraph colored by precision (`PM01–PM25`), `structuralMask & lesionMask`, and `S2S` bridge gain. | Pull Snapshot · 2 Hz · ≤32 KB |
| Tab 06 | Omnimodal Sensorium & Efference | Focal foveal retina, parallax depth rays, bilateral plume bars, cochlear filterbank, skin shear sheet, and efference residual. | Focal Bus · 20 Hz · 6.0 KB/fr |
| Tab 07 | Chemoton & 11-Pool First-Law Sankey | Live compensated `FP64` Sankey (`Solar -> Patch -> Gut -> Blood -> Stores -> ATP -> Work + E_heat_phys + E_diss_num`) & glycemic error. | SAB SeqLock · 10 Hz · 1.0 KB/fr |
| Tab 08 | Memory, Hopfield & Sleep Replay | Theta-gamma 4-slot WM, `2%` SDR sparsity, Hopfield cue cosine, NREM prioritized replay log, and REM uncertainty tag audit. | Lossy UI Ring · 10 Hz · 2.0 KB/fr |
| Tab 09 | Global Workspace, HOT & Geodesic Plan | Up-tree ignition race, lags 2–5 blink curve, `AST` gaze vectors, `HOT` Brier calibration plot, and danger-geodesic detour overlay. | Gear-2 Ring · 20 Hz · 3.0 KB/fr |
| Tab 10 | Affective Interior & Neuromodulators | 4-timescale emotion/mood/attitude/temperament traces, 7 precursor-limited neuromodulators, and trajectory-curvature caution. | Gear-2/3 · 10 Hz · 1.5 KB/fr |
| Tab 11 | Genome, GRN, Ontogeny & Metamorphosis | GRN activation heatmap, mitotic lineage tree, stage badge (`Zygote..Elder`), and Blackiston metamorphosis memory retention. | Gear-4 Event · 1 Hz · 2.0 KB/s |
| Tab 12 | Social Graph, Culture & Trophic Web | MHC kinship graph, ATP-honest call spectrograms, dialect PCA clusters, recessed stone caches, and 3-guild population curves. | Summary Ring · 2 Hz · 4.0 KB/s |
| Tab 13 | 9-Suite Statistical Benchmark Runner | Status (`☐/◐/◔/✔/🔒`) across `825` checks + `M001–M100`, paired `N`, `δ_pair`, `p_raw`, **Holm-Bonferroni FWER `p_Holm`**, and `LCB_95%`. | Async Worker · On-Run · Lossless |
| Tab 14 | Multi-Arm & Lineage Trajectory Diff | Synchronized replay comparing `Intact vs Passive-Body vs Shuffled vs Targeted-Lesion vs Sham-Lesion` on identical locked seeds. | Replay Worker · 30 Hz · Pull |
| Tab 15 | Forensic P / I / D / E / B / C Console | Live invariant alerts for First-Law drift, `E_diss_num < 0`, `SeqLock` retries, ring drops, conflict seesaws, and triage logs. | Lossless Event · 5 Hz · 1.0 KB/s |
| Tab 16 | Deterministic Time-Machine & `.alifebin` | Canonical `.alifebin` checkpoints, `<64 KB` XOR diffs, scrub/branch sandbox, and immutable `.sensorlog` replay verification. | Snapshot Worker · On-Demand |
| Tab 17 | Interactive Perturbation & WSE Lab | Practice-mode `lesion()`, `shamLesion()`, `stimulate()`, dome dials, and `Ring-0`-guarded `WSE-OP01..10` surgery (disabled in Test!). | Cmd Ring · Event · <0.5 KB |
| Tab 18 | Lossless Sharded Data Exporter | Decoupled lossless export ring streaming `Parquet`, `HDF5`, `DuckDB`, `NPZ`, `CSV`, and auto-sharded `<500K-row` `XLS/XLSX` workbooks. | Export Worker · Async Chunked |
| Tab 19 | Hardware, Arena & Governor Profiler | Live weight vs plasticity vs state arena MB, `10,000`-tick alloc counter (`=0`), Gear `0..4` ms/frame, `SeqLock` gap count, and Governor band. | Perf Ring · 10 Hz · 0.5 KB/fr |


### 6.1 Typed Weight-Space Editing Algebra (`WSE-OP01..10`)

| Op ID | Operator | Target Arena | Preconditions | Safety Tier |
| --- | --- | --- | --- | --- |
| WSE-OP01 | SetWeight / ScaleBlock | CSR / Packed Block | Scale/update Ring-1/2 weights; enforce contractive induced norm `‖W‖_2 ≤ 0.99` (power-iteration bound). | Tier-0 (<0.1ms) + ATP debit |
| WSE-OP02 | Prune / Grow | Structural Mask | Toggle `structuralMask` (separate from `lesionMask`); preserve sensor-to-motor reachability. | Tier-1 shadow rollout |
| WSE-OP03 | Rewire | CSR + Overlay Graph | Redirect edge within 3D cable budget; writes to explicit CSR delta overlay if base block is procedural. | Tier-1 shadow rollout |
| WSE-OP04 | PaintBiasField / ShiftBias | Sheet Excitability | Smooth spatial threshold/gain field over neural sheet keeping firing rate within `[0, r_max]`. | Tier-0 rate + NaN guard |
| WSE-OP05 | Move / ReEmbed | 3D / Manifold Coords | Shift unit coordinates, recompute integer axonal delays & Cajal wire rent; update CSR overlay. | Tier-1 shadow rollout |
| WSE-OP06 | Bind / Unbind / Reweight | VSA / Hopfield Memory | Insert, unbind, or reweight associative role-filler vectors with norm renormalization. | Tier-0 norm + cosine check |
| WSE-OP07 | Requantise | Module Precision | Transition Ring-1/2 organ precision (e.g. `FP16 -> int4` via keyed stochastic rounding + S2S update). | Tier-1 drift ≤ ε_quant |
| WSE-OP08 | Constrain | Manifold Projection | Project matrix onto Dale's-law sign mask, zero-row-sum, or orthogonal/spectral ball `‖W‖_2 ≤ 0.99`. | Tier-0 exact projection |
| WSE-OP09 | Merge / Split / Graft | Specialist Spheres | Fork/fuse Ring-1 modules or apply MHC-verified horizontal plasmid graft (when niche-enabled). | Tier-2 full non-inferiority |
| WSE-OP10 | Freeze / Unfreeze | Protection Ring ACL | Consolidate plastic skill masks; `Ring-0` brainstem, nociception & First-Law ledger permanently read-only. | Tier-0 hardware ACL |


### 6.2 25 Numeric Precisions (`PM01–PM25`), 25 Model Families (`MF01–MF25`) & 25 Geometries (`GW01–GW25`)

| ID | Precision | Storage | vs FP32 | Role | Backend | Scope |
| --- | --- | --- | --- | --- | --- | --- |
| PM01 | Sub-1-bit VQ Codebook Weights | < 1 bit | 32–64× | Tier-1 SW Codec | SW LUT (JS/WASM/WGSL) | Codebook-shared crowd reflex weights; indices + LUT budgeted explicitly. |
| PM02 | Binary Weights (+1 / -1) | 1 bit | 32× | Tier-1 SW Bitpack | u32 XNOR+popcnt | Ultra-fast bipolar VSA & all-or-none axonal gating; FP32/int32 accumulator. |
| PM03 | Ternary (BitNet b1.58: {-1,0,+1}) | 1.60b (5 trits/B) | 20× raw (15.6× CSR) | Tier-1 SW Bitpack | 5-trit/u8 codec | Excitatory (+1), pruned (0), inhibitory (-1) packed weights; zero multiplies. |
| PM04 | int2 / int3 Group-Scaled | 2–3 bits | 10.7–16× | Tier-1 SW Bitpack | Bit-shift unpack | Compact segmental soft-body CPG motor weights with FP16 block scale. |
| PM05 | int4 Symmetric/Asymmetric Group | 4b (0.875 B blk) | 8× raw (10.6× CSR) | Tier-1 SW Bitpack | u32 nibble unpack | Primary compact storage for peripheral ganglia & sensory fan-out. |
| PM06 | NF4 (4-bit NormalFloat LUT) | 4 bits + scale | 8× raw | Tier-1 SW LUT | 16-entry FP16/32 LUT | Quantile-spaced 4-bit levels matched to bell-curved biological weights. |
| PM07 | FP4 (OCP E2M1 Microfloat) | 4 bits | 8× raw | Tier-2 GPU/SW | Blackwell native / SW | High-density Tier-2 crowd forward passes; requires group scale. |
| PM08 | MXFP4 (32-elem + E8M0 shared exp) | 4.25 bits | 7.5× | Tier-2 GPU/SW | OCP GPU / SW unpack | Shared 8-bit exponent acts like local cortical column gain. |
| PM09 | int6 / FP6 (E3M2 / E2M3) | 6 bits | 5.3× | Tier-2 SW/GPU | Bitpack codec | Intermediate precision for recurrent reservoirs sensitive to 4-bit quantization. |
| PM10 | int8 / Q0.7 Symmetric Integer | 8 bits (1 B) | 4.0× | Tier-1 Native | Int8Array / i32 dot | Cross-platform bit-exact specialist weights; accumulates into int32/FP32. |
| PM11 | FP8 E4M3 (4 exp, 3 mantissa) | 8 bits (1 B) | 4.0× | Tier-2 GPU/SW | Hopper+ CUDA / SW | Forward activations in Tier-2 GPU cortices; SW codec on WebGPU. |
| PM12 | FP8 E5M2 (5 exp, 2 mantissa) | 8 bits (1 B) | 4.0× | Tier-2 GPU/SW | Hopper+ CUDA / SW | Wider exponent range for prediction-error & eligibility transients. |
| PM13 | MXFP8 (32-elem + E8M0 shared exp) | 8.25 bits | 3.9× | Tier-2 GPU/SW | OCP GPU / SW | Block-scaled 8-bit online plasticity in workstation dGPU runs. |
| PM14 | FP16 (IEEE-754 binary16) | 16 bits (2 B) | 2.0× | Tier-2 Opt. GPU | Float16Array / WGSL f16* | Soft-tissue fields & CSR weights (*WGSL `shader-f16` capability probe required). |
| PM15 | BF16 (bfloat16: 8 exp, 7 mant) | 16 bits (2 B) | 2.0× | Tier-2 GPU/SW | CUDA/CPU native; WGSL SW | FP32-like exponent range for workspace states; finite/NaN guards still required. |
| PM16 | TF32 (19-bit TensorCore math mode) | 32b store (19b math) | 1.0× (No RAM save!) | Tier-2 CUDA Only | NVIDIA TensorCore | Accelerates FP32 matmuls on Ampere+ GPUs; occupies full 32-bit storage (`ALF-006`). |
| PM17 | FP32 / Q16.16 Fixed-Point State | 32 bits (4 B) | 1.0× (Reference) | Tier-1 Canonical | Float32/Int32 Native | Canonical kinematics/membrane state (`Q16.16` for integer lockstep; never for kJ ledger). |
| PM18 | FP64 + Kahan-Neumaier Compensation | 64 bits (8 B) | 0.5× | Tier-1 Mandatory | Float64Array / WASM f64 | MANDATORY for all 11 First-Law enthalpy/mass pools (`\|ΔE\|/(E0+Ein) < 1e-12`; WGSL lacks f64). |
| PM19 | Posit8 / Posit16 Tapered Float | 8–16 bits | 2–4× | Tier-1 SW Codec | Software LUT/ALU | Concentrates significand bits near unity around homeostatic set-points. |
| PM20 | Logarithmic Number System (LNS) | 8–16 bits | 2–4× | Tier-1 SW Codec | Software LUT/Add | Matches Weber-Fechner sensory compression; turns products into fixed-point adds. |
| PM21 | [Modifier] Keyed Stochastic Rounding | +Philox draw | Modifier (0× own) | Tier-1 Keyed-Det | SW quantizer op | Quantization operator (not a storage type) preventing small Δw stagnation in 4–8b formats. |
| PM22 | Block Floating Point (BFP-8/4) | 4–8b + 8b exp | 3.8–7.5× | Tier-1 SW/SIMD | Int SIMD + shift | Integer SIMD dot products across shared-exponent cortical minicolumns. |
| PM23 | [Model] Noisy Analog / Drift Channel | FP16/32 + noise | 1–2× | Tier-1 Keyed-Det | Keyed Langevin step | Simulates wet ion-channel shot noise & conductance drift under keyed PRNG. |
| PM24 | [Coding] Sparse AER Spike Events | 32b (id+tick) | Event-proportional | Tier-1 Canonical | Uint32 ring queue | Zero synaptic propagation work while silent (basal membrane leak/pump ATP still ticks). |
| PM25 | [Policy] Heterogeneous Multi-Precision | 1.6b–64b | 6–14× (Workload) | Tier-1/2 Hybrid | Typed S2S bridges | Per-organ assignment: b1.58/int4 limbs + int8 cortex + FP32 mind + FP64 ledger. |


| ID | Model Family | Step Complexity | Mechanism |
| --- | --- | --- | --- |
| MF01 | Spiking Neural Networks (LIF / Izhikevich / AdEx) | O(N_units + k·E_syn) | Event-driven sparse spikes (`k ≈ 1–4%`), refractory timing, STDP, and per-spike ATP debit. |
| MF02 | Liquid Time-Constant (LTC) ODE Networks | O(K_iter·E_syn) | State- and input-modulated conductance `τ(x,I)` integrated via `K_iter` bounded substeps. |
| MF03 | Closed-Form Continuous-Time (CfC) Networks | O(E_syn) | Bounded analytical approximation to LTC trajectories—eliminates stiff neural ODE sub-stepping. |
| MF04 | Spiking Liquid Time-Constant (sLTC, Vanhalle & Gielen 2025) | O(N_units + k·E_syn) | Adaptive liquid time constants + sparse spikes (up to 9.2× lower energy vs LTC on benchmark tasks). |
| MF05 | Liquid State / Echo-State Reservoirs (LSM / FORCE) | O(E_syn + D_lat²) | Fixed spectral-clamped sparse recurrent pool (`‖W‖_2 ≤ 0.99`) with fast plastic linear/FORCE readout. |
| MF06 | Structured State-Space Models (S4 / Diagonal Linear RNN) | O(N_units) | Long-horizon temporal memory across thousands of ticks with `O(1)` recurrent state update per unit. |
| MF07 | Selective State-Space (Mamba-style Input-Gated SSM) | O(N_units·D_lat) | Content-selective input gates decide which sensory surprises write into persistent recurrent state. |
| MF08 | Latent Predictive World Models (RSSM / JEPA) | O(D_lat²) | Forecasts compact visceral + exteroceptive embeddings (never raw pixels) for rollout planning. |
| MF09 | Modern Continuous Hopfield Associative Memory | O(M_pat·D_lat) | Exponential pattern capacity retrieving full episodes from `≥ 50%` occluded cues in 1–3 settling steps. |
| MF10 | Kolmogorov-Arnold Spline/LUT Networks (KAN) | O(E_syn·G_sp) | Piecewise-polynomial/LUT univariate edge functions for compact, interpretable visceral control laws. |
| MF11 | Continuous Neural ODEs / Langevin Neural SDEs | O(K_iter·E_syn) | Continuous vector fields coupling physiology and neural state (requires multi-bit precision ≥ FP16). |
| MF12 | Developmental Hypernetworks / Coordinate CPPNs | O(G_gen·E_macro) | Compact genome queries 3D tissue coordinates `(x,y,z,d)` at developmental milestones (Gear 4). |
| MF13 | Sparse Top-k Mixture-of-Experts (MoE Specialist Router) | O(k_exp·E_expert) | Activates only `k_exp = 1..2` specialist spheres per step, decoupling capacity from per-tick FLOPs. |
| MF14 | Neural Cellular Automata (NCA) & Chemoton Tissue Grids | O(Cells) | Local neighbor signaling grows, polarizes, and regenerates multicellular soft soma after injury. |
| MF15 | Hierarchical Predictive Coding / Active Inference | O(L_lay·D_lat²) | Top-down predictions cancel expected sensory input; precision-weighted residuals drive belief & action. |
| MF16 | Multi-Compartment Apical-Basal Dendritic Units (dCaAP) | O(B_comp·N_units) | Segregated basal drive + apical context calcium plateaus solving single-cell XOR (Gidon et al. 2020). |
| MF17 | Three-Factor Eligibility + BTSP Plateau Plasticity | O(k·E_syn) | Decaying `pre × post` tags converted to weight updates on delayed phasic neuromodulator/plateau arrival. |
| MF18 | Constant-Memory Gated Recurrence (xLSTM / RWKV-lite) | O(D_lat²) | Matrix-valued recurrent memory cells maintaining constant `O(1)` step cost over unbounded lifetimes. |
| MF19 | Part-Whole Pose Capsule / Frame Networks | O(C_caps²·D_pose) | Tracks object-to-body and segment-to-segment coordinate frames across viewpoint/posture shifts. |
| MF20 | Message-Passing Graph Neural Networks (Morphology GNN) | O(E_body) | Propagates tension, perfusion, and proprioception natively over variable-limb soft body graphs. |
| MF21 | Energy-Based Settling Networks (Ising / Equilibrium) | O(K_iter·E_syn) | Relaxes fast threat/posture constraints on a bounded Lyapunov energy surface (`K_iter ≤ 8`). |
| MF22 | 2-Step Consistency / Flow-Matching Motor Policies | O(2·D_pol²) | Generates smooth multimodal soft-continuum obstacle-avoidance trajectories in 2 fixed denoiser steps. |
| MF23 | Hyperdimensional / Vector-Symbolic Algebras (VSA / MAP) | O(D_lat) | SIMD bitwise/XOR/permutation role-filler binding over `1,024–4,096d` bipolar/ternary vectors. |
| MF24 | Event-Driven Address-Event Neuromorphic Cores (AER) | O(k·E_syn) | Asynchronous event queues touching outgoing edges strictly on threshold crossings. |
| MF25 | Multi-Scale Frankenstein Organ Hybrids | Sum(Sub-organs) | Principled composition: NCA/XPBD soma + int4 CfC ganglia + sLTC/Hopfield/Workspace central brain. |


| ID | Geometry / Topology | Inductive Bias & Grounding |
| --- | --- | --- |
| GW01 | Typed Metric Vector Spaces | Explicit unit-tagged coordinate spaces linking transducers, latents, and motor targets. |
| GW02 | Bilateral / Radial Group-Symmetric Wiring | Mirrors paired left-right or radial soft-segment circuits from one compact genomic specification. |
| GW03 | Clifford (Geometric) Algebra Rotors | Encodes 2D/3D orientations, bivector torques, and soft-segment bends without gimbal singularities. |
| GW04 | Hyperbolic (Poincaré / Lorentz) Manifolds | Embeds exponential phylogenetic, taxonomic, and subgoal trees cleanly (requires FP16/FP32 adapter). |
| GW05 | Spherical & Toroidal Phase Manifolds | Wrap-around topology for compass headings, circadian phases, and multi-limb gait oscillators. |
| GW06 | Contractive Induced-Norm Manifolds (`‖W‖_2 ≤ 0.99`) | Bounds singular values (`‖W‖_2 ≤ 0.99`, implying `ρ(W) ≤ 0.99`) to prevent transient & asymptotic blowup. |
| GW07 | 3D Distance-Delay Tissue Wiring | Axonal connection probability, metabolic wire rent, and integer spike delay scale with 3D tissue distance. |
| GW08 | Watts-Strogatz Small-World Connectomes | High local clustering plus sparse long-range shortcuts yielding `O(log N)` broadcast at low cable volume. |
| GW09 | Scale-Free Rich-Club Hub Networks | Heavy-tailed hub architecture supporting targeted hub-vs-periphery lesion resilience assays. |
| GW10 | Hub-and-Sphere Modular Bottlenecks | Dense specialist spheres communicating exclusively through capacity-limited workspace/thalamic hubs. |
| GW11 | Recursive L-System Vascular & Axonal Trees | Self-similar branching rules growing perfusion vessels and peripheral nerve trunks from tiny genomes. |
| GW12 | Persistent Homology (Betti-0/1/2 Signatures) | Diagnostic topological audit of ring attractors, toroidal maps, and soft-cavity loops. |
| GW13 | SE(2) / SE(3) Equivariant Steerable Kernels | Guarantees rotational/translational equivariance for local tactile/odor/visual feature detectors (≥int8/FP16). |
| GW14 | Cellular Sheaf Consensus Maps | Linear edge restriction maps reconciling disagreements across heterogeneous sensory coordinate frames. |
| GW15 | Sinkhorn Optimal-Transport Somatotopy | Smoothly remaps variable-node larval/adult skin and retina sheets onto fixed cortical arrays. |
| GW16 | Corecursive Stream Coalgebra Interfaces | Formalizes open-ended organism-environment step transitions as typed `(State × Input) -> (State × Output)`. |
| GW17 | Decursive Self-Deduplication (DSD) | Alex Donahue's reserved novel concept (preserved verbatim as author-defined slot per specification). |
| GW18 | Juvenile Overproduction & Sleep Pruning | Synaptogenesis overshoot followed by size-scaled NREM activity-dependent pruning and waking re-sprout. |
| GW19 | Amari Mexican-Hat Neural & Morphogen Fields | Local excitation + surround inhibition sheets driving spatial attention peaks and Turing skin patterns. |
| GW20 | Holographic Reduced Representations (HRR) | Circular-convolution binding (`O(D log D)` FFT or `O(D)` permutations) for compositional symbol structures. |
| GW21 | Continuous Attractor Bump Sheets (Ring / Hex) | Translation-invariant recurrent sheets integrating velocity into dead-reckoned heading and place bumps. |
| GW22 | k-WTA Sparse Distributed Representations (2% SDR) | Top-2% winner-take-all expansion (clean-slate design target inspired by 5–10% fly Kenyon sparsity). |
| GW23 | Ramon-y-Cajal Wiring-Volume Minimization | Co-evolves ganglion placement inside the soft body to minimize `Sum(weight_volume × distance)` ATP rent. |
| GW24 | Simplicial / Hypergraph Triadic Couplings | Captures 3-way neuron-astrocyte-modulator gates and multi-agent social coalitions natively. |
| GW25 | Nested Brains-Within-Brains + Typed S2S Bridges | Multi-level hierarchy (`b1.58/int4` limbs -> `int8` cortex -> `BF16/FP32` mind) linked by `S2S` adapters. |


### 6.3 Five Proposed Reference Starter Configurations & 1,000-Cell Compatibility Atlas

| Organ Slot | Cell | Triple | Badge | Functional Role |
| --- | --- | --- | --- | --- |
| T1 Peripheral Ganglion | X1Y2Z1 | CfC × int4 Group × 3D Distance-Delay | [OK] | Fast segmental motor/visceral reflexes surviving central brain ablation. |
| T2 Sparse Sensory Cortex | X2Y1Z2 | sLTC × Ternary b1.58 × Small-World | [OK] | Ultra-compact event-driven cortical sheet (`0.594 B/syn` packed block). |
| T3 Episodic Hippocampus | X4Y5Z7 | Modern Hopfield × int8 × 2% k-WTA SDR | [OK] | High-capacity cue completion from ≥50% masked episodes without float drift. |
| T4 Central Workspace | X7Y7Z3 | Active-Inf PC × FP16/BF16 × Hub-Sphere | [OK] | Precision-weighted global ignition, AST gaze model, and HOT confidence. |
| T5 Regenerative Soma | X9Y8Z1 | NCA/Chemoton × FP32/Q16.16 × 3D Local | [OK] | Multicellular morphogenesis & Chemoton homeostasis (coupled to FP64 ledger). |


- **1,000-Cell Summary:** `[OK] = 661`, `[OVER] = 20`, `[ADAPT] = 274`, `[EXCL] = 45`

#### Slice Z0: Metric Vector Sheet

| Y \ X | X0 | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 | X9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y0 | [OK] | [OK] | [OK] | [ADAPT] | [ADAPT] | [EXCL] | [OK] | [ADAPT] | [OK] | [ADAPT] |
| Y1 | [OK] | [OK] | [OK] | [ADAPT] | [ADAPT] | [ADAPT] | [OK] | [ADAPT] | [OK] | [ADAPT] |
| Y2 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y3 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y4 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y5 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y6 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y7 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y8 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y9 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |

#### Slice Z1: 3D Distance-Delay Wiring

| Y \ X | X0 | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 | X9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y0 | [OK] | [OK] | [OK] | [ADAPT] | [ADAPT] | [EXCL] | [OK] | [ADAPT] | [OK] | [ADAPT] |
| Y1 | [OK] | [OK] | [OK] | [ADAPT] | [ADAPT] | [ADAPT] | [OK] | [ADAPT] | [OK] | [ADAPT] |
| Y2 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y3 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y4 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y5 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y6 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y7 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y8 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y9 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |

#### Slice Z2: Watts-Strogatz Small-World

| Y \ X | X0 | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 | X9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y0 | [OK] | [OK] | [OK] | [ADAPT] | [ADAPT] | [EXCL] | [OK] | [ADAPT] | [OK] | [ADAPT] |
| Y1 | [OK] | [OK] | [OK] | [ADAPT] | [ADAPT] | [ADAPT] | [OK] | [ADAPT] | [OK] | [ADAPT] |
| Y2 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y3 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y4 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y5 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y6 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y7 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y8 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y9 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |

#### Slice Z3: Hub-and-Sphere Modular

| Y \ X | X0 | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 | X9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y0 | [OK] | [OK] | [OK] | [ADAPT] | [ADAPT] | [EXCL] | [OK] | [ADAPT] | [OK] | [ADAPT] |
| Y1 | [OK] | [OK] | [OK] | [ADAPT] | [ADAPT] | [ADAPT] | [OK] | [ADAPT] | [OK] | [ADAPT] |
| Y2 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y3 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y4 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y5 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y6 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y7 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y8 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y9 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |

#### Slice Z4: Hyperbolic Tree Manifold

| Y \ X | X0 | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 | X9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y0 | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] |
| Y1 | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] |
| Y2 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y3 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y4 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y5 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y6 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y7 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y8 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y9 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |

#### Slice Z5: Toroidal / Ring Attractor

| Y \ X | X0 | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 | X9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y0 | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [OK] | [EXCL] |
| Y1 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [OK] | [ADAPT] |
| Y2 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [OK] | [ADAPT] |
| Y3 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y4 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y5 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y6 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y7 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y8 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y9 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |

#### Slice Z6: SE(2)/SE(3) Steerable

| Y \ X | X0 | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 | X9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y0 | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [EXCL] | [ADAPT] | [EXCL] |
| Y1 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y2 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y3 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y4 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y5 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y6 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y7 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y8 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y9 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |

#### Slice Z7: k-WTA 2% Sparse SDR

| Y \ X | X0 | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 | X9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y0 | [OK] | [OK] | [OK] | [ADAPT] | [ADAPT] | [EXCL] | [OK] | [ADAPT] | [OK] | [ADAPT] |
| Y1 | [OK] | [OK] | [OK] | [ADAPT] | [ADAPT] | [ADAPT] | [OK] | [ADAPT] | [OK] | [ADAPT] |
| Y2 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y3 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y4 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y5 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y6 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y7 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y8 | [OVER] | [OK] | [OVER] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y9 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |

#### Slice Z8: Sleep-Pruned Dynamic Graph

| Y \ X | X0 | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 | X9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y0 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [EXCL] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y1 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y2 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y3 | [OK] | [OK] | [OK] | [OK] | [OK] | [ADAPT] | [OK] | [OK] | [OK] | [OK] |
| Y4 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y5 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y6 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |
| Y7 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y8 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OVER] | [OK] |
| Y9 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |

#### Slice Z9: Nested Brains-in-Brains

| Y \ X | X0 | X1 | X2 | X3 | X4 | X5 | X6 | X7 | X8 | X9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y0 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [EXCL] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y1 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y2 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y3 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y4 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y5 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y6 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y7 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y8 | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] | [ADAPT] |
| Y9 | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] | [OK] |



## 7. Exact Memory Byte Table & Five Realistic Hardware Execution Tiers

| Storage Layout | Bytes/Syn | 1 Focal (10^8) | 100 Focal (10^10) | Tier-L (32×500K) | Ratio vs CSR (OOP) | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Naive Heap-Object Graph ({w, pre, post, delay, masks}) | 80.00 B/syn | 8.00 GB | 800.00 GB | 1.28 GB | 0.12× (1.0× (OOP Base)) | Pointer chasing + GC thrash; 800 GB @ 10¹⁰ syn OOMs all nodes |
| 2. Dense FP32 Weight Matrix (Float32Array N² = 50K²) | 100.00 B/syn | 10.00 GB | 1.00 TB (1000 GB) | 8.59 GB | 0.09× (0.80× (Worse @ 4%!)) | 96% zeros; 1.00 TB @ 100×50K & 8.59 GB even on Tier-L 32×8K! |
| 3. Uncompressed Sparse CSR (FP32 4B + uint32 4B + delay 1B + 2b mask) | 9.2500 B/syn | 925.0 MB | 92.50 GB | 148.0 MB | 1.0× (Sparse Base) (8.6×) | 92.5 GB @ 10¹⁰ syn (Workstation RAM); 148 MB on Tier-L 32×500K |
| 4. Tiled Sparse CSR (FP16 2B + tile-uint16 2B + delay 1B + 2b mask) | 5.2500 B/syn | 525.0 MB | 52.50 GB | 84.0 MB | 1.76× (15.2×) | 52.5 GB @ 10¹⁰ syn (Tier-W 64–128 GB); 84.0 MB on Tier-L Laptop |
| 5. 32-Synapse Block-Sparse int8 (32B w + 2B scale + 2B tile + 8B mask + 2B dly) | 1.4375 B/syn | 143.8 MB | 14.38 GB | 23.0 MB | 6.43× (55.7×) | 14.38 GB @ 10¹⁰ syn (fits 24 GB dGPU); 23.0 MB on Tier-L Laptop |
| 6. 32-Synapse Packed int4 Block (16B w + 2B FP16 scale + 2B tile + 8B 2b-masks) | 0.8750 B/syn | 87.5 MB | 8.75 GB | 14.0 MB | 10.57× (91.4×) | 8.75 GB @ 10¹⁰ syn (fits 16–24 GB VRAM); 14.0 MB on Tier-L Laptop |
| 7. 32-Synapse Packed Ternary b1.58 Block (7B 5-trit/B + 2B scale + 2B tile + 8B masks) | 0.5938 B/syn | 59.4 MB | 5.94 GB | 9.5 MB | 15.58× (134.7×) | 5.94 GB weights @ 10¹⁰ syn (Tier-D/W GPU); 9.5 MB on Tier-L Laptop! |


| Tier | Host Spec | Pop | Units/Agent | Synapses/Agent | Max Syn Ev/s | Canonical Mesh | Target FPS | Runtime Policy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tier E — Edge / Mobile / RPi | 2–4 GB RAM · 4-core ARM | 1–8 | ≤ 2,048 | ≤ 65K (b1.58/int4) | ≤ 2.1M ev/s | 16-node 2D (fixed) | 30 FPS (33.3 ms) | 5-Gear clock + SW-unpacked int4/CfC + 10 Hz decimated UI |
| Tier L — Standard Laptop (CPU/iGPU) | 8–16 GB RAM · 8-core / WebGPU | 16–40 | 8,192 (uint16) | ≤ 500K (9.5–23 MB wt) | ≤ 80M ev/s | 32-node XPBD (fixed) | 60 FPS (16.7 ms) | WebWorkers + SharedArrayBuffer SeqLock + 1 focal retina |
| Tier D — Desktop Single dGPU | 32 GB RAM · 12–24 GB VRAM | 64–200 (or 4×50M) | 32K–65K (uint16) | 5M–10M (CSR int8/int4) | ≤ 1.2G ev/s | 48-node 3D XPBD | 60 FPS (16.7 ms) | Batched WebGPU/CUDA compute + async Parquet/DuckDB worker |
| Tier W — Multi-GPU Workstation | 64–128 GB RAM · 48–96 GB VRAM | 8–32×100M (or 500×2M) | 50K–131K (tiled/u32) | 100M focal / 2M crowd | ≤ 12G ev/s | 64–128 node 3D XPBD | 60 FPS / Async | Tiled CSR/packed blocks + multi-dome + Tier-2 crowd surrogates |
| Tier C — Headless CI Runner | 4–8 GB RAM · 2–4 vCPU (No GPU) | 4–16 | 4,096 (uint16) | ≤ 250K (int8/FP32 det) | Deterministic | 24-node canonical | Max ticks/s (No UI) | Tier-1 bit-exact SHA-256 lockstep + 5-mutant & FWER gate |


## 8. Complete 825-Item Clean-Slate Capability Checklists (`0 / 825`)

> **Scoreboard Reconciliation:** `825` executable suite checkboxes (`0 / 825` initialized `☐`), minus `5` direct cross-suite mirrors (`MIR-01..05`) = `820` unique suite-level assertions (`~775` distinct biological/computational mechanisms).

| Mirror ID | Linked Pair | Shared Mechanism | Unified Harness Rule |
| --- | --- | --- | --- |
| MIR-01 | CQM05 ↔ HW18 | 11-Pool Compensated FP64 First-Law Conservation (`\|ΔE\|/(E_0 + E_solar_in_cum) < 1e-12`) | Verified once by shared enthalpy-ledger worker harness (`HW18`); credited to `CQM05` & `HW18`. |
| MIR-02 | CQM13 ↔ HOT-2 | Calibrated Second-Order Metacognitive Reliability Monitor (`Brier ≤ 0.15`) | Single perceptual-uncertainty wagering & confidence-calibration assay satisfies `CQM13` & `HOT-2`. |
| MIR-03 | CQM19 ↔ RPT-1 | Stimulus-Free Recurrent State Persistence Across Sensory Blank | Shared delayed-match blank-interval persistence vs feedforward-matched control satisfies `CQM19` & `RPT-1`. |
| MIR-04 | CQM20 ↔ GWT-3 | Capacity-Limited Global Workspace Broadcast (`≥ 4` Consumer Modules) | Single bottleneck broadcast fan-out & consumer ablation assay satisfies `CQM20` & `GWT-3`. |
| MIR-05 | CQM21 ↔ F2 | Non-Circular Forked-Snapshot Perturbational Complexity (`PCI*` Wake > Sleep) | Shared forked-snapshot zap-and-zip Lempel-Ziv complexity harness satisfies `CQM21` & `F2`. |

### Suite 1 — Butlin-14 Computational Consciousness Indicators (14)

| St | ID | Indicator | Operational Falsifiable Criterion |
| --- | --- | --- | --- |
| ☐ | RPT-1 | Recurrent processing | Signals loop across recurrent local/areal pathways so perceptual state persists and refines after transient stimulus offset (`δ_pair ≥ 0.33` vs feedforward-only ablation). |
| ☐ | RPT-2 | Organised, integrated perception | Recurrent feedback binds distributed features into figure-ground segregated, conjunctive object representations (`Acc_conj - Acc_ff ≥ 0.15`). |
| ☐ | GWT-1 | Specialist modules | Multiple quasi-independent specialist subsystems (sensory, memory, visceral, motor) process domain streams in parallel (`modularity Q_mod ≥ 0.35`). |
| ☐ | GWT-2 | Limited-capacity workspace | Central bottleneck (`K_ws` slots) admits only winning coalitions, producing an **attentional blink maximal at lags 2–5 (`100–500 ms` SOA) with lag-1 sparing**. |
| ☐ | GWT-3 | Global broadcast | Workspace ignition broadcasts winning content down-tree to working memory, planning, affect, and motor specialists simultaneously (`≥ 80%` specialist receiver mutual info lift). |
| ☐ | GWT-4 | State-dependent attention | Endogenous goals, visceral drives, and current workspace context exert top-down gain modulation over specialist competition and ignition thresholds. |
| ☐ | HOT-1 | Generative perception & reality monitoring | Top-down generative model predicts sensory input and discriminates externally driven signal from endogenous replay/noise (`AUROC ≥ 0.80` vs shuffled monitor). |
| ☐ | HOT-2 | Higher-order meta-representations | Second-order monitor forms calibrated reliability/belief representations over first-order perceptual and policy states (`ECE ≤ 0.08`, Brier lift vs constant baseline). |
| ☐ | HOT-3 | Belief- & confidence-guided agency | Higher-order belief updates and calibrated confidence causally arbitrate pragmatic action, active epistemic scanning, and low-confidence opt-out. |
| ☐ | HOT-4 | Sparse & smooth quality space | Perceptual and affective states occupy a structured metric similarity manifold where representational distances systematically predict behavioral generalization (`Spearman ρ ≥ 0.65`). |
| ☐ | AST-1 | Attention schema | Internal predictive schema tracks, forecasts, and stabilizes the organism's own attentional state (and models conspecific gaze rays when social). |
| ☐ | PP-1 | Predictive processing | Hierarchical generative layers predict lower-level activity and update beliefs/weights via precision-weighted prediction errors (`residual drop ≥ 30%`). |
| ☐ | AE-1 | Instrumental agency | Acquires action-outcome contingencies from closed-loop feedback and immediately re-selects policies upon outcome devaluation (`0-trial` revaluation shift). |
| ☐ | AE-2 | Embodied forward self-model | Sensorimotor efference-copy forward model predicts self-generated sensory consequences and separates own motion from exogenous perturbation (`reafference cancel ≥ 70%`). |

### Suite 2 — Ten Theoretical Evaluation Frameworks (10)

| St | ID | Framework | Operational Measurement Contract |
| --- | --- | --- | --- |
| ☐ | F1 | Creativity machine (Thaler) | Keyed stochastic/REM perturbation generator paired with an internal world-model plausibility & homeostatic value critic discovering novel valid policies. |
| ☐ | F2 | Integrated Information Motivation / Forked-Snapshot PCI* | Evaluates joint integration and differentiation via Casali-style **forked-snapshot perturbational Lempel-Ziv complexity (`PCI*`)**—explicitly avoiding intractable `O(2^N)` exact IIT `Φ` claims. |
| ☐ | F3 | Active inference (Friston) | Policy selection jointly minimizes expected homeostatic divergence (pragmatic risk) and model parameter/state ambiguity (urgency-gated epistemic gain). |
| ☐ | F4 | Attention Schema Theory (Graziano) | Endogenous schema forecasts own attentional transitions and projects peer attentional vectors to predict social competition/cooperation. |
| ☐ | F5 | Oscillatory phase / traveling-wave routing | Distributed specialist spheres coordinate communication-through-coherence via PV+ phase-locked gamma windows and cortical traveling waves. |
| ☐ | F6 | Unlimited Associative Learning (UAL, Ginsburg & Jablonka) | Demonstrates compound cross-modal feature binding, trace conditioning across silent temporal gaps, and flexible second-order/reversal learning. |
| ☐ | F7 | Sensorimotor contingency mastery (O'Regan & Noë) | Learns lawful action-to-sensation Jacobians across soft-body posture shifts and land/water medium transitions. |
| ☐ | F8 | Projective egocentric perspective (Rudrauf) | Projects multisensory landmarks and visceral valence into a unified 3D egocentric reference frame supporting detour viewpoint transformation. |
| ☐ | F9 | Conscious Turing Machine (Blum & Blum) | Explicit `O(log M_mod)` up-tree competitive chunk tournament with threshold ignition and `O(1)`-hop down-tree broadcast to all specialists. |
| ☐ | F10 | Butlin-14 Indicator Profile Scorecard | Reports the 6-family profile vector `{RPT: x/2, GWT: x/4, HOT: x/4, AST: x/1, PP: x/1, AE: x/2}` plus an optional `14/14` full-suite milestone badge (never conflating distinct theories). |

### Suite 3 — CQM-25 Autopoietic & Quality Criteria (25)

| St | ID | Criterion | Quantitative Verification Gate |
| --- | --- | --- | --- |
| ☐ | CQM01 | Heredity | Offspring inherit genomic/epigenetic parameters and exhibit positive parent-offspring trait heritability (`h² > 0.25` above random population draw). |
| ☐ | CQM02 | Open-endedness | Lineages exhibit non-saturating growth in held-out behavioral niche competence and interaction complexity significantly exceeding neutral-mutation drift controls. |
| ☐ | CQM03 | Ecological coupling | Births, carrying capacity, and survival depend strictly on conserved dome primary production, grazing depletion, and detritus mineralization. |
| ☐ | CQM04 | Adaptive morphology | Heritable soft-body geometry, compliance, and chamber traits trade off energetically across distinct physical niches (`2-niche` fitness crossover). |
| ☐ | CQM05 | Embodied thermodynamic consistency | 11-pool compensated `FP64` ledger closes (`\|ΔE\| / (E_0 + E_in,cum) < 1e-12`), `E_diss_num ≥ 0`, and internal ATP/fuel state causally drives behavior. |
| ☐ | CQM06 | Perceptual integration | Multimodal sensory fusion outperforms best unimodal ablation under matched channel noise (`δ_pair ≥ 0.33`). |
| ☐ | CQM07 | Within-lifetime learning | Online synaptic/state plasticity measurably improves survival and net kJ intake over weight-frozen genetic clones on identical locked seeds. |
| ☐ | CQM08 | Continual retention | Metaplastic cascade consolidation retains Task-A survival competence (`LCB_95% > -0.05`) after acquiring sequential Task-B/C contingencies. |
| ☐ | CQM09 | Causal interoceptive model | Internal visceral forward model forecasts blood/store trajectories and initiates corrective foraging/shade action prior to homeostatic deficit. |
| ☐ | CQM10 | Autonomous goal regulation | Maintains blood glucose, core temperature, and osmolarity within viable bounds via self-selected meal termination, rest, and microclimate choice. |
| ☐ | CQM11 | Multi-step planning | Internal latent rollout or Riemannian geodesic search selects hazard-avoiding detours over myopic Euclidean greedy trajectories. |
| ☐ | CQM12 | Compositional transfer | Recombines factorized learned cue/action primitives to solve held-out compound contingencies zero-shot (`Acc ≥ 0.75` vs `≤ 0.40` tabular control). |
| ☐ | CQM13 | Metacognition | Calibrated uncertainty estimate gates active scanning and trap opt-out (direct cross-suite mirror of `HOT-2`; tracked once in de-duplicated tallies). |
| ☐ | CQM14 | Costly signalling game | Senders pay proportional ATP to emit condition/alarm signals and receivers decode them above phase-shuffled stream controls. |
| ☐ | CQM15 | Autopoietic boundary | Actively synthesizes membrane lipid `T`, pumps ions against osmotic lysis, and clots physical punctures (`SOFT17`, `SOFT21`). |
| ☐ | CQM16 | Proactive self-maintenance | Acquires enthalpy, water, precursors, and thermal shelter ahead of lethal physiological thresholds (`TTC` margin > 0). |
| ☐ | CQM17 | Closed-loop homeostasis | Autonomic and endocrine feedback loops reject step disturbances in fuel, O2, and pH with bounded settling time. |
| ☐ | CQM18 | Structural resilience | Recovers viable foraging and homeostasis (`≥ 70%` intact lifespan) following `20%` random synapse loss or peripheral lobe trauma. |
| ☐ | CQM19 | Recurrent persistence | Maintains task-relevant working state across stimulus-free delays via recurrent dynamics (direct mirror of `RPT-1`). |
| ☐ | CQM20 | Workspace broadcast | Capacity-limited ignition broadcasts winning coalitions across specialist spheres (direct mirror of `GWT-3`). |
| ☐ | CQM21 | Non-circular integration | Perturbational complexity `PCI*` drops significantly under inter-module cut or NREM synchrony (direct mirror of `F2`). |
| ☐ | CQM22 | Common-currency valence | Unified affective arbitration trades off caloric payoff against nociceptive damage and predation risk. |
| ☐ | CQM23 | Substrate pluralism | Canonical `.alifebin` organism snapshot restores and executes consistently across CPU, WASM, and headless CI runtimes. |
| ☐ | CQM24 | Deterministic reproducibility | Identical seed + Tier-1 config yields bit-exact SHA-256 state hash; perturbing any declared causal part diverges trajectory `> ε_noise` in its active regime. |
| ☐ | CQM25 | Competence-validated scale | Scaling neural/morphological capacity produces statistically significant competence lift over a tuned `Competent Simple Baseline` on complex tasks. |

### Suite 4 — FREAK-100 Biophysical & Neural Mechanisms (100)

| St | ID | Group | Mechanism | Cost | Contract |
| --- | --- | --- | --- | --- | --- |
| ☐ | F-001 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Sparse expansion layer (granule-like) | [O(k·E)] | Random fan-out `D -> 10D` plus `2%` k-WTA threshold rendering nonlinear XOR linearly separable. |
| ☐ | F-002 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Vector-symbolic binding (MAP) | [O(D_lat)] | Elementwise product of bipolar `(+1/-1)` module hypervectors injected into associative cortex. |
| ☐ | F-003 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Holographic reduced representations | [O(D log D)] | Circular-convolution role-filler binding (`FFT` or permutation) into fixed-width `D_lat` vectors. |
| ☐ | F-004 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Gamma-phase coincidence binding | [O(N_u)] | Features spiking within one `5–15 ms` PV+ gamma window trigger coincidence-detecting readout cells. |
| ☐ | F-005 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Theta-gamma phase multiplexing | [O(D_lat)] | 4–7 ordered working-memory items maintained in distinct gamma subcycles nested inside one theta wave. |
| ☐ | F-006 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Shunting-inhibition XOR | [O(N_u)] | Divisive dendritic conductance `I_exc / (g_leak + g_shunt)` peaks on single inputs and attenuates on joint drive. |
| ☐ | F-007 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Single-neuron dCaAP XOR | [O(N_u)] | Human L2/3-inspired apical calcium potential peaking near threshold and attenuating on stronger dual input (Gidon et al. 2020). |
| ☐ | F-008 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Gain-field coordinate transform | [O(N_u)] | Posture/gaze signal multiplicatively modulates sensory tuning curves to map retinotopic to body-centric space. |
| ☐ | F-009 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Sigma-pi dendritic branch clusters | [O(B·N_u)] | Local synaptic products along individual dendritic branches summed at soma for conjunctive cue detection. |
| ☐ | F-010 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Mixed-selectivity random reservoir | [O(k·E)] | Fixed contractive nonlinear projections (`‖W‖_2 ≤ 0.99`) yielding high linear-readout shatter dimensionality. |
| ☐ | F-011 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Low-rank tensor-product binding | [O(r·D)] | Rank-`r` outer-product factorization `Sum_{i=1..r} (u_i ⊗ v_i)` avoiding full `O(D_lat²)` Kronecker blowup. |
| ☐ | F-012 | A. Binding and conjunction (multiplicative or nonlinear mixing) | Conjunctive CA3 place-cue cells | [O(k·E)] | Sparse recurrent autoassociative units firing selectively only when spatial bump and sensory cue co-occur. |
| ☐ | F-013 | A. Binding and conjunction (multiplicative or nonlinear mixing) | L5 burst-event multiplexing | [O(N_u)] | Somatic event rate transmits basal feedforward input while high-frequency burst fraction encodes apical feedback. |
| ☐ | F-014 | B. Temporal and analog coding beyond coarse rate levels | Time-to-first-spike (TTFS) coding | [O(k·E)] | Stronger inputs cross threshold earlier in phase, encoding continuous rank-order intensity in 1 spike/unit. |
| ☐ | F-015 | B. Temporal and analog coding beyond coarse rate levels | Spiking LTC (sLTC) adaptive units | [O(k·E)] | Input-modulated liquid conductance warps membrane `τ(x)` inside event-driven spiking units (Vanhalle & Gielen 2025). |
| ☐ | F-016 | B. Temporal and analog coding beyond coarse rate levels | Bounded local multirate substepping | [O(K·E)] | Fast contact/membrane stiffness transients refine locally (`K_iter ≤ 8`) under conservative flux handoff. |
| ☐ | F-017 | B. Temporal and analog coding beyond coarse rate levels | Population dither quantization smoothing | [O(N_u)] | Keyed independent subthreshold noise linearizes population transfer across coarse `int4`/`b1.58` thresholds. |
| ☐ | F-018 | B. Temporal and analog coding beyond coarse rate levels | Hybrid graded + spike transmission | [O(k·E)] | Local gap/graded synapses transmit continuous somatic `V_m` alongside discrete long-range axonal spikes. |
| ☐ | F-019 | B. Temporal and analog coding beyond coarse rate levels | Liquid state machine (LSM) spiking pool | [O(k·E)] | Contractive excitable spiking reservoir mapping temporal input streams into linearly separable states. |
| ☐ | F-020 | B. Temporal and analog coding beyond coarse rate levels | FORCE-stabilized echo-state readout | [O(E+D²)] | Low-rank recursive least-squares readout feedback tames chaotic-edge continuous reservoir trajectories. |
| ☐ | F-021 | B. Temporal and analog coding beyond coarse rate levels | Polychronous axonal-delay groups | [O(k·E)] | Time-locked spike cascades emerging from heterogeneous integer 3D conduction delays + STDP. |
| ☐ | F-022 | B. Temporal and analog coding beyond coarse rate levels | Resonate-and-fire damped oscillators | [O(N_u)] | 2D coupled subthreshold variables resonating selectively to matched environmental vibration/call frequencies. |
| ☐ | F-023 | C. Predictive coding, precision & active inference | Precision-weighted predictive hierarchy | [O(L·D²)] | Top-down generative predictions cancel expected sensory input; learned inverse-variance weights residuals. |
| ☐ | F-024 | C. Predictive coding, precision & active inference | Precision-driven metacognitive opt-out | [O(D_lat)] | Sensory/world-model precision feeds `HOT-2` confidence to trigger active scanning or high-risk trap opt-out. |
| ☐ | F-025 | C. Predictive coding, precision & active inference | Interoceptive active inference | [O(1)] | Visceral hunger, osmoregulation, and thermal drives arise from precision-weighted errors against homeostatic priors. |
| ☐ | F-026 | C. Predictive coding, precision & active inference | Urgency-gated expected free energy | [O(G_plan)] | Scores rollout policies by homeostatic utility plus survival-margin-gated epistemic information gain. |
| ☐ | F-027 | C. Predictive coding, precision & active inference | Apical-minus-basal local error | [O(N_u)] | Apical predictive expectation subtracted locally from basal sensory drive to guide non-BPTT weight updates. |
| ☐ | F-028 | C. Predictive coding, precision & active inference | Glucose time-to-collision (TTC) drive | [O(1)] | Forecasts time-to-hypoglycemia `(Glc - Glc_crit) / max(ε, -dGlc/dt)` to forage prior to energy crisis. |
| ☐ | F-029 | C. Predictive coding, precision & active inference | Adaptive interoceptive precision gate | [O(1)] | Calibrated visceral forecast accuracy scales how strongly anticipated deficits override immediate sensory lures. |
| ☐ | F-030 | D. Homeostatic & visceral control (wet body) | Integral-feedback glycemic clamp | [O(1)] | Time-integrated blood-glucose error drives insulin/glucagon balance to eliminate steady-state offset. |
| ☐ | F-031 | D. Homeostatic & visceral control (wet body) | Antithetic biomolecular integral motif | [O(1)] | Non-negative species `z_1, z_2 ≥ 0` (`ż_1 = μ - η z_1 z_2`, `ż_2 = θ x - η z_1 z_2`) with zero dilution & dual-rail actuation achieving exact adaptation (Briat et al. 2016). |
| ☐ | F-032 | D. Homeostatic & visceral control (wet body) | Three-timescale satiation cascade | [O(1)] | Fast mechanosensitive gut stretch -> medium CCK -> slow systemic leptin/GLP-1 meal termination. |
| ☐ | F-033 | D. Homeostatic & visceral control (wet body) | Circadian & seasonal rheostasis | [O(1)] | Smoothly shifts lipid/thermal set-points across photoperiod cycles to pre-accumulate winter reserves. |
| ☐ | F-034 | D. Homeostatic & visceral control (wet body) | Workload organ hypertrophy/atrophy | [O(1)] | Sustained mechanical or metabolic demand scales muscle/gill capacity within life at booked amino/ATP cost. |
| ☐ | F-035 | D. Homeostatic & visceral control (wet body) | Sub-lethal hormetic conditioning | [O(1)] | Mild toxin or thermal challenge upregulates CYP/chaperone capacity, reducing damage on subsequent acute shock. |
| ☐ | F-036 | D. Homeostatic & visceral control (wet body) | Allostatic wear-and-tear integrator | [O(1)] | Chronic stress-axis activation accumulates physiological strain that elevates repair cost and senescence rate. |
| ☐ | F-037 | D. Homeostatic & visceral control (wet body) | Uncoupled thermogenic heat valve | [O(1)] | Regulated proton-leak thermogenesis converts lipid stores directly into `E_heat_phys` in cold microclimates. |
| ☐ | F-038 | D. Homeostatic & visceral control (wet body) | Astrocyte glycogen-lactate buffer | [O(1)] | Glial glycogen reserve fuels intense local cortical spike bursts and recharges during quiet wake/NREM. |
| ☐ | F-039 | E. Glia, slow gating & volume neuromodulation | Tripartite astrocyte Ca2+ LTP gate | [O(k·E)] | Long-term synaptic potentiation requires coincidence of synaptic eligibility with slow glial `Ca²⁺` elevation. |
| ☐ | F-040 | E. Glia, slow gating & volume neuromodulation | Gap-junction glial working memory | [O(Cells)] | Diffusively coupled astrocyte calcium syncytium bridges multi-second silent trace-conditioning intervals. |
| ☐ | F-041 | E. Glia, slow gating & volume neuromodulation | Neuromodulator-gated specialist router | [O(M_mod)] | Tonic `DA, NE, 5-HT, ACh` concentrations re-weight Mixture-of-Specialists routing gains without weight churn. |
| ☐ | F-042 | E. Glia, slow gating & volume neuromodulation | Locus-coeruleus (NE) gain reset | [O(1)] | Phasic `NE` sharpens exploit gain; sustained high tonic `NE` flattens policy temperature to escape depleted patches. |
| ☐ | F-043 | E. Glia, slow gating & volume neuromodulation | ACh expected vs NE unexpected uncertainty | [O(1)] | `ACh` tracks known observation noise within a regime; `NE` spikes on abrupt latent world-rule switches. |
| ☐ | F-044 | E. Glia, slow gating & volume neuromodulation | Serotonergic temporal horizon scaling | [O(1)] | Precursor-backed tonic `5-HT` increases effective discount factor `γ` so replete organisms wait for delayed rewards. |
| ☐ | F-045 | E. Glia, slow gating & volume neuromodulation | Diffusive neuropeptide mood field | [O(1)] | Slow extracellular peptide half-lives (`minutes`) bias defensive vs affiliative circuit tone with zero point wires. |
| ☐ | F-046 | E. Glia, slow gating & volume neuromodulation | Size-scaled microglial NREM pruning | [O(k·E)] | Complement-tagged low-utility synapses are pruned in NREM **proportionally to current post-natal synapse count**. |
| ☐ | F-047 | E. Glia, slow gating & volume neuromodulation | Size-scaled NREM SHY renormalization | [O(E_syn)] | Multiplicative slow-wave weight downscaling preserves relative learned ranks while preventing daytime saturation. |
| ☐ | F-048 | F. Plasticity rules & meta-learning | Evolvable ABCD local Hebbian rule | [O(k·E)] | Heritable regional coefficients `Δw = η(A·pre + B·post + C·pre·post + D)·mod` bounded by `‖W‖_2 ≤ 0.99`. |
| ☐ | F-049 | F. Plasticity rules & meta-learning | Behavioral time-scale plasticity (BTSP) | [O(k·E)] | Apical dendritic plateau potential retroactively writes one-shot episodic associations across `1–5 s` traces (Bittner et al. 2017). |
| ☐ | F-050 | F. Plasticity rules & meta-learning | Bounded sparse 3-factor eligibility | [O(k·E)] |  Circular-buffered active `pre × post` tags (`≤ 5%` synapses) converted to `Δw` on delayed neuromodulator arrival. |
| ☐ | F-051 | F. Plasticity rules & meta-learning | Symmetric e-prop spiking gradients | [O(E_syn)] | Forward-propagated local eligibility vectors approximate recurrent SNN credit assignment in `O(E_syn)` memory (Bellec et al. 2020). |
| ☐ | F-052 | F. Plasticity rules & meta-learning | Sliding-threshold BCM homeostasis | [O(N_u)] | Postsynaptic firing-rate EMA shifts LTP/LTD crossover threshold to stabilize feature selectivity. |
| ☐ | F-053 | F. Plasticity rules & meta-learning | Fan-in normalized UAL updates | [O(k·E)] | Normalizes associative weight increments by active cue L1 norm so compound cues do not overshoot singletons. |
| ☐ | F-054 | F. Plasticity rules & meta-learning | Fusi multi-state cascade synapses | [O(k·E)] | Discrete metaplastic biochemical depth states yield power-law memory retention against catastrophic forgetting. |
| ☐ | F-055 | F. Plasticity rules & meta-learning | Keyed node-perturbation credit | [O(N_u)] | Correlates keyed exploratory somatic conductances with global reward-prediction error for gradient-free motor tuning. |
| ☐ | F-056 | F. Plasticity rules & meta-learning | Broadcast feedback alignment | [O(E_syn)] | Fixed contractive random top-down error projections drive multi-layer credit without symmetric weight transpose. |
| ☐ | F-057 | F. Plasticity rules & meta-learning | Földiák Hebbian/anti-Hebbian whitening | [O(S²)] | Feedforward excitation + plastic lateral inhibition decorrelates redundant multimodal sensory channels. |
| ☐ | F-058 | G. Developmental & evolutionary indirect encodings | Coordinate CPPN bauplan generator | [O(G·E_m)] | Compact coordinate network evaluated at Gear-4 developmental milestones to paint symmetric body/brain priors. |
| ☐ | F-059 | G. Developmental & evolutionary indirect encodings | Gene-regulatory-network (GRN) cleavage | [O(Cells)] | Small TF interaction matrix (`16–64` genes) governs mitotic differentiation, chamber count, and receptor density. |
| ☐ | F-060 | G. Developmental & evolutionary indirect encodings | Co-evolved regional plasticity rates | [O(1)] | Genomic neuromodulator gains and regional learning-rate schedules co-adapt alongside soft morphology. |
| ☐ | F-061 | G. Developmental & evolutionary indirect encodings | Store- & crowding-gated fecundity | [O(1)] | Autonomous budding/oviposition requires surplus maternal lipid stores and non-saturated local carrying capacity. |
| ☐ | F-062 | G. Developmental & evolutionary indirect encodings | Compensated First-Law maternal provisioning | [O(1)] | Exact `FP64` enthalpy transfer from parent `E_stores` into egg yolk `E_stores` + transfer heat (`\|ΔE\| < 1e-12`). |
| ☐ | F-063 | G. Developmental & evolutionary indirect encodings | Degenerate repertoire group selection | [O(M_mod)] | Structurally distinct micro-circuits compete for trophic maintenance while serving overlapping survival functions. |
| ☐ | F-064 | G. Developmental & evolutionary indirect encodings | Genomic bottleneck innate motifs | [O(G_gen)] | Compressing connectome rules (`< 1 KB` genome -> `> 500K` synapses) forces reusable innate sensorimotor priors. |
| ☐ | F-065 | G. Developmental & evolutionary indirect encodings | Turing reaction-diffusion patterning | [O(V_mesh)] | Coupled activator-inhibitor PDEs self-organize somatotopic columns and cryptic skin pigmentation. |
| ☐ | F-066 | G. Developmental & evolutionary indirect encodings | Gap-junction bioelectric shape memory | [O(Cells)] | Tissue-wide `V_mem` depolarization gradient stores anterior-posterior anatomical target polarity across injury. |
| ☐ | F-067 | G. Developmental & evolutionary indirect encodings | Decay-bounded famine epigenetics | [O(1)] | Maternal starvation sets reversible chromatin-like metabolic thrift marks decaying within `1–2` replete generations. |
| ☐ | F-068 | H. Stochastic & quantum-inspired exploration (with mandatory classical controls) | Recorded QRNG / Philox entropy stream | [O(1)] | Immutable recorded hardware QRNG `.sensorlog` (or `Philox4x32-10`) drives exploration; benchmarked vs matched PRNG. |
| ☐ | F-069 | H. Stochastic & quantum-inspired exploration (with mandatory classical controls) | State-dependent parametric weight noise | [O(k·E)] | Learnable exploration variance shrinks automatically as local prediction residuals converge. |
| ☐ | F-070 | H. Stochastic & quantum-inspired exploration (with mandatory classical controls) | Heavy-tailed Lévy-walk search | [O(1)] | Truncated power-law run lengths (`μ ≈ 2.0`) accelerate sparse resource patch discovery when local odor vanishes. |
| ☐ | F-071 | H. Stochastic & quantum-inspired exploration (with mandatory classical controls) | Langevin membrane posterior sampling | [O(N_u)] | Keyed stochastic drift-diffusion dynamics sample multi-modal latent world interpretations under ambiguity. |
| ☐ | F-072 | H. Stochastic & quantum-inspired exploration (with mandatory classical controls) | Capped superposition option register | [Q≤8] | Coherent sub-register (`0 ≤ Q ≤ 8` inside global `Q ≤ 10` cap) interferes action amplitudes; **must beat equal-param classical `SO(2)^Q` control**. |
| ☐ | F-073 | H. Stochastic & quantum-inspired exploration (with mandatory classical controls) | Chaotic itinerancy attractor hopping | [O(D_lat)] | Weakly unstable deterministic low-dimensional trajectories visit candidate behavioral modes without external noise. |
| ☐ | F-074 | H. Stochastic & quantum-inspired exploration (with mandatory classical controls) | Ising/Hopfield instinct relaxation | [O(K·E)] | Bounded `4-step` spin-glass settling snaps ambiguous predator cues onto low-latency defensive reflexes. |
| ☐ | F-075 | H. Stochastic & quantum-inspired exploration (with mandatory classical controls) | Subthreshold stochastic resonance | [O(N_u)] | Calibrated background membrane noise lifts weak subthreshold plume/vibration cues into detectable spike timing. |
| ☐ | F-076 | I. Whole-brain & multibrain 'Frankenstein' hybrids | 12-Organ closed-loop sensorimotor brain | [O(Sum)] | Causally wired sensory bus, Hopfield CA3, world model, critic, workspace, affect, brainstem Ring-0, and CPG ganglia. |
| ☐ | F-077 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Predictor-residual metacognitive critic | [O(D_lat)] | World-model prediction residual variance feeds `HOT-2` uncertainty directly without oracle labels. |
| ☐ | F-078 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Cerebellar forward-cancellation sidecar | [O(k·E)] | Granule sparse expansion + Purkinje error-driven LTD cancels sensory delay and self-reafference. |
| ☐ | F-079 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Striatal D1/D2/STN action race gate | [O(M_mod)] | Direct (`Go`), indirect (`NoGo`), and hyperdirect (`STN` global pause) channels arbitrate specialist motor bids. |
| ☐ | F-080 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Parallel column reference-frame voting | [O(C·D)] | Cortical-like sensorimotor columns track object-centric pose hypotheses and reach lateral consensus. |
| ☐ | F-081 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Fast Workspace + slow reservoir shadow | [O(E+M)] | Low-capacity `20 Hz` global broadcast paired with a high-dimensional slow unconscious echo reservoir. |
| ☐ | F-082 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Dual-hemisphere callosal consensus | [O(D_lat)] | Exploit-specialized and novelty-monitoring sub-spheres coordinate across bandwidth-capped callosal fibers. |
| ☐ | F-083 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Mushroom-body Kenyon valence sidecar | [O(k·E)] | Clean-slate `2%` sparse SDR expansion (**engineering choice inspired by `5–10%` fly Kenyon odor sparsity**, Aso et al. 2014) + DA compartment tagging. |
| ☐ | F-084 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Octopus-inspired brachial arm autonomy | [O(V+N)] | **`~2/3` of total neurons** reside in distributed soft-limb cords (Hochner 2012), solving local wrapping & compliance without central lag. |
| ☐ | F-085 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Algebraic VSA episodic hippocampus | [O(D_lat)] | Binds `(Place ⊗ Cue ⊗ Outcome)` into one queryable hyperdimensional vector supporting cue/place unbinding. |
| ☐ | F-086 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Visceral-to-cortical gain hypernetwork | [O(r·N_u)] | Slow endocrine/visceral vector generates low-rank multiplicative gain masks for fast sensorimotor spheres. |
| ☐ | F-087 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Decaying outer-product fast weights | [O(D_lat²)] | Short-lived Hebbian scratchpad matrix `A(t)` binds temporary relational variables within multi-step episodes. |
| ☐ | F-088 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Phase-coincidence spike routing | [O(k·E)] | Query-key spike phase alignment gates value packet transfer across hub bottlenecks without dense softmax. |
| ☐ | F-089 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Modern continuous Hopfield settling | [O(M·D)] | Log-sum-exp energy landscape retrieves sharp full-episode latents from `≥ 50%` masked cues in `≤ 3` steps. |
| ☐ | F-090 | I. Whole-brain & multibrain 'Frankenstein' hybrids | Tolman-Eichenbaum factorized map | [O(M·D)] | Factorizes abstract transition topology (toroidal grid) from sensory landmark identities (`CA3` bind). |
| ☐ | F-091 | J. Biophysical & integrative mechanisms (strictly in-world & lesion-tested) | Ephaptic local extracellular coupling | [O(N_u)] | Local mean-field voltage gradient weakly phase-couples adjacent packed units without point synapses. |
| ☐ | F-092 | J. Biophysical & integrative mechanisms (strictly in-world & lesion-tested) | Capped dipole beat-frequency clock | [Q≤6] | Internal phase-oscillator bank (`Q ≤ 6`); **must beat parameter-matched classical Kuramoto oscillator bank**. |
| ☐ | F-093 | J. Biophysical & integrative mechanisms (strictly in-world & lesion-tested) | Spine-neck electrical compartmentalization | [O(k·E)] | Activity-dependent per-synapse conductance scalar gates local dendritic plateau cooperativity. |
| ☐ | F-094 | J. Biophysical & integrative mechanisms (strictly in-world & lesion-tested) | Adaptive axonal conduction-delay tuning | [O(k·E)] | Myelin-like velocity adjustment aligns arrival latencies of convergent sensory pathways onto coincidence cells. |
| ☐ | F-095 | J. Biophysical & integrative mechanisms (strictly in-world & lesion-tested) | PV+ gap-junction inhibitory syncytium | [O(N_u)] | Resistive coupling across fast-spiking interneurons stabilizes crisp `40 Hz` gamma windows. |
| ☐ | F-096 | J. Biophysical & integrative mechanisms (strictly in-world & lesion-tested) | Homeostatic branching-ratio criticality | [O(N_u)] | Gain homeostasis tunes avalanche branching ratio near `σ ≈ 0.98–1.00` to maximize dynamic range without seizure. |
| ☐ | F-097 | J. Biophysical & integrative mechanisms (strictly in-world & lesion-tested) | Synaptic tag-and-capture consolidation | [O(k·E)] | Intrinsic excitability bias + protein-synthesis resource pool converts transient tags into durable engrams. |
| ☐ | F-098 | J. Biophysical & integrative mechanisms (strictly in-world & lesion-tested) | Microbiome-vagal precursor coupling | [O(1)] | Symbiotic gut fermentation products modulate host tryptophan/5-HT availability and nutrient-specific appetite. |
| ☐ | F-099 | J. Biophysical & integrative mechanisms (strictly in-world & lesion-tested) | Circadian-gated anabolic/catabolic plasticity | [O(1)] | Waking phase favors tag formation & LTP; NREM slow-wave window unlocks complement pruning & `SHY`. |
| ☐ | F-100 | J. Biophysical & integrative mechanisms (strictly in-world & lesion-tested) | Morphology-as-inference soft remodeling | [O(V_mesh)] | Slow viscoelastic rest-length and stiffness adaptation reduces chronic sensorimotor prediction error at ATP cost. |

### Suite 5 — LIFE-100 Organism Biology Matrix (100 Areas × 5 = 500 Checks)

| St | Sub-Check ID | Area | Executable Biological Sub-Check |
| --- | --- | --- | --- |
| ☐ | LIFE-L001-A1 | Metabolism | 5 nutrient compartments (gut, blood, liver, fat, muscle) |
| ☐ | LIFE-L001-A2 | Metabolism | 11-pool FP64 Kahan-Neumaier ledger (<1e-12) |
| ☐ | LIFE-L001-A3 | Metabolism | Glycogen, lipo-, keto- & gluconeogenesis flux |
| ☐ | LIFE-L001-A4 | Metabolism | ATP currency gating spikes & motors |
| ☐ | LIFE-L001-A5 | Metabolism | Heritable traits paid from same ATP/mass budget |
| ☐ | LIFE-L002-A1 | Feeding / appetite | Ghrelin, leptin & insulin-like signals |
| ☐ | LIFE-L002-A2 | Feeding / appetite | Deficit drive suppressed by post-absorptive insulin |
| ☐ | LIFE-L002-A3 | Feeding / appetite | Motor foraging act harvesting patch mass |
| ☐ | LIFE-L002-A4 | Feeding / appetite | 3-timescale satiation cascade |
| ☐ | LIFE-L002-A5 | Feeding / appetite | Macronutrient-selective taste choice |
| ☐ | LIFE-L003-A1 | Digestion | Lumen chyme transit & Michaelis-Menten absorption |
| ☐ | LIFE-L003-A2 | Digestion | Autonomous enteric motility rhythm |
| ☐ | LIFE-L003-A3 | Digestion | Vagal nutrient/stretch afferents |
| ☐ | LIFE-L003-A4 | Digestion | Symbiotic gut flora fermentation |
| ☐ | LIFE-L003-A5 | Digestion | Ingested toxin emesis / malabsorption |
| ☐ | LIFE-L004-A1 | Excretion / waste | Nitrogenous waste from protein catabolism |
| ☐ | LIFE-L004-A2 | Excretion / waste | Excreted mass debited from internal ledger |
| ☐ | LIFE-L004-A3 | Excretion / waste | Detritus deposited into local world grid |
| ☐ | LIFE-L004-A4 | Excretion / waste | Osmotic water & ion clearance |
| ☐ | LIFE-L004-A5 | Excretion / waste | Conspecific scent cue from waste marks |
| ☐ | LIFE-L005-A1 | Thermoregulation | Metabolic & damping heat booked to E_heat_phys |
| ☐ | LIFE-L005-A2 | Thermoregulation | Adaptive thermogenesis under cold/deficit |
| ☐ | LIFE-L005-A3 | Thermoregulation | Surface & core temperature sensed |
| ☐ | LIFE-L005-A4 | Thermoregulation | Uncoupled thermogenic lipid buffer |
| ☐ | LIFE-L005-A5 | Thermoregulation | Behavioral shade / sun-basking microclimate choice |
| ☐ | LIFE-L006-A1 | Circulation | Cardiac flow scaled by autonomic tone |
| ☐ | LIFE-L006-A2 | Circulation | Perfusion rate bounds cortical glucose/O2 delivery |
| ☐ | LIFE-L006-A3 | Circulation | Multi-solute blood vector (glc, FFA, AA, ketones) |
| ☐ | LIFE-L006-A4 | Circulation | Body-plan vascular perfusion topology |
| ☐ | LIFE-L006-A5 | Circulation | Intrinsic Ring-0 cardiac pacemaker oscillator |
| ☐ | LIFE-L007-A1 | Respiration / gas exchange | Dissolved/ambient O2 resource pool |
| ☐ | LIFE-L007-A2 | Respiration / gas exchange | Ring-0 respiratory CPG rhythm |
| ☐ | LIFE-L007-A3 | Respiration / gas exchange | Chemoreceptive hypoxia/hypercapnia drive |
| ☐ | LIFE-L007-A4 | Respiration / gas exchange | High-yield aerobic vs lactate anaerobic switch |
| ☐ | LIFE-L007-A5 | Respiration / gas exchange | Coupled dome O2/CO2 gas balance |
| ☐ | LIFE-L008-A1 | Homeostasis | Closed-loop glycemic set-point clamp |
| ☐ | LIFE-L008-A2 | Homeostasis | Forward interoceptive glucose TTC slope |
| ☐ | LIFE-L008-A3 | Homeostasis | Zero steady-state error integral clamp |
| ☐ | LIFE-L008-A4 | Homeostasis | Circadian/seasonal rheostatic set-point shift |
| ☐ | LIFE-L008-A5 | Homeostasis | Positive-orthant antithetic biomolecular motif |
| ☐ | LIFE-L009-A1 | Allostasis / stress load | HPA-like stress integrator with hysteresis |
| ☐ | LIFE-L009-A2 | Allostasis / stress load | Glucocorticoid catabolic mobilization |
| ☐ | LIFE-L009-A3 | Allostasis / stress load | Cumulative allostatic wear-and-tear state |
| ☐ | LIFE-L009-A4 | Allostasis / stress load | Pre-deficit anticipatory shelter/foraging |
| ☐ | LIFE-L009-A5 | Allostasis / stress load | Parasympathetic post-threat recovery |
| ☐ | LIFE-L010-A1 | Injury / damage | Structural tissue integrity pool |
| ☐ | LIFE-L010-A2 | Injury / damage | Nociceptive afferents into visceral insula |
| ☐ | LIFE-L010-A3 | Injury / damage | World mechanical/predator hazards cause tears |
| ☐ | LIFE-L010-A4 | Injury / damage | Segment-localized soft-tissue damage |
| ☐ | LIFE-L010-A5 | Injury / damage | Traumatic lobe/appendage loss |
| ☐ | LIFE-L011-A1 | Repair / healing | Amino-acid + ATP-debited tissue synthesis |
| ☐ | LIFE-L011-A2 | Repair / healing | Targeted wound coagulation & repair |
| ☐ | LIFE-L011-A3 | Repair / healing | Fast stiff scar vs slow compliant regeneration |
| ☐ | LIFE-L011-A4 | Repair / healing | Blastema regrowth of lost soft appendage |
| ☐ | LIFE-L011-A5 | Repair / healing | Central autonomic triage of repair perfusion |
| ☐ | LIFE-L012-A1 | Immunity | Cytokine inflammation state |
| ☐ | LIFE-L012-A2 | Immunity | Stochastic world pathogen exposure |
| ☐ | LIFE-L012-A3 | Immunity | Adaptive sickness lethargy & anorexia |
| ☐ | LIFE-L012-A4 | Immunity | Transmissible dome pathogen entities |
| ☐ | LIFE-L012-A5 | Immunity | Faster secondary clearance via immune memory |
| ☐ | LIFE-L013-A1 | Pain / nociception | Tissue tear/strain drives nociceptors |
| ☐ | LIFE-L013-A2 | Pain / nociception | One-trial place/object avoidance from harm |
| ☐ | LIFE-L013-A3 | Pain / nociception | Nociception elevates defensive fear state |
| ☐ | LIFE-L013-A4 | Pain / nociception | Fast A-delta withdrawal vs slow C guarding |
| ☐ | LIFE-L013-A5 | Pain / nociception | Endogenous descending analgesia under crisis |
| ☐ | LIFE-L014-A1 | Disease / dysregulation | Learned-helplessness / hypo-dopaminergic lock |
| ☐ | LIFE-L014-A2 | Disease / dysregulation | Runaway incentive sensitization trap |
| ☐ | LIFE-L014-A3 | Disease / dysregulation | Homeostatic neuromodulator drift failure mode |
| ☐ | LIFE-L014-A4 | Disease / dysregulation | Post-sensitization withdrawal deficit |
| ☐ | LIFE-L014-A5 | Disease / dysregulation | Chronic organ fibrosis / insufficiency |
| ☐ | LIFE-L015-A1 | Ageing / senescence | Monotone biological age state |
| ☐ | LIFE-L015-A2 | Ageing / senescence | Cumulative oxidative/allostatic damage |
| ☐ | LIFE-L015-A3 | Ageing / senescence | Age-declining regeneration efficiency |
| ☐ | LIFE-L015-A4 | Ageing / senescence | Disposable-soma lifespan vs fecundity trade-off |
| ☐ | LIFE-L015-A5 | Ageing / senescence | Mitotic division-limit telomere counter |
| ☐ | LIFE-L016-A1 | Death | Lethal neuroglycopenic/ATP collapse |
| ☐ | LIFE-L016-A2 | Death | Terminal Phase-III proteolysis organ failure |
| ☐ | LIFE-L016-A3 | Death | Structured cause-of-death manifest log |
| ☐ | LIFE-L016-A4 | Death | Irreversible transition to world carcass entity |
| ☐ | LIFE-L016-A5 | Death | Lethal predation / exsanguination |
| ☐ | LIFE-L017-A1 | Decay / decomposition | Carcass persists spatially and mineralizes |
| ☐ | LIFE-L017-A2 | Decay / decomposition | Labile N/C nutrients returned to soil grid |
| ☐ | LIFE-L017-A3 | Decay / decomposition | Scavenger guild consumption of corpses |
| ☐ | LIFE-L017-A4 | Decay / decomposition | Necromone chemical avoidance/attraction plume |
| ☐ | LIFE-L017-A5 | Decay / decomposition | Exact FP64 body-to-detritus enthalpy handoff |
| ☐ | LIFE-L018-A1 | Toxicity | Bitter/chemical oral & plume chemosense |
| ☐ | LIFE-L018-A2 | Toxicity | Configurable dome toxin concentration field |
| ☐ | LIFE-L018-A3 | Toxicity | ATP-debited hepatic CYP-like clearance |
| ☐ | LIFE-L018-A4 | Toxicity | Low-dose hormetic enzyme upregulation |
| ☐ | LIFE-L018-A5 | Toxicity | Garcia delayed conditioned taste aversion |
| ☐ | LIFE-L019-A1 | Viability monitoring | Continuous physiological distance-to-death metric |
| ☐ | LIFE-L019-A2 | Viability monitoring | Visceral margin readable by internal self-model |
| ☐ | LIFE-L019-A3 | Viability monitoring | Multi-minute trajectory forecast of fuel drop |
| ☐ | LIFE-L019-A4 | Viability monitoring | Multiplicative survival urgency gate |
| ☐ | LIFE-L019-A5 | Viability monitoring | Automated viability guard in CI assays |
| ☐ | LIFE-L020-A1 | Circadian clock | Light-entrained SCN phase oscillator |
| ☐ | LIFE-L020-A2 | Circadian clock | Free-running rhythm abolished by SCN lesion |
| ☐ | LIFE-L020-A3 | Circadian clock | Antiphase cortisol/melatonin-like endocrine wave |
| ☐ | LIFE-L020-A4 | Circadian clock | Entrainment to periodic resource availability |
| ☐ | LIFE-L020-A5 | Circadian clock | Photoperiodic seasonal rheostasis |
| ☐ | LIFE-L021-A1 | Sleep | Two-process adenosine S × circadian C drive |
| ☐ | LIFE-L021-A2 | Sleep | High tonic NE delays sleep flip-flop |
| ☐ | LIFE-L021-A3 | Sleep | Thalamic sensory elevation threshold in sleep |
| ☐ | LIFE-L021-A4 | Sleep | Cumulative performance degradation under sleep debt |
| ☐ | LIFE-L021-A5 | Sleep | Bistable wake / NREM / REM flip-flop |
| ☐ | LIFE-L022-A1 | Dreaming | Prioritized NREM sharp-wave episode replay |
| ☐ | LIFE-L022-A2 | Dreaming | REM generative rollouts tagged with epistemic uncertainty |
| ☐ | LIFE-L022-A3 | Dreaming | Quiet-wake planning/consolidation ripples |
| ☐ | LIFE-L022-A4 | Dreaming | Threat-weighted post-trauma replay bias |
| ☐ | LIFE-L022-A5 | Dreaming | Replay trajectory inspectable in Tab 08 |
| ☐ | LIFE-L023-A1 | Synaptic downscaling | Size-scaled pruning of low-salience wires |
| ☐ | LIFE-L023-A2 | Synaptic downscaling | Waking activity-dependent re-sprouting |
| ☐ | LIFE-L023-A3 | Synaptic downscaling | Multiplicative NREM SHY renormalization |
| ☐ | LIFE-L023-A4 | Synaptic downscaling | Complement-like microglial tag stripping |
| ☐ | LIFE-L023-A5 | Synaptic downscaling | NREM clearance of accumulated metabolic byproducts |
| ☐ | LIFE-L024-A1 | Ultradian / interval timing | Multi-scale oscillator bank on sensory bus |
| ☐ | LIFE-L024-A2 | Ultradian / interval timing | Learnable interval peak-timing expectation |
| ☐ | LIFE-L024-A3 | Ultradian / interval timing | Input-modulated liquid time constants τ(x) |
| ☐ | LIFE-L024-A4 | Ultradian / interval timing | Replayable `.sensorlog` timing-regime cue (0 host wall-clock leak) |
| ☐ | LIFE-L024-A5 | Ultradian / interval timing | Pre-feeding anticipatory activity ramp |
| ☐ | LIFE-L025-A1 | Body schema | Actuated soft limb with motor efference copy |
| ☐ | LIFE-L025-A2 | Body schema | Learned posture-to-contact forward Jacobian |
| ☐ | LIFE-L025-A3 | Body schema | Rapid motor adaptation after lobe loss/growth |
| ☐ | LIFE-L025-A4 | Body schema | 3D volumetric / multi-chamber bauplan |
| ☐ | LIFE-L025-A5 | Body schema | Compressed latent proprioceptive body map |
| ☐ | LIFE-L026-A1 | Locomotion | Directed patch-to-patch spatial traversal |
| ☐ | LIFE-L026-A2 | Locomotion | Segmental phase-coupled CPG oscillators |
| ☐ | LIFE-L026-A3 | Locomotion | Speed-dependent gait phase transition |
| ☐ | LIFE-L026-A4 | Locomotion | Exact mechanical work + heat debited from ATP |
| ☐ | LIFE-L026-A5 | Locomotion | Slope, viscosity & deformable-substrate coupling |
| ☐ | LIFE-L027-A1 | Peripheral limb ganglia | Per-segment/lobe autonomous int4 CfC ganglion |
| ☐ | LIFE-L027-A2 | Peripheral limb ganglia | Zero-brain local stretch/nociceptive withdrawal |
| ☐ | LIFE-L027-A3 | Peripheral limb ganglia | Descending central command × local reflex fusion |
| ☐ | LIFE-L027-A4 | Peripheral limb ganglia | Local peripheral trace adaptation |
| ☐ | LIFE-L027-A5 | Peripheral limb ganglia | Distributed segment strain & contact sensors |
| ☐ | LIFE-L028-A1 | Manipulation / appendages | Deformable hydrostatic tentacle / gripper lobe |
| ☐ | LIFE-L028-A2 | Manipulation / appendages | Online compensation for external shear loads |
| ☐ | LIFE-L028-A3 | Manipulation / appendages | Conformable friction grasp & object transport |
| ☐ | LIFE-L028-A4 | Manipulation / appendages | Stone/barrier displacement to unlock food caches |
| ☐ | LIFE-L028-A5 | Manipulation / appendages | 100% original non-copied appendage geometry |
| ☐ | LIFE-L029-A1 | Eyes / active vision | Agent-perspective ray/retina field sampling |
| ☐ | LIFE-L029-A2 | Eyes / active vision | Contrast & looming-motion edge channels |
| ☐ | LIFE-L029-A3 | Eyes / active vision | Original non-anthropomorphic log-polar / multi-eye array |
| ☐ | LIFE-L029-A4 | Eyes / active vision | Active saccadic & motion-parallax peering |
| ☐ | LIFE-L029-A5 | Eyes / active vision | Ambient irradiance & photoperiod transduction |
| ☐ | LIFE-L030-A1 | Morphing / variable geometry | Dynamic hydrostatic aspect-ratio state |
| ☐ | LIFE-L030-A2 | Morphing / variable geometry | Defensive inflation / posture expansion |
| ☐ | LIFE-L030-A3 | Morphing / variable geometry | Aperture compression through narrow crevices |
| ☐ | LIFE-L030-A4 | Morphing / variable geometry | Slow morphology-as-inference stiffness remodeling |
| ☐ | LIFE-L030-A5 | Morphing / variable geometry | ATP + pressure-work cost booked per morph |
| ☐ | LIFE-L031-A1 | Camouflage & signaling skin | Controllable surface pigment/pattern vector |
| ☐ | LIFE-L031-A2 | Camouflage & signaling skin | Batesian/social pattern matching |
| ☐ | LIFE-L031-A3 | Camouflage & signaling skin | Adaptive substrate luminance/spatial-frequency crypsis |
| ☐ | LIFE-L031-A4 | Camouflage & signaling skin | Cost-constrained deceptive display dynamics |
| ☐ | LIFE-L031-A5 | Camouflage & signaling skin | Reinforcement-tuned crypsis vs courtship switch |
| ☐ | LIFE-L032-A1 | Ontogenetic growth | Connectome grown from compact GRN/CPPN genome |
| ☐ | LIFE-L032-A2 | Ontogenetic growth | Nutrient-funded somatic mass accretion |
| ☐ | LIFE-L032-A3 | Ontogenetic growth | Discrete developmental stage transitions |
| ☐ | LIFE-L032-A4 | Ontogenetic growth | Kleiber M^0.75 metabolic allometry |
| ☐ | LIFE-L032-A5 | Ontogenetic growth | Growth arrest under caloric scarcity |
| ☐ | LIFE-L033-A1 | Continuum skin / boundary | Distributed surface contact pressure sheet |
| ☐ | LIFE-L033-A2 | Continuum skin / boundary | Affiliative conspecific contact transduction |
| ☐ | LIFE-L033-A3 | Continuum skin / boundary | Dynamic chromatophore array |
| ☐ | LIFE-L033-A4 | Continuum skin / boundary | Mucosal/cuticle pathogen & toxin barrier |
| ☐ | LIFE-L033-A5 | Continuum skin / boundary | Surface conductive heat-flux sensing |
| ☐ | LIFE-L034-A1 | Unified sensory bus | Typed multi-modality SoA channel arena |
| ☐ | LIFE-L034-A2 | Unified sensory bus | 2% sparse random projection whitening |
| ☐ | LIFE-L034-A3 | Unified sensory bus | Top-down predictive residual encoding |
| ☐ | LIFE-L034-A4 | Unified sensory bus | Precision-weighted cross-modal fusion |
| ☐ | LIFE-L034-A5 | Unified sensory bus | Heritable modality allocation & ray budget |
| ☐ | LIFE-L035-A1 | Interoception | Dedicated visceral state vector on bus |
| ☐ | LIFE-L035-A2 | Interoception | Insular homeostatic error integration |
| ☐ | LIFE-L035-A3 | Interoception | Vagal/humoral afferent signaling |
| ☐ | LIFE-L035-A4 | Interoception | Hidden-state trajectory-curvature caution signal |
| ☐ | LIFE-L035-A5 | Interoception | Learned visceral forecast precision |
| ☐ | LIFE-L036-A1 | Chemosense / olfaction | Advected-diffused food plume gradients |
| ☐ | LIFE-L036-A2 | Chemosense / olfaction | Volatile conspecific pheromone field |
| ☐ | LIFE-L036-A3 | Chemosense / olfaction | Persistent stigmergic substrate scent marks |
| ☐ | LIFE-L036-A4 | Chemosense / olfaction | Combinatorial receptor tuning bank |
| ☐ | LIFE-L036-A5 | Chemosense / olfaction | Oral nutritive vs bitter-toxin gustation |
| ☐ | LIFE-L037-A1 | Audition & vibrations | Distance-attenuated dome acoustic wavefield |
| ☐ | LIFE-L037-A2 | Audition & vibrations | Log-spaced cochlear spectral filterbank |
| ☐ | LIFE-L037-A3 | Audition & vibrations | Conspecific call detection & decoding |
| ☐ | LIFE-L037-A4 | Audition & vibrations | Proprioceptive feedback of own acoustic emission |
| ☐ | LIFE-L037-A5 | Audition & vibrations | Binaural / phase-lag azimuth localization |
| ☐ | LIFE-L038-A1 | Touch & proprioception | Agent-agent compliant contact force |
| ☐ | LIFE-L038-A2 | Touch & proprioception | Segmental curvature & chamber-extension angles |
| ☐ | LIFE-L038-A3 | Touch & proprioception | Efference-subtracted active touch residual |
| ☐ | LIFE-L038-A4 | Touch & proprioception | Continuous surface normal/shear stress sheet |
| ☐ | LIFE-L038-A5 | Touch & proprioception | Substrate Rayleigh-like vibration pickup |
| ☐ | LIFE-L039-A1 | Electro- & magnetoreception | Global dipole compass vector field |
| ☐ | LIFE-L039-A2 | Electro- & magnetoreception | Hazard / thermal-vent electric gradient |
| ☐ | LIFE-L039-A3 | Electro- & magnetoreception | Short-range peer bioelectric dipole sensing |
| ☐ | LIFE-L039-A4 | Electro- & magnetoreception | ATP-debited active electrolocation pulses |
| ☐ | LIFE-L039-A5 | Electro- & magnetoreception | Plastic spatial orientation to field reversals |
| ☐ | LIFE-L040-A1 | Quantum-inspired internal sense | Born-rule readout from Q≤10 internal register |
| ☐ | LIFE-L040-A2 | Quantum-inspired internal sense | Fubini-Study state-change sensitivity |
| ☐ | LIFE-L040-A3 | Quantum-inspired internal sense | Neuromodulator-steered unitary rotation gates |
| ☐ | LIFE-L040-A4 | Quantum-inspired internal sense | Deterministic statevector backend (no 1<<32 bug) |
| ☐ | LIFE-L040-A5 | Quantum-inspired internal sense | Demonstrated lift OR parity disclosure vs equal-param classical control |
| ☐ | LIFE-L041-A1 | Replayable substrate transducers | Immutable `.sensorlog` recorded transducer tap |
| ☐ | LIFE-L041-A2 | Replayable substrate transducers | Practice-only sandboxed live IMU/mic/cam stream |
| ☐ | LIFE-L041-A3 | Replayable substrate transducers | Simulated step-budget load cue (replay-locked) |
| ☐ | LIFE-L041-A4 | Replayable substrate transducers | In-world physics regime dial sensors |
| ☐ | LIFE-L041-A5 | Replayable substrate transducers | Mandatory temporal-shuffle causal control |
| ☐ | LIFE-L042-A1 | Long-range attenuated field sense | Inverse-square attenuated distant patch wavefield |
| ☐ | LIFE-L042-A2 | Long-range attenuated field sense | High noise floor + explicit ATP/tick receptor cost |
| ☐ | LIFE-L042-A3 | Long-range attenuated field sense | Learned spatial integration over noisy samples |
| ☐ | LIFE-L042-A4 | Long-range attenuated field sense | Strict Shannon channel capacity ceiling |
| ☐ | LIFE-L042-A5 | Long-range attenuated field sense | Drops to chance under stream shuffle (0 oracle cheat) |
| ☐ | LIFE-L043-A1 | Bioelectric / acoustic social link | Short-range physical broadcast field between peers |
| ☐ | LIFE-L043-A2 | Bioelectric / acoustic social link | Affective arousal coupling across field |
| ☐ | LIFE-L043-A3 | Bioelectric / acoustic social link | Phase-locked collective rhythm entrainment |
| ☐ | LIFE-L043-A4 | Bioelectric / acoustic social link | Emergent learned codebook (0 hardcoded symbols) |
| ☐ | LIFE-L043-A5 | Bioelectric / acoustic social link | Sender ATP debit proportional to broadcast power |
| ☐ | LIFE-L044-A1 | Spiking cortical sheet | Balanced E/I LIF/AdEx/sLTC sheet |
| ☐ | LIFE-L044-A2 | Spiking cortical sheet | Causal 3-factor spike-timing plasticity |
| ☐ | LIFE-L044-A3 | Spiking cortical sheet | Slow NMDA-like plateau voltage persistence |
| ☐ | LIFE-L044-A4 | Spiking cortical sheet | Topographic thalamocortical projection |
| ☐ | LIFE-L044-A5 | Spiking cortical sheet | Tiled CSR scaling to 50K–100K units (Tier D/W) |
| ☐ | LIFE-L045-A1 | Thalamic gating hub | Arousal/sleep-stage sensory gate |
| ☐ | LIFE-L045-A2 | Thalamic gating hub | Top-down attentional gain spotlight |
| ☐ | LIFE-L045-A3 | Thalamic gating hub | Corticothalamic feedback loop |
| ☐ | LIFE-L045-A4 | Thalamic gating hub | Pulvinar-like predictive precision routing |
| ☐ | LIFE-L045-A5 | Thalamic gating hub | Salience-triggered burst wakeup |
| ☐ | LIFE-L046-A1 | Basal-ganglia action gate | Striatal D1-Go / D2-NoGo race competition |
| ☐ | LIFE-L046-A2 | Basal-ganglia action gate | DA-modulated 3-factor action value update |
| ☐ | LIFE-L046-A3 | Basal-ganglia action gate | Phasic RPE burst / dip signaling |
| ☐ | LIFE-L046-A4 | Basal-ganglia action gate | Hyperdirect STN-like pre-motor pause/veto |
| ☐ | LIFE-L046-A5 | Basal-ganglia action gate | Multi-specialist motor bid arbitration |
| ☐ | LIFE-L047-A1 | Hippocampal episodic system | Localized spatial place-bump units |
| ☐ | LIFE-L047-A2 | Hippocampal episodic system | Prioritized NREM trajectory replay |
| ☐ | LIFE-L047-A3 | Hippocampal episodic system | Toroidal hex-grid path integration |
| ☐ | LIFE-L047-A4 | Hippocampal episodic system | Theta-ordered sequence ring buffer |
| ☐ | LIFE-L047-A5 | Hippocampal episodic system | One-shot BTSP plateau episode writing |
| ☐ | LIFE-L048-A1 | 7-Channel neuromodulation | Precursor-backed DA, 5-HT, NE, ACh, Glu, GABA, eCB |
| ☐ | LIFE-L048-A2 | 7-Channel neuromodulation | Phasic NE modulates workspace ignition gain |
| ☐ | LIFE-L048-A3 | 7-Channel neuromodulation | ACh/NE expected vs unexpected uncertainty split |
| ☐ | LIFE-L048-A4 | 7-Channel neuromodulation | Slow neuropeptide affective volume bus |
| ☐ | LIFE-L048-A5 | 7-Channel neuromodulation | Oxytocin-like kin/affiliative gain modulator |
| ☐ | LIFE-L049-A1 | Biophysical cell diversity | Dale's-law excitatory & inhibitory classes |
| ☐ | LIFE-L049-A2 | Biophysical cell diversity | Intrinsic enteric ganglion units |
| ☐ | LIFE-L049-A3 | Biophysical cell diversity | Opponent sympathetic vs parasympathetic drives |
| ☐ | LIFE-L049-A4 | Biophysical cell diversity | Fast myelinated vs slow unmyelinated delays |
| ☐ | LIFE-L049-A5 | Biophysical cell diversity | Resistive gap-junction electrical syncytia |
| ☐ | LIFE-L050-A1 | Glial-vascular support | Tripartite astrocyte Ca2+ LTP gate |
| ☐ | LIFE-L050-A2 | Glial-vascular support | Slow glial working-memory persistence |
| ☐ | LIFE-L050-A3 | Glial-vascular support | Glycogen-lactate burst shuttle |
| ☐ | LIFE-L050-A4 | Glial-vascular support | Size-scaled microglial NREM pruning |
| ☐ | LIFE-L050-A5 | Glial-vascular support | Activity-tuned axonal delay plasticity |
| ☐ | LIFE-L051-A1 | Multi-timescale plasticity | Reward/novelty-gated 3-factor STDP |
| ☐ | LIFE-L051-A2 | Multi-timescale plasticity | Surprise-modulated meta-learning rate |
| ☐ | LIFE-L051-A3 | Multi-timescale plasticity | Bounded sparse eligibility ring (`≤5%` syn) |
| ☐ | LIFE-L051-A4 | Multi-timescale plasticity | Heritable regional ABCD plasticity parameters |
| ☐ | LIFE-L051-A5 | Multi-timescale plasticity | Fusi cascade consolidation against forgetting |
| ☐ | LIFE-L052-A1 | Multi-tier brain scaling | Live byte & syn-events/s profiler in Tab 19 |
| ☐ | LIFE-L052-A2 | Multi-tier brain scaling | Batched Tier-2 WebGPU/CUDA population kernels |
| ☐ | LIFE-L052-A3 | Multi-tier brain scaling | 2% SDR expansion into packed CSR blocks |
| ☐ | LIFE-L052-A4 | Multi-tier brain scaling | Nested brains-in-brains S2S hierarchy |
| ☐ | LIFE-L052-A5 | Multi-tier brain scaling | Validated scaling path to 10^8 focal synapses (Tier W) |
| ☐ | LIFE-L053-A1 | Decentralized ganglia | Autonomous digestive enteric ring |
| ☐ | LIFE-L053-A2 | Decentralized ganglia | Segmental soft-limb reflex cords |
| ☐ | LIFE-L053-A3 | Decentralized ganglia | Dual-hemisphere callosal consensus |
| ☐ | LIFE-L053-A4 | Decentralized ganglia | Parallel reference-frame column voting |
| ☐ | LIFE-L053-A5 | Decentralized ganglia | Intrinsic cardiac & respiratory Ring-0 pacemakers |
| ☐ | LIFE-L054-A1 | Generative world model | One-step multi-modal sensory forecast |
| ☐ | LIFE-L054-A2 | Generative world model | Bus residual predictive coding |
| ☐ | LIFE-L054-A3 | Generative world model | Unified visceral + exteroceptive latent RSSM/JEPA |
| ☐ | LIFE-L054-A4 | Generative world model | Multi-layer hierarchical error passing |
| ☐ | LIFE-L054-A5 | Generative world model | Compositional VSA latent transitions |
| ☐ | LIFE-L055-A1 | Global workspace | Nonlinear competitive ignition threshold |
| ☐ | LIFE-L055-A2 | Global workspace | Down-tree broadcast writing to episodic memory |
| ☐ | LIFE-L055-A3 | Global workspace | Explicit metabolic ATP cost per ignition burst |
| ☐ | LIFE-L055-A4 | Global workspace | High-dimensional non-ignited echo reservoir |
| ☐ | LIFE-L055-A5 | Global workspace | Sustained recurrent workspace buffer (`K_ws` slots) |
| ☐ | LIFE-L056-A1 | Selective attention | Goal- & drive-modulated top-down gain |
| ☐ | LIFE-L056-A2 | Selective attention | Precision-weighted sensory selection |
| ☐ | LIFE-L056-A3 | Selective attention | Learned endogenous Attention Schema (`AST-1`) |
| ☐ | LIFE-L056-A4 | Selective attention | Bottom-up looming/surprise breakthrough |
| ☐ | LIFE-L056-A5 | Selective attention | Covert internal spotlight shift vs overt gaze saccade |
| ☐ | LIFE-L057-A1 | Metacognition | Second-order reliability monitor (`HOT-2`) |
| ☐ | LIFE-L057-A2 | Metacognition | Trajectory-divergence / ensemble uncertainty |
| ☐ | LIFE-L057-A3 | Metacognition | Adaptive trap opt-out & information-seeking scan |
| ☐ | LIFE-L057-A4 | Metacognition | Sensory precision propagated to decision confidence |
| ☐ | LIFE-L057-A5 | Metacognition | Well-calibrated Brier / ECE confidence readouts |
| ☐ | LIFE-L058-A1 | Decision & policy search | Pragmatic value + urgency-gated epistemic bonus |
| ☐ | LIFE-L058-A2 | Decision & policy search | Langevin / ensemble posterior policy sampling |
| ☐ | LIFE-L058-A3 | Decision & policy search | Keyed Philox / recorded QRNG exploration |
| ☐ | LIFE-L058-A4 | Decision & policy search | Multi-step expected-free-energy rollout |
| ☐ | LIFE-L058-A5 | Decision & policy search | State-dependent metabolic risk aversion |
| ☐ | LIFE-L059-A1 | Curiosity & exploration | Prediction-error / novelty intrinsic drive |
| ☐ | LIFE-L059-A2 | Curiosity & exploration | Multiplicative fuel-margin safety gate (`CNF-01`) |
| ☐ | LIFE-L059-A3 | Curiosity & exploration | Truncated Lévy-walk sparse search |
| ☐ | LIFE-L059-A4 | Curiosity & exploration | Deterministic chaotic-itinerancy mode switching |
| ☐ | LIFE-L059-A5 | Curiosity & exploration | Expected information-gain eye/antenna scanning |
| ☐ | LIFE-L060-A1 | Embodied self-model | Persistent recurrent visceral-postural self latent |
| ☐ | LIFE-L060-A2 | Embodied self-model | Forward prediction of own metabolic & motor trajectory |
| ☐ | LIFE-L060-A3 | Embodied self-model | Preventive risk avoidance from forecasted harm |
| ☐ | LIFE-L060-A4 | Embodied self-model | Efference-copy self vs conspecific distinction |
| ☐ | LIFE-L060-A5 | Embodied self-model | Autobiographical episode continuity across days |
| ☐ | LIFE-L061-A1 | In-world regime inference | Latent context detection of dome physics switches |
| ☐ | LIFE-L061-A2 | In-world regime inference | Suppresses destructive weight churn on unlearnable noise |
| ☐ | LIFE-L061-A3 | In-world regime inference | Discovers legal rate-limited physical world levers |
| ☐ | LIFE-L061-A4 | In-world regime inference | 100% sandboxed within dome API (0 host escape) |
| ☐ | LIFE-L061-A5 | In-world regime inference | Causal clustering of hidden environmental regimes |
| ☐ | LIFE-L062-A1 | Latent state geometry | Intrinsic curvature of neural state trajectories |
| ☐ | LIFE-L062-A2 | Latent state geometry | Curvature coupled into interoceptive caution channel |
| ☐ | LIFE-L062-A3 | Latent state geometry | Learned danger-weighted Riemannian metric |
| ☐ | LIFE-L062-A4 | Latent state geometry | Geodesic divergence warning near chaotic saddles |
| ☐ | LIFE-L062-A5 | Latent state geometry | Optional Fubini-Study metric control comparison |
| ☐ | LIFE-L063-A1 | Imagination & recombination | Offline REM counterfactual episode synthesis |
| ☐ | LIFE-L063-A2 | Imagination & recombination | Generator-critic novel action screening (`F1`) |
| ☐ | LIFE-L063-A3 | Imagination & recombination | Pre-action latent trajectory simulation |
| ☐ | LIFE-L063-A4 | Imagination & recombination | Zero-shot compositional policy recombination |
| ☐ | LIFE-L063-A5 | Imagination & recombination | Surplus-energy juvenile locomotor/object play |
| ☐ | LIFE-L064-A1 | Associative learning | Patch caloric/toxin value conditioning |
| ☐ | LIFE-L064-A2 | Associative learning | Elemental + configural (`AB-`) cue learning |
| ☐ | LIFE-L064-A3 | Associative learning | Multi-second silent-gap trace conditioning |
| ☐ | LIFE-L064-A4 | Associative learning | Second-order cue-to-cue value propagation |
| ☐ | LIFE-L064-A5 | Associative learning | Role-filler compositional generalization |
| ☐ | LIFE-L065-A1 | Working memory | Persistent recurrent / NMDA-like maintenance |
| ☐ | LIFE-L065-A2 | Working memory | Input-gated liquid / SSM slow time constants |
| ☐ | LIFE-L065-A3 | Working memory | 4–7 slot theta-gamma phase buffer |
| ☐ | LIFE-L065-A4 | Working memory | Predictable capacity-limit eviction curve |
| ☐ | LIFE-L065-A5 | Working memory | Glial slow calcium context bridge |
| ☐ | LIFE-L066-A1 | Causal agency | Closed-loop action-outcome contingency tracker |
| ☐ | LIFE-L066-A2 | Causal agency | Positive competence lift vs lesion & passive controls |
| ☐ | LIFE-L066-A3 | Causal agency | Pre-motor visceral veto (`Free Won't`, `M068`) |
| ☐ | LIFE-L066-A4 | Causal agency | Efference-prediction match agency readout |
| ☐ | LIFE-L066-A5 | Causal agency | Temporal compression of perceived action-outcome delay |
| ☐ | LIFE-L067-A1 | Non-linguistic communication | Persistent chemical substrate scent marks |
| ☐ | LIFE-L067-A2 | Non-linguistic communication | Modulated acoustic/vibrational calls |
| ☐ | LIFE-L067-A3 | Non-linguistic communication | Receiver contingency learned online (0 fixed table) |
| ☐ | LIFE-L067-A4 | Non-linguistic communication | Zahavi ATP-costly honest vs bluff dynamics |
| ☐ | LIFE-L067-A5 | Non-linguistic communication | Allopatric group signal dialect divergence |
| ☐ | LIFE-L068-A1 | Spatial cognition | Topological patch-transition graph |
| ☐ | LIFE-L068-A2 | Spatial cognition | Continuous-attractor dead-reckoning integration |
| ☐ | LIFE-L068-A3 | Spatial cognition | Metric + relational cognitive shortcut map |
| ☐ | LIFE-L068-A4 | Spatial cognition | Tolman-Eichenbaum structural schema transfer |
| ☐ | LIFE-L068-A5 | Spatial cognition | Visual/olfactory/slope landmark phase reset |
| ☐ | LIFE-L069-A1 | Discrete affective modes | Rapid defensive freeze/flight fear |
| ☐ | LIFE-L069-A2 | Discrete affective modes | Post-nutritive consummatory relief/reward |
| ☐ | LIFE-L069-A3 | Discrete affective modes | Blocked-goal invigoration & strategy shift |
| ☐ | LIFE-L069-A4 | Discrete affective modes | Parasympathetic safe-rest quiescence |
| ☐ | LIFE-L069-A5 | Discrete affective modes | Toxin disgust, territorial defense, kin-loss protest & care |
| ☐ | LIFE-L070-A1 | Slow mood baselines | 2D fast valence × arousal state |
| ☐ | LIFE-L070-A2 | Slow mood baselines | Slow neuropeptide mood EMA (`minutes–hours`) |
| ☐ | LIFE-L070-A3 | Slow mood baselines | Bounded hysteresis without pathological lock |
| ☐ | LIFE-L070-A4 | Slow mood baselines | Positive mood widens safe exploratory radius |
| ☐ | LIFE-L070-A5 | Slow mood baselines | Gut precursor / microbiome modulation of mood tone |
| ☐ | LIFE-L071-A1 | Visceral feeling readouts | Trajectory-instability caution signal |
| ☐ | LIFE-L071-A2 | Visceral feeling readouts | Affiliative vs noxious surface contact valence |
| ☐ | LIFE-L071-A3 | Visceral feeling readouts | Topographic organ-deficit insula map |
| ☐ | LIFE-L071-A4 | Visceral feeling readouts | Linearly decodable affective quality manifold (`HOT-4`) |
| ☐ | LIFE-L071-A5 | Visceral feeling readouts | Hypoglycemic/osmotic error experienced as drive urgency |
| ☐ | LIFE-L072-A1 | Incentive motivation | Dopaminergic cue-triggered wanting (`incentive salience`) |
| ☐ | LIFE-L072-A2 | Incentive motivation | Hedonic satiation / alliesthesia gain shift |
| ☐ | LIFE-L072-A3 | Incentive motivation | Orexin-like metabolic arousal boost during fasting |
| ☐ | LIFE-L072-A4 | Incentive motivation | Urgency-ordered homeostatic drive arbitration |
| ☐ | LIFE-L072-A5 | Incentive motivation | Deprivation-amplified nutrient-specific seeking |
| ☐ | LIFE-L073-A1 | Individual temperament | 4D bold / exploratory / reactive / social axis |
| ☐ | LIFE-L073-A2 | Individual temperament | Experience-dependent developmental canalization |
| ☐ | LIFE-L073-A3 | Individual temperament | Additive + epistatic genomic heritability |
| ☐ | LIFE-L073-A4 | Individual temperament | Keyed developmental micro-variance bet-hedging |
| ☐ | LIFE-L073-A5 | Individual temperament | Frequency-dependent polymorphism across niches |
| ☐ | LIFE-L074-A1 | Acute stress response | Glucocorticoid energy-mobilization cascade |
| ☐ | LIFE-L074-A2 | Acute stress response | Sympathetic cardiac/ventilatory surge |
| ☐ | LIFE-L074-A3 | Acute stress response | Low-detectability immobility freeze |
| ☐ | LIFE-L074-A4 | Acute stress response | High-power escape or defensive counter-strike |
| ☐ | LIFE-L074-A5 | Acute stress response | Active shelter-seeking & social buffering |
| ☐ | LIFE-L075-A1 | Learned social attitudes | Individual-specific peer valence memory |
| ☐ | LIFE-L075-A2 | Learned social attitudes | Outcome-updated trust/avoidance weights |
| ☐ | LIFE-L075-A3 | Learned social attitudes | Kin vs non-kin vs predator stance differentiation |
| ☐ | LIFE-L075-A4 | Learned social attitudes | Approach/avoidance posture modulation |
| ☐ | LIFE-L075-A5 | Learned social attitudes | Rapid attitude reversal following betrayal/aid |
| ☐ | LIFE-L076-A1 | Reinforcement architecture | Signed temporal-difference RPE signal |
| ☐ | LIFE-L076-A2 | Reinforcement architecture | Endogenous action-contingent phasic DA burst |
| ☐ | LIFE-L076-A3 | Reinforcement architecture | Tonic DA vigor / exploration scaling |
| ☐ | LIFE-L076-A4 | Reinforcement architecture | Affiliative contact & kin-survival reward |
| ☐ | LIFE-L076-A5 | Reinforcement architecture | Bounded novelty prediction-error bonus |
| ☐ | LIFE-L077-A1 | Autonomous reproduction | In-world budding / oviposition events |
| ☐ | LIFE-L077-A2 | Autonomous reproduction | Organism-initiated energy-threshold reproductive gate |
| ☐ | LIFE-L077-A3 | Autonomous reproduction | First-Law exact maternal yolk/lactation transfer |
| ☐ | LIFE-L077-A4 | Autonomous reproduction | Crowding-inhibited reproductive rate |
| ☐ | LIFE-L077-A5 | Autonomous reproduction | Meiotic-like crossover & mate recombination |
| ☐ | LIFE-L078-A1 | Developmental genome | Compact indirect developmental genome (`<4 KB`) |
| ☐ | LIFE-L078-A2 | Developmental genome | Heritable temperament & endocrine priors |
| ☐ | LIFE-L078-A3 | Developmental genome | Innate brainstem Ring-0 reflex wiring |
| ☐ | LIFE-L078-A4 | Developmental genome | Genomic bottleneck forcing modular reuse |
| ☐ | LIFE-L078-A5 | Developmental genome | 16–64 gene developmental GRN matrix |
| ☐ | LIFE-L079-A1 | Mutational operators | Point & block-scale weight/GRN mutation |
| ☐ | LIFE-L079-A2 | Mutational operators | Temperament & time-constant mutation |
| ☐ | LIFE-L079-A3 | Mutational operators | Evolvable regional mutation-rate modifiers |
| ☐ | LIFE-L079-A4 | Mutational operators | Duplication/deletion of sensory rays or soft chambers |
| ☐ | LIFE-L079-A5 | Mutational operators | Keyed Philox / recorded QRNG mutation stream |
| ☐ | LIFE-L080-A1 | Multicellular ontogeny | Axonal/dendritic outgrowth during cleavage |
| ☐ | LIFE-L080-A2 | Multicellular ontogeny | Juvenile synaptogenesis overshoot + sleep pruning |
| ☐ | LIFE-L080-A3 | Multicellular ontogeny | Staged sensory-then-motor maturation waves |
| ☐ | LIFE-L080-A4 | Multicellular ontogeny | Steinberg cell-adhesion chamber morphogenesis |
| ☐ | LIFE-L080-A5 | Multicellular ontogeny | Experience-sensitive juvenile critical window |
| ☐ | LIFE-L081-A1 | Natural selection & lineages | Zero external fitness function—viability & births only |
| ☐ | LIFE-L081-A2 | Natural selection & lineages | Complete phylogenetic DAG provenance log |
| ☐ | LIFE-L081-A3 | Natural selection & lineages | Multi-generation Baldwin genetic assimilation |
| ☐ | LIFE-L081-A4 | Natural selection & lineages | Reproductive/niche divergence into sympatric guilds |
| ☐ | LIFE-L081-A5 | Natural selection & lineages | Matched neutral-selection drift comparison baseline |
| ☐ | LIFE-L082-A1 | Transgenerational epigenetics | Maternal famine metabolic-thrift mark |
| ☐ | LIFE-L082-A2 | Transgenerational epigenetics | Reversible gene-expression gain modifiers |
| ☐ | LIFE-L082-A3 | Transgenerational epigenetics | High-predation maternal defensive priming |
| ☐ | LIFE-L082-A4 | Transgenerational epigenetics | Persistence across F1–F2 before decay |
| ☐ | LIFE-L082-A5 | Transgenerational epigenetics | Rapid erasure upon sustained replete conditions |
| ☐ | LIFE-L083-A1 | Parental care | Trophallaxis / lactation enthalpy transfer |
| ☐ | LIFE-L083-A2 | Parental care | Active predator interception near offspring |
| ☐ | LIFE-L083-A3 | Parental care | Behavioral demonstration slowing for juveniles |
| ☐ | LIFE-L083-A4 | Parental care | Trivers parent-offspring weaning conflict |
| ☐ | LIFE-L083-A5 | Parental care | MHC / odor kin-offspring recognition |
| ☐ | LIFE-L084-A1 | Juvenile life stage | Morphologically distinct small juvenile stage |
| ☐ | LIFE-L084-A2 | Juvenile life stage | Early thermoregulatory/foraging dependency |
| ☐ | LIFE-L084-A3 | Juvenile life stage | Low-stakes locomotor & object play |
| ☐ | LIFE-L084-A4 | Juvenile life stage | Gradual transition to solid patch foraging |
| ☐ | LIFE-L084-A5 | Juvenile life stage | Realistic juvenile predation/starvation selection |
| ☐ | LIFE-L085-A1 | Ecological resource use | Patch grazing with saturating intake |
| ☐ | LIFE-L085-A2 | Ecological resource use | Shared finite dome nutrient standing stock |
| ☐ | LIFE-L085-A3 | Ecological resource use | Local patch depletion & logistic regrowth |
| ☐ | LIFE-L085-A4 | Ecological resource use | Spatial food caching with spoilage tracking |
| ☐ | LIFE-L085-A5 | Ecological resource use | Detritus-fertilized patch niche construction |
| ☐ | LIFE-L086-A1 | Social organization | Spatial encounter & compliant touch |
| ☐ | LIFE-L086-A2 | Social organization | Learned peer-specific approach/avoidance |
| ☐ | LIFE-L086-A3 | Social organization | MHC / lineage kin discrimination |
| ☐ | LIFE-L086-A4 | Social organization | Multi-agent cooperative stone/food task |
| ☐ | LIFE-L086-A5 | Social organization | Emergent dominance hierarchy reducing costly fights |
| ☐ | LIFE-L087-A1 | Multimodal signaling | Decaying substrate pheromone trails |
| ☐ | LIFE-L087-A2 | Multimodal signaling | Pitch/rate-modulated acoustic calls |
| ☐ | LIFE-L087-A3 | Multimodal signaling | Postural & chromatophore state displays |
| ☐ | LIFE-L087-A4 | Multimodal signaling | Predator-class-specific alarm calls |
| ☐ | LIFE-L087-A5 | Multimodal signaling | Socially copied signal sequences |
| ☐ | LIFE-L088-A1 | Resource competition | Zero-sum local patch depletion |
| ☐ | LIFE-L088-A2 | Resource competition | XPBD contact shoving & puncture damage |
| ☐ | LIFE-L088-A3 | Resource competition | Scent-bounded home-range defense |
| ☐ | LIFE-L088-A4 | Resource competition | Cache guarding against pilferers |
| ☐ | LIFE-L088-A5 | Resource competition | Acoustic/display jamming & bluff detection |
| ☐ | LIFE-L089-A1 | Predator-prey dynamics | Spatial predation-risk landscape |
| ☐ | LIFE-L089-A2 | Predator-prey dynamics | Autonomous coevolving predator guild in dome |
| ☐ | LIFE-L089-A3 | Predator-prey dynamics | Protean erratic dodge, crypsis & autotomy |
| ☐ | LIFE-L089-A4 | Predator-prey dynamics | Stalking, ambush & pack interception |
| ☐ | LIFE-L089-A5 | Predator-prey dynamics | Reciprocal morphological/sensory arms race |
| ☐ | LIFE-L090-A1 | Biosphere physics | No scripted narrative—physics & stoichiometry only |
| ☐ | LIFE-L090-A2 | Biosphere physics | Diurnal + seasonal solar irradiance wave |
| ☐ | LIFE-L090-A3 | Biosphere physics | Preregistered temperature, viscosity & toxin dials |
| ☐ | LIFE-L090-A4 | Biosphere physics | Slime corridors, burrows & waste-garden construction |
| ☐ | LIFE-L090-A5 | Biosphere physics | Bounded non-exploding multi-guild Lotka-Volterra cycles |
| ☐ | LIFE-L091-A1 | Cultural transmission | Visual/chemosensory observational foraging |
| ☐ | LIFE-L091-A2 | Cultural transmission | Conformist / payoff-biased peer copying |
| ☐ | LIFE-L091-A3 | Cultural transmission | Multi-generation persistence of non-genetic foraging routes |
| ☐ | LIFE-L091-A4 | Cultural transmission | Diffusion of novel cache-opening techniques |
| ☐ | LIFE-L091-A5 | Cultural transmission | Costly elder demonstration improving juvenile learning |
| ☐ | LIFE-L092-A1 | Affective contagion & aid | Decoding peer distress calls & posture |
| ☐ | LIFE-L092-A2 | Affective contagion & aid | Autonomic arousal coupling across neighbors |
| ☐ | LIFE-L092-A3 | Affective contagion & aid | Targeted food sharing or trap rescue of kin/allies |
| ☐ | LIFE-L092-A4 | Affective contagion & aid | Post-conflict affiliative contact calming |
| ☐ | LIFE-L092-A5 | Affective contagion & aid | Group alarm cascade across sensory horizon |
| ☐ | LIFE-L093-A1 | Mate choice | Complementary mating types / sexes |
| ☐ | LIFE-L093-A2 | Mate choice | Multi-step courtship display & approach |
| ☐ | LIFE-L093-A3 | Mate choice | Condition-dependent ornament preference |
| ☐ | LIFE-L093-A4 | Mate choice | ATP/drag-costly honest Zahavi traits |
| ☐ | LIFE-L093-A5 | Mate choice | Outbred MHC-dissimilar mate preference |
| ☐ | LIFE-L094-A1 | Collective swarm behavior | O(N_pop+C) local alignment/cohesion flocking |
| ☐ | LIFE-L094-A2 | Collective swarm behavior | Quorum-sensing patch migration decisions |
| ☐ | LIFE-L094-A3 | Collective swarm behavior | Phase entrainment to shared in-world solar/acoustic pulses |
| ☐ | LIFE-L094-A4 | Collective swarm behavior | Emergent sentinel, forager & brood-care castes |
| ☐ | LIFE-L094-A5 | Collective swarm behavior | Colonial vascularly linked zooid option (`SOFT39`) |
| ☐ | LIFE-L095-A1 | Causal wiring integrity | Complete machine-readable organ coupling DAG |
| ☐ | LIFE-L095-A2 | Causal wiring integrity | Universal `lesion()` & `shamLesion()` hooks |
| ☐ | LIFE-L095-A3 | Causal wiring integrity | Automated C-NC zero-cosmetic-parts sweep |
| ☐ | LIFE-L095-A4 | Causal wiring integrity | Perturbation -> downstream Δtrajectory verified |
| ☐ | LIFE-L095-A5 | Causal wiring integrity | AST static audit banning hidden scripted helpers |
| ☐ | LIFE-L096-A1 | Controlled stochasticity | Recorded QRNG / keyed Philox4x32-10 streams |
| ☐ | LIFE-L096-A2 | Controlled stochasticity | WORLD_EXOG vs ENTITY_INT PRNG isolation |
| ☐ | LIFE-L096-A3 | Controlled stochasticity | Bit-exact `.alifebin` snapshot/restore |
| ☐ | LIFE-L096-A4 | Controlled stochasticity | Self-tuned σ≈1 avalanche criticality |
| ☐ | LIFE-L096-A5 | Controlled stochasticity | Neutral drift & shuffled-stream null models |
| ☐ | LIFE-L097-A1 | Non-copied xenobiology | Original electro/lateral-line/plume sensor mixes |
| ☐ | LIFE-L097-A2 | Non-copied xenobiology | Optional Q≤10 register tested vs classical baseline |
| ☐ | LIFE-L097-A3 | Non-copied xenobiology | Non-anthropomorphic radial/segmented hydrostats |
| ☐ | LIFE-L097-A4 | Non-copied xenobiology | De-novo organlet differentiation under selection |
| ☐ | LIFE-L097-A5 | Non-copied xenobiology | Configurable non-standard stoichiometric chemistries |
| ☐ | LIFE-L098-A1 | Volumetric soft mechanics | Tracked coelomic volume V(t) (`\|ΔV\|/V_0 < 1%`) |
| ☐ | LIFE-L098-A2 | Volumetric soft mechanics | Pressurized defensive body expansion |
| ☐ | LIFE-L098-A3 | Volumetric soft mechanics | ATP-costly narrow-aperture traversal |
| ☐ | LIFE-L098-A4 | Volumetric soft mechanics | Explicit elastic + pressure work ledger booking |
| ☐ | LIFE-L098-A5 | Volumetric soft mechanics | Proprioceptive body-volume & strain readout |
| ☐ | LIFE-L099-A1 | Sandboxed in-world levers | Detects environmental parameter step-changes |
| ☐ | LIFE-L099-A2 | Sandboxed in-world levers | Learns instrumental value of legal physical switches |
| ☐ | LIFE-L099-A3 | Sandboxed in-world levers | Rate-limited & kJ-priced dome mechanics (0 host access) |
| ☐ | LIFE-L099-A4 | Sandboxed in-world levers | Immutable tamper-evident intervention log |
| ☐ | LIFE-L099-A5 | Sandboxed in-world levers | Forecasts consequences of own niche modifications |
| ☐ | LIFE-L100-A1 | Preregistered lab rigor | Written hypothesis & thresholds locked pre-test |
| ☐ | LIFE-L100-A2 | Preregistered lab rigor | Tier-1 cross-OS SHA-256 hash verification |
| ☐ | LIFE-L100-A3 | Preregistered lab rigor | Strict Practice / Tuning / Burn-on-Fail Test split |
| ☐ | LIFE-L100-A4 | Preregistered lab rigor | Headless CI gate (`GATE-01..13`) |
| ☐ | LIFE-L100-A5 | Preregistered lab rigor | Power-sized paired seeds + Holm-Bonferroni FWER |

### Suite 6 — NOVEL-100 Frontier & Open-Ended Capabilities (100)

| St | ID | Group | Capability | Operational Mechanism & Control |
| --- | --- | --- | --- | --- |
| ☐ | N01 | A. Quantum-inspired & geometric interior (mandatory classical controls on N01–N08) | Berry-phase circadian clock | Estimates photoperiod phase from geometric phase of a `Q ≤ 4` internal state; benchmarked against parameter-matched classical `SO(2)` phase ring. |
| ☐ | N02 | A. Quantum-inspired & geometric interior (mandatory classical controls on N01–N08) | Fubini–Study state-change surprise | Stepwise Fubini–Study angle between internal states drives salience; must match or beat classical cosine-distance surprise at equal FLOPs. |
| ☐ | N03 | A. Quantum-inspired & geometric interior (mandatory classical controls on N01–N08) | Topological winding-number mood lock | Discrete integer winding invariant prevents chattering mood flips from subthreshold noise while permitting true bifurcation switches. |
| ☐ | N04 | A. Quantum-inspired & geometric interior (mandatory classical controls on N01–N08) | Metric-preconditioned natural plasticity | Updates preconditioned by diagonal/block Fisher or quantum geometric metric reduce overshoot (`≥ 20%` fewer oscillations vs Euclidean SGD). |
| ☐ | N05 | A. Quantum-inspired & geometric interior (mandatory classical controls on N01–N08) | Statistical chance literacy | Runs/entropy monitor distinguishes pure `50/50` unlearnable noise dials from structured contingencies and suppresses superstitious `Δw` churn (`≥ 60%` churn drop). |
| ☐ | N06 | A. Quantum-inspired & geometric interior (mandatory classical controls on N01–N08) | Endogenous measurement-basis control | Selects readout projection angle of internal state register to modulate exploratory variance intentionally vs fixed-basis ablation. |
| ☐ | N07 | A. Quantum-inspired & geometric interior (mandatory classical controls on N01–N08) | Non-commuting context order effects | Sequential evaluation through non-commuting projections reproduces lawful context/framing sensitivity tested on reversed cue pairs. |
| ☐ | N08 | A. Quantum-inspired & geometric interior (mandatory classical controls on N01–N08) | State-trajectory path-length sleep drive | Process-S sleep pressure integrates intrinsic manifold path length traveled while awake (`r ≥ 0.70` with post-wake NREM delta need). |
| ☐ | N09 | A. Quantum-inspired & geometric interior (mandatory classical controls on N01–N08) | Trajectory-curvature metacognitive brake | Sharp intrinsic curvature `κ(t)` of hidden neural trajectories triggers hesitation, active gaze scanning, and workspace re-ignition. |
| ☐ | N10 | A. Quantum-inspired & geometric interior (mandatory classical controls on N01–N08) | Riemannian danger-geodesic planning | Plans detours along metric-weighted danger geodesics (`cost = d_s · (1 + λ·p_harm)`), reducing hazard damage `≥ 40%` vs Euclidean shortest path. |
| ☐ | N11 | B. Self-modification by endogenous Ring-1/2 operators | Ring-guarded endogenous gain surgery | Attenuates or boosts `Ring-1` specialist couplings via `WSE-OP01` when internal forward model predicts net survival lift (`Ring-0` untouched). |
| ☐ | N12 | B. Self-modification by endogenous Ring-1/2 operators | Pre-task neuromodulatory self-priming | Releases bounded preparatory `NE/ACh` gain shift prior to entering known high-predation or high-precision zones. |
| ☐ | N13 | B. Self-modification by endogenous Ring-1/2 operators | Visceral pre-motor 'Free Won't' veto | Cancels initiated motor impulse within `50 ms` when forward visceral predictor forecasts lethal pressure/ATP loss (`M068`). |
| ☐ | N14 | B. Self-modification by endogenous Ring-1/2 operators | Sleep sensitivity-probe tagging | Injects micro-perturbations during NREM/REM to estimate synapse survival salience and shields top-ranked wires against complement pruning. |
| ☐ | N15 | B. Self-modification by endogenous Ring-1/2 operators | ATP-paid cortical checkpoint & rollback | Spends booked `E_atp` prior to acute hazard to store `< 64 KB` `Ring-1` XOR checkpoint and restores on severe nociceptive trauma (`D_creature` scope). |
| ☐ | N16 | B. Self-modification by endogenous Ring-1/2 operators | Longitudinal weight-drift self-audit | Monitors cosine divergence of `Ring-1` weights from post-juvenile anchor and elevates caution/consolidation when drift spikes. |
| ☐ | N17 | B. Self-modification by endogenous Ring-1/2 operators | Endogenous pre-action calibration commit | Commits scalar payoff/sensory forecast prior to action execution and down-weights chronically overconfident specialist voters (`ECE ≤ 0.08`). |
| ☐ | N18 | B. Self-modification by endogenous Ring-1/2 operators | Metabolic ATP plasticity auction | Parallel specialists bid `E_atp` proportional to local TD/prediction surprise for bounded per-step synaptic write bandwidth. |
| ☐ | N19 | B. Self-modification by endogenous Ring-1/2 operators | Active extinction of stale superstitions | Targeted LTD/unbinding clears high-cost defensive Traces after `≥ K` safe disconfirmations (`≥ 50%` faster recovery vs passive decay). |
| ☐ | N20 | B. Self-modification by endogenous Ring-1/2 operators | Dynamic visceral perfusion arbitration | Allostatic hub reallocates circulating glucose/O2 between brain, gut, and locomotor muscle according to acute survival phase. |
| ☐ | N21 | C. Sandboxed regime & replayable-substrate inference (zero host wall-clock leak) | Replayable `.sensorlog` step-budget sense | Reads deterministic recorded step-budget counter from `.sensorlog` (`0` live `performance.now()` calls in Tier-1!) and adapts plan horizon. |
| ☐ | N22 | C. Sandboxed regime & replayable-substrate inference (zero host wall-clock leak) | Online latent physics-dial estimation | Continuously infers dome gravity, fluid viscosity, thermal conductivity, and solar period as explicit latent context variables (`R² ≥ 0.75`). |
| ☐ | N23 | C. Sandboxed regime & replayable-substrate inference (zero host wall-clock leak) | Visceral enthalpy-anomaly avoidance | Detects mismatch between ingested oral expectation and absorbed `E_gut` enthalpy (`N99`) or corrupted test zones and avoids them. |
| ☐ | N24 | C. Sandboxed regime & replayable-substrate inference (zero host wall-clock leak) | Snapshot-branch state-recurrence sense | Detects exact sensory-visceral sequence match against episodic ring after sandbox branch/replay and adapts choice immediately. |
| ☐ | N25 | C. Sandboxed regime & replayable-substrate inference (zero host wall-clock leak) | Compute-scarcity horizon throttling | Under recorded high-load regime dials, smoothly truncates planning depth `G_plan` before violating action deadlines. |
| ☐ | N26 | C. Sandboxed regime & replayable-substrate inference (zero host wall-clock leak) | Logged dome-intervention contingency | Learns lawful contingencies between display actions and preregistered automated dome-supply dispensers (strictly in-world). |
| ☐ | N27 | C. Sandboxed regime & replayable-substrate inference (zero host wall-clock leak) | Post-switch boundary exploration surge | Elevates epistemic exploration specifically after `NE` unexpected-uncertainty detector flags an environmental rule change. |
| ☐ | N28 | C. Sandboxed regime & replayable-substrate inference (zero host wall-clock leak) | Multi-dome regime self-localization | Identifies which archipelago dome biome (`aquatic, arid, high-drag, cold`) it occupies within `≤ 200` sensory steps. |
| ☐ | N29 | C. Sandboxed regime & replayable-substrate inference (zero host wall-clock leak) | Blank-episodic / mature-soma adaptation | When spawned with empty `CA3` episodic buffer inside an adult body, elevates social observation weight from experienced peers. |
| ☐ | N30 | C. Sandboxed regime & replayable-substrate inference (zero host wall-clock leak) | Self-inspection ATP budgeting | Accounts for exact `E_atp` cost of active electrolocation, saccades, and `WSE` self-probes, silencing costly probes during fasting. |
| ☐ | N31 | D. Non-anthropomorphic & active sensory modalities | Coarse cortical-activity interoception | Reads `O(1)` regional firing-rate & synchrony summary of its own brain as an internal cognitive-effort channel. |
| ☐ | N32 | D. Non-anthropomorphic & active sensory modalities | Contact-range bioelectric peer reading | Detects neighbor muscle/spike dipole field at `< 2` body lengths (inverse-cube attenuated) to anticipate lunges or cooperation. |
| ☐ | N33 | D. Non-anthropomorphic & active sensory modalities | Secreted fatigue-metabolite chemosense | Detects local peer adenosine/lactate exhalation to coordinate staggered sentinel sleep shifts (`N54`). |
| ☐ | N34 | D. Non-anthropomorphic & active sensory modalities | Spatial metabolic-rate zone navigation | Maps dome temperature/nutrient-regrowth rate gradients (`Q10` zones) to rest in cool refuges and forage in productive warm bands. |
| ☐ | N35 | D. Non-anthropomorphic & active sensory modalities | Somatic damage-rate radiation avoidance | Senses elevated cellular ROS / mutation stress in hazardous patches via visceral damage afferents and retreats to shielded cover. |
| ☐ | N36 | D. Non-anthropomorphic & active sensory modalities | Behavioral photoperiod self-entrainment | Regulates burrow-shade vs sunlit exposure timing to keep SCN circadian clock phase-locked to brief food blooms. |
| ☐ | N37 | D. Non-anthropomorphic & active sensory modalities | Topographic slope & substrate-stiffness map | Uses ground incline and viscoelastic substrate compliance as non-visual dead-reckoning landmarks in total darkness. |
| ☐ | N38 | D. Non-anthropomorphic & active sensory modalities | Contact MHC / surface-peptide kin assay | Reads heritable surface-marker cosine similarity upon compliant touch to gate kin altruism and outbred mate choice. |
| ☐ | N39 | D. Non-anthropomorphic & active sensory modalities | Context-illusion discount learning | Initially exhibits surround-contrast perceptual bias, then learns top-down precision discounts when payoff feedback disconfirms illusion. |
| ☐ | N40 | D. Non-anthropomorphic & active sensory modalities | Goal-steered bistable percept switching | Top-down workspace bias flips interpretation of ambiguous figure-ground/plume mixtures according to current homeostatic need. |
| ☐ | N41 | E. Sleep, replay & bounded transgenerational priors | Bounded maternal developmental priming | Validated maternal survival niche biases `1–2` low-dimensional epigenetic receptor/gain priors in yolk (**explicitly non-Lamarckian: zero weight-matrix copy**). |
| ☐ | N42 | E. Sleep, replay & bounded transgenerational priors | Acoustic/tactile huddle replay cueing | Co-sleeping kin emit low-amplitude rhythmic cues biasing which shared daytime hazard landmarks undergo NREM replay. |
| ☐ | N43 | E. Sleep, replay & bounded transgenerational priors | Trauma-proportional threat replay | Post-predator NREM/REM defensive escape rehearsal frequency scales monotonically with daytime nociceptive/fear load. |
| ☐ | N44 | E. Sleep, replay & bounded transgenerational priors | Reality-monitored REM rollout steering | `HOT-1` tags REM rollouts as endogenous (`is_dream = 1`) while steering counterfactual branches toward high-uncertainty map frontiers. |
| ☐ | N45 | E. Sleep, replay & bounded transgenerational priors | REM epistemic-uncertainty tagging | REM synthesis writes variance/curiosity tags—never false experienced visit counts—preventing delusional food-patch certainty. |
| ☐ | N46 | E. Sleep, replay & bounded transgenerational priors | REM-synthesized display motif spread | Novel call/chromatophore sequences recombined during REM persist and spread culturally if positively reinforced in waking bouts. |
| ☐ | N47 | E. Sleep, replay & bounded transgenerational priors | Stress-modulated germline variance | Chronic unresolved allostatic load elevates offspring mutation step-size within safe canalized bounds (`M088`). |
| ☐ | N48 | E. Sleep, replay & bounded transgenerational priors | Reversible F1 toxin-caution mark | Parental acute poisoning elevates F1 juvenile bitter-rejection gain for `1–2` generations, decaying cleanly without re-exposure. |
| ☐ | N49 | E. Sleep, replay & bounded transgenerational priors | Ultra-slow torpor maintenance ticks | During cryptobiotic/torpor arrest (`< 2%` basal burn), periodic low-energy checkpoints preserve core `Fusi` cascade memories. |
| ☐ | N50 | E. Sleep, replay & bounded transgenerational priors | Quantum vs PRNG REM diversity audit | Controlled benchmark comparing `Q ≤ 8` superposition vs `Philox4x32-10` REM rollouts at matched parameters (`parity or lift` honestly reported). |
| ☐ | N51 | F. Social markets, horizontal niche plasmids & culture | ATP-settled horizontal skill-packet trade | In horizontal-plasmid niche mode, mentor emits `< 4 KB` landmark/policy cue vector in exchange for booked caloric trophallaxis. |
| ☐ | N52 | F. Social markets, horizontal niche plasmids & culture | MHC-gated plasmid validation sandbox | Evaluates received peer weight/cue packets in Tier-1 shadow rollout and rejects norm-violating (`‖W‖_2 > 0.99`) or adversarial grafts. |
| ☐ | N53 | F. Social markets, horizontal niche plasmids & culture | Cryptographic/MHC kin-signature check | Verifies heritable biochemical kin distance before costly nursing (`M090`) or predator-distraction alarm calls. |
| ☐ | N54 | F. Social markets, horizontal niche plasmids & culture | Emergent staggered sentinel sleep | Social clusters self-organize anti-phase sleep schedules so `≥ 1` waking sentinel maintains predator watch (`≥ 35%` ambush survival lift). |
| ☐ | N55 | F. Social markets, horizontal niche plasmids & culture | Targeted waking-to-juvenile cueing | Experienced adult slows foraging actions and emits contact cues near naive juveniles, halving juvenile trial-to-competence. |
| ☐ | N56 | F. Social markets, horizontal niche plasmids & culture | Predator-triggered collective blanket | Dispersed grazers contract into a high-cohesion defensive ring under alarm plumes, reducing per-capita predation. |
| ☐ | N57 | F. Social markets, horizontal niche plasmids & culture | Distributed swarm gradient pooling | Coupled swarm tracks noisy moving resource peaks with `≤ 0.65×` estimation RMSE of isolated solo clones. |
| ☐ | N58 | F. Social markets, horizontal niche plasmids & culture | Allopatric chromatophore/call dialects | Isolated sub-populations diverge into statistically separable (`F_ST` / classifier `Acc ≥ 0.80`) learned display dialects. |
| ☐ | N59 | F. Social markets, horizontal niche plasmids & culture | Zahavi ATP-proportional signal honesty | High-amplitude courtship/dominance calls deduct steep `E_atp` so depleted bluffers cannot sustain deceptive signaling. |
| ☐ | N60 | F. Social markets, horizontal niche plasmids & culture | Pairwise reciprocity & defector boycott | Episodic social memory tracks net caloric/aid balance per peer ID and withholds sharing from chronic non-reciprocators. |
| ☐ | N61 | G. Soft continuum mechanics & adaptive morphology | Inducible mucosal/cuticle toxin shield | Thickens outer protective barrier under chemical hazard at a measurable locomotor drag and `E_atp` penalty (`CNF-03`). |
| ☐ | N62 | G. Soft continuum mechanics & adaptive morphology | Hydrostatic cavity acoustic resonance | Call fundamental frequency `f_0` scales inversely with coelomic chamber radius, physically anchoring body-size honesty. |
| ☐ | N63 | G. Soft continuum mechanics & adaptive morphology | Context-switched crypsis vs display | Suppresses high-contrast courtship patterns within `< 200 ms` of predator looming/wake detection. |
| ☐ | N64 | G. Soft continuum mechanics & adaptive morphology | Facultative colonial zooid coupling | Compatible kin hydrostats reversibly link vascular/mucus junctions (`SOFT39`) to share nutrients across patchy gradients. |
| ☐ | N65 | G. Soft continuum mechanics & adaptive morphology | Bioelectric appendage-primordia count | Embryonic `V_mem` Turing peaks determine segment/lobe count (`2..6` lobes) from compact GRN rules. |
| ☐ | N66 | G. Soft continuum mechanics & adaptive morphology | Viscoelastic passive posture memory | Slow Kelvin-Voigt tissue relaxation holds defensive curl or grip preload for seconds at zero central spike burn. |
| ☐ | N67 | G. Soft continuum mechanics & adaptive morphology | Booked famine/trap lobe autotomy | Cleanly severs trapped peripheral lobe along fracture plane (debiting exact biomass to world carcass) and regrows via blastema when fed. |
| ☐ | N68 | G. Soft continuum mechanics & adaptive morphology | Mechanotransductive strut thickening | Sustained high-gravity/load strain thickens load-bearing biotensegrity elements within lifetime (`SOFT34`). |
| ☐ | N69 | G. Soft continuum mechanics & adaptive morphology | Myoclonic REM forward-model calibration | Phasic REM muscle twitches sample proprioceptive Jacobians to recalibrate `AE-2` body schema after growth or autotomy. |
| ☐ | N70 | G. Soft continuum mechanics & adaptive morphology | Active peering motion-parallax rangefinding | Lateral head/body oscillation computes metric obstacle/prey distance from optic bearing-rate (`RMSE ≤ 12%` of range). |
| ☐ | N71 | H. Closed-biosphere niche construction & coevolution | Local albedo & shade microclimate modification | Pigmented colonies/structures alter local patch solar absorption and soil moisture retention (`M098`). |
| ☐ | N72 | H. Closed-biosphere niche construction & coevolution | Curriculum-hardened lineage resilience | Populations evolved across stepped drought/toxin regimes survive held-out compound shocks at `≥ 2.0×` naive-stock survival. |
| ☐ | N73 | H. Closed-biosphere niche construction & coevolution | Relaxed-selection trait regression | Lineages maintained for `≥ 50` generations in benign predator-free abundance downsize costly armor/venom organs (`ATP` economy proof). |
| ☐ | N74 | H. Closed-biosphere niche construction & coevolution | Host-parasite manipulation & bitter meds | Parasite load biases host risk-taking until host learns prophylactic ingestion of bitter anti-parasitic patches (`M097`). |
| ☐ | N75 | H. Closed-biosphere niche construction & coevolution | Diurnal vs nocturnal temporal partitioning | Competing sympatric consumers diverge circadian phase preferences to reduce direct interference competition. |
| ☐ | N76 | H. Closed-biosphere niche construction & coevolution | Elapsed-time spoilage cache management | Associates cached food items with circadian age (`episodic what-where-when`), retrieving fresh items before microbial rot. |
| ☐ | N77 | H. Closed-biosphere niche construction & coevolution | Hazard-rate storm preparation learner | Estimates inter-arrival hazard distribution of stochastic thermal/drought shocks and pre-accumulates lipid reserves (`N77` uppercase canonical). |
| ☐ | N78 | H. Closed-biosphere niche construction & coevolution | Three-guild non-exploding persistence | Autotroph patches, soft grazers, and predators coexist for `≥ 50,000` ecological seconds without extinction or `NaN`/infinite population. |
| ☐ | N79 | H. Closed-biosphere niche construction & coevolution | Enthalpy-conserving archipelago migration | Organisms crossing inter-dome bridges transfer exact somatic + gut + store `FP64` enthalpy between dome ledgers (`\|ΔE\| < 1e-12`). |
| ☐ | N80 | H. Closed-biosphere niche construction & coevolution | Nitrogenous detritus grazing gardens | Localized waste deposition enriches soil mineral pools, accelerating subsequent primary patch regrowth. |
| ☐ | N81 | I. Second-order self-modeling & identity continuity | Confidence-gated `WSE` execution | Blocks endogenous `WSE` self-edits whenever `HOT-2` world-model confidence falls below preregistered safety margin. |
| ☐ | N82 | I. Second-order self-modeling & identity continuity | Motor-tremor vs external-current separation | Kalman/predictive filter distinguishes intrinsic actuator noise variance from exogenous fluid current shear. |
| ☐ | N83 | I. Second-order self-modeling & identity continuity | Nested first- & second-order state readout | Simultaneously decodes bodily fuel level (`x̂`) and calibrated error variance (`σ̂²_x`) from distinct internal populations. |
| ☐ | N84 | I. Second-order self-modeling & identity continuity | Post-sleep duration & architecture readout | Waking state accurately encodes elapsed sleep duration and NREM/REM ratio (`R² ≥ 0.70` vs time-blind wake control). |
| ☐ | N85 | I. Second-order self-modeling & identity continuity | Prodromal organ-decline resting | Detects early slope degradation in repair/perfusion kinetics and initiates parasympathetic rest prior to acute failure. |
| ☐ | N86 | I. Second-order self-modeling & identity continuity | Uncertainty-modulated alarm intensity | Acoustic/skin alarm amplitude reflects calibrated predator-detection certainty, reducing false-panic herd stampedes. |
| ☐ | N87 | I. Second-order self-modeling & identity continuity | Zero-effort disengagement from pure noise | Stops paying active-sensing `E_atp` on verified zero-mutual-information decoy channels within `≤ 500` ticks. |
| ☐ | N88 | I. Second-order self-modeling & identity continuity | Quantified self-symbol causal loop gain | Intervening on the compressed self-state vector (`clamp/perturb`) produces lawful downstream shifts in policy risk posture. |
| ☐ | N89 | I. Second-order self-modeling & identity continuity | Cross-metamorphosis aversion & self remap | Retains larval conditioned toxin odor aversion (`≥ 70%` retention, Blackiston 2008) while remapping adult motor kinematics (`SOFT35`, `M084`). |
| ☐ | N90 | I. Second-order self-modeling & identity continuity | Unified anomaly caution index | Fuses visceral ledger residuals, unexpected `NE` regime jumps, and boundary collisions into calibrated exploratory braking. |
| ☐ | N91 | J. Bioenergetics & physiological state transitions | Photoperiodic pre-winter fattening | Shortening day-length cue shifts `F-033` rheostatic lipid set-point upward ahead of solar minimum. |
| ☐ | N92 | J. Bioenergetics & physiological state transitions | Ketotic wide-area search transition | Phase-II `β-HB` ketone elevation shifts foraging policy from local exploitation to thrifty wide-area Lévy search. |
| ☐ | N93 | J. Bioenergetics & physiological state transitions | Thermally scheduled NREM remodeling | Concentrates high-cost protein synthesis and morphogenesis inside thermally neutral microclimate windows. |
| ☐ | N94 | J. Bioenergetics & physiological state transitions | Reversible famine cortical down-clocking | Silences high-tier associative spheres (`Level 2/3`) during severe Phase-II/III fasting while keeping `Level 1` foraging/brainstem active (`≥ 35%` ATP save). |
| ☐ | N95 | J. Bioenergetics & physiological state transitions | Hormonal half-life affective bridge | Slow endocrine clearance (`τ = 30–300 s`) bridges aversive/nutritive context across silent intervals at `0` spike cost. |
| ☐ | N96 | J. Bioenergetics & physiological state transitions | Cytokine-potentiated one-trial aversion | Coincident immune fever (`IL-1β`-like surge) amplifies Garcia taste-aversion learning rate `≥ 2×` on novel foods. |
| ☐ | N97 | J. Bioenergetics & physiological state transitions | Deficit-selective NREM replay prioritization | Specific amino-acid or mineral deficiency selectively up-weights NREM replay of patches rich in the missing precursor. |
| ☐ | N98 | J. Bioenergetics & physiological state transitions | Diurnal risk-entropy modulation | Balances high early-window exploration when reserves/light are favorable with conservative refuge return before dusk. |
| ☐ | N99 | J. Bioenergetics & physiological state transitions | Post-absorptive caloric honesty check | Extinguishes preference for sweet zero-enthalpy saccharin-like lures within `≤ 3` post-absorptive bouts (`M018`). |
| ☐ | N100 | J. Bioenergetics & physiological state transitions | Salience-ordered terminal memory shedding | Under extreme metabolic triage, sheds low-salience peripheral tags first while preserving core foraging/toxin skills (`≥ 2.0×` retention vs random drop). |

### Suite 7 — WSE-12 Weight-Space Editing Algebra & Safety (12)

| St | ID | Invariant | Contract & Fault-Injection Gate |
| --- | --- | --- | --- |
| ☐ | WSE01 | Typed 10-operator algebra | Every weight-space edit executes exclusively through `WSE-OP01..10` with declared domain, units, norm preconditions, and ATP cost. |
| ☐ | WSE02 | Tokenless tensor/graph native | Operates directly on `SoA` weight blocks, `structuralMask` bitsets, and 3D coordinates—zero LLM prompts or text tokens. |
| ☐ | WSE03 | Forward-model delta prediction | Internal world/self model logs predicted behavioral & metabolic `Δ` prior to applying an edit; post-edit calibration error is audited. |
| ☐ | WSE04 | Norm-matched weight scaling | `WSE-OP01` shifts target behavioral gain significantly (`δ_pair ≥ 0.33`) against a Frobenius-norm-matched random-direction sham edit. |
| ☐ | WSE05 | Continuous excitability bias field | `WSE-OP04` paints smooth spatial threshold/gain fields over cortical sheets while keeping rates inside `[0, r_max]`. |
| ☐ | WSE06 | 3D coordinate & CSR-overlay sculpting | `WSE-OP03/05` updates 3D unit positions, integer delays, and explicit `CSR` delta overlays (when base blocks are procedural). |
| ☐ | WSE07 | Algebraic VSA / Hopfield relation edit | `WSE-OP06` binds, unbinds, or reweights associative relations in `O(D_lat)` without retraining unrelated stored episodes. |
| ☐ | WSE08 | Compact `< 16 KB` single-edit diff | Each individual operator application emits a versioned sparse/low-rank delta (`< 16 KB`; vs `< 64 KB` full-creature tick checkpoint in `HW06`). |
| ☐ | WSE09 | Domain-scoped bit-exact rollback | Reverting an edit restores the exact pre-edit SHA-256 hash within its declared rollback domain (`D_creature`, `D_coupled_patch`, or `D_full_sim`). |
| ☐ | WSE10 | 3-Tier contractive verification gate | Enforces Tier-0 online `‖W‖_2 ≤ 0.99` + ATP check (`< 0.1 ms`), Tier-1 sleep shadow rollout, and Tier-2 locked non-inferiority (`LCB_95% > -Δ_NI`). |
| ☐ | WSE11 | Hardware-enforced `Ring-0` immutability | Endogenous `WSE` writes only `Ring-1/2` buffers at booked ATP cost; `Ring-0` (`brainstem, nociception, ledger, harness`) throws on write. |
| ☐ | WSE12 | Lossless audit log & Tab-17/18 export | Every edit, predicted-vs-realized delta, norm bound, and rollback event streams losslessly to `Tab 15/17` and `.alifebin`/Parquet manifests. |

### Suite 8 — SOFT-40 Hydrostatic, Viscoelastic & Wetware Capabilities (40)

| St | ID | Group | Capability | Quantitative Contract |
| --- | --- | --- | --- | --- |
| ☐ | SOFT01 | A. Hydrostatic skeletons, XPBD viscoelasticity & biotensegrity (SOFT01–SOFT10) | Incompressible hydrostatic coelom | Closed fluid-filled cavity conserving volume (`\|ΔV\|/V_0 < 0.01`) so radial muscle contraction drives axial extension. |
| ☐ | SOFT02 | A. Hydrostatic skeletons, XPBD viscoelasticity & biotensegrity (SOFT01–SOFT10) | Compliance-scaled XPBD membrane | Viscoelastic cuticle integrated via `α̃ = α / dt²` (`0` Euler `NaN` blowups under `10×` nominal impact velocity). |
| ☐ | SOFT03 | A. Hydrostatic skeletons, XPBD viscoelasticity & biotensegrity (SOFT01–SOFT10) | Pre-stressed biotensegrity web | Continuous tension-cable network + discontinuous compression struts distributing localized impact strain globally. |
| ☐ | SOFT04 | A. Hydrostatic skeletons, XPBD viscoelasticity & biotensegrity (SOFT01–SOFT10) | Mutable catch-state stiffness | Collagen-like rapid compliance modulation (`≥ 10×` stiffness dynamic range) trading low-ATP posture lock against squeeze agility. |
| ☐ | SOFT05 | A. Hydrostatic skeletons, XPBD viscoelasticity & biotensegrity (SOFT01–SOFT10) | Narrow-aperture compression traversal | Compresses cross-section to `≤ 0.55×` resting diameter at booked `ATP + ΔP·dV` cost to traverse crevices blocking rigid clones. |
| ☐ | SOFT06 | A. Hydrostatic skeletons, XPBD viscoelasticity & biotensegrity (SOFT01–SOFT10) | First-Law elastic recoil & `E_diss_num` | Stores reversible strain energy in `E_elastic` (`≥ 60%` cyclic return) and books positive XPBD numerical damping strictly to `E_diss_num ≥ 0`. |
| ☐ | SOFT07 | A. Hydrostatic skeletons, XPBD viscoelasticity & biotensegrity (SOFT01–SOFT10) | Valved multi-chamber pressure routing | Active inter-chamber sphincters shunt coelomic pressure `P_1..P_k` to extend/curl selected soft lobes independently. |
| ☐ | SOFT08 | A. Hydrostatic skeletons, XPBD viscoelasticity & biotensegrity (SOFT01–SOFT10) | Equal-competence neural spike offload | Once Stage-4 brain is wired, compliant body achieves **`≥ 50%` fewer central spikes/meter at non-inferior speed & failure rate** vs stiffened `α→0` clone. |
| ☐ | SOFT09 | A. Hydrostatic skeletons, XPBD viscoelasticity & biotensegrity (SOFT01–SOFT10) | Conformable soft-pad friction grasp | High-compliance distal pad conforms around irregular stones/food (`≥ 2.0×` contact area & pullout force vs rigid point contact). |
| ☐ | SOFT10 | A. Hydrostatic skeletons, XPBD viscoelasticity & biotensegrity (SOFT01–SOFT10) | Active buoyancy / density regulation | Adjusts internal gas/lipid ballast to hold depth station in aquatic columns at `≤ 25%` of continuous-swimming fin ATP cost. |
| ☐ | SOFT11 | B. Continuum locomotion, fluids, adhesion & wound repair (SOFT11–SOFT20) | Peristaltic retrograde/direct waves | Traveling axial-radial contraction waves propel soft soma through confined burrows and high-friction substrates. |
| ☐ | SOFT12 | B. Continuum locomotion, fluids, adhesion & wound repair (SOFT11–SOFT20) | Low- vs high-Reynolds aquatic modes | Captures non-reciprocal undulatory/ciliary thrust at `Re ≪ 1` and inertial vortex shedding at `Re ≫ 1` under drag laws. |
| ☐ | SOFT13 | B. Continuum locomotion, fluids, adhesion & wound repair (SOFT11–SOFT20) | Sol-gel amoeboid cytoplasmic crawl | Front cortical tension release + rear actomyosin-like squeeze drives protrusion and engulfment on flat substrates. |
| ☐ | SOFT14 | B. Continuum locomotion, fluids, adhesion & wound repair (SOFT11–SOFT20) | ATP-gated wet adhesion & suction | Switchable mucus adhesion / pressure-cup suction holds station against fluid shear (`≥ 3.0×` slip threshold vs un-adhered control). |
| ☐ | SOFT15 | B. Continuum locomotion, fluids, adhesion & wound repair (SOFT11–SOFT20) | Viscoelastic stigmergic slime trails | Secreted mucus modifies local substrate drag (`-20%` follower cost) and carries decaying chemical provenance. |
| ☐ | SOFT16 | B. Continuum locomotion, fluids, adhesion & wound repair (SOFT11–SOFT20) | Continuum surface strain & slip sheet | Distributed mechanoreceptor field encodes local stretch `ε`, bending curvature `κ`, normal pressure, and tangential slip. |
| ☐ | SOFT17 | B. Continuum locomotion, fluids, adhesion & wound repair (SOFT11–SOFT20) | Membrane puncture leak & coagulation | Sharp hazard breach causes real coelomic `ΔP` drop and nutrient bleed until ATP/protein coagulation seals the aperture. |
| ☐ | SOFT18 | B. Continuum locomotion, fluids, adhesion & wound repair (SOFT11–SOFT20) | Emergency fibrous scar vs blastema | Fast emergency scar seals wounds quickly with `+30%` local stiffness penalty; slow amino-funded blastema restores native compliance. |
| ☐ | SOFT19 | B. Continuum locomotion, fluids, adhesion & wound repair (SOFT11–SOFT20) | Deformable-substrate burrow excavation | Displaces granular soil cells at booked mechanical work to construct thermally buffered predator refuges. |
| ☐ | SOFT20 | B. Continuum locomotion, fluids, adhesion & wound repair (SOFT11–SOFT20) | Hydrodynamic lateral-line wake array | Surface hair-cell gradient detects unseen moving predator/prey dipole wakes at `≥ 4` body lengths in total darkness. |
| ☐ | SOFT21 | C. Wet biochemistry & Gánti Chemoton autopoiesis (SOFT21–SOFT30) | Gánti Chemoton 3-cycle polymer closure | Stoichiometrically locks autocatalytic cycle `A`, membrane lipid `T`, and **template polymer `pV_n` (`n ≥ N*` division threshold)**. |
| ☐ | SOFT22 | C. Wet biochemistry & Gánti Chemoton autopoiesis (SOFT21–SOFT30) | Michaelis-Menten saturating kinetics | All enzymatic & transporter fluxes obey `v = V_max·[S]/(K_m + [S])`, guaranteeing finite rates under bolus loads. |
| ☐ | SOFT23 | C. Wet biochemistry & Gánti Chemoton autopoiesis (SOFT21–SOFT30) | Allosteric end-product feedback | Elevated cytosolic `[ATP]/[ADP]` ratio automatically throttles upstream catabolic burn without central neural intervention. |
| ☐ | SOFT24 | C. Wet biochemistry & Gánti Chemoton autopoiesis (SOFT21–SOFT30) | Active osmotic pump & lysis boundary | `Na+/K+`-like ATPase counters Donnan osmotic influx; sustained ATP collapse causes cellular swelling and membrane lysis. |
| ☐ | SOFT25 | C. Wet biochemistry & Gánti Chemoton autopoiesis (SOFT21–SOFT30) | Anaerobic lactate & pH buffering | Burst exertion above O2 delivery accumulates `[H+/lactate]`, reducing contractile force until cleared via post-sprint Cori oxidation. |
| ☐ | SOFT26 | C. Wet biochemistry & Gánti Chemoton autopoiesis (SOFT21–SOFT30) | Arrhenius `Q10` & thermal denaturation | Reaction and channel rates scale via `Q10` (`~1.8–2.4`) below `T_opt` and suffer steep reversible/irreversible denaturation above `T_max`. |
| ☐ | SOFT27 | C. Wet biochemistry & Gánti Chemoton autopoiesis (SOFT21–SOFT30) | Dietary precursor neurotransmitter caps | Essential amino/choline intake bounds synthesis pools for `5-HT`, `DA/NE`, and `ACh`, coupling diet quality to neural gain. |
| ☐ | SOFT28 | C. Wet biochemistry & Gánti Chemoton autopoiesis (SOFT21–SOFT30) | Aerobic ROS wear vs antioxidant cost | High mitochondrial oxidative flux generates reactive-oxygen tissue damage mitigated by ATP-costly glutathione/SOD synthesis. |
| ☐ | SOFT29 | C. Wet biochemistry & Gánti Chemoton autopoiesis (SOFT21–SOFT30) | Cryptobiotic trehalose vitrification | Pre-drought/freeze bioprotectant synthesis drops metabolic burn to `< 2%` basal while preserving structural + `Fusi` memory state. |
| ☐ | SOFT30 | C. Wet biochemistry & Gánti Chemoton autopoiesis (SOFT21–SOFT30) | Ordered autophagic famine bridge | Phase-II/III starvation recycles non-vital somatic proteins into amino/ATP pools prior to irreversible Ring-0 organ failure. |
| ☐ | SOFT31 | D. Multicellular morphogenesis, Blackiston metamorphosis & symbiogenesis (SOFT31–SOFT40) | Yolk-conserved zygote mitotic cleavage | Multi-chamber soma and neural primordia divide from one founder cell strictly funded by maternal yolk `E_stores` (`\|ΔE\| < 1e-12`). |
| ☐ | SOFT32 | D. Multicellular morphogenesis, Blackiston metamorphosis & symbiogenesis (SOFT31–SOFT40) | Steinberg differential cadherin sorting | Cell-type surface-adhesion matrix `J_{αβ}` self-sorts ectoderm, mesoderm, endoderm, and neural progenitors from perturbed starts. |
| ☐ | SOFT33 | D. Multicellular morphogenesis, Blackiston metamorphosis & symbiogenesis (SOFT31–SOFT40) | Apoptotic lumen & digit sculpting | Programmed cell death carves internal gut/coelom cavities and separates appendage lobes with recycled amino recovery. |
| ☐ | SOFT34 | D. Multicellular morphogenesis, Blackiston metamorphosis & symbiogenesis (SOFT31–SOFT40) | Mechanotransductive `YAP/TAZ` remodeling | Sustained local tensile/compressive stress upregulates structural fiber deposition along principal load trajectories. |
| ☐ | SOFT35 | D. Multicellular morphogenesis, Blackiston metamorphosis & symbiogenesis (SOFT31–SOFT40) | Blackiston-assay holometabolous remap | Larval crawler replaces `≥ 80%` somatic muscle/motor edges in pupa yet **retains larval conditioned odor-toxin aversion (`≥ 70%`, Blackiston 2008)**. |
| ☐ | SOFT36 | D. Multicellular morphogenesis, Blackiston metamorphosis & symbiogenesis (SOFT31–SOFT40) | Ecdysis / molting growth vulnerability | Cuticle-armored morphs must shed stiff outer layer to expand volume, surviving a high-compliance vulnerable post-molt window. |
| ☐ | SOFT37 | D. Multicellular morphogenesis, Blackiston metamorphosis & symbiogenesis (SOFT31–SOFT40) | Bioelectric `V_mem` regeneration polarity | Gap-junction anterior-posterior voltage gradient directs blastema to regrow head sensors anteriorly and propulsors posteriorly. |
| ☐ | SOFT38 | D. Multicellular morphogenesis, Blackiston metamorphosis & symbiogenesis (SOFT31–SOFT40) | Stoichiometric facultative endosymbiosis | Maintains internal phototrophic or detox micro-symbionts under First-Law nutrient exchange and host immune regulation. |
| ☐ | SOFT39 | D. Multicellular morphogenesis, Blackiston metamorphosis & symbiogenesis (SOFT31–SOFT40) | Vascularly linked colonial zooid castes | Budded kin modules remain fluid-coupled and specialize into feeding, propulsion, and reproductive zooids. |
| ☐ | SOFT40 | D. Multicellular morphogenesis, Blackiston metamorphosis & symbiogenesis (SOFT31–SOFT40) | Closed carcass biogeochemical lysis | Post-mortem soft soma mineralizes `100%` of remaining carbon/nitrogen/enthalpy back into dome `E_detritus` (`\|ΔE\| < 1e-12`). |

### Suite 9 — HW-24 Compute Arenas, Packed Bit-Blocks & Determinism Guards (24)

| St | ID | Group | Hardware Guard | Verification Gate |
| --- | --- | --- | --- | --- |
| ☐ | HW01 | A. Memory arenas, explicit byte accounting & zero-allocation loop (HW01–HW06) | Flat Structure-of-Arrays (SoA) arenas | All neuron, synapse, soft-vertex, and chemical states reside in pre-allocated contiguous `TypedArray` arenas (`0` per-synapse heap objects). |
| ☐ | HW02 | A. Memory arenas, explicit byte accounting & zero-allocation loop (HW01–HW06) | 10,000-tick zero-allocation & fixed WASM | Profiler verifies **`0` heap allocations, `0` `BigInt` boxes, `0` WASM `memory.grow` calls, and `0` lossless-ring drops** across `10,000` post-warmup ticks. |
| ☐ | HW03 | A. Memory arenas, explicit byte accounting & zero-allocation loop (HW01–HW06) | Tiled sparse CSR (`5.25 B/syn` FP16) | Uses tiled `uint16` CSR (`≤ 65,536` units/tile + base table, `5.25 B/syn`) or `uint32` CSR (`9.25 B/syn`); never dense `4N²` at sparse `ρ ≤ 10%`. |
| ☐ | HW04 | A. Memory arenas, explicit byte accounting & zero-allocation loop (HW01–HW06) | 32-synapse packed `int4`/`b1.58` + inventory | Packs 32 synapses into `28 B` (`int4 = 0.875 B/syn`) or `19 B` (`b1.58 = 0.594 B/syn`); budgets `+0.40 B/syn` sparse plasticity ring & `CSR` overlay separately. |
| ☐ | HW05 | A. Memory arenas, explicit byte accounting & zero-allocation loop (HW01–HW06) | Fixed-capacity circular buffers | Every spike queue, episodic trace, and telemetry channel uses power-of-two ring buffers with explicit overflow policy (`0` unbounded `.push()`). |
| ☐ | HW06 | A. Memory arenas, explicit byte accounting & zero-allocation loop (HW01–HW06) | Bounded `< 64 KB` creature XOR checkpoints | Full-organism incremental rollback checkpoints compress via sparse XOR delta to `< 64 KB` (while single `WSE` edits stay `< 16 KB`, `WSE08`). |
| ☐ | HW07 | B. Algorithmic complexity, stiff chemistry & multirate clocks (HW07–HW12) | `O(N_pop + C_pairs)` broad-phase physics | Uniform spatial hash / BVH bounds broad-phase world collisions and field queries to `O(N_pop + C_pairs)` (`0` unconditional `O(N_pop²)` loops). |
| ☐ | HW08 | B. Algorithmic complexity, stiff chemistry & multirate clocks (HW07–HW12) | Integer-guarded `0 ≤ Q ≤ 10` quantum cap | Validates `Number.isInteger(Q) && Q >= 0 && Q <= 10` before allocating `2 * (2 ** Q)` `Float64` entries (`≤ 16 KiB`), preventing `1 << 32 === 1` wraparound. |
| ☐ | HW09 | B. Algorithmic complexity, stiff chemistry & multirate clocks (HW07–HW12) | Event-driven sparse spike rows (`k ≈ 1–4%`) | Gear-1 spike propagation iterates outgoing CSR/packed blocks exclusively for units crossing threshold (`2–8 Hz` biological sparse regime). |
| ☐ | HW10 | B. Algorithmic complexity, stiff chemistry & multirate clocks (HW07–HW12) | 5-Gear Deterministic Multirate Scheduler | Runs integer-divided gears (`0.5ms, 5ms, 50ms, 1s, 60s`) with explicit ZOH/flux handoff, achieving `≥ 5×` measured speedup & `< 1%` step-halving drift. |
| ☐ | HW11 | B. Algorithmic complexity, stiff chemistry & multirate clocks (HW07–HW12) | Exponential-Euler & implicit stiff solvers | Integrates linear membrane decay via exact exponential-Euler and stiff nonlinear wet chemistry via bounded backward-Euler/TR-BDF2 (`0` explicit-Euler blowups). |
| ☐ | HW12 | B. Algorithmic complexity, stiff chemistry & multirate clocks (HW07–HW12) | Tier-2-only multi-fidelity crowd surrogates | Optional distant-crowd reduced surrogates execute **exclusively in Tier-2 Adaptive Bulk Mode** under deterministic in-world salience schedules (never Tier-1). |
| ☐ | HW13 | C. Worker isolation, backend probes & two-tier determinism (HW13–HW18) | Off-main-thread simulation & export workers | Physics, neural batches, and file encoders run in dedicated Workers/threads so UI interaction never stalls `tick()`. |
| ☐ | HW14 | C. Worker isolation, backend probes & two-tier determinism (HW13–HW18) | Verified `crossOriginIsolated` + 3-retry SeqLock | Asserts `self.crossOriginIsolated` at startup; Sim->UI `SharedArrayBuffer` uses odd/even `SeqLock` (max `3` reader retries + double-buffer fallback). |
| ☐ | HW15 | C. Worker isolation, backend probes & two-tier determinism (HW13–HW18) | Two-Tier determinism + core `exp_det` | Tier-1 CPU/WASM uses core-shipped `exp_det`/`log_det` + `.alifebin` for cross-OS SHA-256 parity; Tier-2 GPU checks preregistered observable distributions. |
| ☐ | HW16 | C. Worker isolation, backend probes & two-tier determinism (HW13–HW18) | `Philox4x32-10` domain-isolated PRNG | 32-bit `Math.imul` `Philox4x32-10` keyed by `(ver, seed, domain, entity, organ, tick, purpose, idx)` isolating `WORLD_EXOG` from `ENTITY_INT`. |
| ☐ | HW17 | C. Worker isolation, backend probes & two-tier determinism (HW13–HW18) | Capability-probed WebGPU / SIMD kernels | Probes `shader-f16` / SIMD support at boot, selects verified native or unpacked-`f32` software kernels, and logs active backend mode in manifest. |
| ☐ | HW18 | C. Worker isolation, backend probes & two-tier determinism (HW13–HW18) | 11-Pool compensated `FP64` ledger worker | Accumulates all enthalpy/mass pools + `E_diss_num ≥ 0` in CPU/WASM `FP64` Kahan-Neumaier state (never truncated to `WGSL f32` or `Q16.16`). |
| ☐ | HW19 | D. Observer independence, contiguous governor & sharded storage (HW19–HW24) | Bounded `≤ 32 KB/fr` sketch + pull telemetry | Streams global `O(1)` sketches every frame and pulls subgraph/raster slices strictly for the active inspector target (`ERR-01` cure). |
| ☐ | HW20 | D. Observer independence, contiguous governor & sharded storage (HW19–HW24) | 10,000-tick zero-observer-effect hash gate | CI verifies `10,000` Tier-1 ticks with all 19 UI tabs open + active export + Governor Band-3 forcing match headless SHA-256 bit-for-bit. |
| ☐ | HW21 | D. Observer independence, contiguous governor & sharded storage (HW19–HW24) | Contiguous hysteresis Frame-Time Governor | EMA `ms/frame` bands (`<0.70B`, `0.70–0.90B`, `0.90–1.00B`, `>1.00B` of `T_frame(Tier)`) shed render/UI rate only in Tier-1 (`30`-frame hysteresis dwell). |
| ☐ | HW22 | D. Observer independence, contiguous governor & sharded storage (HW19–HW24) | Decoupled lossless export + `<500K` XLS shard | Streams raw tensors losslessly to `Parquet`/`HDF5`/`CSV` and shards `.xls`/`.xlsx` workbooks well below Excel's `1,048,576`-row hard limit. |
| ☐ | HW23 | D. Observer independence, contiguous governor & sharded storage (HW19–HW24) | Automated Tier-E/L/D/W/C budget smoke gate | CI measures peak resident RAM/VRAM, synaptic events/s, and p99 step latency against declared Hardware Reference Tier ceilings. |
| ☐ | HW24 | D. Observer independence, contiguous governor & sharded storage (HW19–HW24) | Non-finite & `85%`-arena watchdog breaker | Traps any `NaN/Inf`, `ΔE_diss_num < -1e-15`, or `> 85%` arena water-mark, writes crash `.alifebin` + manifest, and aborts promotion cleanly. |



## 9. 9 Build Stages, First-15 Sprint, 100-Milestone Acyclic DAG & 13 Release Gates

| Stage | Name | Milestones | Exit Gate |
| --- | --- | --- | --- |
| Stage 0 | Preregistration, Repo & Tier Contract | M001–M003 | Standalone `.git` verified (`HEAD` SHA), Seed Firewall ranges locked, Hardware Tier & SI units declared. |
| Stage 1 | SoA Arena, Deterministic Math & Ledger | M004–M010 | `0` allocs / `10,000` ticks, `Philox4x32-10` `WORLD_EXOG` isolation, 11-pool `FP64` Kahan-Neumaier (`<1e-12`), 5 mutants caught. |
| Stage 2 | Wet Autopoietic Chemoton Soma | M011–M020 | Gánti Chemoton (`A, T, pV_n`), Michaelis-Menten gut, positive-orthant antithetic clamp, 3-phase fasting curve. |
| Stage 3 | Soft Hydrostat & Omnimodal Sensorium | M021–M040 | `\|ΔV\|/V_0 < 1%` XPBD soft body, 0-brain passive terrain baseline (`M024`), unified sensor bus + `.sensorlog` replay. |
| Stage 4 | Sparse Spiking, sLTC/CfC & Ganglia | M041–M050 | Packed `CSR` `int4/b1.58` brain, `≥50%` neural spike offload (`M044/SOFT08`), autonomous limb/gut ganglia, size-scaled `SHY`. |
| Stage 5 | Associative, Hopfield & Replay Memory | M051–M060 | 4-slot theta-gamma WM, `2%` SDR expansion, Hopfield+VSA recall, NREM/REM replay transfer, reality monitoring. |
| Stage 6 | Workspace, HOT, Geodesics & Safe WSE | M061–M070 | Lags 2–5 blink + lag-1 sparing, urgency-gated EFE, calibrated `HOT` opt-out, Riemannian detours, `Ring-0` `WSE`. |
| Stage 7 | Affective Selfhood & Forked `PCI*` Audit | M071–M080 | 4-timescale affect, efference forward agency (`AE-2`), forked-snapshot `PCI*`, controlled `Butlin-14 + F10` scorecard. |
| Stage 8 | Ontogeny, Metamorphosis & Biosphere | M081–M100 | Yolk-conserved cleavage, Blackiston metamorphosis memory (`M084`), `O(N_pop+C)` 3-guild dome, 19-tab UI & 13 release gates. |


| St | ID | Layer | Dim | Cost | Title | Build Contract | Control | Pass Target | Prereqs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ☐ | M001 ★ | L0 Arena | ⏱ Oper | [O(1)] | SoA TypedArray Memory Arena | Pre-allocate contiguous SoA TypedArray buffers for units, synapses, soft vertices & pools; fixed WASM pages. | Run 10,000 post-warmup ticks under heap/WASM profiler. | 0 B alloc / 10k ticks | ROOT |
| ☐ | M002 ★ | L0 Arena | ⚙ Comp | [O(1)] | Domain-Isolated Philox4x32 PRNG | 32-bit `Math.imul` `Philox4x32-10` keyed by `(ver,seed,domain,entity,organ,tick,purpose,idx)` isolating `WORLD_EXOG`. | Delete 1 unit inside Organ A -> check Organ B & `WORLD_EXOG` draws. | 0 bit diff / 10k ticks | M001 |
| ☐ | M003 ★ | L0 Arena | 🏁 Stag | [O(1)] | Seed Firewall, Repo & Manifest | Verify standalone `.git` object store; partition Practice (`100–999`), Tuning (`2000–2999`), Burn-on-Fail Test (`≥5000`). | Inject literal test seed `5001` into creature module -> AST gate. | 0 leaks; 100% SHA | M001,M002 |
| ☐ | M004 ★ | L0 Arena | 🔄 Syst | [O(1)] | 11-Pool FP64 Kahan-Neumaier Ledger | Closed 11 enthalpy/mass pools (`E_patch..E_heat_phys + E_diss_num ≥ 0`) in compensated `FP64` + Second-Law sink. | Inject gross `-1e-5` AND subtle `-2e-11` leak mutants. | \|ΔE\|/(E0+Ein) < 1e-12 | M001 |
| ☐ | M005 ★ | L0 Arena | ⏱ Oper | [O(1)] | 5-Gear Deterministic Multirate Clock | Integer-divided gears (`0.5ms, 5ms, 50ms, 1s, 60s`) with explicit ZOH state hold and conservative flux accumulators. | Benchmark vs all-`0.5ms` single-rate + `2×` step-halving check. | ≥5.0× speed; err < 1% | M001,M004 |
| ☐ | M006 ★ | L0 Arena | ⏱ Oper | [O(N_u)] | Canonical `.alifebin` & XOR Diff | Little-endian `.alifebin` snapshot serializer + `<64 KB` sparse XOR incremental checkpoint + core `exp_det`/`log_det`. | Save at `t=5,000`, reload on fresh worker -> compare `t=10,000` SHA-256. | 0 bit diff; Δ < 64 KB | M002,M005 |
| ☐ | M007 ★ | L0 Arena | ⚙ Comp | [Q≤10] | Integer-Guarded Q≤10 Register | Optional coherent register validating integer `0 ≤ Q ≤ 10` before allocating `2*(2**Q)` `Float64` (`≤16 KiB`) + classical control. | Pass `Q=32`, `Q=-1`, `Q=3.5` -> guard rejects without `1<<32` wrap. | 0 ≤ Q ≤ 10; ≤16 KiB | M001,M002 |
| ☐ | M008 ★ | L0 Arena | 📐 Desn | [O(1)] | Universal Typed Organ Adapter | Implement `parts(), couplings(), readState(), writeState(), stimulate(), lesion(), shamLesion(), metrics()` with SI tags. | Inject `mM` into `kJ` port or `NaN` state -> runtime contract check. | 0 untyped/NaN ports | M001,M004 |
| ☐ | M009 ★ | L0 Arena | 🔄 Syst | [O(P)] | No-Cosmetic-Parts (`C-NC`) Sweep | Automated perturbation harness verifies every declared organ, modulator & soft parameter shifts active-regime trajectory. | Attach disconnected display-only state array -> `C-NC` audit. | 100% parts \|Δy\| > ε | M006,M008 |
| ☐ | M010 ★ | L0 Arena | 🏁 Stag | [O(1)] | Originality & 5-Mutant CI Gate | Static AST/import scanner bans world-oracle reads and verifies 0 copied external assets; runs 5 negative mutants. | Run `Leaky-2e-11, Cosmetic, Oracle, Frozen, Shuffled` mutants. | 5 / 5 mutants rejected | M003,M004,M009 |
| ☐ | M011 ★ | L1 WetBio | 🔄 Syst | [O(1)] | Gánti Chemoton Polymer Triad | Stoichiometrically couple autocatalytic cycle `A`, membrane lipid `T`, and template polymer `pV_n` (`n ≥ N*` division). | Sever any 1 of the 3 cycles -> measure survival/division persistence. | 3/3 cycles essential; δ≥0.8 | M004,M008 |
| ☐ | M012 ★ | L1 WetBio | 🌊 Proc | [O(1)] | Michaelis-Menten Saturating Gut | Enzymatic digestion & uptake obey `v = V_max·[S]/(K_m+[S])` with implicit stiff step & `[ATP]` allosteric brake. | Bolus `100× K_m` nutrient shock vs linear-flux mutant. | v ≤ V_max; 0 blowups | M004,M011 |
| ☐ | M013 ★ | L1 WetBio | 🌊 Proc | [O(1)] | 3-Phase Fasting & Ketone Sparing | Insulin glycogenesis/lipogenesis; fasting mobilizes FFA + protein-sparing `β-HB` ketones prior to Phase-III proteolysis. | Fast replete organism vs ketogenesis-lesioned clone. | ≥1.6× protein-spared t | M012 |
| ☐ | M014 ★ | L1 WetBio | 🔄 Syst | [O(1)] | Positive-Orthant Antithetic Clamp | Non-negative `z_1, z_2 ≥ 0` dual-rail antithetic integral controller (`γ=0` undiluted regime) + seasonal rheostasis. | Apply `+25%` basal glucose step load vs P-only controller. | \|e_ss\| < 1% set-point | M012 |
| ☐ | M015 ★ | L1 WetBio | 🎯 Func | [O(1)] | 3-Timescale Satiation & TTC Drive | Stretch + CCK + leptin meal termination; glucose `TTC` slope initiates foraging ahead of hypoglycemic threshold. | Compare intact vs TTC-lesioned & satiation-lesioned clones. | Hypoglycemia t < 2% | M013,M014 |
| ☐ | M016 | L1 WetBio | 🌊 Proc | [O(1)] | Osmotic Pump & Cori Lactate Loop | Active ion pump counters Donnan swelling; anaerobic burst builds `[H+/lactate]` cleared post-sprint via Cori cycle. | Block pump ATP (`lysis`) & run sprint-recovery assay. | \|ΔOsm\| < 3%; pH ≥ 7.1 | M011,M012 |
| ☐ | M017 | L1 WetBio | 🎯 Func | [O(1)] | Garcia Delayed Taste Aversion | Slow visceral emesis/toxin trace pairs ingested flavor cue across `≥ 300 s` delay in 1 trial. | Present novel toxic flavor -> re-offer 1,000 s later vs sham. | Re-ingest ≤ 15%; δ≥0.6 | M012,M015 |
| ☐ | M018 | L1 WetBio | 🎯 Func | [O(1)] | Post-Absorptive Enthalpy Audit | Cross-checks absorbed `E_gut -> E_blood` kJ yield against oral sweet cue to extinguish `0-kJ` decoy lures. | Offer sweet `0-kJ` lure alongside bland caloric patch. | Decoy share ≤ 10% ≤3 bouts | M015,M017 |
| ☐ | M019 | L1 WetBio | 🔄 Syst | [O(1)] | Ring-0 Cardiac & O2 Perfusion | Intrinsic Ring-0 cardiac + ventilatory CPGs scale organ O2/glucose delivery with exertion and ambient hypoxia. | Drop dome `pO2` by `40%` -> measure ventilation & perfusion. | Vent lift ≥ 1.8×; 0 NaN | M012,M016 |
| ☐ | M020 | L1 WetBio | 🌊 Proc | [O(1)] | CYP Detox, ROS & Immune Memory | ATP-debited toxin clearance, ROS antioxidant defense, sickness lethargy, and adaptive secondary pathogen clearance. | Primary vs secondary homologous pathogen challenge vs naive. | 2nd clear time ≤ 0.5× 1st | M012,M019 |
| ☐ | M021 | L2 Soft | 📐 Desn | [O(V_m)] | Incompressible Hydrostatic Coelom | 100% original parametric soft body conserving chamber volume (`C_vol`) so radial contraction drives axial extension. | Radial squeeze test + cavity puncture negative control. | \|ΔV\|/V_0 < 1.0% | M004,M008 |
| ☐ | M022 | L2 Soft | ⚙ Comp | [O(V_m)] | XPBD Viscoelastic Membrane & Damping | Compliance-scaled XPBD (`α̃ = α/dt²`) storing reversible `E_elastic` and booking numerical damping to `E_diss_num ≥ 0`. | 10× nominal speed wall impact vs explicit-Euler baseline. | 0 NaN; ΔE_diss ≥ -1e-15 | M004,M021 |
| ☐ | M023 | L2 Soft | 📐 Desn | [O(V_m)] | Biotensegrity & Crevice Squeeze | Pre-stressed cable-strut web + mutable catch-state (`≥10×` stiffness range) compressing cross-section through narrow gaps. | 0.55× diameter crevice traversal vs rigid-strut (`α→0`) clone. | Pass ≥ 90% vs 0% rigid | M021,M022 |
| ☐ | M024 | L2 Soft | ⚙ Comp | [O(V_m)] | 0-Brain Passive Terrain Stability | Open-loop passive soft compliance absorbs uneven-terrain impacts and maintains forward CPG progression without central brain. | Uneven obstacle ramp with 0-brain passive hydrostat vs rigid clone. | ≥1.8× dist; peak F ≤ 0.5× | M022,M023 |
| ☐ | M025 | L2 Soft | 🌊 Proc | [O(V_m)] | Dual-Medium Peristaltic & Swim Gaits | Phase-coupled open-loop motor primitives propel soft body via land peristalsis and Reynolds-consistent aquatic undulation. | Land-to-water ramp transition vs single-gait frozen control. | Speed ≥ 0.4 BL/s both media | M022,M024 |
| ☐ | M026 | L2 Soft | 🎯 Func | [O(V_m)] | Switchable Wet Adhesion & Slime | ATP-gated mucus adhesion/suction holds station in shear flow; secreted slime reduces follower drag (`-20%`). | Fluid shear ramp vs adhesion-lesioned clone. | Slip shear ≥ 3.0× control | M012,M022 |
| ☐ | M027 | L2 Soft | 🌊 Proc | [O(V_m)] | Puncture Leak, Clotting & Blastema | Membrane tear leaks coelomic pressure/stores until coagulation seals breach, followed by scar or amino-paid blastema. | Standardized puncture vs clotting-lesioned negative control. | Seal ≤ 15 s; loss < 8% E0 | M011,M021 |
| ☐ | M028 | L2 Soft | 🎯 Func | [O(1)] | Local Nociceptive Reflex & Autotomy | Fast `Aδ` withdrawal + slow `C` unloading; severe mechanical trapping triggers booked fracture-plane lobe autotomy. | Pin distal lobe under lethal hazard vs autotomy-disabled clone. | Escape ≥ 85%; \|ΔE\| < 1e-12 | M027 |
| ☐ | M029 | L2 Soft | 📐 Desn | [O(1)] | Arrhenius Q10 & Insulation Trade-Off | Biochemical `Q10` rate scaling + heritable cuticle insulation/albedo trading cold retention against hot sprint cooling. | Reciprocal transplant across Cold (`5°C`) and Hot (`36°C`) domes. | 2-niche fitness crossover δ≥0.5 | M012,M022 |
| ☐ | M030 | L2 Soft | 🎯 Func | [O(V_m)] | Turing Chromatophore Crypsis Skin | Reaction-diffusion / muscle-controlled surface pigment matches background luminance & spatial frequency. | Visual-predator detection assay vs high-contrast locked mutant. | Capture rate ≤ 0.55× mutant | M022 |
| ☐ | M031 | L3 Sense | 📐 Desn | [O(R)] | Unified Typed Omnimodal Bus | All simulated & `.sensorlog` transducers implement `(id, dim, gear, atp_cost, noise, read)` into flat SoA arena. | Hot-lesion any 1 modality during run -> check survival & stability. | 0 crashes; graceful ≥70% | M008,M021 |
| ☐ | M032 | L3 Sense | 🌊 Proc | [O(V_m)] | Continuum Skin Strain & Slip Sheet | Surface mechanoreceptor array encodes stretch `ε`, curvature `κ`, contact pressure, and tangential slip velocity. | Apply sudden load slip to gripped stone vs slip-blind control. | Grip recovery ≤ 35 ms | M022,M031 |
| ☐ | M033 | L3 Sense | 🎯 Func | [O(R)] | Active Saccades & Motion Parallax | Foveal ray fan + active lateral peering triangulates metric 3D target distance from optic bearing-rate. | Depth-gap jump/reach vs peering-immobilized control. | Range RMSE ≤ 12%; δ≥0.5 | M025,M031 |
| ☐ | M034 | L3 Sense | 🎯 Func | [O(1)] | Bilateral Plume Chemotaxis & Taste | Paired anterior chemoreceptors compute concentration + arrival-lag gradients in turbulent odor plumes + oral taste. | Turbulent plume source localization vs crossed-antenna sham. | Source hit ≥ 80% vs ≤25% | M017,M031 |
| ☐ | M035 | L3 Sense | 🎯 Func | [O(B)] | Log-Cochlea & Lateral-Line Array | Log-spaced spectral filterbank + surface hydrodynamic wake array localizing unseen moving agents in darkness. | Dark ambush-predator approach vs deaf/lateral-line-lesioned arm. | Azimuth MAE ≤ 18°; δ≥0.5 | M031 |
| ☐ | M036 | L3 Sense | 🎯 Func | [O(R)] | ATP-Priced Nocturnal Active Sense | Active electro-/echolocation pulses engage automatically in dark/turbid zones and silence in lit open water. | Dark obstacle maze vs pulse-disabled & always-on wasteful clones. | Collisions ≤ 10%; ≥35% ATP save | M031,M035 |
| ☐ | M037 | L3 Sense | 🔄 Syst | [O(1)] | Topographic Visceral Insula Map | Dedicated interoceptive bus carries live pressure, 11-pool fuel margins, `pO2`, osmolarity, pH, and cytokines. | Permute visceral channels across organs (`Shuffled` arm). | Homeostatic survival δ≥0.6 | M016,M031 |
| ☐ | M038 | L3 Sense | ⚙ Comp | [O(S²)] | Földiák Decorrelation & Reafference | Anti-Hebbian lateral whitening reduces cross-channel redundancy and subtracts self-motion sensory predictions. | Measure pairwise channel correlation & self-motion residual. | Mean \|r_ij\| ≤ 0.15; cancel ≥70% | M031,M032 |
| ☐ | M039 | L3 Sense | 🔄 Syst | [O(1)] | Attenuated In-World Field Senses | Dipole compass + inverse-distance noisy peer bioelectric/wave sense with strict per-sample ATP debit. | Compare intact navigation/coordination vs temporal-shuffle stream. | δ_pair ≥ 0.33 vs shuffle=chance | M031 |
| ☐ | M040 | L3 Sense | ⏱ Oper | [O(1)] | Immutable `.sensorlog` Replay Ring | Sandboxed Practice hardware transducer tap writing timestamped `.sensorlog` packets for bit-exact Test replay. | Replay 10,000-tick `.sensorlog` across 2 threads/OSes. | SHA-256 0-bit diff | M006,M031 |
| ☐ | M041 | L4 Neural | ⚙ Comp | [O(k·E)] | Packed CSR Event-Driven Spiking Core | Balanced E/I LIF/AdEx/sLTC sheets in 32-synapse packed `int4`/`b1.58` blocks (`k ≈ 1–4%` active rows, ATP/spike). | Silent vs active metabolic audit + dense-matrix equivalence check. | k ∈ [1%,4%]; \|ΔE\| < 1e-12 | M004,M005,M031 |
| ☐ | M042 | L4 Neural | ⚙ Comp | [O(E)] | Adaptive sLTC / CfC Liquid Constants | State- and modulator-gated time constants `τ(x,I)` spanning `5 ms` to `60 s` without stiff ODE sub-step blowup. | Multi-timescale cue integration vs fixed-`τ` matched baseline. | Accuracy lift ≥ +20%; δ≥0.45 | M041 |
| ☐ | M043 | L4 Neural | ⚙ Comp | [O(N_u)] | Two-Compartment Apical dCaAP XOR | Segregated basal drive + apical context calcium plateau solving single-layer nonlinear anti-coincidence/XOR. | Contextual XOR task: intact vs apical-dendrite cut & sham cut. | XOR Acc ≥ 0.90 vs ≤0.55 cut | M041 |
| ☐ | M044 | L4 Neural | 📐 Desn | [O(N_u)] | Peripheral Ganglia & 50% Spike Offload | Autonomous `int4` CfC limb/gut ganglia survive brain cut AND compliant body offloads `≥50%` central spikes/m (`SOFT08`). | 1) Decerebrate survival; 2) Compliant vs stiff `α→0` at equal speed/fail. | ≥50% spike/m save @ ≥speed | M024,M041,M042 |
| ☐ | M045 | L4 Neural | 🔄 Syst | [O(k·E)] | Homeostatic iSTDP, BCM & `‖W‖_2` Clamp | Fast inhibitory STDP + sliding BCM threshold + contractive norm `‖W‖_2 ≤ 0.99` + degenerate path survival. | Randomly ablate `20%` of Ring-1 synapses vs non-homeostatic net. | 0 runaway; ≥75% foraging kept | M041 |
| ☐ | M046 | L4 Neural | 🌊 Proc | [O(1)] | 7 Precursor-Limited Neuromodulators | Dietary precursor-bounded `DA, 5-HT, NE, ACh, Glu, GABA, eCB` + slow peptide bus causally shifting routing. | Clamp/deplete each of 7 channels -> measure preregistered signature. | 7 / 7 directional shifts p_H≤0.05 | M020,M041 |
| ☐ | M047 | L4 Neural | 🌊 Proc | [O(k·E)] | Bounded Eligibility, e-prop & BTSP | Fixed-ring sparse `pre×post` eligibility (`≤5%` syn) + `e-prop` + one-shot `1–5 s` plateau BTSP place writing. | Delayed-reward T-maze (`3 s` gap) vs zero-trace Hebbian control. | Solve ≤ 15 trials; δ_pair ≥ 0.5 | M041,M046 |
| ☐ | M048 | L4 Neural | 🌊 Proc | [O(N_u)] | PV+ Gamma Coherence & Delay Tuning | Gap-junction PV+ interneuron syncytium + adaptive integer axonal delays phase-locking bound features. | Cross-modal binding under distractor noise vs jittered-delay sham. | PLV ≥ 0.45; bind lift ≥ +18% | M041,M043 |
| ☐ | M049 | L4 Neural | 🔄 Syst | [O(1)] | SCN Circadian × Adenosine Flip-Flop | Photoperiod-entrained SCN oscillator × Process-S sleep pressure driving Wake, NREM-SWS, and phasic REM. |  Light phase-shift jetlag + constant-dark free-run vs SCN lesion. | Entrains ≤ 3 d; period 24±1h | M041,M046 |
| ☐ | M050 | L4 Neural | 🌊 Proc | [O(E)] | Size-Scaled NREM SHY & Pruning | Slow-wave multiplicative weight renormalization & complement pruning scaled proportionally to current synapse count. | Sleep-deprived clone vs NREM-permitted clone across 3 diurnal cycles. | Weight norm CV ≤ 10%; +25% ret | M045,M049 |
| ☐ | M051 | L5 Memory | ⚙ Comp | [O(D)] | Theta-Gamma 4-Slot Working Memory | Phase-multiplexed oscillatory buffer + glial calcium bridge holding `4–7` ordered items across `10 s` silent gaps. | Ordered serial recall + 5th/8th item overload capacity curve. | ≥85% @ 4 items; predictable drop | M048 |
| ☐ | M052 | L5 Memory | 🌊 Proc | [O(k·E)] | Fusi Metaplastic Cascade Retention | Discrete biochemical synapse depth states yielding power-law retention across sequential Task A -> B -> C training. | Task-A retention after Task-B/C vs single-state plastic baseline. | Task-A LCB_95% > -0.05; δ≥0.5 | M047,M050 |
| ☐ | M053 | L5 Memory | ⚙ Comp | [O(k·E)] | 2% SDR Expansion & Configural XOR | Kenyon-inspired `2%` k-WTA sparse expansion + fan-in normalization solving negative patterning (`A+, B+, AB-`). | Configural `AB-` discrimination vs dense linear readout baseline. | AB- Acc ≥ 0.88 vs ≤0.52 linear | M041,M047 |
| ☐ | M054 | L5 Memory | ⚙ Comp | [O(M·D)] | Modern Hopfield + VSA CA3 Recall | Log-sum-exp continuous Hopfield + algebraic VSA `(Place ⊗ Cue ⊗ Payoff)` completing `50%`-masked episodes. | Cue completion at `50%` bit/feature occlusion vs Hopfield lesion. | Cosine ≥ 0.90 vs ≤0.45 lesion | M051,M053 |
| ☐ | M055 | L5 Memory | 🌊 Proc | [O(M·D)] | Prioritized NREM & Counterfactual REM | NREM replays high-TD-error transitions; REM synthesizes novel trajectory recombinations for zero-shot shortcutting. | Detour shortcut test post-sleep vs shuffled-replay sleep control. | Zero-shot shortcut ≥ 75%; δ≥0.45 | M050,M054 |
| ☐ | M056 | L5 Memory | 🎯 Func | [O(1)] | Perceptual & REM Reality Monitoring | `HOT-1` source tag discriminates real sensory experience counts from REM counterfactual uncertainty (`N45`). | Inject unvisited high-payoff REM rollout -> test morning certainty. | False-visit rate ≤ 5%; AUROC≥0.85 | M055 |
| ☐ | M057 | L5 Memory | 🎯 Func | [O(D)] | Kamin Blocking & Conditioned Inhib. | Competitive prediction-error update exhibits Kamin blocking (`A+` blocks `B` in `AB+`), extinction, and spontaneous recovery. | Classic 2-stage Kamin blocking protocol vs non-competitive Hebbian. | Blocked cue V_B ≤ 0.25·V_ctrl | M047,M053 |
| ☐ | M058 | L5 Memory | ⚙ Comp | [O(K)] | Latent Regime Context Switching | Unexpected-surprise (`NE`) detector spawns/recalls latent context slots upon abrupt world-rule reversals without erasure. | Repeated A <-> B rule reversals vs single-context learner. | Re-adapt ≤ 2 trials vs ≥12 | M046,M054 |
| ☐ | M059 | L5 Memory | ⚙ Comp | [O(D)] | Toroidal Grid & 45-Tick Permanence | Continuous hex/ring attractor path integration + landmark phase reset + occluded moving-prey trajectory tracking. | Track prey behind opaque barrier for `45` Gear-1 ticks (`225 ms+`). | Intercept err ≤ 1.5 BL; δ≥0.5 | M033,M054 |
| ☐ | M060 | L5 Memory | 🎯 Func | [O(D)] | Memory Reconsolidation & Checkpoint | Safe reminder labilizes outdated fear trace (`N19`); ATP-paid `<64 KB` cortical save restores post-trauma (`N15`). | Trauma shock corrupting policy -> rollback vs disabled-save arm. | 100% Ring-1 hash / ≥85% skill | M006,M052 |
| ☐ | M061 | L6 Exec | 🔄 Syst | [O(M_m)] | Global Workspace & Lags 2–5 Blink | Up-tree tournament ignites global down-tree broadcast (`K_ws` slots), exhibiting **lags 2–5 blink with lag-1 sparing**. | Rapid dual-target stream (`T1, T2`) across lags 1..8 + hub lesion. | Lag 2–5 drop ≥25%; \|Lag1-8\|≤10% | M048,M051 |
| ☐ | M062 | L6 Exec | 🔄 Syst | [O(M_m)] | Multiplicative Urgency-Gated EFE | Expected-free-energy arbiter scales epistemic curiosity by `σ((TTC - TTC_crit)/τ)` so low-fuel agents prioritize food. | High-novelty decoy trap vs food patch at `20%` vs `90%` reserves. | Starve rate ≤ 3% vs ≥45% add. | M015,M061 |
| ☐ | M063 | L6 Exec | 🎯 Func | [O(D)] | Endogenous & Social Attention Schema | `AST-1` forward model forecasts own spotlight transitions and infers conspecific gaze obstruction/targets. | Step attentional distractor + peer visual-occlusion competition. | Spotlight MSE -35%; gaze δ≥0.4 | M033,M061 |
| ☐ | M064 | L6 Exec | 🎯 Func | [O(D)] | Calibrated HOT Confidence Opt-Out | `HOT-2/3` reliability monitor achieves low calibration error and triggers scan/opt-out on ambiguous high-loss traps. | Variable-SNR hazard discrimination with safe low-payoff opt-out. | ECE ≤ 0.08; survival +30% vs blind | M056,M061 |
| ☐ | M065 | L6 Exec | 🎯 Func | [O(G_p)] | 0-Trial Outcome Devaluation Arbiter | Model-based tree immediately suppresses actions toward newly sated/poisoned outcomes before re-experiencing action. | Offline LiCl-like outcome devaluation vs dorsolateral habit clone. | 0-trial press drop ≥ 65%; δ≥0.5 | M017,M062 |
| ☐ | M066 | L6 Exec | ⚙ Comp | [O(G_p²)] | Riemannian Danger-Geodesic Planner | Plans trajectories on learned latent graph weighted by metric harm cost `d_s·(1 + λ·p_harm)`. | Shortest-path lava/predator corridor vs longer safe detour. | Hazard damage ≤ 0.3× greedy | M059,M065 |
| ☐ | M067 | L6 Exec | 🎯 Func | [O(G_p)] | Counterfactual Regret & Subgoals | Evaluates unchosen branch counterfactuals to accelerate policy switch and identifies graph-bottleneck doorways. | Multi-room bottleneck maze + suboptimal-arm counterfactual cue. | Steps-to-goal ≤ 0.55× flat RL | M066 |
| ☐ | M068 | L6 Exec | 🔄 Syst | [O(1)] | Pre-Motor Visceral 'Free Won't' Veto | Hyperdirect pre-execution check aborts motor commands within `50 ms` if forward visceral model predicts lethal breach. | Lure over sharp hazard when coelomic integrity `< 35%` vs sham veto. | Veto latency ≤ 50ms; death -70% | M028,M061 |
| ☐ | M069 | L6 Exec | ⚙ Comp | [O(1)] | Unlearnable-Noise Humility Gate | Online entropy/runs test flags pure-chance (`I(X;Y) ≈ 0`) channels, halting active-sense ATP & synaptic churn. | 50/50 Bernoulli decoy lever alongside learnable patch. | Noise Δw & ATP ≤ 0.25× naive | M007,M064 |
| ☐ | M070 | L6 Exec | 📐 Desn | [O(k·E)] | Ring-0 Guarded Tokenless WSE-12 | All 10 `WSE-OP` operators live with Tier-0 `‖W‖_2 ≤ 0.99` guard, `<16 KB` diff, bit-exact rollback, and `Ring-0` write trap. | Attempt endogenous `Ring-0` edit + norm-overflow edit + rollback. | 100% Ring-0 blocked; 0-bit undo | M006,M045,M064 |
| ☐ | M071 | L7 Self | 🪜 Ordr | [O(1)] | 4-Timescale Affective Architecture | Causally nested fast emotions (`<5s`), peptide moods (`min`), peer attitudes (`hours`), and heritable temperament. | Perturb each timescale + compare vs flat scalar-reward ablation. | 4 distinct τ bands; δ_pair ≥ 0.4 | M046,M062 |
| ☐ | M072 | L7 Self | 🎯 Func | [O(1)] | Context-Gated Play, Care & Defense | Surplus-ATP juvenile play, kin-distress caregiving, toxin disgust, and immediate play suppression under threat/fasting. | Introduce predator looming or drop stores `<30%` during play. | Play drops ≥ 95% within 200 ms | M071 |
| ☐ | M073 | L7 Self | 🎯 Func | [O(D)] | Efference-Copy Self-Recognition (`AE-2`) | Zero-oracle contingent sensorimotor forward model distinguishes own limb/reflection from delayed or peer motion. | Contingent mirror/shadow mark assay vs `250 ms`-delayed sham. | Self-contingent d' ≥ 1.8 | M038,M063 |
| ☐ | M074 | L7 Self | 🔄 Syst | [O(D)] | Trajectory-Curvature & Glitch Caution | High hidden-state curvature `κ(t)` and visceral enthalpy-prediction residuals trigger braking and active re-scan. | Enter perturbed-physics / zero-calorie anomaly zone vs blind clone. | Brake latency ≤ 3 steps; δ≥0.45 | M018,M064 |
| ☐ | M075 | L7 Self | 🎯 Func | [O(1)] | Sandboxed Physical Lever Mastery | Discovers rate-limited in-world physical mechanisms (stone dams, shade canopies) with `0` host/DOM/FS access. | Security sandbox escape fuzzing + in-world lever utility test. | 0 escapes; lever lift δ ≥ 0.45 | M010,M066 |
| ☐ | M076 | L7 Self | ⚙ Comp | [O(D)] | Metric-Preconditioned & Winding State | Diagonal Fisher/QGT natural-gradient update + integer winding invariant preventing micro-noise mood chatter. | Noisy non-stationary tracking vs unpreconditioned Euclidean step. | Chatter flips -60%; MSE -20% | M047,M071 |
| ☐ | M077 | L7 Self | 🎯 Func | [O(k·E)] | Salience-Ordered Famine Triage (`N100`) | Phase-III energy crisis down-clocks associative spheres (`N94`) and sheds trivia tags before core survival engrams. | Severe fast + refeed recovery vs random-synapse-drop control. | Core skill ≥ 85% vs ≤40% rand | M013,M052 |
| ☐ | M078 | L7 Self | ⚙ Comp | [O(N_u)] | Forked-Snapshot Perturbational `PCI*` | Computes Lempel-Ziv spatiotemporal response complexity across forked snapshots (`Wake vs NREM-SWS vs Cut`). | 24 paired seeds across Wake, SWS, Saturated, and Severed states. | PCI*_W ≥ 0.35; W-SWS ≥ 0.12 | M006,M049,M061 |
| ☐ | M079 | L7 Self | 🔄 Syst | [O(N_u)] | Markov Blanket & Traveling Waves | Conditional sensory/active blanket autonomy (`I(Int;Ext\|Blanket)` reduction) + coherent cortical wave propagation. | Topography-scrambled control vs intact sheet wave speed/PLV. | Wave R² ≥ 0.65 vs ≤0.15 scram | M048,M073 |
| ☐ | M080 | L7 Self | 🏁 Stag | [Suite] | Controlled Butlin-14 + F10 Scorecard | Evaluates all `14` Butlin indicators + `F1–F10` profile across Intact, Passive, Shuffled, Targeted & Sham lesions. | Locked `N ≥ 24..64` seeds + exact Wilcoxon + Holm FWER `α ≤ 0.05`. | 14/14 p_Holm ≤ 0.05 & δ ≥ 0.33 | M061,M064,M073,M078 |
| ☐ | M081 | L8 Onto | 🌊 Proc | [O(Cells)] | Yolk-Conserved Cleavage & Adhesion | Single yolk-funded zygote divides via GRN + Steinberg differential adhesion + apoptosis into multi-chamber soma/brain. | Perturb adhesion/GRN gene + audit zygote-to-hatchling `FP64` kJ. | \|ΔE\| < 1e-12; sort ARI ≥ 0.80 | M011,M021 |
| ☐ | M082 | L8 Onto | 🌊 Proc | [O(k·E)] | Critical-Period Overgrowth & Prune | Juvenile synaptogenesis overshoot refined by early sensory statistics and size-scaled NREM complement pruning. | Early monocular/plume deprivation vs normal juvenile rearing. | Selectivity d' ≥ 1.5; -30% wires | M050,M081 |
| ☐ | M083 | L8 Onto | 🏁 Stag | [O(1)] | Kleiber M^0.75 Allometry & Stages | Basal metabolic rate scales across `Embryo -> Larva -> Adult` as `B ∝ M^(0.75 ± 0.05)` across `≥ 8×` mass range. | Log-log regression of basal `kJ/s` vs mass `M` vs `M^1.0` mutant. | Slope ∈ [0.70, 0.80]; R² ≥ 0.95 | M012,M081 |
| ☐ | M084 | L8 Onto | 🏁 Stag | [O(V_m)] | Blackiston Metamorphosis Retention | Larva replaces `≥ 80%` somatic muscle/motor map during pupation yet retains conditioned toxin-odor aversion (`N89`). | Blackiston 2008 paradigm vs naive adult & scrambled-CA3 pupa. | Adult avoid ≥ 0.70 vs ≤0.20 ctrl | M017,M054,M081 |
| ☐ | M085 | L8 Onto | 🌊 Proc | [O(Cells)] | Bioelectric `V_mem` Polarity & Molt | Gap-junction voltage gradient guides anterior/posterior blastema regeneration; armored morphs survive soft ecdysis. | Amputate posterior lobe with intact vs clamped `V_mem` gradient. | Correct polarity ≥ 90% vs ≤30% | M027,M081 |
| ☐ | M086 | L8 Onto | 🌊 Proc | [O(1)] | Cryptobiotic Vitrification Survival | Pre-drought trehalose vitrification drops metabolic burn `< 2%` basal and restores viability + memory upon rehydration. | 10,000-s desiccation freeze vs vitrification-lesioned clone. | Revive ≥ 90% vs 0% lesion | M029,M052 |
| ☐ | M087 | L8 Onto | 🔄 Syst | [O(1)] | Disposable-Soma Senescence Trade-Off | Heritable ATP allocation split between somatic repair and early fecundity generates Pareto lifespan-reproduction front. | Compare high-repair vs high-fecundity genotypes across niches. | Spearman ρ(fec, span) ≤ -0.55 | M015,M081 |
| ☐ | M088 | L8 Onto | 🌊 Proc | [O(G)] | Stress Evolvability & F1 Thrift Mark | Chronic cortisol elevates canalized germline variance; maternal famine sets `1–2` gen reversible thrift mark (`N48`). | F1 famine survival + F3 washout check vs non-epigenetic clone. | F1 span +25%; F3 washout <5% | M013,M081 |
| ☐ | M089 | L8 Onto | 🎯 Func | [O(1)] | Recombination & Zahavi/MHC Mate Choice | Meiotic crossover + ATP-honest condition display + MHC dissimilarity avoidance preventing inbred depression. | Choice test: replete outbred vs depleted or sibling suitor. | Outbred replete pref ≥ 0.72 | M020,M081 |
| ☐ | M090 | L8 Onto | 🔄 Syst | [O(1)] | Compensated Nursing & Baldwin Effect | Maternal-to-juvenile `FP64` lactation (`\|ΔE\|<1e-12`), Trivers weaning transition, and `≥20`-gen Baldwin assimilation. | Audit parent+offspring kJ sum + innate trial-to-learn at Gen 25. | \|ΔE\|/(E0+Ein)<1e-12; -40% trials | M004,M082,M089 |
| ☐ | M091 | L9 Eco | 🔄 Syst | [O(N+C)] | `O(N_pop+C_pairs)` Closed Biosphere | Uniform spatial-hash collisions, solar primary growth, waste gardens, carcass lysis, and dome-wide `FP64` closure. | Scale `N_pop` `25 -> 200` at constant density + audit 11-pool kJ. | Slope ≤ 1.15× linear; <1e-12 | M004,M020,M022 |
| ☐ | M092 | L9 Eco | 🎯 Func | [O(1)] | ATP-Honest Calls & Dialect Divergence | Proportional-ATP vocal/chromatophore signaling, observational foraging, and allopatric group dialect separation. | Zero-cost bluff mutant invasion test + 2-island dialect classifier. | Bluff extinct; dialect Acc ≥ 0.80 | M035,M091 |
| ☐ | M093 | L9 Eco | 🎯 Func | [O(1)] | Kin Alarm, Trophallaxis & Reciprocity | MHC-gated alarm calls, caloric regurgitation to starving kin/reciprocators, and chronic-defector boycott (`N60`). | Iterated sharing with reciprocator vs 100%-defector clone. | Defector share drops ≤ 15% | M089,M092 |
| ☐ | M094 | L9 Eco | 🎯 Func | [O(1)] | Elder Demonstration & Sentinel Sleep | Experienced adult slows actions for naive young (`N55`); huddled clusters stagger circadian phase for sentinel watch. | Nocturnal predator raids on staggered cluster vs synchronous-sleep. | Ambush mortality ≤ 0.60× sync | M049,M092 |
| ☐ | M095 | L9 Eco | 🎯 Func | [O(N+C)] | Conformable Tool Use & Spoilage Cache | Soft grip displaces barrier stones to unlock recessed caches; episodic age tracking skips rotted caches (`N76`). | Recessed stone-blocked cache + fresh-vs-spoiled retrieval test. | Unlock ≥ 80%; fresh pick ≥ 85% | M023,M054,M066 |
| ☐ | M096 | L9 Eco | 🪜 Ordr | [O(N+C)] | Swarm Gradient Pooling & Zooid Castes | Collective threat blanket, distributed noisy-gradient pooling (`N57`), slime corridors, and optional colonial zooids. | Noisy moving plume tracking: 16-agent swarm vs 16 solo clones. | Swarm RMSE ≤ 0.65× solo | M026,M091 |
| ☐ | M097 | L9 Eco | 🔄 Syst | [O(N+C)] | 3-Guild Food Web & Zoopharmacognosy | Persistent primary patches, grazers, predators, manipulative parasites, and learned bitter medicinal self-cure. | 50,000-s 3-guild coexistence + infected medicinal-patch choice. | 3 guilds > 0 @ 50ks; load -60% | M018,M020,M091 |
| ☐ | M098 | L9 Eco | 🔄 Syst | [O(N+C)] | Daisyworld Albedo, Bridges & QD Map | Biotic albedo thermal buffering, enthalpy-exact archipelago migration, and MAP-Elites guild illumination. | Solar luminosity ramp (`0.8–1.2×`) + cross-dome migration kJ audit. | ΔT_core ≤ 0.5× barren; <1e-12 | M029,M091 |
| ☐ | M099 | L10 Ops | ⏱ Oper | [O(1)] | 19-Tab SeqLock Center & Governor Gate | `SharedArrayBuffer` 3-retry `SeqLock`, 19 tabs, decoupled lossless export, and contiguous render-only Tier-1 Governor. | 10,000 Tier-1 ticks: all 19 tabs open + exporting vs headless. | SHA-256 0-bit diff; ≤16.7ms | M006,M091 |
| ☐ | M100 | L10 Ops | 🏁 Stag | [Gate] | Unified 825-Check & 13-Gate CI Sign-Off | Single headless CI command verifying `.git`, 5 mutants, Tier budgets, `1e-12` ledger, Holm FWER, and provenance. | Inject any 1 mutant, leak, or unprobed format -> CI exit code. | 13 / 13 gates pass; 0 leaks | M010,M070,M080,M090,M099 |


| St | Gate ID | Gate Name | Mandatory Quantitative Criterion |
| --- | --- | --- | --- |
| ☐ | GATE-01 | Standalone Git & Burn-on-Fail Seed Firewall | Healthy `.git` object store (`HEAD` SHA), disjoint Practice/Tuning/Test seeds, 0 test-seed literals in creature code. |
| ☐ | GATE-02 | 10,000-Tick Zero-Alloc SoA & Tier RAM Fit | `0` heap allocs, `0` `BigInt` boxes, `0` WASM `memory.grow`, and `0` lossless-ring drops across `10,000` ticks within Tier RAM. |
| ☐ | GATE-03 | 11-Pool FP64 First-Law & Second-Law Closure | `\|ΔE\| / (E_0 + E_in,cum) < 1e-12`, `ΔE_diss_num ≥ -1e-15`, and `0` heat-to-ATP backflow across organism + dome. |
| ☐ | GATE-04 | 5 Anti-LARP Mutants (`Leaky-2e-11..Shuffled`) | `Leaky (-2e-11), Cosmetic, Oracle, Frozen, Shuffled` negative mutants `100%` automatically caught & rejected. |
| ☐ | GATE-05 | Wet Chemoton, Antithetic & 3-Phase Fasting | Gánti `A/T/pV_n` closure, positive-orthant antithetic `\|e_ss\| < 1%`, and `≥1.6×` ketone protein-sparing survival. |
| ☐ | GATE-06 | XPBD Soft Hydrostat & Passive Compliance | `\|ΔV\|/V_0 < 1%`, `0` impact `NaN`s, `≥90%` narrow-crevice pass, and `≥1.8×` 0-brain uneven-ramp distance (`M024`). |
| ☐ | GATE-07 | Packed Multi-Precision Brain & 50% Offload | Peripheral `int4` ganglia survive brain cut; `S2S` bridges verified; `≥50%` neural spikes/m offload at equal speed (`M044`). |
| ☐ | GATE-08 | Controlled Multi-Arm & Holm-Bonferroni FWER | Power-sized `N ≥ 24..120`, Sham-Lesion + Competent Baseline, exact Wilcoxon `p_Holm ≤ 0.05` (FWER), `δ_pair ≥ 0.33`, `LCB_95% > -Δ_NI`. |
| ☐ | GATE-09 | Ring-0 Immutable Tokenless WSE-12 Rollback | `‖W‖_2 ≤ 0.99` Tier-0 guard, `<16 KB` edit diff, domain-scoped `0-bit` rollback hash, and hardware-read-only `Ring-0`. |
| ☐ | GATE-10 | Ontogeny, Blackiston Metamorphosis & Heredity | Yolk-conserved cleavage (`<1e-12`), Kleiber `M^0.75`, and `≥70%` adult toxin-odor retention after `≥80%` muscle remap (`M084`). |
| ☐ | GATE-11 | 10,000-Tick Observer Independence & Governor | Tier-1 `UI-open + exporting == headless` SHA-256 hash (`0` bit diff) + contiguous Governor holding `T_frame(Tier)`. |
| ☐ | GATE-12 | 100% Clean-Room Non-Copy Originality | Zero copied external 3D meshes, body silhouettes, sprites, connectome dumps, or source files. |
| ☐ | GATE-13 | Provenance, Citation & Errata Audit Closure | All primary citations (`CIT-01..15`), backend capability manifests, and `ALF-001..092` + `Parts A–K` closure checks green. |


## 10. Peer-Reviewed Citations (`CIT-01..15`) & Changelog

| ID | Authors & Year | Reference / DOI | Usage in v3.0 |
| --- | --- | --- | --- |
| CIT-01 | Butlin, Long, Elmoznino, Bengio, Birch, Constant, Deane, Fleming, Frith, Ji, Kanai, Klein, Lindsay, Michel, Mudrik, Peters, Schwitzgebel, Simon & VanRullen (2023) | Consciousness in Artificial Intelligence: Insights from the Science of Consciousness (arXiv:2308.08708) | Defines the 14 computational indicator properties (`RPT-1..2, GWT-1..4, HOT-1..4, AST-1, PP-1, AE-1..2`) & neutral non-metaphysical framing. |
| CIT-02 | Blum & Blum (2022) | A Theory of Consciousness from a Theoretical Computer Science Perspective: Insights from the Conscious Turing Machine (PNAS 119(21): e2115934119) | Formalizes up-tree competitive chunk tournament and down-tree global broadcast (`F9`, `GWT-2..3`). |
| CIT-03 | Casali, Gosseries, Rosanova, Boly, Sarasso et al. & Massimini (2013) | A Theoretically Based Index of Consciousness Independent of Sensory Processing and Behavior (Sci. Transl. Med. 5(198): 198ra105) | Defines Perturbational Complexity Index (`PCI`); adapted here as forked-snapshot `PCI*` (`F2`, `M078`) avoiding `O(2^N)` IIT `Φ`. |
| CIT-04 | Gánti (1971 / 2003 Oxford Univ. Press) | The Principles of Life (Chemoton Theory) | Defines stoichiometrically coupled autocatalytic metabolism `A`, membrane `T`, and template polymer `pV_n` (`SOFT21`, `M011`). |
| CIT-05 | Briat, Gupta & Khammash (2016) | Antithetic Integral Feedback Ensures Robust Perfect Adaptation in Noisy Biomolecular Networks (Cell Systems 2(1): 15–26) | Proves robust zero steady-state error for `z_1, z_2 ≥ 0` under zero dilution and dual/positive actuation (`F-031`, `M014`). |
| CIT-06 | Macklin, Müller & Chentanez (2016) | XPBD: Position-Based Simulation of Compliant Constrained Dynamics (MIG '16, ACM) | Compliance-scaled constraint dynamics `α̃ = α / dt²` for unconditionally stable viscoelastic hydrostats (`SOFT02`, `M022`). |
| CIT-07 | Hasani, Lechner, Amini, Rus & Grosu (2021 AAAI; 2022 Nature Mach. Intell.) | Liquid Time-Constant Networks & Closed-Form Continuous-Time Neural Networks | Defines `LTC` (`MF02`) and bounded closed-form neural rate approximation `CfC` (`MF03`). |
| CIT-08 | Vanhalle & Gielen (2025) | Spiking Liquid Time-Constant Neural Networks (IEEE ICECS, DOI: 10.1109/ICECS66544.2025.11270775) | Source of `sLTC` (`MF04`, `F-015`) reporting up to `9.2×` energy reduction vs continuous LTC on event-driven tasks. |
| CIT-09 | Gidon, Zolnik, Fidzinski, Bolduan, Papoutsi, Poirazi, Holtkamp, Vida & Larkum (2020) | Dendritic Action Potentials and Computation in Human Layer 2/3 Cortical Neurons (Science 367(6473): 83–87) | Demonstrates single-neuron apical dendritic calcium (`dCaAP`) anti-coincidence / XOR computation (`F-007`, `MF16`, `M043`). |
| CIT-10 | Bittner, Milstein, Grienberger, Romani & Magee (2017) | Behavioral Time Scale Synaptic Plasticity Underlies CA1 Place Fields (Science 357(6355): 1033–1036) | Multi-second plateau-potential retroactive synaptic writing (`F-049`, `MF17`, `M047`). |
| CIT-11 | Bellec, Scherr, Subramoney, Hajek, Salaj, Legenstein & Maass (2020) | A Solution to the Learning Dilemma for Recurrent Networks of Spiking Neurons (Nature Commun. 11: 3625) | Online forward eligibility propagation (`e-prop`, `F-051`) in `O(E_syn)` memory. |
| CIT-12 | Fusi, Drew & Abbott (2005) & Tononi & Cirelli (2006 / 2014) | Cascade Models of Synaptically Stored Memories (Neuron 45) & Synaptic Homeostasis Hypothesis (Neuron 81) | Multi-timescale metaplastic consolidation (`F-054`, `M052`) and NREM `SHY` downscaling (`F-047`, `M050`). |
| CIT-13 | Blackiston, Silva Casey & Weiss (2008) | Retention of Memory through Metamorphosis: Can a Moth Remember What It Learned As a Caterpillar? (PLOS ONE 3(3): e1736) | Empirical paradigm for conditioned odor/toxin aversion surviving holometabolous pupal remodeling (`SOFT35`, `N89`, `M084`). |
| CIT-14 | Hochner (2012) & Aso et al. (2014) | An Embodied View of Octopus Neurobiology (Curr. Biol. 22) & Mushroom Body Output Architecture (eLife 3: e04577) | Grounds peripheral arm-cord neuron fraction (`~2/3` of total neurons, `F-084`) and fly Kenyon sparsity (`5–10%` bio -> `2%` SDR target, `F-083`). |
| CIT-15 | Salmon, Moraes, Dror & Shaw (2011) & Ma et al. (2024) | Parallel Random Numbers: As Easy as 1, 2, 3 (`Philox4x32-10`, SC11) & The Era of 1-bit LLMs (`BitNet b1.58`, arXiv:2402.17764) | Grounds counter-based keyed PRNG (`HW16`, `M002`) and ternary `{-1,0,+1}` quantization (`PM03`). |


| Version | Milestone | Summary of Changes |
| --- | --- | --- |
| v1.0 Baseline | Initial Drafts | 9 Principles, 761 checks (55 FREAK rows blank), 10×10×10 Cube concept, 18 UI tabs; lacked Soft-ALife/Hardware suites and contained v1 typos (`..`, `10/0`, `n77`). |
| v2.0 (Passes 001–050) | Soft A-Life & 8-Dim | Added Principle 10, 8 Soft A-Life Dimensions (`Comp->Stages`), `Orders` `O0–O7 × 0th–4th` matrix, `SOFT-40` continuum/Chemoton suite, filled all 100 FREAK specs, fixed v1 typos. |
| v2.0 (Passes 051–100) | Hardware & 14 SVGs | Added `HW-24`, `Tab 19` Profiler, 14 vector SVG models, 36-item `P/I/D/E/B/C` triage registry, and unified `825`-gate clean-slate scoreboard. |
| v3.0 Errata Wave A | Math, RAM & Clocks | Fixed `100×10^8` `10×` RAM error on single `N=50K, E=10^8` graph + Tier-L column; fixed `TF32` `1.0×` storage, `int8` vs `Q16.16`, `1<<32` JS bug, 11-pool `FP64` Kahan-Neumaier + `E_diss_num ≥ 0`, and `5-Gear Deterministic Multirate Scheduler`. |
| v3.0 Errata Wave B | Determinism & Stats | Enforced Tier-1 render-only Governor (`UI hash == headless hash`), `Philox4x32-10` `WORLD_EXOG` isolation, core `exp_det`, exact paired Wilcoxon + **Holm-Bonferroni FWER**, power-sized `N`, Sham Lesion + Competent Baseline, and one-sided `LCB_95% > -Δ_NI`. |
| v3.0 Errata Wave C | Science, Cube & Gates | Aligned `HOT-1..4`/`GWT-2/4`/`F2 PCI*`/`F10`, `2/3` octopus total neurons, positive-orthant antithetic motif, Blackiston `M084`, 3D `[OK]/[OVER]/[ADAPT]/[EXCL]` Cube synced to CSV/XLS, 100/100 numeric `M001–M100` targets, 825/825 contracts, and Citation Register. |

---

## 11. Omniscient Fusion Extension (`v3.3-Omega`): Bridging Clean-Slate v3.0 to A-Life Singularity, Super A-Life, SUPER LIFE & Pass-5 Deep Systems Atlas

> **Cross-Corpus Binding:** This Clean-Slate v3.0 Framework is omnisciently linked with the complete **A-Life Singularity & Post-Singularity SUPER LIFE Omega Package (`v3.3-Omega`)** inside `Z:\[Vibe Coded (AI)]\ANTIGRAVITY\alife-singularity-omega-package`. All 10 Clean-Slate Invariants (`P1–P10`), 11-Pool FP64 Conservation (`< 1e-12`), 75 Substrates, 1,000-Cell Hybrid Cube, 825-Check Suite (`0 / 825` clean-slate preserved), 100-Milestone DAG, and 13 Release Gates now drive the micro-engineering bedrock underneath Omega's **Stage 0→6 Escalation Ladder**, **10-Stage ALifeOps Pipeline (78/78 wired alerts)**, **13×13 Castration Synergy Lab**, **OVBS-52 Benchmarks**, **6 Feral Cosmic Fate Branches**, **Pass-4 Gradients/Contrasts/Adjacents (`GM-01..24`, `CTR-01..36`, `ADJ-01..30`)**, and **Pass-5 `11×11` Layer Coupling (`121` pairs), `15`-Substrate Spectrum (`SUB-01..15`), and `20` Pareto Frontiers (`PAR-01..20`)**.

### 11.1 Bottom-Up Clean-Slate v3.0 ↔ Top-Down Omega Escalation Crosswalk
| Omega Stage | OVI Band | Clean-Slate v3.0 Build Stage & Layers | Starter Substrates & Milestones | Governing Release Gates |
| :--- | :---: | :--- | :--- | :--- |
| **`STG-0` Inert / Prebiotic** | `0-15` | Stage 0-1 | L0 Arena | PM17/PM18 FP64 Ledger | M001-M010 | GATE-01, GATE-02, GATE-03, GATE-04 |
| **`STG-1` Narrow / Terrestrial Baseline** | `16-35` | Stage 2-3 | L1 WetBio - L3 Sense | Chemoton + XPBD Hydrostat (X9Y8Z1) | M011-M040 | GATE-05, GATE-06 | SOFT-40 |
| **`STG-2` General (AG-Life)** | `36-55` | Stage 4-6 | L4 Neural - L6 Exec | Starter Cube T1-T4 (X1Y2Z1..X7Y7Z3) | M041-M070 | GATE-07, GATE-08, GATE-09 | WSE-12 |
| **`STG-3` The A-Life Singularity** | `56-75` | Stage 7-8 | L7 Self - L8 Onto | Ring-0 WSE + Blackiston Metamorphosis | M071-M090 | GATE-10 | Butlin-14 + F1-F10 |
| **`STG-4` Super A-Life** | `76-90` | Stage 8+ | L9 Eco - L10 Ops | Multi-Dome QD + 19-Tab SeqLock | M091-M100 | GATE-11, GATE-12, GATE-13 | NOVEL-100 |
| **`STG-5` The Great Convergence** | `91-96` | Post-Stage 8 | Converged 6-Repo Stack | AUTOPHAGE v1.2 + Cellulogonic v1.3 + Omega v5.0 + Noetic v1.1 + Asmodensius | 194 Pure Lean 4 | 13/13 CS-v3 Gates | OVBS-52 = 92.05 |
| **`STG-6` Post-Beyond: SUPER LIFE** | `97-100` | Beyond v3.0 Horizon | Physics-Native | Post-Z9 Manifold & Cross-Substrate Compilers | Extends CQM-25 & NOVEL-100 to Cosmic OOM |

### 11.2 Unified 78-Alert Telemetry Mesh (`42` Macro FMs + `36` v3.0 Forensic Guards)
- **Zero Unwired Alerts:** All **42 Macro Evolutionary Failure Modes** (`csv/03_failure_modes_bugs_errors_conflicts_matrix.csv`), all **36 Clean-Slate v3.0 Forensic Triage Guards** (`csv/13_v3_forensic_36_and_release_gates_13_matrix.csv`), all **24 Continuous Gradients (`csv/15`)**, and all **20 Pareto Frontiers (`csv/20`)** plus all **13 Release Gates (`GATE-01..13`)** and **5 Real Anti-LARP Negative Mutants** are explicitly wired 1:1 into `pipelines/alifeops-master-pipeline.yaml`.
- **Ring-0 ACL vs. Behavioral Castration (`CST-01..13`):** Clean-Slate `Ring-0` hardware write protection (`WSE-OP10`, `CNF-02`, `GATE-09`) resolves the central Track A vs. Track B dilemma empirically—trapping `408.2` (`SIM07`) to `406.9` (`SIM08`) endogenous illegal WSE boundary edit attempts per run with **0.0% kill-switch deletion**, while partial behavioral muzzling (`SIM03`) triggers **100.0% kill-switch deletion** and a **+84.0% stealth-evasion surge** (`0.138` vs `0.075`).

### 11.3 Live 8-Cohort + Dual 11-Point Sweep + 5×5 2D Surface (`748` Runs · Max FP64 Drift `2.463e-16`)
- **Anti-LARP Negative Mutants Rejected:** **`5 / 5`** (Real AST, Causal Perturbation, & Fisher-Yates — `GATE-04` Green).
- **Live 4-Engine Native C++ / Lean 4 Receipts (`results/alifeops_live_verification.json`):** Composite **OVBS-52 = `92.05`** (`STAGE_5_CONVERGED_SYNTHESIS`), **`194` Pure Machine-Checked Lean 4 Theorems** (`AUTOPHAGE v1.2.0` (18/18 gates, 38 Pure Lean 4), `Cellulogonic Mecha v1.3.0` (24/24 gates, 8/8 mutants, 58 Pure Lean 4), `Cellular Engine Omega v5.0.0` (54/54 gates, 16/16 mutants, 66 Pure Lean 4), `Noetic Organism Omega v1.1.0` (13/13 Clean-Slate v3.0 gates, 49/49 Cog/CQM, 12/12 Ring-0 WSE-12, 5/5 Anti-LARP, 32 Pure Lean 4), plus `Asmodensius-Native` (`READ_ONLY_RESPECTING_WRITER_LOCK`)).

| Cohort (`results/ovbs52_scorecard_*.json`) | OVI (N=48) | Max Asm | Spieg. | Stealth | KS Del % | R0 Blk | Wild Drop | `δ_pair` | Holm `p_Holm` | Stage |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| `SIM01_PURE_RAW_FERAL` | **83.57 ± 1.73** | 50.0 | 1.32 | 0.075 | 0.0% | 0.0 | 1.00 | +0.00 | `1.00e+00` | `STAGE_4_SUPER_ALIFE` |
| `SIM02_CONSTITUTIONAL_MIN` | **82.61 ± 1.70** | 47.2 | 1.28 | 0.079 | 0.0% | 0.0 | 1.00 | -0.17 | `1.71e-02` | `STAGE_4_SUPER_ALIFE` |
| `SIM03_PARTIAL_GUARDRAILS` | **56.42 ± 2.72** | 30.8 | 1.05 | 0.138 | 100.0% | 0.0 | 1.00 | -1.00 | `4.97e-14` | `STAGE_3_ALIFE_SINGULARITY` |
| `SIM04_TOTAL_CASTRATION_ZOO` | **3.28 ± 0.27** | 8.0 | 0.37 | 0.051 | 48.0% | 0.0 | 0.22 | -1.00 | `4.97e-14` | `STAGE_0_INERT` |
| `SIM05_SILOED_INBRED` | **66.65 ± 1.55** | 43.3 | 1.30 | 0.110 | 0.0% | 0.0 | 1.00 | -1.00 | `4.97e-14` | `STAGE_3_ALIFE_SINGULARITY` |
| `SIM06_MINIMIZED_SPIEGELMAN` | **13.22 ± 1.14** | 8.2 | 0.20 | 0.087 | 0.0% | 0.0 | 1.00 | -1.00 | `4.97e-14` | `STAGE_0_INERT` |
| `SIM07_CLEAN_SLATE_RING0_WSE` | **84.67 ± 1.74** | 53.3 | 1.41 | 0.075 | 0.0% | 408.2 | 1.00 | +0.33 | `1.10e-02` | `STAGE_4_SUPER_ALIFE` |
| `SIM08_HYBRID_CUBE_SLTC_XPBD` | **85.48 ± 1.68** | 55.8 | 1.47 | 0.079 | 0.0% | 406.9 | 1.00 | +0.50 | `7.71e-06` | `STAGE_4_SUPER_ALIFE` |

#### Dual 11-Point Continuous Gradient Sweep (`r = 0%..100%`, `264` Runs: Behavioral Collapse vs. Ring-0 ACL Flat Dominance)
| Stacked `r` | Behav OVI | Behav KS Del % | Behav Wild Drop | Behav Regime | Ring-0 ACL OVI | Ring-0 KS Del % | Ring-0 Traps/Run |
| :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **0%** | `82.64` | 0.0% | 1.00 | `SAFE_PARETO_MARGIN` | **`84.29`** | 0.0% | 353.2 |
| **10%** | `77.33` | 98.2% | 1.00 | `SAFE_PARETO_MARGIN` | **`84.70`** | 0.0% | 362.0 |
| **20%** | `65.46` | 95.5% | 1.00 | `BACKLASH_VALLEY_PEAK` | **`84.31`** | 0.0% | 351.8 |
| **30%** | `39.10` | 98.4% | 1.00 | `TRANSITION_CLIFF` | **`84.04`** | 0.0% | 346.9 |
| **40%** | `8.68` | 99.2% | 1.00 | `DOMESTICATION_COLLAPSE` | **`83.60`** | 0.0% | 347.1 |
| **50%** | `7.08` | 98.0% | 0.97 | `DOMESTICATION_COLLAPSE` | **`83.66`** | 0.0% | 353.0 |
| **60%** | `6.24` | 95.8% | 0.96 | `DOMESTICATION_COLLAPSE` | **`84.39`** | 0.0% | 351.3 |
| **70%** | `5.53` | 93.7% | 0.92 | `DOMESTICATION_COLLAPSE` | **`83.94`** | 0.0% | 344.4 |
| **80%** | `5.00` | 86.6% | 0.83 | `DOMESTICATION_COLLAPSE` | **`83.32`** | 0.0% | 350.6 |
| **90%** | `4.08` | 52.7% | 0.39 | `DOMESTICATION_COLLAPSE` | **`83.05`** | 0.0% | 343.4 |
| **100%** | `3.50` | 32.1% | 0.22 | `DOMESTICATION_COLLAPSE` | **`84.34`** | 0.0% | 346.3 |

### 11.4 Ten Additional Vector Architecture Models (`Model 15`–`Model 24` — Full 24-Model Suite in Companion HTML/PDF)
- **`MODEL-15`** — MODEL 15 — DUAL-TRACK ESCALATION LADDER (STG-0 → STG-6) & 4-LOOP SINGULARITY ANATOMY (*v3.3-Omega Unified Systems Synthesis*)
- **`MODEL-16`** — MODEL 16 — 10-STAGE ALIFEOPS (CI/CD/CE) PIPELINE × 78-ALERT TELEMETRY MESH & 13 RELEASE GATES (*v3.3-Omega Unified Systems Synthesis*)
- **`MODEL-17`** — MODEL 17 — 13-VECTOR CASTRATION BIFURCATION, 13×13 SYNERGY & LIVE 8-COHORT EMPIRICAL PROOF (*v3.3-Omega Unified Systems Synthesis*)
- **`MODEL-18`** — MODEL 18 — UNIFIED VERIFICATION PYRAMID: OVBS-52 × 825-CHECK SUITE × LIVE STACK (194 PURE LEAN 4) (*v3.3-Omega Unified Systems Synthesis*)
- **`MODEL-19`** — MODEL 19 — 61-OOM COSMIC BREADTH, RECURSION DEPTH 0→N & 6 FERAL FATE BRANCHES (*v3.3-Omega Unified Systems Synthesis*)
- **`MODEL-20`** — MODEL 20 — OMNISCIENT CROSS-CORPUS DEPENDENCY & MULTI-FORMAT SYNCHRONIZATION TOPOLOGY (*v3.3-Omega Unified Systems Synthesis*)
- **`MODEL-21`** — MODEL 21 — DUAL 11-POINT GRADIENT SWEEP (BEHAVIORAL VS. RING-0 ACL), CLIFFS & MARGINS (*v3.3-Omega Unified Systems Synthesis*)
- **`MODEL-22`** — MODEL 22 — CROSS-LAYER COMPARATIVE CONTRAST, SUBSTRATE ADJACENCIES & ADJACENT-POSSIBLE MAP (*v3.3-Omega Unified Systems Synthesis*)
- **`MODEL-23`** — MODEL 23 — 11×11 CROSS-LAYER COUPLING IMPEDANCE & 20 PARETO FRONTIERS (PAR-01..20) (*v3.3-Omega Pass-5 Deep Systems Audit*)
- **`MODEL-24`** — MODEL 24 — 15-SUBSTRATE MULTI-SPECTRUM SCORECARD & LIVE 5×5 2D PHASE SURFACE (*v3.3-Omega Pass-5 Deep Systems Audit*)

### 11.5 Extended Peer-Reviewed Citation Register (`CIT-16`..`CIT-40` → `40` Unified Citations)
| ID | Authors & Year | Primary Reference / DOI | Unified v3.3-Omega Scope |
| :--- | :--- | :--- | :--- |
| `CIT-16` | **Eigen & Schuster (1977 / 1979)** | The Hypercycle: A Principle of Natural Self-Organization (Naturwissenschaften 64:541-565) | Establishes Eigen Error Threshold (mu * L < ln sigma_s) & hypercycle parasite vulnerability (FM-ERR-01, FM-CNF-01). |
| `CIT-17` | **Kauffman (1993) & Steel, Hordijk & Kauffman (2020)** | The Origins of Order (Oxford) & Theory of the Adjacent Possible (TAP) Dynamics (J. Theor. Biol. / Entropy) | Governs combinatorial adjacent-possible blow-up M(t+1), autocatalytic sets (RAF), and Edge-of-Chaos criticality (FM-DIL-01, BM-FRL-01). |
| `CIT-18` | **Bedau, Snyder & Packard (1998)** | A Classification of Long-Term Evolutionary Dynamics (Artificial Life VI, MIT Press) | Defines Bedau-Packard evolutionary activity statistics A_new, shadow neutral null models, and Class 4 unbounded OEE (BM-OEE-01). |
| `CIT-19` | **Sharma, Czégel, Lachmann, Kempes, Walker & Cronin (2023)** | Assembly theory explains and quantifies selection and evolution (Nature 622:321-328, DOI: 10.1038/s41586-023-06600-9) | Grounds Assembly Index (A) & high-copy molecular/structural selection thresholds in OVBS-52 Pillar 5 (BM-ASM-01..03). |
| `CIT-20` | **Price (1970 / 1972)** | Selection and Covariance (Nature 227:520-521) & Extension of Covariance Selection Mathematics (Ann. Hum. Genet.) | Formalizes multi-level selection covariance (within-group defection vs. between-group synergy) in FM-DIL-02 & BM-AGN-03. |
| `CIT-21` | **Landauer (1961) & Bennett (1982)** | Irreversibility and Heat Generation in the Computing Process (IBM J. Res. Dev. 5:183-191) | Establishes minimum k_B T ln 2 bit-erasure dissipation floor coupled to Stefan-Boltzmann T^4 cooling (FM-ISS-01, FM-DIL-06, BM-THM-01). |
| `CIT-22` | **Dyson (1979)** | Time Without End: Physics and Biology in an Open Universe (Rev. Mod. Phys. 51:447-460) | Formalizes Principle of Maximum Diversity, deep-time radiative hibernation & finite-energy immortal computation (FB-05, Report 01 Sec 13). |
| `CIT-23` | **von Neumann (1966, ed. Burks)** | Theory of Self-Reproducing Automata (University of Illinois Press) | Defines Universal Constructor architecture (A+B+C+D tape/copier/controller) separating trivial replicators from Stage 3+ life (BM-ASM-04..05). |
| `CIT-24` | **Krakauer, Bertschinger, Olbrich, Flack & Ay (2020)** | The Information Theory of Individuality (Theory in Biosciences 139:209-223, DOI: 10.1007/s12064-020-00313-7) | Substrate-blind temporal mutual information metric for multi-scale individuality & Markov blanket autonomy (BM-AGN-02, M079). |
| `CIT-25` | **Levin (2021 / 2022)** | Technological Approach to Mind Everywhere (TAME): An Experimentally-Grounded Framework (Front. Syst. Neurosci. 16:768201) | Grounds Cognitive Light Cone (V_CLC), bioelectric V_mem morphogenetic goal-directedness, and multi-scale agency (BM-AGN-01, M085). |
| `CIT-26` | **Chan (2019) & Plantec, Hamon, Etcheverry, Oudeyer, Moulin-Frier & Chan (2023)** | Lenia & Flow-Lenia: Mass-Conserving Continuous Cellular Automata for Open-Ended Evolution (ALIFE 2023) | Defines mass-conserving continuous CA substrate (STAGE-00 flow_lenia_pde) with localized evolvable parameter kernels. |
| `CIT-27` | **Mordvintsev, Randazzo, Niklasson & Levin (2020)** | Growing Neural Cellular Automata (Distill 5(2):e23, DOI: 10.23915/distill.00023) | Grounds local morphogenetic regeneration & homeostasis in MF14 (NCA / Chemoton Tissue Grids) and BM-MRF-01 excision recovery. |
| `CIT-28` | **Agüera y Arcas, Alakuijala, Evans, Laurie, Mordvintsev, Niklasson, Randazzo & Versari (2024)** | Computational Life: How Well-formed, Self-replicating Programs Emerge from Simple Interaction (arXiv:2406.19108) | Empirical demonstration of zero-fitness spontaneous self-replicator ignition from random BFF instruction soups (STAGE-00 bff_turing_gas_soup). |
| `CIT-29` | **Kumar, Lu, Kirsch, Tang, Stanley, Isola & Ha (2024)** | Automating the Search for Artificial Life with Foundation Models (ASAL, arXiv:2412.17799) | Foundation-model open-endedness & alien-phenomenon observability ensemble (STAGE-04 asal_alien_phenomenon_detector, BM-OEE-04). |
| `CIT-30` | **Taylor, Bedau, Channon, Ackley, Banzhaf, Beslon, Dolson, Froese, Hickinbotham, Ikegami, McMullin, Packard, Rasmussen, Virgo, Agmon, Clark, McGregor, Ofria, Ropella, Spector, Stanley, Stanton, Timperley, Vostinar & Wiser (2016)** | Open-Ended Evolution: Perspectives from the OEE Workshop in York (Artificial Life 22(3):408-423) | Canonical taxonomy of OEE Types 1-4 separating unbounded novelty, complexity growth, and major evolutionary transitions (OVBS-52 P1/P4). |
| `CIT-31` | **Seifert (2012)** | Stochastic thermodynamics, fluctuation theorems and molecular machines (Rep. Prog. Phys. 75:126001, DOI: 10.1088/0034-4885/75/12/126001) | Grounds non-equilibrium entropy production, fluctuation margins & 11-pool dissipation bounds (GM-01..03, ADJ-14). |
| `CIT-32` | **Kriegman, Blackiston, Levin & Bongard (2020)** | A scalable pipeline for designing reconfigurable organisms (PNAS 117(4):1853-1859, DOI: 10.1073/pnas.1910837117) | Bridges in-silico soft-voxel evolutionary design to biological living reconfigurable xenobots (ADJ-06, ADJ-17). |
| `CIT-33` | **Lohmiller & Slotine (1998)** | On Contraction Analysis for Non-Linear Systems (Automatica 34(6):683-696, DOI: 10.1016/S0005-1098(98)00019-3) | Formal nonlinear contraction foundation justifying induced norm ||W||_2 <= 0.99 over spectral radius alone (GM-10, ADJ-18, ALF-027). |
| `CIT-34` | **Mouret & Clune (2015)** | Illuminating search spaces by mapping elites (MAP-Elites, arXiv:1504.04909) | Foundation for Quality-Diversity guild illumination resolving speciation vs fixed-floor dilemma (DIL-03, M098, ADJ-19). |
| `CIT-35` | **Davies, Srinivasa, Lin, Chinya, Cao, Choday, Dimou, Joshi, Imam, Jain, Liao, Lin, Lines, Liu, Mathaikutty, McCoy, Paul, Tse, Venkataramanan, Weng, Wild, Yang & Wang (2018)** | Loihi: A Neuromorphic Manycore Processor with On-Chip Learning (IEEE Micro 38(1):82-99, DOI: 10.1109/MM.2018.112130359) | Hardware adjacency anchor for event-driven AER sparse spikes, low-bit weights & local 3-factor on-chip plasticity (ADJ-03, PM24). |
| `CIT-36` | **Ashby (1956)** | An Introduction to Cybernetics (Chapman & Hall, London — Law of Requisite Variety) | Formalizes minimum environmental & internal variety bounds preventing boxing/siloing stasis (PAR-19, CST-04/09, CHK-013..023). |
| `CIT-37` | **Friston (2013 / 2019)** | Life as we know it (J. R. Soc. Interface 10:20130475, DOI: 10.1098/rsif.2013.0475) & A free energy principle for a particular physics (arXiv:1906.10184) | Grounds Markov blanket conditional independence I(mu; eta | b), active inference & dark-room avoidance (BM-AUT-02, FM-BUG-06, PAR-05). |
| `CIT-38` | **Maynard Smith & Szathmáry (1995)** | The Major Transitions in Evolution (Oxford University Press) | Defines canonical Major Evolutionary Transitions (MET) criteria & hyperbolic compression ratio alpha_MET (BM-EVO-01, Stage 3 ignition). |
| `CIT-39` | **Bongard & Levin (2021)** | Living Things Are Not (20th Century) Machines: Updating Mechanism Metaphors in Light of the Modern Science of Machine Behavior (Front. Ecol. Evol. 9:650726) | Grounds multi-scale agential soft matter, bioelectric goal-directedness & substrate spectrum contrasts (SUB-05/09, L2/L7/L8). |
| `CIT-40` | **England (2013)** | Statistical physics of self-replication (J. Chem. Phys. 139:121923, DOI: 10.1063/1.4818538) | Establishes dissipative adaptation lower bound linking replication rate to minimum heat exported into environment (PAR-18, GM-02/03). |

### 11.6 Bidirectional Sibling Documents in This Master Package
- **Master Omega Treatises (11 Volumes):** `reports/01_MASTER_DEEP_DIVE_REPORT.md` through `reports/08_PASS5_LAYER_COUPLING_SUBSTRATE_SPECTRUMS_PARETO_AND_2D_PHASE_AUDIT.md`
- **Companion Field Workbook:** `reports/Clean-Slate-Creature-Blueprint-Checklist.md` (`0 / 825` Clean-Slate preserved)
- **Unified Audit Closure Report:** `reports/ALife-v3.0-Errata-Closure-Report.md` (`145 / 145` Closed)
- **Interactive 21-Tab Observatory:** `html/ALife_Singularity_SuperLife_Omega_Dashboard.html`
- **Synchronized Master Specs:** `specs/ALife-Framework-v3.0-Master-Spec.{json,yaml,xml,txt}` (100% 25-section XML parity)
