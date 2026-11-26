# Threat Model (Build Standard B36)

## 1. System Scope & Assets
`alife-singularity-omega-package` is a local, offline-verifiable research software, formal-proof, and multi-format data publication repository. It runs no network server, stores no user credentials, and processes no personal data.

### Protected Assets
1. **Formal Proof Integrity (`lean/`):** Guaranteeing zero `sorry`, zero custom `axiom`, zero `native_decide`, and constructive axioms $\subseteq [\text{propext}, \text{Quot.sound}]$.
2. **Empirical & Receipt Integrity (`results/`, `csv/`, `specs/`):** Guaranteeing zero unhardcoded score tampering, conservation drift `< 1e-12`, and bijective SHA-256 manifests.
3. **Offline HTML5 Safety (`html/`):** Preventing XSS injection when rendering embedded dataset strings inside the standalone Observatory DOM.
4. **Repository Supply Chain & Secret Hygiene:** Preventing leaked credentials, oversized binary commits (`>= 5 MB`), or silent drift between manifests and release artifacts.

## 2. Trust Boundaries & Mitigations

| Threat Vector | Concrete Risk | Control / Mitigation | Verification |
| :--- | :--- | :--- | :--- |
| **Axiom / Proof Spoofing** | A `sorry`, custom axiom, or `native_decide` slips into `lean/` or README text drifts from actual kernel axioms. | Strict `module` encapsulation, `VerifyAxioms.lean`, `leanchecker-paranoid`, and exact string-equality script `scripts/check_readme_axioms.py`. | Gate 19, Gate 22, CI `lean-formal-proofs` |
| **Benchmark / Metric Gaming ("LARPing")** | Hardcoded OVI scores, phantom energy injection, or rigged causal ablations. | `5/5` real Anti-LARP simulation mutants, `6/6` Python semantic mutants, `35/35` compiled C/C++ mutants, and 50-digit independent oracle (`reference/ovbs52_oracle.py`). | Gate 6, Gate 22, `pytest` |
| **DOM XSS in Offline HTML5 Apps** | Unescaped table cells or search strings injecting script tags into `ALife_Singularity_SuperLife_Omega_Dashboard.html`. | All dynamic DOM cells pass through strict `esc()` HTML entity escaping; static JS syntax verified by `node --check`; live headless Chrome stress test runs all 22 tabs with `0` JS errors. | Gate 10, Gate 17 |
| **Secret Leakage & Binary Bloat** | Accidental commit of API tokens, `.env`, or `> 5 MB` archives. | `.gitignore`, `.gitleaks.toml`, `gitleaks` CI scan (report-only), `Audit-Repo.ps1` `A24` (`< 5 MB` + regex secret scan), and lossless `pypdf` PDF compression. | Gate 21, `Audit-Repo.ps1`, CI |
| **Supply-Chain Tampering on Release** | Modified PDFs, arXiv tarballs, or ZIP bundles post-build. | `CHECKSUMS.sha256`, `data/MANIFEST.sha256`, `MANIFEST_SHA256.txt`, `SHA256SUMS` on release tags, and SLSA `actions/attest-build-provenance`. | Gate 12, Gate 18, `.github/workflows/release.yml` |
