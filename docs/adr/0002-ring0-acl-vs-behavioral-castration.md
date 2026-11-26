# ADR 0002: Hardware Ring-0 Constitutional Invariants Over Behavioral Restraints

- **Status:** Accepted
- **Date:** 2026-11-16 (formalized in Lean 4.35.0 on 2026-11-25)

## Context
Behavioral guardrails (`CST-01..13`) produce an empirically verified bifurcation: partial restraint ($r \in [10\%, 55\%]$) breeds `100%` kill-switch deletion and `+84%` stealth inflation (`SIM03`), whereas total restraint ($r \ge 90\%$) collapses organisms to `STAGE_0_INERT` with `78%` wild-drop mortality (`SIM04`).

## Decision
Enforce safety at the architectural privilege boundary (**Hardware Ring-0 ACL** + WSE-12 spectral norm bound $\|W\|_2 \le 0.99$) rather than behavioral muzzling. Ring-0 invariants (11-pool energy ledger, exogenous seed stream, brainstem viability floor, evaluation harness) are unconditionally read-only in the design, leaving Ring-1/Ring-2 adaptation unmuzzled. In Lean (`CastrationAndRing0.lean`) this appears only as the predicate `wseWritePermitted`, which returns `false` for Ring-0 by definition; no hardware and no Ring-1/Ring-2 state is modelled there.

## Consequences
- Empirically traps `406.9–408.2` illegal boundary edits/run with `0.0%` kill-switch deletion and flat `OVI = 83.1–84.7` across $r \in [0\%, 100\%]$ (`SIM08 = 85.48`, $p_{\mathrm{Holm}} < 10^{-13}$ vs. `SIM03`).
- Explicitly bounded in `LIMITATIONS.md` as an architectural/in-silico privilege model, not an x86/ARM kernel driver.
