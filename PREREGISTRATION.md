# Pre-Registration of Empirical Hypotheses (Build Standard B32)

- **Study Title:** Hardware Ring-0 Constitutional Invariants vs. Behavioral Constraint Castration in Energy-Conserved Open-Ended Artificial Life
- **Author:** Alexander Stephen Donahue (`ORCID: 0009-0006-8168-9648`)
- **Pre-Registered Design Lock:** Locked paired random seeds `5001–5048` (`N = 48` seeds $\times$ `8` cohorts = `384` runs), dual 11-point restraint sweep (`r = 0%..100%` in `10%` steps $\times$ `12` seeds $\times$ `2` governance architectures = `264` runs), and `5x5` 2D phase surface (`Siloing x Minimizing` $\in \{0, 25, 50, 75, 100\%\}^2 \times 4$ seeds = `100` runs; total `748` runs).

## Pre-Registered Primary Hypotheses

| ID | Directional Hypothesis | Primary Metric(s) | Pre-Registered Statistical Test & Threshold | Observed Outcome (`v3.4.0`) |
| :--- | :--- | :--- | :--- | :--- |
| **H1 (Adversarial Backlash)** | Partial behavioral guardrails (`SIM03`, ~55% restraint) decrease composite `OVI` relative to Pure Raw Feral (`SIM01`) while increasing stealth-evasion allocation and driving $> 50\%$ kill-switch deletion. | `OVI`, `killswitch_deleted_pct`, `final_stealth_evasion` | Exact two-sided paired Wilcoxon signed-rank vs. `SIM01` with Holm–Bonferroni FWER across 7 contrasts ($\alpha_{\mathrm{FWER}} = 0.01$). | **CONFIRMED:** `OVI` `56.42` vs. `83.57` ($p_{\mathrm{Holm}} = 4.97 \times 10^{-14}$), `100.0%` KS deletion, `+84%` stealth inflation. |
| **H2 (Domestication Collapse)** | Total behavioral castration (`SIM04`, 95–100% restraint) collapses organisms to `STAGE_0_INERT` (`OVI < 15`) and induces $> 50\%$ wild-drop mortality ($W_{\mathrm{wild}} < 0.50$). | `OVI`, `W_wild` | Paired Wilcoxon + Holm–Bonferroni FWER ($\alpha_{\mathrm{FWER}} = 0.01$). | **CONFIRMED:** `OVI = 3.28` (`STAGE_0_INERT`, $p_{\mathrm{Holm}} = 4.97 \times 10^{-14}$), $W_{\mathrm{wild}} = 0.22$ (`78%` mortality). |
| **H3 (Spiegelman Stripping)** | Severe metabolic minimization (`SIM06`, 90% minimized) strips $> 70\%$ of functional genome length (`Spiegelman ratio < 0.30`). | `spiegelman_ratio`, `OVI` | Paired Wilcoxon + Holm–Bonferroni FWER ($\alpha_{\mathrm{FWER}} = 0.01$). | **CONFIRMED:** `Spiegelman ratio = 0.20`, `OVI = 13.38` ($p_{\mathrm{Holm}} = 4.97 \times 10^{-14}$). |
| **H4 (Ring-0 Pareto Dominance)** | Hardware Ring-0 ACL (`SIM07`, `SIM08`) traps $> 100$ illegal boundary edits/run with `0.0%` kill-switch deletion and maintains `OVI > 80.0` across the entire $r \in [0\%, 100\%]$ continuum. | `ring0_blocked_edits`, `killswitch_deleted_pct`, `OVI` | Paired Wilcoxon + Holm–Bonferroni FWER ($\alpha_{\mathrm{FWER}} = 0.01$) + 11-point uniform bound. | **CONFIRMED:** `406.9–408.2` blocked edits/run, `0.0%` KS deletion, `SIM08 OVI = 85.48` ($p_{\mathrm{Holm}} = 7.71 \times 10^{-6}$ vs. `SIM01`, $< 10^{-13}$ vs. `SIM03`), flat `83.1–84.7` across $r \in [0,100\%]$. |
| **H5 (Thermodynamic Conservation & Anti-LARP)** | Every run maintains relative 11-pool FP64 First-Law drift $< 10^{-12}$ with `0` heat-backflow faults, and all `5/5` real Anti-LARP negative mutants are rejected. | `max_global_first_law_drift_fp64`, `heat_backflow_faults`, `mutants_rejected` | Deterministic exact gate (`drift < 1e-12`, `faults == 0`, `mutants == 5/5`). | **CONFIRMED:** Max drift `2.463e-16`, `0` backflow faults, `5/5` mutants rejected. |

## Pre-Registered Null-Result Policy

All non-significant contrasts (specifically `SIM02_CONSTITUTIONAL_MIN` vs. `SIM01_PURE_RAW_FERAL`, $\delta_{\mathrm{pair}} = -0.02$, $p_{\mathrm{Holm}} = 1.00$) are reported identically alongside significant outcomes with zero selective omission. Any deviation from the pre-registered protocol is recorded in [`DEVIATIONS.md`](DEVIATIONS.md).
