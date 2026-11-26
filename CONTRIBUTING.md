# Contributing Guide

Thank you for your interest in `alife-singularity-omega-package`! This repository follows **Build Standard for LLMs v1.2.0** ([`docs/build-standard.md`](docs/build-standard.md)).

## Workflow & Hard Rules

1. **Trunk Workflow (`main`):** All development proceeds on `main` (or short-lived local branches merged directly to `main`). Per Hard Rules `R1–R4`, this repository uses **no** git hooks, **no** PR templates, and **informational report-only CI**.
2. **Classification of Findings:** Every bug, error, or gap reported via GitHub Issues must be classified into exactly one of the 10 finding classes (`bug`, `error`, `issue`, `problem`, `concern`, `dilemma`, `conflict`, `gap`, `hole`, `blindspot`) defined in [`docs/glossary.md`](docs/glossary.md).
3. **Zero Consolidation & Clean-Slate Invariants:**
   - Never delete or collapse any of the 17 baked Clean-Slate v3.0 deliverables.
   - Never emit `U+2611` (`☑`) in any Clean-Slate Markdown, HTML, CSV, or PDF file.
   - Never introduce `sorry`, `admit`, `axiom`, or `native_decide` in `lean/`.
   - Keep all Git-tracked files strictly `< 5.00 MB`.
4. **Verification Before Pushing:**
   - Run `just lean` (zero warnings, axioms $\subseteq [\text{propext}, \text{Quot.sound}]$).
   - Run `just test` (`pytest` + Hypothesis + differential oracle).
   - Run `just mutate` (`6/6` mutants killed).
   - Run `just forensic` (`22/22` Forensic Gates PASS).
   - Run `just audit` (`100.0%` Build Standard v1.2.0).

## Licensing of Contributions

- Prose, documentation, datasets, and figures are licensed under **CC-BY-4.0** (`LICENSE`).
- Code, scripts, tests, and Lean 4 formalizations are licensed under **Apache-2.0** (`LICENSE-CODE`).
By submitting a contribution, you agree that it may be distributed under these dual terms.
