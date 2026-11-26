# AGENTS.md — Canonical Agent Instructions (`alife-singularity-omega-package` v3.4.0)

> This file is the single canonical agent instruction file (< 32 KiB). `CLAUDE.md`, `GEMINI.md`, and `.cursor/rules/build-standard.mdc` all point here.

## Identity & Legal Scope

- **Author:** Alexander Stephen Donahue (`Independent Researcher, Spokane, WA, USA`)
- **ORCID:** `0009-0006-8168-9648` (`https://orcid.org/0009-0006-8168-9648`)
- **Email / GitHub:** `0_0@0thernes.art` · `https://github.com/0thernes/alife-singularity-omega-package`
- **CRITICAL LEGAL RULE:** Never write `"0thernes LLC"` anywhere in prose, metadata, licenses, or code — no LLC has been legally formed. Always use `"Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA)"`.
- **Dual License:** Code/Lean 4/tests = `Apache-2.0` (`LICENSE`); Prose/datasets/figures = `CC-BY-4.0` (`LICENSE-DOCS`).

## Hard Rules (Build Standard v1.2.0 `R1–R8`)

- **R1–R4:** Trunk workflow directly on `main`. Never add git hooks, branch protection scripts, PR templates, Dependabot/Renovate, CodeRabbit, `.github/copilot-instructions.md`, or `FUNDING.yml`. CI is informational/report-only.
- **Zero Consolidation:** Preserve 100% of the 17 baked Clean-Slate v3.0 deliverables alongside all Omega files.
- **Clean-Slate `0 / 825` Policy:** Never emit `U+2611` (`☑`) in any Clean-Slate MD, HTML, CSV, or PDF file.
- **Honest Verification & Non-Retirement Boundary:** Exactly **`0 / 1,900`** overarching open problems in `0thernes/unsolved-problems-mega-atlas` (V2.4.0) are solved or retired. Never claim peer review, fabricated DOIs, or sentience.
- **Strict File-Size Hygiene (`A24`):** Every Git-tracked file must remain `< 5.00 MB` (`5,242,880` B). Chrome PDFs are losslessly compressed via `pypdf`; `ALife_Singularity_SuperLife_Omega_Package.zip` is gitignored and attached to GitHub Releases.
- **Lean 4 Purity:** Zero `sorry`, `admit`, custom `axiom`, or `native_decide` in `lean/`. Axioms must stay strictly within `[propext, Quot.sound]`.
- **Exact Theorem Arithmetic:** `48` (AUTOPHAGE v1.4.0) + `70` (Cellulogonic Mecha v1.5.0) + `89` (Cellular Engine Omega v5.2.0) + `54` (Noetic Organism Omega v2.1.0) + `30` (Asmodensius-Native v1.1.0) = **`291`** Native Pure 6-Kernel Lean 4.35.0 Theorems + **`36`** Local `lean/OmegaPackageProofs/` Theorems (`+ 4` Palomar comparator certificates = `40` `#print axioms` lines) = **`327` Pure 6-Kernel Lean 4.35.0 Theorems**. Never write `240`, `244`, or `280` for current live counts!
- **PowerShell Bracket Safety (Windows `Z:`):** Because the canonical local checkout lives under `Z:\[Vibe Coded (AI)]\ANTIGRAVITY\alife-singularity-omega-package`, always pass `-LiteralPath` to PowerShell file cmdlets.

## One-Word Commands (`justfile`)

| Command | Action |
| :--- | :--- |
| `just lean` | Build `lean/OmegaPackageProofs/` (Lean 4.35.0), run `VerifyAxioms.lean`, `leanchecker`, and `leanchecker-paranoid` |
| `just paper` | Generate 4 vector PDF figures + `docs/media/social-preview.png`, compile `paper/main.tex` (`0` overfull hboxes), build & verify clean-room `dist/arxiv_submission.tar.gz` |
| `just build` | Rebuild 24 CSVs (`2,822` rows), 4 Specs (`26` XML), 5 Excel Workbooks, 3 HTML5 apps (`22`-tab Observatory), 3 lossless Chrome PDFs, manifests, ZIP, and 22 Forensic Gates |
| `just test` | Run `pytest` unit, negative, regression, Hypothesis (`1,000+` examples) & 50-digit differential oracle (`2,000+` cases) |
| `just mutate` | Run `scripts/run_mutation_audit.py` (`6/6 = 100%` semantic mutants killed) |
| `just forensic` | Run all `22/22` automated forensic integrity gates (`scripts/audit_omniscient_integrity.py`) |
| `just audit` | Score repository against Build Standard v1.2.0 (`scripts/Audit-Repo.ps1`, target `100.0%`) |
| `just reproduce` | End-to-end clean-clone reproduction of every headline result |

## 10 Finding Classes (Mandatory Classification)

Every finding in issues, reviews, and `HARDENING_LOG.md` uses exactly one class:
`bug` · `error` · `issue` · `problem` · `concern` · `dilemma` · `conflict` · `gap` · `hole` · `blindspot`.
