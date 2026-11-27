# Security Policy

## Supported Versions

| Version | Supported |
| :--- | :--- |
| `3.4.x` | Yes (Active) |
| `< 3.5.0` | No (Upgrade to `v3.5.0`) |

## Scope & Threat Model

This repository ships static scientific datasets, offline HTML5 applications, Python verification scripts, Lean 4 proofs, and AMS-LaTeX sources. It does **not** operate a network service or process personal data. See [`docs/threat-model.md`](docs/threat-model.md) for the full threat model (supply-chain provenance, HTML/XSS sanitization via `esc()`, secret hygiene via `.gitleaks.toml`, and Lean kernel trust boundaries).

## Reporting a Vulnerability

Please report security concerns privately rather than opening a public issue:
- **GitHub Security Advisories:** `https://github.com/0thernes/alife-singularity-omega-package/security/advisories/new`
- **Direct Contact:** `0_0@0thernes.art` (Alexander Stephen Donahue)

Expected initial acknowledgment within 72 hours. Validated findings are patched transparently and credited in `CHANGELOG.md` and `ERRATA.md`.
