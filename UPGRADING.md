# Upgrading Guide

## Upgrading from `v3.3-Omega` (`c5319dd`) to `v3.4.0`

### Breaking / Structural Changes
1. **Git Release Bundle Policy (`A24`):** `ALife_Singularity_SuperLife_Omega_Package.zip` (`> 5 MB`) is no longer tracked inside Git commits. Run `just build` (or download from GitHub Releases) to obtain the complete ZIP bundle locally.
2. **Version Strings & Master Spec Schema:** `spec_meta.unified_fusion_version` incremented from `"3.3.0-omega"` to `"3.4.0-omega"`; `ALife-Framework-v3.0-Master-Spec.xml` grew from `25` to `26` fusion sections (adding `MegaAtlasCrosswalk25`); `csv/` grew from `23` to `24` CSVs (`2,782 -> 2,822` rows); `ALife-v3.0-Errata-Closure-Register.csv` grew from `145` to `160` rows (`OMG-146..160`).
3. **Observatory LocalStorage Key:** Checklist browser storage key updated from `alife_omega_checklist_v3_3` to `alife_omega_checklist_v3_4` (Tab 22 `Mega-Atlas 1,900` added).
4. **Author & Legal Identity Normalization:** All references to unformed `"0thernes LLC"` were replaced with `"Alexander Stephen Donahue (Independent Researcher, Spokane, WA, USA)"` (`ORCID: 0009-0006-8168-9648`).
5. **Theorem Count Arithmetic Fix:** Native 5-engine theorem sum corrected from erroneous `240` to exact `42 + 62 + 72 + 48 + 20 = 244`, plus `36` local Lean 4.35.0 package theorems = **`280` Pure Lean 4 Theorems**.

### Migration Steps
1. Pull `v3.4.0` and ensure `lean/lean-toolchain` (`leanprover/lean4:v4.35.0`) is installed via `elan`.
2. Update any downstream scripts parsing `ALife-Framework-v3.0-Master-Spec.json` to read `errata_closures_160` (legacy fallback keys remain compatible in the HTML Observatory) and `citations_omega_30` (`45` total citations).
3. Run `just reproduce` to verify all 22 forensic gates and Lean 4.35.0 theorems cleanly.
