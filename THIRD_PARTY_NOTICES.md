# Third-Party Notices and Attribution

This repository builds upon open-source toolchains, scientific Python packages, and repository governance standards. All third-party dependencies are installed at build/test time and are not vendored into this repository unless explicitly noted.

| Component | License | Usage in This Repository |
| :--- | :--- | :--- |
| **Lean 4 (`v4.35.0`) & Lake** (`leanprover/lean4`) | Apache-2.0 | Zero-Mathlib formal theorem proving (`lean/OmegaPackageProofs/`) and independent kernel validation (`leanchecker`, `leanchecker-paranoid`) |
| **Build Standard for LLMs (`v1.2.0`)** (`docs/build-standard.md`, `repo-standard.schema.json`, `scripts/Audit-Repo.ps1`, `scripts/audit-repo.sh`, `scripts/audit-checks.tsv`, `.github/labels.tsv`) | Author's own reusable standard (`Alexander Stephen Donahue`) | Repository governance, 90-item audit rubric, and 10-class finding taxonomy |
| **Python 3.12 (`PSF-2.0`) & `uv` (`MIT`/`Apache-2.0`)** | PSF-2.0 / MIT / Apache-2.0 | Reproducible environment resolution and build/verification scripting |
| **NumPy & SciPy** | BSD-3-Clause | Statistical Wilcoxon signed-rank / Holm–Bonferroni FWER calculations and figure arrays |
| **Matplotlib** | PSF-based (Matplotlib License) | Publication vector PDF figure and social-preview card synthesis |
| **OpenPyXL (`MIT`), `xlwt` (`BSD`), `xlrd` (`BSD`)** | MIT / BSD | Generation and binary readback verification of 5 Excel workbooks |
| **PyYAML (`MIT`) & `jsonschema` (`MIT`)** | MIT | Draft 2020-12 schema validation for `OVBS-52` scorecards, `ALifeOps` YAML, and `repo.yaml` |
| **pypdf** | BSD-3-Clause | Lossless level-9 content-stream compression and deep PDF text hygiene verification |
| **pytest (`MIT`) & Hypothesis (`MPL-2.0`)** | MIT / MPL-2.0 | Unit, regression, negative, differential, and 1,000-example property-based testing |
| **Ruff (`MIT`) & Mypy (`MIT`)** | MIT | Report-only static linting and strict type checking (`reference/`) |
| **Tectonic (`MIT`) & AMS-LaTeX (`LPPL-1.3c`)** | MIT / LPPL-1.3c | Reproducible `amsart` white paper and clean-room `arxiv_submission.tar.gz` compilation |
| **Node.js** | MIT | Embedded Observatory JavaScript syntax check (`node --check`) |
| **Chromium / Google Chrome** | BSD-3-Clause | Headless vector PDF rendering and 22-tab live DOM click-through stress test |
