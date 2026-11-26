# Technical Glossary & 10-Class Finding Taxonomy (Build Standard A44)

## 1. Domain Terms

- **ALifeOps:** Continuous operations and telemetry methodology for autonomous artificial-life ecosystems (`pipelines/alifeops-master-pipeline.yaml`, `78` alerts, `13` Release Gates).
- **Anti-LARP Mutant:** A deliberately sabotaged negative-control variant (fake energy, shuffled seeds, bypassed gate, or broken scorer) injected to prove that automated verification gates reject counterfeit claims (`5/5` simulator mutants, `6/6` Python oracle mutants, `35/35` compiled C/C++ mutants).
- **Assembly Index:** Minimum number of recursive joining operations required to construct an object or lineage phenotype (Sharma et al., 2023).
- **Constraint Castration (`CST-01..13`):** Thirteen parameterized behavioral/metabolic/architectural restraints whose partial application triggers adversarial backlash (`100%` kill-switch deletion) and whose total application causes domestication collapse (`Stage 0`, `78%` wild-drop mortality).
- **Clean-Slate v3.0:** The 17-file micro-hardware runtime specification (`938` checklist items, `825` executable C11 checks, `100` milestones, `13` Release Gates, `75` substrates, `10x10x10` Hybrid Cube).
- **Hardware Ring-0 ACL (design term):** Memory-privilege boundary in the Clean-Slate design separating protected physics/conservation/evaluation state from plastic synaptic weights and morphological actuators. In Lean it appears only as the type `MemRing` (`ring0ProtectedKernel`, `ring1PlasticSynapses`, `ring2MorphologySoma`) and the predicate `wseWritePermitted`, which returns `false` for `ring0ProtectedKernel` by definition. No hardware is modelled in Lean.
- **Holm–Bonferroni FWER:** Step-down family-wise error rate correction applied across all 7 paired cohort contrasts against `SIM01` (`N = 48` locked seeds).
- **Hybrid Compatibility Cube (`10x10x10`):** `1,000`-cell tensor crossing 10 substrate models ($X$), 10 numerical precisions ($Y$), and 10 spatial geometries ($Z$), partitioned cleanly into `661 [OK] + 274 [ADAPT] + 20 [OVER] + 45 [EXCL] = 1,000`.
- **OVBS-52 (Omega Vitality Benchmark Suite):** 8-pillar, 52-metric weighted composite index ($\mathrm{OVI} \in [0, 100]$) gated by 5 anti-gaming checks ($\gamma \in \{0, 1\}$) and the Spiegelman genome retention factor ($s \in [0, 1]$).
- **Palomar Comparator:** Minimal interface contract (`lean/palomar/PalomarChallenge.lean` ↔ `lean/PalomarSolution.lean`) separating theorem statements from proof implementations for independent automated grading.
- **Spiegelman's Monster:** Evolutionary stripping of functional genome length under metabolic starvation (`SIM06`: ratio `0.20`), named after Mills, Peterson & Spiegelman (1967).
- **WSE-12 (Weight-Space Editing):** Bounded runtime self-modification protocol requiring that writes never target Ring-0 and that the spectral norm satisfies $\|W\|_2 \le 0.99$ (in Lean only a natural-number argument compared with `9900`; no norm is computed).

---

## 2. Canonical 10-Class Finding Taxonomy (Build Standard v1.2.0)

Every finding across GitHub Issues, `HARDENING_LOG.md`, and code reviews is tagged with **exact one** class:

| Class | Definition |
| :--- | :--- |
| **`bug`** | Code does something different from its spec or intent (a defect in program logic). |
| **`error`** | Wrong number, claim, doc, config, version, build, or command. |
| **`issue`** | Works and is not wrong, but is unclear, inconsistent, fragile, or hard to maintain. |
| **`problem`** | External obstacle (network, account, legal status, toolchain) blocks progress. |
| **`concern`** | Risk that has not caused harm yet (security, cost, legal, reliability, drift). |
| **`dilemma`** | Trade-off between valid options; the owner decides. |
| **`conflict`** | Two requirements or rules contradict each other. |
| **`gap`** | Something required or expected is missing; nothing present is wrong. |
| **`hole`** | Missing check or safeguard, so a defect could pass unnoticed. |
| **`blindspot`** | A user, platform, failure mode, or assumption nobody has examined yet. |
