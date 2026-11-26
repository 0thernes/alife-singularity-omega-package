# Configuration & Environment Guide (Build Standard A33)

All scripts execute deterministically out of the box with **zero required secrets or cloud API keys**. Optional environment overrides are documented in [`.env.example`](../.env.example).

| Variable / CLI Flag | Default | Purpose |
| :--- | :--- | :--- |
| `ALIFE_CHROME_EXE` | `C:\Program Files\Google\Chrome\Application\chrome.exe` (falls back to Edge) | Headless browser used for Chrome vector PDF rendering and Gate 17 22-tab DOM stress test. |
| `ALIFE_TECTONIC_EXE` | `tectonic` (or `~/.local/bin/tectonic.exe`) | Tectonic compiler for `paper/main.tex` and clean-room `dist/arxiv_submission.tar.gz`. |
| `ALIFE_LAKE_EXE` | `lake` (or `~/.elan/bin/lake.exe`) | Lean 4.35.0 Lake build tool (`lean/lean-toolchain`). |
| `ALIFE_MIRROR_ROOT` / `--mirror-root` | *(none)* | Secondary drive mirror directory verified byte-for-byte under Gate 18 (e.g., `I:\A-Life God Plan\A-Life Master Folder Build`). |
| `--reuse-sim` (`build_omega_package.py`) | `False` | Reuses locked `results/empirical_sim_summary.json` (`748` runs) for rapid package rebuilds without re-executing the 25-second Monte Carlo sweep. |
| `ALIFE_PAIRED_SEEDS` | `48` | Number of paired locked seeds (`5001..5048`) in `run_alife_castration_sim.py` (`384 + 264 + 100 = 748` runs). |

## Toolchain Pinning
- **Python:** `>= 3.12` (`pyproject.toml`, pinned dependencies in `requirements.txt`).
- **Lean 4:** `leanprover/lean4:v4.35.0` (`lean/lean-toolchain`).
- **Node.js:** `>= 20` (for `node --check` on embedded Observatory JS).
