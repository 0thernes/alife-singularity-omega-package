# Frequently Asked Questions (FAQ)

### 1. Did this project solve any of the 1,900 open problems in `unsolved-problems-mega-atlas`?
**No.** An exhaustive automated and manual audit across all `1,900` open problems in `0thernes/unsolved-problems-mega-atlas` (V2.4.0) confirms that **exactly `0 / 1,900` overarching open problems are solved or retired**. We transparently document `25` scoped in-silico sub-results, formal bounds, and operational proxies in `csv/21_mega_atlas_1900_open_problems_crosswalk.csv` and `reports/09_MEGA_ATLAS_1900_OPEN_PROBLEMS_CROSSCHECK.md` while keeping every parent problem strictly **OPEN**.

### 2. What is the figure 327, and which Lean declarations are checked inside *this* repository?
- **36 core declarations + 4 Palomar comparator wrappers (`40` audited `#print axioms` lines)** live in this repository (`lean/OmegaPackageProofs/`) and compile in `< 5` seconds on a clean clone using zero-Mathlib **Lean 4.35.0**, with axioms within `[propext, Quot.sound]`. They are kernel-checked by Lean (`lake build`, `leanchecker`); in Ubuntu CI the `4` comparator targets were also accepted by `6` independent kernels. A local multi-checker transcript is in `results/lean4-multi-kernel.txt`.
- Of the `36`, `15` are quantified statements about the package's own scoring definitions; `21` are closed evaluations, literal sums or non-vacuity witnesses. `ring0_kernel_state_invariant` holds because the modelled write function returns its input for every ring.
- **291 further Lean 4.35.0 theorems** (`48` AUTOPHAGE v1.4.0 + `70` Cellulogonic Mecha v1.5.0 + `89` Cellular Engine Omega v5.2.0 + `54` Noetic Organism Omega v2.1.0 + `30` Asmodensius-Native v1.1.0) are reported by the five companion C11/C23 repositories at those versions and recorded in `results/alifeops_live_verification.json`. They are not built or checked here.
- `327 = 291 + 36` is a sum of reported counts. Lean checks only the arithmetic, not the existence of the `291` theorems.

### 3. Why isn't `ALife_Singularity_SuperLife_Omega_Package.zip` committed inside Git?
Per Build Standard v1.2.0 `A24`, no Git-tracked file may exceed `5.00 MB`. The full package ZIP (~`6–8 MB`) is gitignored locally, generated on demand by `just build`, mirrored to `I:`, and uploaded automatically to GitHub Releases with `SHA256SUMS` and SLSA provenance. Meanwhile, all three Chrome vector PDFs are losslessly compressed via `pypdf` (`< 2.5 MB` each with 100% text parity).

### 4. Why does `Clean-Slate` forbid the `☑` (`U+2611`) character?
The Clean-Slate v3.0 verification policy guarantees that blank checklists shipped in templates (`0 / 825` pre-checked boxes) never visually imply unexecuted checks have passed. Gate 9 and Gate 16 enforce `0` occurrences of `U+2611` across Clean-Slate Markdown, HTML, CSV, and extracted PDF text.

### 5. Do the `Noetic Organism Omega` cognitive checks prove digital consciousness?
**No.** All `29` consciousness/cognitive checks (`Butlin-14`, `F1–F10`, `CQM-25` subset) are explicitly labeled `EXECUTED_PASS_INDICATOR_ONLY` (ADR 0018). They measure functional dynamical architectures only and make zero claims regarding subjective phenomenal qualia.

### 6. Why did the author replace `"0thernes LLC"` with `"Independent Researcher"`?
Following the Defensible Independent AI Research Playbook v1.3 (Finding 1), because no formal LLC corporate entity has been registered yet, all legal, copyright, ORCID, CITATION, and white-paper metadata accurately list **Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA)** (`ORCID: 0009-0006-8168-9648`).
