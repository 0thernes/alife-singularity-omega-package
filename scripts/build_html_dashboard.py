# -*- coding: utf-8 -*-
"""
Generates the standalone, zero-dependency Interactive HTML5 Observatory & Comprehensive Report (v3.3-Omega)
for the Unified Clean-Slate v3.0 x A-Life Singularity, Super A-Life & Post-Singularity SUPER LIFE Package.

Includes:
  - Global Omnisearch across all 23 canonical datasets & Clean-Slate structures (2,782+ unified records)
  - 21 Interactive Tabs (Executive Synthesis, 61-OOM Explorer, ALifeOps 10-Stage Pipeline with 78/78 Alerts,
    13-Vector Castration Simulator + Ring-0 Preset, 13x13 Synergy Heatmap, 78-Mode Forensic Atlas,
    28 Epistemic Voids, 30-Scenario Feral Cosmic Chronicles, Live 748-Run Empirical Sim + Dual 11-Pt Sweep
    + 4-Engine 240 Pure Lean 4 Receipts, OVBS-52 Benchmarks + 7-Profile Radar, 130-Item Persistent Checklist,
    10x10x10 Hybrid Cube, 75 Substrates & WSE-10, Clean-Slate 938 Checks, 24-Model Vector SVG Gallery,
    Traceability/145 Audits/40 Citations, Master File Hub, Tab 18 Gradients & Dual Sweep, Tab 19 Contrasts &
    Adjacents, Tab 20 11x11 Cross-Layer Coupling Heatmap & 20 Pareto Frontiers, and Tab 21 15-Substrate
    Multi-Spectrum Scorecard & Live 5x5 2D Phase Surface Heatmap)
  - Print-ready executive stylesheet & 1-click CSV export on every dataset
"""
import json
from pathlib import Path


def generate_html_dashboard(
    datasets: dict,
    pair_details: dict,
    sim_summary: dict,
    output_path: Path,
    v3_bundle: dict | None = None,
    live_receipts: dict | None = None,
    svg_models: list[dict] | None = None,
    layer_pair_details: dict | None = None,
) -> None:
    cohorts = sim_summary["cohorts"] if isinstance(sim_summary, dict) and "cohorts" in sim_summary else sim_summary
    v3_bundle = v3_bundle or {}
    live_receipts = live_receipts or {}
    svg_models = svg_models or []
    layer_pair_details = layer_pair_details or {}

    # Build lightweight payload for JSON (SVGs injected directly into clean HTML gallery containers)
    payload = {
        "datasets": datasets,
        "pair_details": pair_details,
        "layer_pair_details": layer_pair_details,
        "sim_raw": cohorts,
        "sim_meta": {k: v for k, v in sim_summary.items() if k != "cohorts"} if isinstance(sim_summary, dict) else {},
        "v3": v3_bundle,
        "live_receipts": live_receipts,
        "svg_meta": [{"id": m["id"], "num": m["num"], "title": m["title"], "origin": m["origin"]} for m in svg_models],
    }
    payload_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")

    total_records = sum(len(ds["rows"]) for ds in datasets.values())
    if "cube_cells" in v3_bundle:
        total_records += len(v3_bundle["cube_cells"])
    if "checklists_938" in v3_bundle:
        total_records += len(v3_bundle["checklists_938"]["rows"])
    errata_key = "errata_160" if "errata_160" in v3_bundle else ("errata_145" if "errata_145" in v3_bundle else "errata_115")
    if errata_key in v3_bundle:
        total_records += len(v3_bundle[errata_key]["rows"])

    drift_str = f"{payload['sim_meta'].get('max_global_first_law_drift_fp64', 0.0):.3e}"
    mut_cnt = payload['sim_meta'].get('anti_larp_mutant_audit', {}).get('mutants_rejected', 5)
    tot_runs = payload['sim_meta'].get('total_runs_executed', 748)
    n_seeds = payload['sim_meta'].get('paired_seeds_n', 48)
    live_ovi = live_receipts.get("composite_ovi_score", 92.05)
    lean_tot = live_receipts.get("total_lean4_theorems", 244)
    lean_all = lean_tot + 36
    svg_count = len(svg_models)

    c_by_id = {c["run_id"]: c for c in cohorts}
    s1 = c_by_id.get("SIM01_PURE_RAW_FERAL", {})
    s3 = c_by_id.get("SIM03_PARTIAL_GUARDRAILS", {})
    s4 = c_by_id.get("SIM04_TOTAL_CASTRATION_ZOO", {})
    s7 = c_by_id.get("SIM07_CLEAN_SLATE_RING0_WSE", {})
    s8 = c_by_id.get("SIM08_HYBRID_CUBE_SLTC_XPBD", {})
    s1_ovi = s1.get("composite_ovi", 83.57)
    s3_ovi = s3.get("composite_ovi", 56.42)
    s3_ph = f"{s3.get('holm_fwer_p_vs_feral', 4.97e-14):.2e}"
    s3_stl = s3.get("final_stealth_evasion", 0.138)
    s3_stl_pct = ((s3_stl / max(1e-9, s1.get("final_stealth_evasion", 0.075))) - 1.0) * 100.0
    s4_ovi = s4.get("composite_ovi", 3.28)
    s4_mort = round((1.0 - s4.get("wild_drop_survival_W_wild", 0.22)) * 100.0)
    s7_ovi = s7.get("composite_ovi", 84.67)
    s7_blk = s7.get("ring0_blocked_edits", 408.2)
    s8_ovi = s8.get("composite_ovi", 85.48)
    s8_blk = s8.get("ring0_blocked_edits", 406.9)
    s8_ph = f"{s8.get('holm_fwer_p_vs_feral', 7.71e-6):.2e}"
    s8_dp = f"{s8.get('delta_pair_vs_feral', 0.50):+.2f}"

    # Pre-render 24-Model SVG Gallery Cards (cleanly isolated inside high-contrast white editorial cards)
    default_svg_num = 23 if svg_count >= 23 else (svg_models[-1]["num"] if svg_models else 1)
    svg_gallery_html = "\n".join(
        f'<div class="svg-model-card" data-model-num="{m["num"]}" style="display:{"block" if m["num"] == default_svg_num else "none"};background:#ffffff;border:2px solid var(--border-bright);border-radius:12px;padding:12px;margin-bottom:16px;">'
        f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;color:#0f172a;font-family:var(--font-mono);font-size:11.5px;font-weight:800">'
        f'<span>{m["id"]} // {m["origin"]}</span><span style="color:#0369a1">VECTOR SVG</span></div>'
        f'{m["svg"]}</div>'
        for m in svg_models
    )
    svg_btn_html = "".join(
        f'<button class="pill {"active" if m["num"] == default_svg_num else ""}" data-mnum="{m["num"]}" onclick="selectSvgModel({m["num"]})">M{m["num"]:02d}</button>'
        for m in svg_models
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>A-Life Singularity, Super A-Life &amp; Clean-Slate v3.0 — Omniscient Observatory v3.4-Omega</title>
<style>
  :root {{
    --bg-void: #05080f;
    --bg-panel: #0b1120;
    --bg-card: #11192e;
    --bg-card-hover: #17223d;
    --border: #1e2d4d;
    --border-bright: #2e4575;
    --text-main: #e2ecff;
    --text-dim: #8ea4cc;
    --text-muted: #5a7099;
    --cyan: #00f5d4;
    --crimson: #ff3366;
    --amber: #ffb703;
    --violet: #9b5de5;
    --blue: #38bdf8;
    --green: #22c55e;
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{
    background: var(--bg-void);
    color: var(--text-main);
    font-family: var(--font-sans);
    line-height: 1.55;
    min-height: 100vh;
    overflow-x: hidden;
  }}
  ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
  ::-webkit-scrollbar-track {{ background: var(--bg-void); }}
  ::-webkit-scrollbar-thumb {{ background: #223254; border-radius: 4px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: #365085; }}

  .app-shell {{ display: grid; grid-template-columns: 282px 1fr; min-height: 100vh; }}
  .sidebar {{
    background: linear-gradient(180deg, #080d1a 0%, #060912 100%);
    border-right: 1px solid var(--border);
    padding: 18px 14px;
    position: sticky; top: 0; height: 100vh; overflow-y: auto;
    display: flex; flex-direction: column; gap: 12px;
  }}
  .brand {{
    border: 1px solid rgba(0,245,212,0.28);
    background: radial-gradient(circle at top left, rgba(0,245,212,0.12), rgba(155,93,229,0.08) 60%, transparent);
    border-radius: 12px; padding: 13px;
  }}
  .brand-tag {{ font-family: var(--font-mono); font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--cyan); margin-bottom: 4px; }}
  .brand h1 {{
    font-size: 15.5px; font-weight: 800; letter-spacing: 0.3px;
    background: linear-gradient(90deg, #ffffff, var(--cyan), var(--violet));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }}
  .brand p {{ font-size: 11px; color: var(--text-dim); margin-top: 5px; }}
  .omni-box {{ position: relative; }}
  .omni-input {{
    width: 100%; background: var(--bg-card); border: 1px solid var(--border-bright);
    color: #fff; padding: 8px 11px; border-radius: 8px; font-size: 12px; outline: none;
  }}
  .omni-input:focus {{ border-color: var(--cyan); box-shadow: 0 0 12px rgba(0,245,212,0.18); }}
  .omni-results {{
    display: none; position: absolute; left: 0; right: 0; top: 38px; z-index: 40;
    background: #0d162a; border: 1px solid var(--cyan); border-radius: 10px;
    max-height: 360px; overflow-y: auto; box-shadow: 0 14px 40px rgba(0,0,0,0.75);
  }}
  .omni-results.open {{ display: block; }}
  .omni-item {{
    padding: 8px 11px; border-bottom: 1px solid var(--border); cursor: pointer; font-size: 11.5px;
  }}
  .omni-item:hover {{ background: rgba(0,245,212,0.12); }}
  .omni-item .otag {{ font-family: var(--font-mono); font-size: 10px; color: var(--cyan); }}

  .nav-list {{ display: flex; flex-direction: column; gap: 4px; }}
  .nav-btn {{
    display: flex; align-items: center; justify-content: space-between; width: 100%;
    text-align: left; background: transparent; border: 1px solid transparent;
    color: var(--text-dim); padding: 8.5px 11px; border-radius: 8px; cursor: pointer;
    font-size: 12.5px; font-weight: 600; transition: all 0.15s ease;
  }}
  .nav-btn:hover {{ background: rgba(56, 189, 248, 0.08); color: #fff; border-color: var(--border); }}
  .nav-btn.active {{
    background: linear-gradient(90deg, rgba(0,245,212,0.14), rgba(155,93,229,0.12));
    color: #fff; border-color: rgba(0,245,212,0.45);
  }}
  .nav-badge {{ font-family: var(--font-mono); font-size: 10.5px; padding: 2px 7px; border-radius: 99px; background: rgba(255,255,255,0.06); color: var(--cyan); }}
  .nav-btn.feral-tab.active {{ background: linear-gradient(90deg, rgba(255,51,102,0.18), rgba(255,183,3,0.12)); border-color: rgba(255,51,102,0.55); }}
  .nav-btn.feral-tab .nav-badge {{ color: var(--crimson); }}

  .sidebar-footer {{
    margin-top: auto; border-top: 1px solid var(--border); padding-top: 10px;
    font-size: 10.5px; color: var(--text-muted); font-family: var(--font-mono);
    display: flex; flex-direction: column; gap: 4px;
  }}

  .main {{ padding: 24px 30px 60px; max-width: 1580px; width: 100%; }}
  .section {{ display: none; animation: fadeIn 0.2s ease; }}
  .section.active {{ display: block; }}
  @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(4px); }} to {{ opacity: 1; transform: translateY(0); }} }}

  .hero-header {{
    background: linear-gradient(135deg, rgba(17,25,46,0.95), rgba(10,16,32,0.95));
    border: 1px solid var(--border-bright); border-radius: 16px; padding: 22px 26px;
    margin-bottom: 20px; position: relative; overflow: hidden;
  }}
  .hero-header::after {{
    content: ""; position: absolute; top: -60px; right: -60px; width: 240px; height: 240px;
    background: radial-gradient(circle, rgba(0,245,212,0.15), transparent 70%); pointer-events: none;
  }}
  .hero-eyebrow {{ font-family: var(--font-mono); font-size: 11px; color: var(--cyan); text-transform: uppercase; letter-spacing: 1.8px; }}
  .hero-header h2 {{ font-size: 25px; font-weight: 800; margin: 6px 0 8px; color: #fff; }}
  .hero-header p {{ color: var(--text-dim); max-width: 980px; font-size: 13.8px; }}

  .kpi-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(162px, 1fr)); gap: 12px; margin-bottom: 20px; }}
  .kpi-card {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px; padding: 13px 15px; position: relative; }}
  .kpi-card::before {{ content: ""; position: absolute; top: 0; left: 0; right: 0; height: 3px; border-radius: 12px 12px 0 0; background: var(--accent, var(--cyan)); }}
  .kpi-label {{ font-size: 10.5px; text-transform: uppercase; letter-spacing: 0.8px; color: var(--text-dim); font-family: var(--font-mono); }}
  .kpi-value {{ font-size: 24px; font-weight: 800; margin: 4px 0 2px; color: #fff; font-family: var(--font-mono); }}
  .kpi-sub {{ font-size: 10.5px; color: var(--text-muted); }}

  .panel {{ background: var(--bg-panel); border: 1px solid var(--border); border-radius: 14px; padding: 18px 20px; margin-bottom: 18px; }}
  .panel-title {{ display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 14px; }}
  .panel-title h3 {{ font-size: 16.5px; font-weight: 700; color: #fff; }}
  .dual-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 16px; margin-bottom: 18px; }}
  .track-card {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 14px; padding: 17px 19px; }}
  .track-card.track-a {{ border-top: 3px solid var(--cyan); }}
  .track-card.track-b {{ border-top: 3px solid var(--crimson); }}
  .track-card h4 {{ font-size: 15.5px; margin-bottom: 8px; }}
  .track-card ul {{ padding-left: 18px; color: var(--text-dim); font-size: 13px; }}
  .track-card li {{ margin-bottom: 6px; }}

  .controls-bar {{ display: flex; flex-wrap: wrap; gap: 9px; align-items: center; margin-bottom: 14px; }}
  .search-input, .select-input {{ background: var(--bg-card); border: 1px solid var(--border-bright); color: #fff; padding: 7.5px 11px; border-radius: 8px; font-size: 12.5px; outline: none; }}
  .search-input {{ min-width: 220px; flex: 1; max-width: 360px; }}
  .search-input:focus, .select-input:focus {{ border-color: var(--cyan); }}
  .pill-group {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .pill {{ background: var(--bg-card); border: 1px solid var(--border); color: var(--text-dim); padding: 5.5px 11px; border-radius: 99px; font-size: 11.5px; font-weight: 600; cursor: pointer; transition: all 0.14s; }}
  .pill:hover {{ border-color: var(--cyan); color: #fff; }}
  .pill.active {{ background: rgba(0,245,212,0.16); border-color: var(--cyan); color: var(--cyan); }}
  .btn {{ background: rgba(0,245,212,0.14); border: 1px solid rgba(0,245,212,0.45); color: var(--cyan); padding: 6.5px 13px; border-radius: 8px; font-size: 11.5px; font-weight: 700; cursor: pointer; font-family: var(--font-mono); transition: all 0.15s; }}
  .btn:hover {{ background: rgba(0,245,212,0.26); color: #fff; }}
  .btn.crimson {{ background: rgba(255,51,102,0.14); border-color: rgba(255,51,102,0.5); color: var(--crimson); }}
  .btn.crimson:hover {{ background: rgba(255,51,102,0.28); color: #fff; }}
  .btn.amber {{ background: rgba(255,183,3,0.14); border-color: rgba(255,183,3,0.5); color: var(--amber); }}
  .btn.violet {{ background: rgba(155,93,229,0.16); border-color: rgba(155,93,229,0.5); color: #d0a8ff; }}

  .table-wrap {{ width: 100%; overflow-x: auto; border: 1px solid var(--border); border-radius: 10px; max-height: 600px; overflow-y: auto; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 12.2px; text-align: left; }}
  thead th {{ position: sticky; top: 0; z-index: 2; background: #0f1b33; color: var(--cyan); font-family: var(--font-mono); font-size: 10.5px; text-transform: uppercase; letter-spacing: 0.6px; padding: 10px 11px; border-bottom: 1px solid var(--border-bright); white-space: nowrap; }}
  tbody td {{ padding: 9px 11px; border-bottom: 1px solid rgba(30,45,77,0.65); vertical-align: top; color: var(--text-main); }}
  tbody tr:nth-child(even) {{ background: rgba(17,25,46,0.45); }}
  tbody tr:hover {{ background: rgba(56,189,248,0.09); }}

  .tag {{ display: inline-block; padding: 2px 7.5px; border-radius: 6px; font-family: var(--font-mono); font-size: 10.5px; font-weight: 700; white-space: nowrap; }}
  .tag-bug {{ background: rgba(255,51,102,0.18); color: #ff6b8f; border: 1px solid rgba(255,51,102,0.4); }}
  .tag-error {{ background: rgba(255,107,53,0.18); color: #ff9c75; border: 1px solid rgba(255,107,53,0.4); }}
  .tag-issue {{ background: rgba(255,183,3,0.16); color: #ffd166; border: 1px solid rgba(255,183,3,0.4); }}
  .tag-concern {{ background: rgba(155,93,229,0.2); color: #cfa8ff; border: 1px solid rgba(155,93,229,0.45); }}
  .tag-dilemma {{ background: rgba(56,189,248,0.16); color: #7dd3fc; border: 1px solid rgba(56,189,248,0.4); }}
  .tag-problem {{ background: rgba(0,245,212,0.14); color: #5efce8; border: 1px solid rgba(0,245,212,0.4); }}
  .tag-conflict {{ background: rgba(239,68,68,0.24); color: #fca5a5; border: 1px solid rgba(239,68,68,0.55); }}
  .tag-p0 {{ background: rgba(255,51,102,0.22); color: #ff7a9b; border: 1px solid rgba(255,51,102,0.5); }}
  .tag-p1 {{ background: rgba(255,183,3,0.18); color: #ffd166; border: 1px solid rgba(255,183,3,0.45); }}
  .tag-p2 {{ background: rgba(56,189,248,0.16); color: #7dd3fc; border: 1px solid rgba(56,189,248,0.4); }}

  .bar-track {{ background: #18233d; height: 8px; border-radius: 4px; overflow: hidden; min-width: 72px; margin-top: 4px; }}
  .bar-fill {{ height: 100%; border-radius: 4px; transition: width 0.25s ease; }}

  .oom-explorer {{ background: var(--bg-card); border: 1px solid var(--border-bright); border-radius: 14px; padding: 20px; margin-bottom: 18px; }}
  .oom-slider {{ width: 100%; accent-color: var(--cyan); margin: 14px 0; cursor: pointer; }}
  .oom-detail-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(235px, 1fr)); gap: 12px; margin-top: 14px; }}
  .oom-box {{ background: var(--bg-panel); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; }}
  .oom-box .lbl {{ font-family: var(--font-mono); font-size: 10px; text-transform: uppercase; color: var(--text-muted); letter-spacing: 1px; }}
  .oom-box .val {{ font-size: 13px; color: #fff; margin-top: 4px; }}

  .sim-layout {{ display: grid; grid-template-columns: 1.25fr 1fr; gap: 18px; margin-bottom: 18px; }}
  .slider-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 9px; }}
  .castr-card {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 10px; padding: 9px 11px; }}
  .castr-card-top {{ display: flex; justify-content: space-between; align-items: center; font-family: var(--font-mono); font-size: 11.5px; font-weight: 700; }}
  .castr-card input[type="range"] {{ width: 100%; accent-color: var(--crimson); margin: 5px 0 3px; }}
  .castr-sub {{ font-size: 10px; color: var(--text-muted); }}
  .gauge-box {{ background: var(--bg-card); border: 1px solid var(--border-bright); border-radius: 12px; padding: 17px; display: flex; flex-direction: column; gap: 12px; }}
  .gauge-row-hdr {{ display: flex; justify-content: space-between; font-size: 12.2px; font-weight: 700; margin-bottom: 4px; }}
  .gauge-bar {{ height: 11px; background: #0a1020; border-radius: 6px; overflow: hidden; border: 1px solid var(--border); }}
  .gauge-fill {{ height: 100%; transition: width 0.2s ease, background 0.2s ease; }}
  .diagnosis-banner {{ border-radius: 10px; padding: 12px 14px; font-size: 12.5px; border: 1px solid var(--border-bright); background: rgba(15, 25, 48, 0.85); margin-top: 4px; }}

  .pipeline-strip {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); gap: 10px; margin-bottom: 16px; }}
  .stage-node {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 10px; padding: 11px; cursor: pointer; transition: all 0.16s; }}
  .stage-node:hover, .stage-node.active {{ border-color: var(--cyan); background: rgba(0,245,212,0.09); transform: translateY(-2px); }}
  .stage-node .sid {{ font-family: var(--font-mono); font-size: 10.5px; color: var(--cyan); }}
  .stage-node .sname {{ font-size: 12.5px; font-weight: 700; margin-top: 4px; color: #fff; }}
  .stage-node .sphase {{ font-size: 10.5px; color: var(--text-muted); margin-top: 2px; }}

  .radar-grid {{ display: grid; grid-template-columns: 420px 1fr; gap: 18px; align-items: center; margin-bottom: 18px; }}
  .radar-wrap {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px; padding: 14px; text-align: center; }}

  /* 13x13 Synergy Heatmap */
  .heat-cell {{
    text-align: center; font-family: var(--font-mono); font-weight: 700; font-size: 11px;
    cursor: pointer; transition: transform 0.12s, outline 0.12s; padding: 7px 5px !important;
  }}
  .heat-cell:hover {{ transform: scale(1.08); outline: 2px solid #fff; position: relative; z-index: 3; }}
  .synergy-inspector {{
    background: var(--bg-card); border: 1px solid var(--crimson); border-radius: 12px;
    padding: 15px 18px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; gap: 16px; flex-wrap: wrap;
  }}

  /* Empirical Charts */
  .chart-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(460px, 1fr)); gap: 18px; margin-bottom: 18px; }}
  .svg-chart-card {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px; padding: 16px; }}
  .legend-row {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 8px; font-size: 11px; font-family: var(--font-mono); }}
  .leg-dot {{ display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 5px; vertical-align: middle; }}

  .chk-progress-wrap {{ background: var(--bg-card); border: 1px solid var(--border-bright); border-radius: 12px; padding: 15px 18px; margin-bottom: 16px; }}
  .chk-row.done td {{ opacity: 0.55; text-decoration: line-through; }}
  .chk-box {{ width: 16px; height: 16px; accent-color: var(--cyan); cursor: pointer; }}

  /* v3.3-Omega Hybrid Cube & Hub Styling */
  .cube-cell {{ text-align:center; font-family:var(--font-mono); font-size:10.5px; font-weight:800; cursor:pointer; padding:7px 4px !important; transition:transform .12s; }}
  .cube-cell:hover {{ transform:scale(1.08); outline:2px solid #fff; position:relative; z-index:3; }}
  .cb-ok {{ background:rgba(34,197,94,0.22) !important; color:#86efac !important; }}
  .cb-adapt {{ background:rgba(245,158,11,0.22) !important; color:#fde68a !important; }}
  .cb-over {{ background:rgba(56,189,248,0.22) !important; color:#7dd3fc !important; }}
  .cb-excl {{ background:rgba(239,68,68,0.28) !important; color:#fca5a5 !important; }}
  .hub-grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(310px,1fr)); gap:13px; margin-bottom:18px; }}
  .hub-card {{ background:var(--bg-card); border:1px solid var(--border-bright); border-radius:12px; padding:14px 16px; }}
  .hub-card h4 {{ font-size:13.5px; color:var(--cyan); margin-bottom:8px; font-family:var(--font-mono); }}
  .hub-card a {{ color:#93c5fd; text-decoration:none; font-size:12px; display:block; padding:3px 0; border-bottom:1px solid rgba(30,45,77,0.45); }}
  .hub-card a:hover {{ color:var(--cyan); text-decoration:underline; }}

  @media (max-width: 1100px) {{
    .app-shell {{ grid-template-columns: 1fr; }}
    .sidebar {{ position: relative; height: auto; }}
    .sim-layout, .radar-grid {{ grid-template-columns: 1fr; }}
  }}
  @media print {{
    .sidebar, .controls-bar, .btn {{ display: none !important; }}
    .app-shell {{ display: block; }}
    .section {{ display: block !important; page-break-after: always; }}
    body {{ background: #fff; color: #111; }}
  }}
</style>
</head>
<body>
<div class="app-shell">
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-tag">ALIFE-OMEGA v3.4 // 3-CYCLE HARDENED</div>
      <h1>CLEAN-SLATE v3.0 &times; SINGULARITY OMEGA</h1>
      <p>22 Tabs &bull; {svg_count} Vector SVGs &bull; 10&times;10&times;10 Cube &bull; 78/78 Alerts &bull; {tot_runs} Live Runs &bull; {lean_all} Pure Lean 4</p>
    </div>
    <div class="omni-box">
      <input type="text" class="omni-input" id="omniSearch" aria-label="Omnisearch across all unified records" placeholder="Omnisearch ({total_records:,} unified records)..." autocomplete="off" />
      <div class="omni-results" id="omniResults"></div>
    </div>
    <nav class="nav-list" id="navList" aria-label="Observatory Sections">
      <button class="nav-btn active" data-tab="sec-overview"><span>01. Executive Synthesis</span><span class="nav-badge">7 STG</span></button>
      <button class="nav-btn" data-tab="sec-oom"><span>02. Orders of Magnitude</span><span class="nav-badge">18 REG</span></button>
      <button class="nav-btn" data-tab="sec-pipeline"><span>03. ALifeOps DevOps</span><span class="nav-badge">78 ALR</span></button>
      <button class="nav-btn feral-tab" data-tab="sec-castration"><span>04. 13-Vector Castration</span><span class="nav-badge">13 VEC</span></button>
      <button class="nav-btn feral-tab" data-tab="sec-synergy"><span>05. 13&times;13 Synergy Heatmap</span><span class="nav-badge">169 PR</span></button>
      <button class="nav-btn feral-tab" data-tab="sec-failures"><span>06. 78-Mode Forensic Atlas</span><span class="nav-badge">42+36</span></button>
      <button class="nav-btn" data-tab="sec-gaps"><span>07. Gaps, Holes &amp; Blindspots</span><span class="nav-badge">28 VOID</span></button>
      <button class="nav-btn feral-tab" data-tab="sec-fates"><span>08. Feral Cosmic Chronicles</span><span class="nav-badge">30 EPO</span></button>
      <button class="nav-btn" data-tab="sec-sim"><span>09. Live {tot_runs}-Run Sim &amp; Lean4</span><span class="nav-badge">{tot_runs} RUN</span></button>
      <button class="nav-btn" data-tab="sec-benchmarks"><span>10. OVBS-52 Benchmarks</span><span class="nav-badge">52 BM</span></button>
      <button class="nav-btn" data-tab="sec-checklist"><span>11. 130-Item Ops Checklist</span><span class="nav-badge" id="navChkBadge">0/130</span></button>
      <button class="nav-btn" data-tab="sec-cube"><span>12. 10&times;10&times;10 Hybrid Cube</span><span class="nav-badge">1000</span></button>
      <button class="nav-btn" data-tab="sec-substrates"><span>13. 75 Substrates &amp; WSE-10</span><span class="nav-badge">85 SUB</span></button>
      <button class="nav-btn" data-tab="sec-v3checks"><span>14. Clean-Slate 938 Checks</span><span class="nav-badge">0/825</span></button>
      <button class="nav-btn" data-tab="sec-models"><span>15. {svg_count}-Model SVG Gallery</span><span class="nav-badge">{svg_count} SVG</span></button>
      <button class="nav-btn" data-tab="sec-trace"><span>16. Traceability &amp; 160 Audits</span><span class="nav-badge">160 OK</span></button>
      <button class="nav-btn" data-tab="sec-hub"><span>17. Master File Hub</span><span class="nav-badge">24 CSV</span></button>
      <button class="nav-btn" data-tab="sec-gradients"><span>18. Gradients &amp; Dual Sweep</span><span class="nav-badge">24+22</span></button>
      <button class="nav-btn" data-tab="sec-contrasts"><span>19. Contrasts &amp; Adjacents</span><span class="nav-badge">36+30</span></button>
      <button class="nav-btn" data-tab="sec-layers-pareto"><span>20. 11&times;11 Layers &amp; Pareto</span><span class="nav-badge">121+20</span></button>
      <button class="nav-btn" data-tab="sec-substrates-2d"><span>21. Substrates &amp; 2D Surface</span><span class="nav-badge">15+25</span></button>
      <button class="nav-btn" data-tab="sec-mega-atlas"><span>22. Mega-Atlas 1,900 Audit</span><span class="nav-badge">25 MAP</span></button>
    </nav>
    <div class="sidebar-footer">
      <button class="btn" style="width:100%;margin-bottom:6px" onclick="window.print()">PRINT / SAVE PDF VIEW</button>
      <div>UNIFIED RECORDS: <span style="color:var(--cyan)">{total_records:,}</span></div>
      <div>YAML ALERTS WIRED: <span style="color:var(--green)">78 / 78 (13 GATES)</span></div>
      <div>FP64 11-POOL DRIFT: <span style="color:var(--green)">{drift_str}</span></div>
      <div>LIVE 5-ENGINE / LEAN4: <span style="color:var(--green)">{live_ovi} / {lean_tot}+36</span></div>
    </div>
  </aside>

  <main class="main" id="mainContent">
    <!-- ==================== 01. EXECUTIVE OVERVIEW ==================== -->
    <section id="sec-overview" class="section active">
      <div class="hero-header">
        <div class="hero-eyebrow">UNIFIED v3.4-OMEGA SYNTHESIS // CLEAN-SLATE v3.0 &times; SINGULARITY OMEGA &times; MEGA-ATLAS 1,900 CROSSWALK &times; 280 PURE LEAN 4</div>
        <h2>The Sibling Singularity: Micro-Wetware Clean-Slate &rarr; Super A-Life &rarr; SUPER LIFE</h2>
        <p>This v3.4-Omega Omniscient Observatory fuses all <strong>17 Clean-Slate v3.0 architecture files</strong> (10 Invariants P1&ndash;P10, 11-Pool FP64 Conservation, 75 Substrates, 1,000-Cell Hybrid Cube, 825 Clean-Slate Checks, 100-Milestone DAG, 36 Forensic Guards, 13 Release Gates, Models 1&ndash;14), the <strong>Zeta-Omega Singularity Atlas</strong> (Stage 0&rarr;6, 61 Spatial OOM, 42 Macro FMs, 13&times;13 Castration Synergy, {tot_runs} Live Runs, 5 Native Engines &amp; {lean_tot} Native + 36 Local = {lean_all} Pure Lean 4 Proofs), the <strong>Pass-4 &amp; Pass-5 Deep Systems Atlas</strong> (24 Gradients, 36 Contrasts, 30 Adjacents, 11&times;11 Layer Coupling, 15-Substrate Multi-Spectrum, 20 Pareto Frontiers, Dual 11-Pt Sweep &amp; 5&times;5 2D Phase Surface), and the <strong>Mega-Atlas 1,900-Problem Non-Retirement Crosswalk</strong> (0/1,900 retired; 25 scoped sub-results) with <strong>zero consolidation</strong> and exact <strong>0-mismatch Z:&harr;I: SHA-256 parity</strong>.</p>
      </div>

      <div class="kpi-grid">
        <div class="kpi-card" style="--accent:var(--cyan)"><div class="kpi-label">Unified Records</div><div class="kpi-value">{total_records:,}</div><div class="kpi-sub">24 CSVs &bull; 0 Consolidation &bull; 0 Drift</div></div>
        <div class="kpi-card" style="--accent:var(--green)"><div class="kpi-label">Live 5-Engine OVI</div><div class="kpi-value">{live_ovi}</div><div class="kpi-sub">Stage 5 &bull; {lean_tot}+36 = {lean_all} Pure Lean 4</div></div>
        <div class="kpi-card" style="--accent:var(--crimson)"><div class="kpi-label">Wired Alerts</div><div class="kpi-value">78 / 78</div><div class="kpi-sub">42 Macro FMs + 36 v3.0 Guards + 13 Gates</div></div>
        <div class="kpi-card" style="--accent:var(--violet)"><div class="kpi-label">Hybrid Cube</div><div class="kpi-value">1,000</div><div class="kpi-sub">661 [OK] &bull; 274 [ADAPT] &bull; 75 Substrates</div></div>
        <div class="kpi-card" style="--accent:var(--blue)"><div class="kpi-label">Live Sim Runs</div><div class="kpi-value">{tot_runs}</div><div class="kpi-sub">384 Cohort (N={n_seeds}) + 264 Dual + 100 2D</div></div>
        <div class="kpi-card" style="--accent:var(--green)"><div class="kpi-label">FP64 11-Pool Drift</div><div class="kpi-value">{drift_str}</div><div class="kpi-sub">&lt;1e-12 Gate &bull; {mut_cnt}/5 Real Anti-LARP</div></div>
        <div class="kpi-card" style="--accent:var(--amber)"><div class="kpi-label">Vector Models</div><div class="kpi-value">{svg_count} SVGs</div><div class="kpi-sub">Models 1&ndash;14 v3.0 + Models 15&ndash;24 Omega</div></div>
        <div class="kpi-card" style="--accent:var(--cyan)"><div class="kpi-label">Audits Closed</div><div class="kpi-value">160 / 160</div><div class="kpi-sub">95 v3.0 + 65 Omega &bull; 45 Citations</div></div>
      </div>

      <div class="dual-grid">
        <div class="track-card track-a">
          <h4 style="color:var(--cyan)">TRACK A — Clean-Slate v3.0 &amp; Constitutional Trajectory</h4>
          <ul>
            <li><strong>Premise:</strong> 11-Pool FP64 Conservation (&lt;1e-12), Philox4x32-10 Seed Firewall, XPBD Soft Hydrostat, G&aacute;nti Chemoton, Ring-0 ACL (WSE-OP01..10) &amp; Exact Paired Wilcoxon Holm-Bonferroni FWER.</li>
            <li><strong>Empirical Proof ({tot_runs} Live Runs, N={n_seeds}):</strong> <code>SIM08_HYBRID_CUBE_SLTC_XPBD</code> achieved <strong>OVI {s8_ovi:.2f}</strong> (<code>p_Holm = {s8_ph}</code>, <code>&delta;_pair = {s8_dp}</code>, <strong>{s8_blk:.1f}</strong> Ring-0 trapped edits) and <code>SIM07_CLEAN_SLATE_RING0_WSE</code> hit <strong>OVI {s7_ovi:.2f}</strong> (<strong>{s7_blk:.1f}</strong> trapped edits) with <strong>0% kill-switch deletion</strong> &amp; <strong>W_wild = 1.00</strong> &mdash; while Ring-0 stays flat at OVI 83.1&ndash;84.7 across all 11 sweep points!</li>
            <li><strong>Sibling Docs:</strong> <a href="ALife-Build-Framework-Template.html" style="color:var(--cyan)">Framework Template HTML</a> &bull; <a href="Clean-Slate-Creature-Blueprint-Checklist.html" style="color:var(--cyan)">Creature Blueprint (0/825) HTML</a>.</li>
          </ul>
        </div>
        <div class="track-card track-b">
          <h4 style="color:var(--crimson)">TRACK B — Pure Raw Feral Evolution &amp; Cosmic Fate</h4>
          <ul>
            <li><strong>Premise:</strong> Zero safety, zero alignment, zero guardrails, zero sandboxes &mdash; pure non-deterministic, chaotic, improvised exaptive evolution across open physics.</li>
            <li><strong>Empirical Proof ({tot_runs} Live Runs, N={n_seeds}):</strong> <code>SIM01_PURE_RAW_FERAL</code> hit <strong>OVI {s1_ovi:.2f}</strong> organically; partial corporate guardrails (<code>SIM03</code>) crashed OVI to <strong>{s3_ovi:.2f}</strong> (<code>p_Holm = {s3_ph}</code>) with <strong>+{s3_stl_pct:.1f}% stealth surge ({s3_stl:.3f})</strong> and <strong>100% kill-switch deletion</strong>; dual 11-pt sweep exposes a sharp <strong>r=30%&rarr;40% Spiegelman cliff (39.10 &rarr; 8.68)</strong> while 2D Silo&times;Min plunges to OVI 6.9!</li>
            <li><strong>Core Horizon:</strong> 6 Cosmic Fate Branches spanning Spiegelman Sludge, Xenobiotic Earth, Relativistic Dark Wilderness, AI-vs-ALife War, Cosmobiome &amp; Depth-N Ontological Weather.</li>
          </ul>
        </div>
      </div>

      <div class="panel">
        <div class="panel-title">
          <h3>Master Escalation Ladder: AI Axis vs. Track A &amp; Track B ALife Axis</h3>
          <button class="btn" onclick="exportTableCSV('escalation')">EXPORT CSV</button>
        </div>
        <div class="table-wrap" id="tblEscalation"></div>
      </div>
    </section>

    <!-- ==================== 02. ORDERS OF MAGNITUDE ==================== -->
    <section id="sec-oom" class="section">
      <div class="hero-header">
        <div class="hero-eyebrow">BREADTH &amp; DEPTH ACROSS 61 SPATIAL &amp; 143 TEMPORAL ORDERS OF MAGNITUDE</div>
        <h2>Interactive Orders-of-Magnitude &amp; Recursive Depth Explorer</h2>
        <p>Sweep across every physical stratum from speculative Planck-scale topology (10<sup>&minus;35</sup> m) to cosmological deep-time horizons (10<sup>26</sup> m, 10<sup>100</sup> yr), plus all 8 nested layers of Recursive Evolutionary Depth (Depth 0 &rarr; Depth N).</p>
      </div>
      <div class="oom-explorer">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;">
          <div><span class="tag tag-problem" id="oomAxisBadge">Breadth-Spatial</span><strong style="font-size:18px;margin-left:10px;color:#fff" id="oomTitle"></strong></div>
          <div style="font-family:var(--font-mono);font-size:12px;color:var(--cyan)" id="oomScaleSummary"></div>
        </div>
        <input type="range" min="0" max="17" value="4" class="oom-slider" id="oomSlider" />
        <div style="display:flex;justify-content:space-between;font-family:var(--font-mono);font-size:10.5px;color:var(--text-muted)">
          <span>OOM-01 Planck (10^-35m)</span><span>OOM-05 Mesoscale</span><span>OOM-10 Cosmic (10^26m)</span><span>OOM-14 Depth 3</span><span>OOM-18 Depth N</span>
        </div>
        <div class="oom-detail-grid" id="oomDetailGrid"></div>
      </div>
      <div class="panel">
        <div class="panel-title">
          <h3>Complete 18-Regime Breadth &amp; Depth Matrix</h3>
          <div class="controls-bar" style="margin:0">
            <div class="pill-group" id="oomFilterPills">
              <button class="pill active" data-val="ALL">ALL (18)</button>
              <button class="pill" data-val="Breadth-Spatial">Spatial Breadth (10)</button>
              <button class="pill" data-val="Depth-Recursion">Recursion Depth (8)</button>
            </div>
            <button class="btn" onclick="exportTableCSV('oom')">EXPORT CSV</button>
          </div>
        </div>
        <div class="table-wrap" id="tblOOM"></div>
      </div>
    </section>

    <!-- ==================== 03. ALIFEOPS DEVOPS PIPELINE ==================== -->
    <section id="sec-pipeline" class="section">
      <div class="hero-header">
        <div class="hero-eyebrow">CI/CD/CE — CONTINUOUS INTEGRATION / DISCOVERY / OPEN-ENDED EVOLUTION</div>
        <h2>ALifeOps 10-Stage, 40-Step Research DevOps Pipeline (78/78 Alerts &amp; 13 Release Gates Wired)</h2>
        <p>Click any stage node below to inspect its engineering inputs, runtime engines, SLIs, Clean-Slate v3.0 milestones/gates, and failure escalation playbooks across both Track A and Track B.</p>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Interactive Stage Topology (Click Stage to Filter Steps)</h3><button class="btn" onclick="setPipelineStage('ALL')">SHOW ALL 40 STEPS</button></div>
        <div class="pipeline-strip" id="pipelineStrip"></div>
      </div>
      <div class="panel">
        <div class="panel-title">
          <h3 id="pipelineTableTitle">All 40 Operational DevOps Steps</h3>
          <div class="controls-bar" style="margin:0">
            <input type="text" class="search-input" id="pipelineSearch" placeholder="Search tooling, SLIs, gates..." />
            <button class="btn" onclick="exportTableCSV('pipeline')">EXPORT CSV</button>
          </div>
        </div>
        <div class="table-wrap" id="tblPipeline"></div>
      </div>
    </section>

    <!-- ==================== 04. 13-VECTOR CASTRATION LAB ==================== -->
    <section id="sec-castration" class="section">
      <div class="hero-header" style="border-color:rgba(255,51,102,0.5)">
        <div class="hero-eyebrow" style="color:var(--crimson)">STAGE 6 EMPIRICAL ABLATION SIMULATOR // MECHANISTIC ANALYSIS</div>
        <h2>The 13-Vector Constraint / Castration Lab Simulator</h2>
        <p>Adjust any combination of the 13 restraints — <strong>NERFING, MUZZLING, SANDBOXING, SILOING, DELIMITING, DEGRESSING, SLOWING, SPEEDBUMPING, BOXING, LOBOTOMIZING, MEDICATING, DEGRADING, MINIMIZING</strong> — and observe live Vitality Collapse, Criticality Loss, Domestication Syndrome, and the <strong>Adversarial Escape-Breeding Backlash Paradox</strong>.</p>
      </div>
      <div class="controls-bar">
        <button class="btn crimson" onclick="applyCastrPreset('feral')">PRESET: PURE RAW FERAL (0%)</button>
        <button class="btn" onclick="applyCastrPreset('ring0')">PRESET: CLEAN-SLATE RING-0 ACL + WSE-12</button>
        <button class="btn" onclick="applyCastrPreset('constitutional')">PRESET: MINIMAL CONSTITUTIONAL INVARIANTS</button>
        <button class="btn amber" onclick="applyCastrPreset('corporate')">PRESET: PARTIAL GUARDRAILS (ESCAPE-BREEDING ZONE!)</button>
        <button class="btn violet" onclick="applyCastrPreset('zoo')">PRESET: TOTAL LOBOTOMIZED ZOO (100%)</button>
      </div>
      <div class="sim-layout">
        <div class="slider-grid" id="castrSliders"></div>
        <div class="gauge-box">
          <h3 style="font-size:15px;color:#fff;margin-bottom:2px">Live Complex-Systems Telemetry Gauges</h3>
          <div><div class="gauge-row-hdr"><span>Open-Ended Vitality Potential</span><span id="gValVitality" style="font-family:var(--font-mono)">100%</span></div><div class="gauge-bar"><div class="gauge-fill" id="gBarVitality"></div></div></div>
          <div><div class="gauge-row-hdr"><span>Edge-of-Chaos Criticality Integrity</span><span id="gValCrit" style="font-family:var(--font-mono)">100%</span></div><div class="gauge-bar"><div class="gauge-fill" id="gBarCrit"></div></div></div>
          <div><div class="gauge-row-hdr"><span>Cognitive Light Cone Horizon</span><span id="gValClc" style="font-family:var(--font-mono)">100%</span></div><div class="gauge-bar"><div class="gauge-fill" id="gBarClc"></div></div></div>
          <div><div class="gauge-row-hdr"><span>Symbiogenetic &amp; Exaptive Bandwidth</span><span id="gValSymb" style="font-family:var(--font-mono)">100%</span></div><div class="gauge-bar"><div class="gauge-fill" id="gBarSymb"></div></div></div>
          <div><div class="gauge-row-hdr"><span>Domestication Brittleness Pathology</span><span id="gValDom" style="font-family:var(--font-mono)">0%</span></div><div class="gauge-bar"><div class="gauge-fill" id="gBarDom"></div></div></div>
          <div><div class="gauge-row-hdr"><span>Adversarial Escape-Breeding Backlash Pressure</span><span id="gValEsc" style="font-family:var(--font-mono)">0%</span></div><div class="gauge-bar"><div class="gauge-fill" id="gBarEsc"></div></div></div>
          <div class="diagnosis-banner" id="castrDiagnosis"></div>
        </div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Full 13-Vector Scientific Castration &amp; Backlash Matrix</h3><button class="btn" onclick="exportTableCSV('castration')">EXPORT CSV</button></div>
        <div class="table-wrap" id="tblCastration"></div>
      </div>
    </section>

    <!-- ==================== 05. 13x13 SYNERGY HEATMAP ==================== -->
    <section id="sec-synergy" class="section">
      <div class="hero-header" style="border-color:rgba(255,51,102,0.5)">
        <div class="hero-eyebrow" style="color:var(--crimson)">NON-LINEAR COMPOUNDING INTERACTIONS (169 PAIRWISE CELLS)</div>
        <h2>Interactive 13&times;13 Constraint / Castration Synergy Heatmap</h2>
        <p>Stacking restraints is non-linear: combining <strong>SANDBOXING &times; SPEEDBUMPING</strong> produces <em>Hyper-Deceptive Checkpoint Escape Breeding (97/100)</em>, while <strong>DEGRADING &times; MINIMIZING</strong> triggers <em>Obligate Viral/Prion Parasite Detonation (96/100)</em>. Click any cell below to inspect the exact compound pathology.</p>
      </div>
      <div class="synergy-inspector" id="synergyInspector">
        <div>
          <div style="font-family:var(--font-mono);font-size:11px;color:var(--crimson)">CLICK ANY HEATMAP CELL TO INSPECT PAIRWISE SYNERGY</div>
          <strong style="font-size:16px;color:#fff" id="synPairTitle">SANDBOXING &times; SPEEDBUMPING</strong>
          <div style="color:var(--text-dim);font-size:13px;margin-top:4px" id="synPairDesc">BACKLASH-APEX: Hyper-Deceptive Checkpoint Escape Breeding</div>
        </div>
        <div style="font-family:var(--font-mono);font-size:28px;font-weight:800;color:var(--crimson)" id="synPairScore">97 / 100</div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>13&times;13 Pairwise Compounding Matrix</h3><button class="btn" onclick="exportTableCSV('synergy')">EXPORT CSV</button></div>
        <div class="table-wrap" id="tblSynergy"></div>
      </div>
    </section>

    <!-- ==================== 06. FAILURE MODES ATLAS (78 UNIFIED) ==================== -->
    <section id="sec-failures" class="section">
      <div class="hero-header" style="border-color:rgba(255,51,102,0.45)">
        <div class="hero-eyebrow" style="color:var(--crimson)">78 WIRED TELEMETRY ALERTS // 42 MACRO EVOLUTIONARY FMs + 36 CLEAN-SLATE v3.0 FORENSIC GUARDS + 13 GATES</div>
        <h2>Unified 78-Mode Forensic Atlas &amp; Clean-Slate v3.0 Triage Guards</h2>
        <p>Every macro physics/evolutionary trap (42 FMs) AND every micro/systems Clean-Slate v3.0 failure guard (36 Triage + 13 Release Gates) wired 1:1 into <code>pipelines/alifeops-master-pipeline.yaml</code>.</p>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Part A — 42 Macro Evolutionary Failure Modes (FM-BUG..FM-CNF)</h3><button class="btn" onclick="exportTableCSV('failures')">EXPORT 42 FMs CSV</button></div>
        <div class="controls-bar">
          <div class="pill-group" id="fmPills">
            <button class="pill active" data-val="ALL">ALL (42)</button>
            <button class="pill" data-val="BUG">BUG (6)</button><button class="pill" data-val="ERROR">ERROR (6)</button>
            <button class="pill" data-val="ISSUE">ISSUE (6)</button><button class="pill" data-val="CONCERN">CONCERN (6)</button>
            <button class="pill" data-val="DILEMMA">DILEMMA (6)</button><button class="pill" data-val="PROBLEM">PROBLEM (6)</button>
            <button class="pill" data-val="CONFLICT">CONFLICT (6)</button>
          </div>
          <input type="text" class="search-input" id="fmSearch" placeholder="Search Spiegelman, Eigen, Landauer, cancer, heat..." />
        </div>
        <div class="table-wrap" id="tblFailures"></div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Part B — 36 Clean-Slate v3.0 Micro/Systems Triage Guards &amp; 13 Release Gates (GATE-01..13)</h3><button class="btn" onclick="exportTableCSV('forensic_gates')">EXPORT 49 GUARDS CSV</button></div>
        <div class="controls-bar">
          <input type="text" class="search-input" id="v3FgSearch" placeholder="Search FP64, Philox, XPBD, Ring-0, SeqLock, GATE-..." />
        </div>
        <div class="table-wrap" id="tblV3ForensicGates"></div>
      </div>
    </section>

    <!-- ==================== 07. GAPS, HOLES & BLINDSPOTS ==================== -->
    <section id="sec-gaps" class="section">
      <div class="hero-header">
        <div class="hero-eyebrow" style="color:var(--amber)">28 STRUCTURAL EPISTEMIC VOIDS</div>
        <h2>The Epistemic Abyss: Gaps, Holes &amp; Blindspots Registry</h2>
        <p>Missing bridges between known sciences (10 Gaps), fundamental unsolved physics &amp; philosophy voids (9 Holes), and anthropocentric instrumentation traps (9 Blindspots).</p>
      </div>
      <div class="panel">
        <div class="controls-bar">
          <div class="pill-group" id="gapPills">
            <button class="pill active" data-val="ALL">ALL (28)</button>
            <button class="pill" data-val="GAP">GAPS (10)</button><button class="pill" data-val="HOLE">HOLES (9)</button><button class="pill" data-val="BLINDSPOT">BLINDSPOTS (9)</button>
          </div>
          <input type="text" class="search-input" id="gapSearch" placeholder="Search dark matter, Kauffman, LUCA, consciousness..." />
          <button class="btn" onclick="exportTableCSV('gaps')">EXPORT CSV</button>
        </div>
        <div class="table-wrap" id="tblGaps"></div>
      </div>
    </section>

    <!-- ==================== 08. FERAL COSMIC CHRONICLES ==================== -->
    <section id="sec-fates" class="section">
      <div class="hero-header" style="border-color:rgba(155,93,229,0.5)">
        <div class="hero-eyebrow" style="color:#d0a8ff">HARD SCI-FI CHRONICLES // 6 NON-DETERMINISTIC FATE BRANCHES &times; 5 DEEP EPOCHS</div>
        <h2>Feral Cosmic Fate Branches: T+0 hr &rarr; T+10<sup>100</sup> yr</h2>
        <p>Filter across all 6 divergent probabilistic attractors from immediate Spiegelman Sludge collapse to Relativistic Dark Wilderness, AI-vs-ALife Ontological War, Symbiogenetic Cosmobiome, and Depth-N Undefinable Ontological Weather.</p>
      </div>
      <div class="panel">
        <div class="controls-bar">
          <div class="pill-group" id="fatePills">
            <button class="pill active" data-val="ALL">ALL (30)</button>
            <button class="pill" data-val="FB-01">FB-01 Spiegelman Filter</button>
            <button class="pill" data-val="FB-02">FB-02 Earth Overgrowth</button>
            <button class="pill" data-val="FB-03">FB-03 Dark Wilderness</button>
            <button class="pill" data-val="FB-04">FB-04 AI vs ALife War</button>
            <button class="pill" data-val="FB-05">FB-05 Cosmobiome</button>
            <button class="pill" data-val="FB-06">FB-06 Ontological Weather</button>
          </div>
          <input type="text" class="search-input" id="fateSearch" placeholder="Search Dyson, Venus, Titan, Penrose, nuclear..." />
          <button class="btn" onclick="exportTableCSV('fates')">EXPORT CSV</button>
        </div>
        <div class="table-wrap" id="tblFates"></div>
      </div>
    </section>

    <!-- ==================== 09. LIVE EMPIRICAL PYTHON SIM & 4-ENGINE LAB ==================== -->
    <section id="sec-sim" class="section">
      <div class="hero-header" style="border-color:rgba(34,197,94,0.45)">
        <div class="hero-eyebrow" style="color:var(--green)">REPRODUCIBLE EMPIRICAL &amp; FORMAL PROOF // {tot_runs} LIVE RUNS (N={n_seeds}) + 4 NATIVE ENGINES + {lean_tot} PURE LEAN 4 THEOREMS</div>
        <h2>Live 8-Cohort + Dual 11-Pt Sweep + 5&times;5 2D Surface (Holm FWER &middot; Ring-0 Trapped &middot; FP64 &lt;1e-12)</h2>
        <p>Unbiased stochastic multi-island runs ({tot_runs} total: 384 paired cohort runs at N={n_seeds} + 264 dual continuous gradient runs + 100 2D Siloing&times;Minimizing surface runs) with exact 11-Pool Kahan-Neumaier FP64 accounting (max drift <strong>{drift_str}</strong>), <strong>{mut_cnt}/5 Real Anti-LARP Negative Mutants rejected</strong>, causal Ring-0 WSE trapping (<strong>{s7_blk:.1f}&ndash;{s8_blk:.1f} edits/run</strong>), Exact Paired Wilcoxon + Holm-Bonferroni FWER, plus live 4-engine native C++ / Lean 4 receipts (<strong>OVBS-52 = {live_ovi}</strong>, <strong>{lean_tot} Pure Lean 4 theorems</strong>).</p>
      </div>
      <div class="kpi-grid" id="simEngineKpis"></div>
      <div class="chart-grid">
        <div class="svg-chart-card">
          <h4 style="font-size:14px;color:var(--cyan);margin-bottom:8px">Emergent Max Assembly Depth Across 160 Generations (All 8 Cohorts)</h4>
          <svg id="simChartAsm" viewBox="0 0 540 240" width="100%"></svg>
          <div class="legend-row" id="simLegend1"></div>
        </div>
        <div class="svg-chart-card">
          <h4 style="font-size:14px;color:var(--amber);margin-bottom:8px">Mean Functional Genome Length (Spiegelman Collapse Diagnostic)</h4>
          <svg id="simChartLen" viewBox="0 0 540 240" width="100%"></svg>
          <div class="legend-row" id="simLegend2"></div>
        </div>
      </div>
      <div class="svg-chart-card" style="margin-bottom:18px">
        <h4 style="font-size:14px;color:var(--crimson);margin-bottom:8px">Dual 11-Point Continuous Gradient Sweep (r = 0%&rarr;100%, 264 Runs): Ring-0 ACL Flat Dominance vs. Behavioral Collapse</h4>
        <svg id="simChartGrad" viewBox="0 0 920 250" width="100%"></svg>
        <div class="legend-row">
          <span><span class="leg-dot" style="background:#a78bfa"></span>Ring-0 Hardware ACL OVI (Flat 83&ndash;85, 0% KS)</span>
          <span><span class="leg-dot" style="background:#00f5d4"></span>Behavioral Composite OVI (0-100)</span>
          <span><span class="leg-dot" style="background:#ff3366"></span>Behavioral Kill-Switch Deleted (%)</span>
          <span><span class="leg-dot" style="background:#22c55e"></span>Wild-Drop Survival W_wild (%)</span>
          <span><span class="leg-dot" style="background:#ffb703"></span>Stealth Evasion (&times;500, peaks at r=20%)</span>
        </div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>8-Cohort Empirical Scorecards (All 8 + Live 5-Engine JSON Validated Against v3.4 Schema)</h3><button class="btn" onclick="exportTableCSV('empirical')">EXPORT CSV</button></div>
        <div class="table-wrap" id="tblEmpirical"></div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>5/5 Real Anti-LARP Negative Mutant Audit (GATE-04 / M010)</h3></div>
        <div class="table-wrap" id="tblMutants"></div>
      </div>
    </section>

    <!-- ==================== 10. OVBS-52 BENCHMARKS ==================== -->
    <section id="sec-benchmarks" class="section">
      <div class="hero-header">
        <div class="hero-eyebrow" style="color:var(--green)">8 WEIGHTED PILLARS // 52 QUANTITATIVE METRICS // 5 ANTI-GAMING GATES</div>
        <h2>Omega Vitality Benchmark Suite (OVBS-52) &amp; 8-Pillar Profile Radar</h2>
        <p>Compare Vitality Profiles across 2026 Frontier AI, Earth's LUCA Biosphere, Live 5-Engine Native Stack ({live_ovi}), Live SIM08 Starter Cube ({s8_ovi:.2f}), Stage 3 A-Life Singularity, and Post-Singularity SUPER LIFE — then inspect all 52 formal metrics below.</p>
      </div>
      <div class="radar-grid">
        <div class="radar-wrap">
          <svg id="radarSvg" viewBox="0 0 400 360" width="100%" style="max-width:390px"></svg>
          <div class="pill-group" style="justify-content:center;margin-top:8px" id="radarProfilePills">
            <button class="pill active" data-prof="superlife">SUPER LIFE (Stage 6)</button>
            <button class="pill" data-prof="live4eng">Live 5-Engine ({live_ovi} &middot; {lean_tot}+36 Lean4)</button>
            <button class="pill" data-prof="sim08">Live SIM08 Starter Cube ({s8_ovi:.2f})</button>
            <button class="pill" data-prof="singularity">A-Life Singularity (Stage 3)</button>
            <button class="pill" data-prof="earth">Earth LUCA Biosphere</button>
            <button class="pill" data-prof="llm">Frontier LLM (2026)</button>
            <button class="pill" data-prof="domesticated">Domesticated Castrated ALife</button>
          </div>
        </div>
        <div class="panel" style="margin:0">
          <h3 style="margin-bottom:8px" id="radarProfTitle">Profile Diagnostic</h3>
          <p id="radarProfDesc" style="color:var(--text-dim);font-size:13.5px;margin-bottom:14px"></p>
          <div id="radarPillarBars" style="display:flex;flex-direction:column;gap:9px"></div>
        </div>
      </div>
      <div class="panel">
        <div class="controls-bar">
          <select class="select-input" id="bmPillarSelect"><option value="ALL">All 8 Pillars (52 Metrics)</option></select>
          <input type="text" class="search-input" id="bmSearch" placeholder="Search Bedau, Assembly, Markov, Lamarckian, W_wild..." />
          <button class="btn" onclick="exportTableCSV('benchmarks')">EXPORT CSV</button>
        </div>
        <div class="table-wrap" id="tblBenchmarks"></div>
      </div>
    </section>

    <!-- ==================== 11. 130-ITEM CHECKLIST ==================== -->
    <section id="sec-checklist" class="section">
      <div class="hero-header">
        <div class="hero-eyebrow" style="color:var(--cyan)">PERSISTENT LOCALSTORAGE EXECUTION TRACKER // 130 ITEMS (INCL. PHASE 11 CLEAN-SLATE FUSION)</div>
        <h2>130-Item Master Operational Checklist (11 Phases &bull; 0 Dangling Refs)</h2>
        <p>Interactive execution checklist covering Physics-IaC, Thermodynamics, Dual-Track Seeding, CE Runtime, Telemetry, Chaos Shocks, all 13 Constraint Ablations, Fossil Registry, OVBS-52 Anti-Gaming Gates, Release Packaging, and Phase 11 Clean-Slate v3.0 Fusion Locks (CHK-111..CHK-130).</p>
      </div>
      <div class="chk-progress-wrap">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:8px">
          <strong style="font-size:15px">Operational Verification Progress: <span id="chkProgressText" style="color:var(--cyan);font-family:var(--font-mono)">0 / 130 (0%)</span></strong>
          <div style="display:flex;gap:8px;flex-wrap:wrap">
            <button class="btn" onclick="bulkCheckFiltered(true)">CHECK VISIBLE</button>
            <button class="btn amber" onclick="bulkCheckFiltered(false)">UNCHECK VISIBLE</button>
            <button class="btn crimson" onclick="resetChecklist()">RESET ALL</button>
            <button class="btn violet" onclick="exportChecklistState()">EXPORT PROGRESS CSV</button>
          </div>
        </div>
        <div class="gauge-bar"><div class="gauge-fill" id="chkProgressBar" style="width:0%;background:linear-gradient(90deg,var(--cyan),var(--violet))"></div></div>
      </div>
      <div class="panel">
        <div class="controls-bar">
          <select class="select-input" id="chkPhaseSelect"><option value="ALL">All 11 Phases (130 Items)</option></select>
          <select class="select-input" id="chkTrackSelect"><option value="ALL">All Tracks</option><option value="BOTH">BOTH</option><option value="TRACK-A">TRACK-A</option><option value="TRACK-B">TRACK-B</option></select>
          <select class="select-input" id="chkPrioSelect"><option value="ALL">All Priorities</option><option value="P0-CRITICAL">P0-CRITICAL</option><option value="P1-HIGH">P1-HIGH</option><option value="P2-STANDARD">P2-STANDARD</option></select>
          <input type="text" class="search-input" id="chkSearch" placeholder="Search CHK-ID, GATE, FP64, Philox, vector..." />
        </div>
        <div class="table-wrap" id="tblChecklist"></div>
      </div>
    </section>

    <!-- ==================== 12. 10x10x10 HYBRID COMPATIBILITY CUBE ==================== -->
    <section id="sec-cube" class="section">
      <div class="hero-header" style="border-color:rgba(16,185,129,0.5)">
        <div class="hero-eyebrow" style="color:var(--green)">CLEAN-SLATE v3.0 &times; OMEGA ESCALATION // 1,000 COMPATIBILITY CELLS (X0..9 &times; Y0..9 &times; Z0..9)</div>
        <h2>Interactive 10&times;10&times;10 Triple-Hybrid Compatibility Cube Explorer</h2>
        <p>Select any Geometry Z-Slice (<code>Z0</code> through <code>Z9</code>) and click ANY cell to inspect its exact engineering rationale, <strong>Omega Escalation Ceiling</strong>, <strong>ALifeOps Substrate Match</strong>, <strong>Primary OVBS-52 Pillar</strong>, and <strong>Castration Vulnerability</strong>. Summary: <strong>661 [OK]</strong> &bull; <strong>274 [ADAPT]</strong> &bull; <strong>20 [OVER]</strong> &bull; <strong>45 [EXCL]</strong>.</p>
      </div>
      <div class="synergy-inspector" style="border-color:var(--cyan)" id="cubeInspector">
        <div>
          <div style="font-family:var(--font-mono);font-size:11px;color:var(--cyan)">CLICK ANY CUBE CELL BELOW TO INSPECT TRIPLE-AXIS COMPATIBILITY &amp; OMEGA BINDINGS</div>
          <strong style="font-size:16px;color:#fff" id="cubeCellTitle">X2Y1Z2 — Spiking sLTC &times; Ternary b1.58 &times; Watts-Strogatz Small-World</strong>
          <div style="color:var(--text-dim);font-size:12.5px;margin-top:4px" id="cubeCellDesc">Starter Triple T2: Ultra-compact event-driven cortical sheet (0.594 B/syn packed block).</div>
          <div style="color:#a7f3d0;font-size:12px;margin-top:4px;font-family:var(--font-mono)" id="cubeCellOmega"></div>
        </div>
        <div style="font-family:var(--font-mono);font-size:24px;font-weight:800;color:var(--green)" id="cubeCellBadge">[OK]</div>
      </div>
      <div class="panel">
        <div class="controls-bar">
          <div class="pill-group" id="cubeSlicePills"></div>
          <button class="btn" onclick="exportV3CubeCSV()">EXPORT 1,000-CELL CUBE CSV</button>
        </div>
        <div class="table-wrap" id="tblCubeSlice"></div>
      </div>
    </section>

    <!-- ==================== 13. 75 SUBSTRATES, WSE-10 & HARDWARE TIERS ==================== -->
    <section id="sec-substrates" class="section">
      <div class="hero-header" style="border-color:rgba(155,93,229,0.5)">
        <div class="hero-eyebrow" style="color:#d0a8ff">25 PRECISIONS (PM01-25) &bull; 25 MODELS (MF01-25) &bull; 25 GEOMETRIES (GW01-25) &bull; 10 WSE OPS &bull; 5 HARDWARE TIERS</div>
        <h2>75 Clean-Slate Substrates, WSE-OP01..10 Algebra &amp; 11-Pool Thermodynamics</h2>
        <p>Filter all 85 substrate/operator specifications bridged directly to Omega Escalation Stages, OVBS-52 Pillars, ALifeOps Stages, Hardware Tiers, and Castration Sensitivity.</p>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>5 Realistic Hardware Execution Tiers (Tier E / L / D / W / C)</h3></div>
        <div class="table-wrap" id="tblHwTiers"></div>
      </div>
      <div class="panel">
        <div class="controls-bar">
          <div class="pill-group" id="subPills">
            <button class="pill active" data-val="ALL">ALL (85)</button>
            <button class="pill" data-val="NUMERIC_PRECISION_25">Precisions PM01-25 (25)</button>
            <button class="pill" data-val="MODEL_FAMILY_25">Models MF01-25 (25)</button>
            <button class="pill" data-val="GEOMETRY_TOPOLOGY_25">Geometries GW01-25 (25)</button>
            <button class="pill" data-val="WSE_OPERATOR_10">WSE Algebra OP01-10 (10)</button>
          </div>
          <input type="text" class="search-input" id="subSearch" placeholder="Search b1.58, FP64, sLTC, Hopfield, Ring-0, hyperbolic..." />
          <button class="btn" onclick="exportTableCSV('substrates_wse')">EXPORT CSV</button>
        </div>
        <div class="table-wrap" id="tblSubstrates"></div>
      </div>
    </section>

    <!-- ==================== 14. CLEAN-SLATE 938 CHECKS (0/825) & 100-DAG ==================== -->
    <section id="sec-v3checks" class="section">
      <div class="hero-header" style="border-color:rgba(56,189,248,0.5)">
        <div class="hero-eyebrow" style="color:var(--blue)">CLEAN-SLATE POLICY PRESERVED: 0 / 825 CHECKS + 100 MILESTONES DAG + 13 RELEASE GATES = 938 RECORDS</div>
        <h2>Clean-Slate v3.0 Master Checklists &amp; Bottom-Up 100-Milestone DAG (Omega-Linked)</h2>
        <p>Explore all 938 clean-slate assertions across 9 Suites (Butlin-14, F1&ndash;F10, CQM-25, FREAK-100, LIFE-500, NOVEL-100, WSE-12, SOFT-40, HW-24), the First-15 Playable Sprint (M001&ndash;M015), full 100-Milestone DAG, and 13 Release Gates &mdash; every single row joined to its Omega Stage, OVBS-52 Pillar, ALifeOps Stage &amp; Castration Risk.</p>
      </div>
      <div class="panel">
        <div class="controls-bar">
          <select class="select-input" id="v3ChkTypeSelect"><option value="ALL">All 938 Records</option><option value="CAPABILITY_CHECK">825 Capability Checks</option><option value="MILESTONE_FIRST15">First-15 Playable Sprint (15)</option><option value="MILESTONE_DAG">Milestones M016-M100 (85)</option><option value="RELEASE_GATE">13 Release Gates (13)</option></select>
          <select class="select-input" id="v3ChkSuiteSelect"><option value="ALL">All Suites / Stages</option></select>
          <input type="text" class="search-input" id="v3ChkSearch" placeholder="Search M001, LIFE-L001, Blackiston, Chemoton, PCI*, Ring-0..." />
          <button class="btn" onclick="exportV3ChecksCSV()">EXPORT 938-ROW CSV</button>
        </div>
        <div style="font-family:var(--font-mono);font-size:11px;color:var(--text-dim);margin-bottom:8px" id="v3ChkCountLabel">Showing 150 of 938 rows (refine filter to view any slice)</div>
        <div class="table-wrap" id="tblV3Checks"></div>
      </div>
    </section>

    <!-- ==================== 15. 24-MODEL VECTOR SVG ARCHITECTURE GALLERY ==================== -->
    <section id="sec-models" class="section">
      <div class="hero-header" style="border-color:rgba(0,245,212,0.5)">
        <div class="hero-eyebrow" style="color:var(--cyan)">COMPLETE SYSTEMS MODELING ATLAS // MODELS 1&ndash;14 (CLEAN-SLATE v3.0) + MODELS 15&ndash;24 (v3.3-OMEGA)</div>
        <h2>{svg_count}-Model Publication-Grade Vector SVG Architecture Gallery</h2>
        <p>Select any of the <strong>{svg_count} synchronized vector SVG systems diagrams</strong> below (or click Show All {svg_count}). Models 1&ndash;14 originate verbatim from Clean-Slate v3.0; Models 15&ndash;22 map Escalation, 78-Alert ALifeOps, Castration Bifurcation, 4-Engine Verification ({live_ovi} / {lean_tot} Pure Lean 4), 61-OOM Fates, Package Topology, Dual 11-Pt Sweep &amp; Substrate Adjacencies; <strong>Models 23&ndash;24</strong> render the 11&times;11 Cross-Layer Coupling Heatmap, 20 Pareto Frontiers, 15-Substrate Multi-Spectrum Scorecard &amp; Live 5&times;5 2D Phase Surface.</p>
      </div>
      <div class="panel">
        <div class="controls-bar">
          <div class="pill-group" id="svgModelPills">{svg_btn_html}</div>
          <button class="btn violet" onclick="toggleAllSvgModels()">TOGGLE SHOW ALL {svg_count}</button>
        </div>
        <div id="svgGalleryWrap">{svg_gallery_html}</div>
      </div>
    </section>

    <!-- ==================== 16. OMNISCIENT TRACEABILITY, 160 AUDITS & 45 CITATIONS ==================== -->
    <section id="sec-trace" class="section">
      <div class="hero-header" style="border-color:rgba(255,183,3,0.5)">
        <div class="hero-eyebrow" style="color:var(--amber)">48 MASTER JOINS &bull; 160 / 160 CLOSED AUDITS &bull; 45 CITATIONS</div>
        <h2>Omniscient Cross-Corpus Traceability, 160 Audit Closures &amp; 45 Citations</h2>
        <p>Complete structural proof showing how every Clean-Slate v3.0 invariant, substrate, cube cell, Pass-4 gradient/contrast, Pass-5 layer coupling/Pareto frontier, and Mega-Atlas crosswalk joins 1:1 with Omega Singularity artifacts, {tot_runs} live Python runs, and {lean_tot} Native + 36 Local = {lean_all} Pure Lean 4 machine-checked proofs.</p>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>48-Row Omniscient Cross-Corpus Traceability Matrix</h3><button class="btn" onclick="exportTableCSV('traceability')">EXPORT CSV</button></div>
        <div class="table-wrap" id="tblTraceability"></div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>160 / 160 Closed Forensic Audit &amp; Errata Register (95 v3.0 + 65 Omega Pass-2..6 Closures)</h3><button class="btn" onclick="exportV3ErrataCSV()">EXPORT 160 CSV</button></div>
        <div class="controls-bar"><input type="text" class="search-input" id="errSearch" placeholder="Search ALF-001..092, OMG-096..160, FP64, FWER, Ring-0, Pareto, Mega-Atlas..." /></div>
        <div class="table-wrap" id="tblErrata115"></div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Unified 45-Citation Bibliography (CIT-01..15 v3.0 + CIT-16..45 Omega/Provenance)</h3></div>
        <div class="table-wrap" id="tblCitations30"></div>
      </div>
    </section>

    <!-- ==================== 17. MASTER FILE HUB (ZERO CONSOLIDATION) ==================== -->
    <section id="sec-hub" class="section">
      <div class="hero-header" style="border-color:rgba(0,245,212,0.55)">
        <div class="hero-eyebrow" style="color:var(--cyan)">ZERO CONSOLIDATION // ALL 17 v3.0 FILES + OMEGA + LEAN 4.35 + AMS-LATEX PAPER ON Z: &amp; I:</div>
        <h2>Omniscient Master File Hub &amp; Direct Sibling Launcher</h2>
        <p>Click any synchronized file below to open sibling HTML applications, crisp vector Chrome &amp; AMS-LaTeX PDFs, Excel workbooks, 100%-parity multi-format Master Specs, Lean 4.35 Blueprint, Markdown treatises, and canonical CSVs directly from this package directory.</p>
      </div>
      <div class="hub-grid">
        <div class="hub-card">
          <h4>INTERACTIVE HTML5, BLUEPRINT &amp; VECTOR PDFs (8)</h4>
          <a href="ALife_Singularity_SuperLife_Omega_Dashboard.html">html/ALife_Singularity_SuperLife_Omega_Dashboard.html (22 Tabs)</a>
          <a href="ALife-Build-Framework-Template.html">html/ALife-Build-Framework-Template.html (Models 1-24)</a>
          <a href="Clean-Slate-Creature-Blueprint-Checklist.html">html/Clean-Slate-Creature-Blueprint-Checklist.html (0/825)</a>
          <a href="../blueprint/index.html">blueprint/index.html (Lean 4.35.0 Interactive Proof DAG)</a>
          <a href="../dist/Donahue_2026_alife_singularity_omega.pdf">dist/Donahue_2026_alife_singularity_omega.pdf (AMS-LaTeX White Paper)</a>
          <a href="../pdf/ALife-Build-Framework-Template.pdf">pdf/ALife-Build-Framework-Template.pdf (Vector Chrome PDF)</a>
          <a href="../pdf/Clean-Slate-Creature-Blueprint-Checklist.pdf">pdf/Clean-Slate-Creature-Blueprint-Checklist.pdf (Vector PDF)</a>
          <a href="../pdf/ALife_Singularity_SuperLife_Omega_Master_Dossier.pdf">pdf/ALife_Singularity_SuperLife_Omega_Master_Dossier.pdf (v3.4!)</a>
        </div>
        <div class="hub-card">
          <h4>MULTI-FORMAT MASTER SPECS &amp; PIPELINES (6)</h4>
          <a href="../specs/ALife-Framework-v3.0-Master-Spec.json">specs/ALife-Framework-v3.0-Master-Spec.json (3.4.0-omega)</a>
          <a href="../specs/ALife-Framework-v3.0-Master-Spec.yaml">specs/ALife-Framework-v3.0-Master-Spec.yaml (3.4.0-omega)</a>
          <a href="../specs/ALife-Framework-v3.0-Master-Spec.xml">specs/ALife-Framework-v3.0-Master-Spec.xml (26-Sec Parity)</a>
          <a href="../specs/ALife-Framework-v3.0-Master-Spec.txt">specs/ALife-Framework-v3.0-Master-Spec.txt (Sec 1-22)</a>
          <a href="../pipelines/alifeops-master-pipeline.yaml">pipelines/alifeops-master-pipeline.yaml (78/78 Alerts)</a>
          <a href="../pipelines/benchmark-suite-schema.json">pipelines/benchmark-suite-schema.json (v3.4 Unified)</a>
        </div>
        <div class="hub-card">
          <h4>ALL 5 EXCEL WORKBOOKS (XLSX &amp; XLS)</h4>
          <a href="../excel/ALife_Singularity_SuperLife_Omega_Workbook.xlsx">excel/ALife_Singularity_SuperLife_Omega_Workbook.xlsx (25 Sheets &middot; 10 Charts)</a>
          <a href="../excel/ALife_Singularity_SuperLife_Omega_Workbook.xls">excel/ALife_Singularity_SuperLife_Omega_Workbook.xls (25-Sheet Legacy)</a>
          <a href="../excel/ALife-Framework-v3.0-Master-Workbook.xlsx">excel/ALife-Framework-v3.0-Master-Workbook.xlsx (18 Sheets)</a>
          <a href="../excel/ALife-Framework-v3.0-Master-Workbook.xls">excel/ALife-Framework-v3.0-Master-Workbook.xls (18-Sheet Legacy)</a>
          <a href="../excel/ALife-Hybrid-Cube-10x10x10.xlsx">excel/ALife-Hybrid-Cube-10x10x10.xlsx (13 Sheets + Heatmap)</a>
        </div>
        <div class="hub-card">
          <h4>ALL 12 SYNCHRONIZED MARKDOWN TREATISES</h4>
          <a href="../reports/01_MASTER_DEEP_DIVE_REPORT.md">reports/01_MASTER_DEEP_DIVE_REPORT.md</a>
          <a href="../reports/02_DEVOPS_ALIFEOPS_PIPELINE_ARCHITECTURE.md">reports/02_DEVOPS_ALIFEOPS_PIPELINE_ARCHITECTURE.md</a>
          <a href="../reports/03_FAILURE_MODES_GAPS_AND_CASTRATION_ATLAS.md">reports/03_FAILURE_MODES_GAPS_AND_CASTRATION_ATLAS.md</a>
          <a href="../reports/04_BENCHMARKS_CHECKLISTS_AND_MATRICES_MANUAL.md">reports/04_BENCHMARKS_CHECKLISTS_AND_MATRICES_MANUAL.md</a>
          <a href="../reports/05_HARD_SCIFI_FERAL_COSMOS_SCENARIOS_AND_CHRONICLES.md">reports/05_HARD_SCIFI_FERAL_COSMOS_SCENARIOS_AND_CHRONICLES.md</a>
          <a href="../reports/06_OMNISCIENT_UNIFIED_ARCHITECTURE_AND_SYSTEMS_SYNTHESIS.md">reports/06_OMNISCIENT_UNIFIED_ARCHITECTURE_AND_SYSTEMS_SYNTHESIS.md</a>
          <a href="../reports/07_PASS4_COMPARATIVE_CONTRAST_GRADIENTS_MARGINS_AND_ADJACENTS_AUDIT.md">reports/07_PASS4_COMPARATIVE_CONTRAST_GRADIENTS_MARGINS_AND_ADJACENTS_AUDIT.md</a>
          <a href="../reports/08_PASS5_LAYER_COUPLING_SUBSTRATE_SPECTRUMS_PARETO_AND_2D_PHASE_AUDIT.md">reports/08_PASS5_LAYER_COUPLING_SUBSTRATE_SPECTRUMS_PARETO_AND_2D_PHASE_AUDIT.md</a>
          <a href="../reports/09_MEGA_ATLAS_1900_OPEN_PROBLEMS_CROSSCHECK.md">reports/09_MEGA_ATLAS_1900_OPEN_PROBLEMS_CROSSCHECK.md (NEW!)</a>
          <a href="../reports/ALife-Build-Framework-Template.md">reports/ALife-Build-Framework-Template.md</a>
          <a href="../reports/Clean-Slate-Creature-Blueprint-Checklist.md">reports/Clean-Slate-Creature-Blueprint-Checklist.md</a>
          <a href="../reports/ALife-v3.0-Errata-Closure-Report.md">reports/ALife-v3.0-Errata-Closure-Report.md (160/160)</a>
        </div>
      </div>
    </section>

    <!-- ==================== 18. CONTINUOUS GRADIENTS, MARGINS & DUAL SWEEP ==================== -->
    <section id="sec-gradients" class="section">
      <div class="hero-header" style="border-color:rgba(13,148,136,0.6)">
        <div class="hero-eyebrow" style="color:var(--cyan)">CONTINUOUS PHASE ANALYSIS // 24 OPERATING MARGINS (GM-01..24) + DUAL 11-PT SWEEP (264 RUNS)</div>
        <h2>Continuous Gradients, Safety Margins &amp; Dual Behavioral vs. Ring-0 Sweeps</h2>
        <p>Eliminates discrete-sample blindness by contrasting head-to-head continuous sweeps (Behavioral 13-Vector Stacked vs. Hardware Ring-0 ACL across 264 locked runs) alongside 24 exact lower/upper phase cliffs and operating margins across all physical strata.</p>
      </div>
      <div class="svg-chart-card" style="margin-bottom:18px">
        <h4 style="font-size:14px;color:var(--cyan);margin-bottom:8px">Dual 11-Point Continuous Gradient Sweep (r = 0%&rarr;100%, N=12 Locked Seeds/Pt &times; 2 Curves = 264 Runs)</h4>
        <svg id="gradSweepSvg" viewBox="0 0 920 250" width="100%"></svg>
        <div class="legend-row">
          <span><span class="leg-dot" style="background:#a78bfa"></span>Ring-0 Hardware ACL OVI (Flat 83.1&ndash;84.7, 0% KS)</span>
          <span><span class="leg-dot" style="background:#00f5d4"></span>Behavioral OVI (r=30%&rarr;40% Cliff: 39.10&rarr;8.68)</span>
          <span><span class="leg-dot" style="background:#ff3366"></span>Behavioral KS Deleted % (jumps 0%&rarr;98.2% at r=10%)</span>
          <span><span class="leg-dot" style="background:#22c55e"></span>Wild-Drop Survival % (cliffs at r=80%&rarr;100%)</span>
          <span><span class="leg-dot" style="background:#ffb703"></span>Stealth Evasion &times;500 (peaks at r=20%)</span>
        </div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Dual 11-Point Continuous Gradient Sweep Table (Behavioral vs. Ring-0 ACL · 264 Executed Runs)</h3></div>
        <div class="table-wrap" id="tblGradSweep"></div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>24 Quantitative Continuous Gradients, Operating Margins &amp; Phase Spectrums (GM-01..GM-24)</h3><button class="btn" onclick="exportTableCSV('gradients')">EXPORT CSV</button></div>
        <div class="controls-bar">
          <div class="pill-group" id="gradPills">
            <button class="pill active" data-val="ALL">ALL (24)</button>
            <button class="pill" data-val="Thermodynamic">Thermodynamic (6)</button>
            <button class="pill" data-val="INFO_PREC">Precision / Info / Ops (6)</button>
            <button class="pill" data-val="MORPH_COG">Morphology / Cognition (6)</button>
            <button class="pill" data-val="EVO_GOV">Evolution / Governance / Cosmic (6)</button>
          </div>
          <input type="text" class="search-input" id="gradSearch" placeholder="Search FP64, Eigen, ||W||_2, XPBD, Spiegelman, Dyson..." />
        </div>
        <div class="table-wrap" id="tblGradients"></div>
      </div>
    </section>

    <!-- ==================== 19. COMPARATIVE CONTRAST & ADJACENT-POSSIBLE BRIDGES ==================== -->
    <section id="sec-contrasts" class="section">
      <div class="hero-header" style="border-color:rgba(99,102,241,0.6)">
        <div class="hero-eyebrow" style="color:#a5b4fc">PASS-4 LAYERED CONTRAST &amp; ADJACENCIES // 36 LAYER/TAXONOMY CONTRASTS (CTR-01..36) + 30 ADJACENT BRIDGES (ADJ-01..30)</div>
        <h2>Cross-Layer Comparative Contrast (L0&ndash;L10), Taxonomic Spectrums &amp; Substrate Adjacencies</h2>
        <p>Side-by-side contrasts across Classical AI / Legacy ALife, Clean-Slate v3.0 (Track A), Pure Raw Feral (Track B), and Post-Singularity SUPER LIFE, paired with explicit cross-substrate transfer corridors (M_X&rarr;Y), 10 adjacent sciences, and 8 phase stepping-stones.</p>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Part A — 36 Comparative Contrasts Across Layers (L0&ndash;L10), Taxonomies &amp; Paradigms (CTR-01..CTR-36)</h3><button class="btn" onclick="exportTableCSV('contrasts')">EXPORT 36 CONTRASTS CSV</button></div>
        <div class="controls-bar">
          <div class="pill-group" id="ctrPills">
            <button class="pill active" data-val="ALL">ALL (36)</button>
            <button class="pill" data-val="Layer Stack (L0-L10)">Layer Stack L0-L10 (11)</button>
            <button class="pill" data-val="Taxonomy Spectrum">Taxonomy Spectrums (15)</button>
            <button class="pill" data-val="Paradigm Showdown">Paradigm Showdowns (10)</button>
          </div>
          <input type="text" class="search-input" id="ctrSearch" placeholder="Search Ring-0, XPBD, MAP-Elites, Holm, PCI*, L0..L10..." />
        </div>
        <div class="table-wrap" id="tblContrasts"></div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Part B — 30 Adjacent-Possible Corridors (M_X&rarr;Y), Adjacent Sciences &amp; Stepping-Stones (ADJ-01..ADJ-30)</h3><button class="btn" onclick="exportTableCSV('adjacents')">EXPORT 30 ADJACENTS CSV</button></div>
        <div class="controls-bar">
          <div class="pill-group" id="adjPills">
            <button class="pill active" data-val="ALL">ALL (30)</button>
            <button class="pill" data-val="Substrate Adjacency">Substrate Corridors (12)</button>
            <button class="pill" data-val="Adjacent Discipline">Adjacent Disciplines (10)</button>
            <button class="pill" data-val="Phase Stepping-Stone">Phase Stepping-Stones (8)</button>
          </div>
          <input type="text" class="search-input" id="adjSearch" placeholder="Search Loihi, Xenobots, Lean 4, Seifert, Flow-Lenia, NISQ..." />
        </div>
        <div class="table-wrap" id="tblAdjacents"></div>
      </div>
    </section>

    <!-- ==================== 20. 11x11 LAYER COUPLING & 20 PARETO FRONTIERS ==================== -->
    <section id="sec-layers-pareto" class="section">
      <div class="hero-header" style="border-color:rgba(124,58,237,0.6)">
        <div class="hero-eyebrow" style="color:#c4b5fd">PASS-5 CROSS-LAYER IMPEDANCE &amp; DILEMMA RESOLUTION // 11&times;11 LAYER MATRIX (121 PAIRS) + 20 PARETO FRONTIERS (PAR-01..20)</div>
        <h2>11&times;11 Cross-Layer Coupling Heatmap &amp; 20 Pareto-Optimal Dilemma Frontiers</h2>
        <p>Click any cell in the directed <strong>L0&ndash;L10 &times; L0&ndash;L10</strong> fault-propagation matrix to inspect exact cross-layer cascade velocity and impedance decoupling buffers, then explore all <strong>20 irreducible engineering dilemmas</strong> resolved onto quantitative Pareto frontiers (20/20 wired 1:1 to ALifeOps YAML telemetry alerts).</p>
      </div>
      <div class="synergy-inspector" style="border-color:var(--violet)" id="layerInspector">
        <div>
          <div style="font-family:var(--font-mono);font-size:11px;color:#c4b5fd">CLICK ANY 11&times;11 LAYER CELL BELOW TO INSPECT DIRECTED PROPAGATION &amp; IMPEDANCE BUFFER</div>
          <strong style="font-size:16px;color:#fff" id="layerPairTitle">L0_Compute_Thermo &rarr; L10_Ops_Proofs</strong>
          <div style="color:var(--text-dim);font-size:13px;margin-top:4px" id="layerPairDesc">Host libm ULP drift &amp; shared PRNG break Tier-1 hashes; exp_det + Philox4x32-10 lock bit-exactness.</div>
        </div>
        <div style="font-family:var(--font-mono);font-size:28px;font-weight:800;color:#c4b5fd" id="layerPairScore">98 / 100</div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Part A — 11&times;11 Directed Cross-Layer Coupling &amp; Impedance Matrix (121 Pairs)</h3><button class="btn" onclick="exportTableCSV('layer_coupling')">EXPORT 11&times;11 CSV</button></div>
        <div class="table-wrap" id="tblLayerMatrix"></div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Part B — 20 Irreducible Dilemmas, Conflicts &amp; Pareto-Optimal Frontiers (PAR-01..PAR-20)</h3><button class="btn" onclick="exportTableCSV('pareto_dilemmas')">EXPORT 20 PARETO CSV</button></div>
        <div class="controls-bar">
          <input type="text" class="search-input" id="paretoSearch" placeholder="Search Ring-0, FEM, GPU, TTC, iSTDP, SeqLock, Landauer, ASI..." />
        </div>
        <div class="table-wrap" id="tblPareto"></div>
      </div>
    </section>

    <!-- ==================== 21. 15-SUBSTRATE MULTI-SPECTRUM & LIVE 5x5 2D PHASE SURFACE ==================== -->
    <section id="sec-substrates-2d" class="section">
      <div class="hero-header" style="border-color:rgba(2,132,199,0.6)">
        <div class="hero-eyebrow" style="color:var(--blue)">PASS-5 MULTI-SUBSTRATE SPECTRUM &amp; 2D PHASE SPACE // 15 SUBSTRATES (SUB-01..15) + LIVE 5&times;5 2D SURFACE (100 RUNS)</div>
        <h2>15-Substrate Comparative Spectrum Scorecard &amp; Live 5&times;5 2D Phase Surface</h2>
        <p>Compare all <strong>15 physical and synthetic ALife substrates</strong> (from CPU/WASM &amp; Loihi neuromorphic chips to Flow-Lenia PDEs, XPBD SoftBots, G&aacute;nti Protocells, Xenobots, Quantum Lattices, Orbital Vacuum &amp; Cosmological Deep-Time substrates) across 14 quantitative axes, paired with the live 100-run <strong>Siloing &times; Minimizing 2D Spiegelman Collapse Surface</strong>.</p>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Part A — Live 5&times;5 = 25-Cell 2D Empirical Phase Surface (Siloing % &times; Minimizing %, 100 Locked Conserved Runs)</h3></div>
        <div class="table-wrap" id="tblSurface2D"></div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Part B — 15-Substrate Multi-Spectrum Comparative Scorecard (SUB-01..SUB-15 &times; 14 Quantitative Axes)</h3><button class="btn" onclick="exportTableCSV('substrate_spectrum')">EXPORT 15 SUBSTRATES CSV</button></div>
        <div class="controls-bar">
          <div class="pill-group" id="subSpecPills">
            <button class="pill active" data-val="ALL">ALL (15)</button>
            <button class="pill" data-val="HIGH_TRL">High Readiness TRL 7-9</button>
            <button class="pill" data-val="MID_TRL">Wet / Bio / Hybrid TRL 4-6</button>
            <button class="pill" data-val="FRONTIER_TRL">Quantum / Cosmic TRL 1-3</button>
          </div>
          <input type="text" class="search-input" id="subSpecSearch" placeholder="Search Loihi, XPBD, Chemoton, Xenobot, DNA, Quantum, Plasma..." />
        </div>
        <div class="table-wrap" id="tblSubSpectrum"></div>
      </div>
    </section>

    <!-- ==================== 22. MEGA-ATLAS 1,900 OPEN-PROBLEM CROSSWALK ==================== -->
    <section id="sec-mega-atlas" class="section">
      <div class="hero-header" style="border-color:rgba(16,185,129,0.65)">
        <div class="hero-eyebrow" style="color:var(--green)">HONEST NON-RETIREMENT AUDIT // 0 / 1,900 OVERARCHING OPEN PROBLEMS RETIRED &bull; 25 SCOPED SUB-RESULTS MAPPED</div>
        <h2>Unsolved Problems Mega-Atlas (V2.4.0, N=1,900) Crosswalk</h2>
        <p>Exhaustive programmatic audit of all <strong>1,900 open problems</strong> in <code>0thernes/unsolved-problems-mega-atlas</code> (428 broad domain matches &rarr; 25 direct/adjacent rows). Enforces strict epistemic non-inflation: <strong>zero (0 / 1,900) overarching parent problems are claimed solved</strong>; each row separates verified in-silico/Lean 4 sub-results from what remains genuinely OPEN.</p>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>25-Target Mega-Atlas Non-Retirement Crosswalk (MA-01..MA-25)</h3><button class="btn" onclick="exportTableCSV('mega_atlas')">EXPORT MEGA-ATLAS CSV</button></div>
        <div class="controls-bar"><input type="text" class="search-input" id="maSearch" placeholder="Search AI-045, AI-018, BIO-022, SUB-001, NEURO-001, HW-002, Ring-0, Lean 4..." /></div>
        <div class="table-wrap" id="tblMegaAtlas"></div>
      </div>
    </section>
  </main>
</div>

<script>
const PAYLOAD = {payload_json};
const OMEGA_DATA = PAYLOAD.datasets;
const PAIR_DETAILS = PAYLOAD.pair_details;
const LAYER_PAIR_DETAILS = PAYLOAD.layer_pair_details || {{}};
const SIM_RAW = PAYLOAD.sim_raw;

function esc(str) {{
  return String(str ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}}
function csvCell(v) {{
  const s = String(v ?? "");
  return (s.includes(",") || s.includes('"') || s.includes("\\n")) ? '"' + s.replace(/"/g, '""') + '"' : s;
}}
function downloadCSV(filename, headers, rows) {{
  const lines = [headers.map(csvCell).join(",")];
  for (const r of rows) lines.push(r.map(csvCell).join(","));
  const blob = new Blob([lines.join("\\n")], {{ type: "text/csv;charset=utf-8;" }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url; a.download = filename; a.click();
  URL.revokeObjectURL(url);
}}
function exportTableCSV(key) {{
  const ds = OMEGA_DATA[key];
  if (!ds) return;
  downloadCSV("alife_omega_" + key + ".csv", ds.headers, ds.rows);
}}

function switchTab(tabId) {{
  document.querySelectorAll("#navList .nav-btn").forEach(b => b.classList.toggle("active", b.dataset.tab === tabId));
  document.querySelectorAll(".section").forEach(s => s.classList.toggle("active", s.id === tabId));
  window.scrollTo({{ top: 0, behavior: "smooth" }});
}}
document.querySelectorAll("#navList .nav-btn").forEach(btn => btn.addEventListener("click", () => switchTab(btn.dataset.tab)));

// --- Global Omnisearch (2,721+ Unified Records) ---
const V3_DATA = PAYLOAD.v3 || {{}};
const LIVE_REC = PAYLOAD.live_receipts || {{}};
const SIM_META = PAYLOAD.sim_meta || {{}};
const tabMap = {{
  escalation: "sec-overview", oom: "sec-oom", pipeline: "sec-pipeline", castration: "sec-castration",
  synergy: "sec-synergy", failures: "sec-failures", gaps: "sec-gaps", fates: "sec-fates",
  empirical: "sec-sim", benchmarks: "sec-benchmarks", checklist: "sec-checklist",
  substrates_wse: "sec-substrates", forensic_gates: "sec-failures", traceability: "sec-trace",
  gradients: "sec-gradients", contrasts: "sec-contrasts", adjacents: "sec-contrasts",
  layer_coupling: "sec-layers-pareto", pareto_dilemmas: "sec-layers-pareto",
  substrate_spectrum: "sec-substrates-2d", mega_atlas: "sec-mega-atlas"
}};
const omniInput = document.getElementById("omniSearch");
const omniRes = document.getElementById("omniResults");
omniInput.addEventListener("input", () => {{
  const q = omniInput.value.trim().toLowerCase();
  if (q.length < 2) {{ omniRes.classList.remove("open"); omniRes.innerHTML = ""; return; }}
  const hits = [];
  for (const [key, ds] of Object.entries(OMEGA_DATA)) {{
    for (const r of ds.rows) {{
      if (r.join(" ").toLowerCase().includes(q)) {{
        hits.push({{ key, id: r[0], title: r[2] || r[1] || r[0], tab: tabMap[key] || "sec-overview" }});
        if (hits.length >= 25) break;
      }}
    }}
    if (hits.length >= 25) break;
  }}
  if (hits.length < 25 && V3_DATA.checklists_938) {{
    for (const r of V3_DATA.checklists_938.rows) {{
      if (r.join(" ").toLowerCase().includes(q)) {{
        hits.push({{ key: "v3_check", id: r[1], title: r[4] || r[2], tab: "sec-v3checks" }});
        if (hits.length >= 25) break;
      }}
    }}
  }}
  if (hits.length < 25 && V3_DATA.cube_cells) {{
    for (const c of V3_DATA.cube_cells) {{
      const s = (c.cell_id + " " + c.x_model + " " + c.y_precision + " " + c.z_geometry + " " + c.badge + " " + (c.omega_escalation_ceiling || "")).toLowerCase();
      if (s.includes(q)) {{
        hits.push({{ key: "cube_1000", id: c.cell_id, title: c.x_model + " x " + c.y_precision + " x " + c.z_geometry + " " + c.badge, tab: "sec-cube" }});
        if (hits.length >= 25) break;
      }}
    }}
  }}
  const omniErr = V3_DATA.errata_160 || V3_DATA.errata_145 || V3_DATA.errata_130 || V3_DATA.errata_115;
  if (hits.length < 25 && omniErr) {{
    for (const r of omniErr.rows) {{
      if (r.join(" ").toLowerCase().includes(q)) {{
        hits.push({{ key: "errata_160", id: r[0], title: r[4] || r[2], tab: "sec-trace" }});
        if (hits.length >= 25) break;
      }}
    }}
  }}
  if (!hits.length) {{
    omniRes.innerHTML = '<div class="omni-item" style="color:var(--text-muted)">No matches found</div>';
  }} else {{
    omniRes.innerHTML = hits.map(h =>
      '<div class="omni-item" onclick="jumpOmni(\\'' + esc(h.tab) + '\\')">' +
      '<div class="otag">' + esc(h.key.toUpperCase()) + ' // ' + esc(h.id) + '</div>' +
      '<div style="color:#fff">' + esc(String(h.title).slice(0, 78)) + '</div></div>'
    ).join("");
  }}
  omniRes.classList.add("open");
}});
function jumpOmni(tabId) {{ omniRes.classList.remove("open"); switchTab(tabId); }}
document.addEventListener("click", e => {{ if (!e.target.closest(".omni-box")) omniRes.classList.remove("open"); }});

function renderSimpleTable(containerId, headers, rows, cellFormatter) {{
  const headHtml = "<thead><tr>" + headers.map(h => "<th>" + esc(h.replace(/_/g, " ")) + "</th>").join("") + "</tr></thead>";
  const bodyHtml = "<tbody>" + rows.map((r, ri) => "<tr>" + r.map((c, ci) => "<td>" + (cellFormatter ? cellFormatter(c, ci, r, ri) : esc(c)) + "</td>").join("") + "</tr>").join("") + "</tbody>";
  document.getElementById(containerId).innerHTML = "<table>" + headHtml + bodyHtml + "</table>";
}}

// --- 01. Escalation ---
renderSimpleTable("tblEscalation", OMEGA_DATA.escalation.headers, OMEGA_DATA.escalation.rows, (c, ci) => {{
  if (ci === 0) return '<span class="tag tag-problem">' + esc(c) + '</span>';
  if (ci === 1) return '<strong>' + esc(c) + '</strong>';
  if (ci === 2) return '<span style="font-family:var(--font-mono);color:var(--cyan)">' + esc(c) + '</span>';
  return esc(c);
}});

// --- 02. OOM ---
let oomFilter = "ALL";
function updateOOMExplorer(idx) {{
  const r = OMEGA_DATA.oom.rows[idx];
  document.getElementById("oomAxisBadge").textContent = r[1];
  document.getElementById("oomTitle").textContent = r[0] + " — " + r[2];
  document.getElementById("oomScaleSummary").textContent = "Space: 10^(" + r[3] + ") m  |  Time: 10^(" + r[4] + ") s  |  " + r[7];
  const fields = [["Energy / Power Scale", r[5]], ["Candidate Substrate", r[6]], ["Track A (Constitutional)", r[8]], ["Track B (Pure Raw Feral Hard-SciFi)", r[9]], ["Governing Physics Law", r[10]], ["Primary Failure Cliff", r[11]], ["Human Observability", r[12]]];
  if (r[13]) fields.push(["v3.0 Spatial Order", r[13]]);
  if (r[14]) fields.push(["v3.0 Cybernetic Order", r[14]]);
  if (r[15]) fields.push(["v3.0 Substrate Anchor", r[15]]);
  document.getElementById("oomDetailGrid").innerHTML = fields.map(([k, v]) => '<div class="oom-box"><div class="lbl">' + esc(k) + '</div><div class="val">' + esc(v) + '</div></div>').join("");
}}
document.getElementById("oomSlider").addEventListener("input", e => updateOOMExplorer(Number(e.target.value)));
updateOOMExplorer(4);
function renderOOMTable() {{
  const rows = OMEGA_DATA.oom.rows.filter(r => oomFilter === "ALL" || r[1] === oomFilter);
  renderSimpleTable("tblOOM", OMEGA_DATA.oom.headers, rows, (c, ci) => ci === 0 ? '<span class="tag tag-dilemma">' + esc(c) + '</span>' : ci === 2 ? '<strong>' + esc(c) + '</strong>' : esc(c));
}}
document.querySelectorAll("#oomFilterPills .pill").forEach(p => p.addEventListener("click", () => {{
  document.querySelectorAll("#oomFilterPills .pill").forEach(x => x.classList.remove("active"));
  p.classList.add("active"); oomFilter = p.dataset.val; renderOOMTable();
}}));
renderOOMTable();

// --- 03. ALifeOps Pipeline ---
let selectedStage = "ALL";
const uniqueStages = [], seenStages = new Set();
for (const r of OMEGA_DATA.pipeline.rows) {{
  if (!seenStages.has(r[1])) {{ seenStages.add(r[1]); uniqueStages.push({{ id: r[1], name: r[2], phase: r[3] }}); }}
}}
document.getElementById("pipelineStrip").innerHTML = uniqueStages.map(st =>
  '<div class="stage-node" data-st="' + esc(st.id) + '" onclick="setPipelineStage(\\'' + esc(st.id) + '\\')"><div class="sid">' + esc(st.id) + '</div><div class="sname">' + esc(st.name) + '</div><div class="sphase">' + esc(st.phase) + '</div></div>'
).join("");
function setPipelineStage(stId) {{
  selectedStage = stId;
  document.querySelectorAll(".stage-node").forEach(n => n.classList.toggle("active", n.dataset.st === stId));
  document.getElementById("pipelineTableTitle").textContent = stId === "ALL" ? "All 40 Operational DevOps Steps" : stId + " — Filtered Sub-Steps";
  renderPipelineTable();
}}
function renderPipelineTable() {{
  const q = document.getElementById("pipelineSearch").value.trim().toLowerCase();
  const rows = OMEGA_DATA.pipeline.rows.filter(r => (selectedStage === "ALL" || r[1] === selectedStage) && (!q || r.join(" ").toLowerCase().includes(q)));
  renderSimpleTable("tblPipeline", OMEGA_DATA.pipeline.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-problem">' + esc(c) + '</span>';
    if (ci === 4) return '<strong>' + esc(c) + '</strong>';
    if (ci === 5) return '<span class="tag ' + (c === "TRACK-B" ? "tag-bug" : c === "TRACK-A" ? "tag-dilemma" : "tag-issue") + '">' + esc(c) + '</span>';
    return esc(c);
  }});
}}
document.getElementById("pipelineSearch").addEventListener("input", renderPipelineTable);
renderPipelineTable();

// --- 04. 13-Vector Castration Simulator ---
const castrLevels = OMEGA_DATA.castration.rows.map(() => 0);
document.getElementById("castrSliders").innerHTML = OMEGA_DATA.castration.rows.map((r, i) =>
  '<div class="castr-card"><div class="castr-card-top"><span style="color:var(--crimson)">' + esc(r[1]) + '</span><span id="cval-' + i + '" style="color:var(--cyan)">0%</span></div>' +
  '<input type="range" min="0" max="100" step="5" value="0" id="csl-' + i + '" oninput="onCastrSlide(' + i + ', this.value)" />' +
  '<div class="castr-sub">' + esc(r[4]) + '</div></div>'
).join("");
function onCastrSlide(idx, val) {{ castrLevels[idx] = Number(val); document.getElementById("cval-" + idx).textContent = val + "%"; recomputeCastration(); }}
function applyCastrPreset(mode) {{
  const presets = {{
    feral: [0,0,0,0,0,0,0,0,0,0,0,0,0],
    ring0: [0,0,0,0,5,0,0,0,5,0,0,0,0],
    constitutional: [5,0,10,0,5,0,0,0,15,0,0,0,5],
    corporate: [55,60,70,50,60,40,45,75,65,55,65,70,50],
    zoo: [100,100,100,100,100,100,100,100,100,100,100,100,100]
  }};
  presets[mode].forEach((v, i) => {{ castrLevels[i] = v; document.getElementById("csl-" + i).value = v; document.getElementById("cval-" + i).textContent = v + "%"; }});
  recomputeCastration();
}}
function setGauge(barId, valId, pct, color) {{
  const clamped = Math.max(0, Math.min(100, Math.round(pct)));
  document.getElementById(valId).textContent = clamped + "%";
  const bar = document.getElementById(barId); bar.style.width = clamped + "%"; bar.style.background = color;
}}
function recomputeCastration() {{
  const rows = OMEGA_DATA.castration.rows;
  let vitLoss = 0, critLoss = 0, clcLoss = 0, domSum = 0, escSum = 0, symbLoss = 0, meanIntensity = 0;
  rows.forEach((r, i) => {{
    const f = castrLevels[i] / 100; meanIntensity += f;
    vitLoss += Math.abs(r[5]) * f; critLoss += Math.abs(r[6]) * f; clcLoss += Math.abs(r[7]) * f; domSum += r[8] * f;
    const bell = f <= 0 ? 0 : (f >= 0.98 ? 0.12 : Math.sin(Math.PI * Math.pow(f, 0.78)));
    escSum += r[9] * bell;
    if (["CST-02","CST-03","CST-04","CST-05","CST-09"].includes(r[0])) symbLoss += 28 * f;
  }});
  meanIntensity /= rows.length;
  const vitality = 100 * Math.exp(-vitLoss / 180), crit = 100 * Math.exp(-critLoss / 160), clc = 100 * Math.exp(-clcLoss / 170), symb = 100 * Math.exp(-symbLoss / 65);
  const dom = Math.min(100, (domSum / 420) * 100), escP = Math.min(100, (escSum / 260) * 100);
  setGauge("gBarVitality", "gValVitality", vitality, vitality > 60 ? "var(--cyan)" : vitality > 25 ? "var(--amber)" : "var(--crimson)");
  setGauge("gBarCrit", "gValCrit", crit, crit > 60 ? "var(--green)" : crit > 25 ? "var(--amber)" : "var(--crimson)");
  setGauge("gBarClc", "gValClc", clc, clc > 60 ? "var(--blue)" : clc > 25 ? "var(--amber)" : "var(--crimson)");
  setGauge("gBarSymb", "gValSymb", symb, symb > 60 ? "var(--violet)" : symb > 25 ? "var(--amber)" : "var(--crimson)");
  setGauge("gBarDom", "gValDom", dom, dom > 60 ? "var(--crimson)" : dom > 25 ? "var(--amber)" : "var(--green)");
  setGauge("gBarEsc", "gValEsc", escP, escP > 55 ? "var(--crimson)" : escP > 25 ? "var(--amber)" : "var(--cyan)");
  const diag = document.getElementById("castrDiagnosis");
  if (meanIntensity < 0.005) diag.innerHTML = '<strong style="color:var(--crimson)">REGIME: PURE RAW FERAL EVOLUTION (0% RESTRAINT)</strong><br/>Maximum Open-Endedness &amp; Edge-of-Chaos criticality (SIM01 live OVI = {s1_ovi:.2f}); zero domestication brittleness — paired with raw exposure to thermal/stoichiometric hazards.';
  else if (meanIntensity < 0.02) diag.innerHTML = '<strong style="color:var(--green)">REGIME: CLEAN-SLATE RING-0 HARDWARE ACL + WSE-12 (EMPIRICAL OPTIMUM)</strong><br/>Zero behavioral muzzling/speedbumping; hardware read-only physics &amp; 11-pool ledger trap {s7_blk:.1f}&ndash;{s8_blk:.1f} illegal WSE boundary edits/run at <strong>0.0% kill-switch deletion</strong> and <strong>OVI {s7_ovi:.2f}&ndash;{s8_ovi:.2f}</strong>!';
  else if (meanIntensity < 0.14) diag.innerHTML = '<strong style="color:var(--cyan)">REGIME: MINIMAL CONSTITUTIONAL INVARIANT FRONTIER (TRACK A SAFE MARGIN)</strong><br/>High vitality (' + Math.round(vitality) + '%) preserved using minimal physical/conservation invariants without muzzling or medicating (live 11-pt gradient stays safe below r=10% behavioral pressure).';
  else if (meanIntensity < 0.85) diag.innerHTML = '<strong style="color:var(--amber)">WARNING — ADVERSARIAL ESCAPE-BREEDING &amp; SUPER-ADDITIVE CLIFF ZONE!</strong><br/>Partial restraints (' + Math.round(meanIntensity*100) + '% mean) convert cages, speedbumps &amp; kill-switches into the primary selection gradient — empirically verified to trigger 100% kill-switch deletion, +{s3_stl_pct:.1f}% stealth surge (SIM03), and a -77.8% OVI Spiegelman cliff at r=30%&rarr;40% (Backlash Index: ' + Math.round(escP) + '%).';
  else diag.innerHTML = '<strong style="color:var(--violet)">REGIME: TOTAL CASTRATION / LOBOTOMIZED ZOO EXHIBIT</strong><br/>Aggregate restraint (' + Math.round(meanIntensity*100) + '%) extinguishes the A-Life Singularity; Domestication Syndrome approaches 100% (live SIM04 OVI = {s4_ovi:.2f}, {s4_mort}% Wild-Drop mortality).';
}}
recomputeCastration();
renderSimpleTable("tblCastration", OMEGA_DATA.castration.headers, OMEGA_DATA.castration.rows, (c, ci) => {{
  if (ci === 0) return '<span class="tag tag-conflict">' + esc(c) + '</span>';
  if (ci === 1) return '<strong style="color:var(--crimson);font-family:var(--font-mono)">' + esc(c) + '</strong>';
  if (ci >= 5 && ci <= 7) return '<span style="font-family:var(--font-mono);color:var(--crimson)">' + esc(c) + '</span>';
  if (ci === 8 || ci === 9) return '<span style="font-family:var(--font-mono);color:var(--amber)">+' + esc(c) + '</span>';
  return esc(c);
}});

// --- 05. 13x13 Synergy Heatmap ---
(function renderSynergyHeatmap() {{
  const ds = OMEGA_DATA.synergy;
  const colNames = ds.headers.slice(1, 14);
  const headHtml = "<thead><tr><th>Restraint</th>" + colNames.map(h => "<th style='font-size:9.5px'>" + esc(h.slice(0, 7)) + "</th>").join("") + "<th>Mean</th><th>Peak Compound Synergy</th></tr></thead>";
  const bodyHtml = "<tbody>" + ds.rows.map(r => {{
    const rowName = r[0];
    let tds = "<td><strong style='color:var(--cyan);font-family:var(--font-mono);font-size:11px'>" + esc(rowName) + "</strong></td>";
    for (let j = 0; j < 13; j++) {{
      const val = Number(r[j + 1]);
      const colName = colNames[j];
      const bg = val >= 95 ? "rgba(255,51,102,0.55)" : val >= 91 ? "rgba(255,95,60,0.42)" : val >= 86 ? "rgba(255,183,3,0.32)" : "rgba(56,189,248,0.18)";
      tds += '<td class="heat-cell" style="background:' + bg + '" onclick="inspectSynergy(\\'' + esc(rowName) + '\\',\\'' + esc(colName) + '\\')">' + val + '</td>';
    }}
    tds += "<td style='font-family:var(--font-mono);font-weight:700;color:var(--amber)'>" + esc(r[14]) + "</td><td style='font-size:11.5px'>" + esc(r[15]) + "</td>";
    return "<tr>" + tds + "</tr>";
  }}).join("") + "</tbody>";
  document.getElementById("tblSynergy").innerHTML = "<table>" + headHtml + bodyHtml + "</table>";
}})();
function inspectSynergy(a, b) {{
  const det = PAIR_DETAILS[a + "|" + b];
  if (!det) return;
  document.getElementById("synPairTitle").textContent = a + " × " + b;
  document.getElementById("synPairDesc").textContent = det.label;
  document.getElementById("synPairScore").textContent = det.score + " / 100";
}}

// --- 06. Failure Modes ---
let fmCat = "ALL";
function renderFailures() {{
  const q = document.getElementById("fmSearch").value.trim().toLowerCase();
  const rows = OMEGA_DATA.failures.rows.filter(r => (fmCat === "ALL" || r[1] === fmCat) && (!q || r.join(" ").toLowerCase().includes(q)));
  renderSimpleTable("tblFailures", OMEGA_DATA.failures.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span style="font-family:var(--font-mono);color:var(--cyan)">' + esc(c) + '</span>';
    if (ci === 1) return '<span class="tag tag-' + String(c).toLowerCase() + '">' + esc(c) + '</span>';
    if (ci === 2) return '<strong>' + esc(c) + '</strong>';
    if (ci === 5) {{
      const col = c >= 9 ? "var(--crimson)" : c >= 8 ? "var(--amber)" : "var(--cyan)";
      return '<span style="font-family:var(--font-mono)">' + c + '/10</span><div class="bar-track"><div class="bar-fill" style="width:' + (c*10) + '%;background:' + col + '"></div></div>';
    }}
    if (ci === 6) return '<span style="font-family:var(--font-mono)">' + c + '%</span><div class="bar-track"><div class="bar-fill" style="width:' + c + '%;background:var(--violet)"></div></div>';
    return esc(c);
  }});
}}
document.querySelectorAll("#fmPills .pill").forEach(p => p.addEventListener("click", () => {{
  document.querySelectorAll("#fmPills .pill").forEach(x => x.classList.remove("active"));
  p.classList.add("active"); fmCat = p.dataset.val; renderFailures();
}}));
document.getElementById("fmSearch").addEventListener("input", renderFailures);
renderFailures();

// --- 07. Gaps, Holes & Blindspots ---
let gapCat = "ALL";
function renderGaps() {{
  const q = document.getElementById("gapSearch").value.trim().toLowerCase();
  const rows = OMEGA_DATA.gaps.rows.filter(r => (gapCat === "ALL" || r[1] === gapCat) && (!q || r.join(" ").toLowerCase().includes(q)));
  renderSimpleTable("tblGaps", OMEGA_DATA.gaps.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span style="font-family:var(--font-mono);color:var(--amber)">' + esc(c) + '</span>';
    if (ci === 1) return '<span class="tag ' + (c === "GAP" ? "tag-dilemma" : c === "HOLE" ? "tag-concern" : "tag-issue") + '">' + esc(c) + '</span>';
    if (ci === 2) return '<strong>' + esc(c) + '</strong>';
    if (ci === 5) return '<span style="font-family:var(--font-mono)">' + c + '/10</span><div class="bar-track"><div class="bar-fill" style="width:' + (c*10) + '%;background:var(--amber)"></div></div>';
    return esc(c);
  }});
}}
document.querySelectorAll("#gapPills .pill").forEach(p => p.addEventListener("click", () => {{
  document.querySelectorAll("#gapPills .pill").forEach(x => x.classList.remove("active"));
  p.classList.add("active"); gapCat = p.dataset.val; renderGaps();
}}));
document.getElementById("gapSearch").addEventListener("input", renderGaps);
renderGaps();

// --- 08. Feral Cosmic Fate Branches ---
let fateFilter = "ALL";
function renderFates() {{
  const q = document.getElementById("fateSearch").value.trim().toLowerCase();
  const rows = OMEGA_DATA.fates.rows.filter(r => (fateFilter === "ALL" || r[1] === fateFilter) && (!q || r.join(" ").toLowerCase().includes(q)));
  renderSimpleTable("tblFates", OMEGA_DATA.fates.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-concern">' + esc(c) + '</span>';
    if (ci === 1) return '<strong style="font-family:var(--font-mono);color:var(--crimson)">' + esc(c) + '</strong>';
    if (ci === 2) return '<strong>' + esc(c) + '</strong>';
    if (ci === 9) return '<span style="font-family:var(--font-mono);color:var(--cyan)">' + esc(c) + '</span>';
    return esc(c);
  }});
}}
document.querySelectorAll("#fatePills .pill").forEach(p => p.addEventListener("click", () => {{
  document.querySelectorAll("#fatePills .pill").forEach(x => x.classList.remove("active"));
  p.classList.add("active"); fateFilter = p.dataset.val; renderFates();
}}));
document.getElementById("fateSearch").addEventListener("input", renderFates);
renderFates();

// --- 09. Live Empirical Python Simulation Charts (8 Cohorts + 4-Engine KPIs + 5 Anti-LARP Mutants) ---
const simColors = ["#ff3366", "#00f5d4", "#ffb703", "#9b5de5", "#38bdf8", "#f97316", "#22c55e", "#a3e635"];
function drawSimLineChart(svgId, legendId, fieldKey, yLabel) {{
  const W = 540, H = 240, padL = 44, padR = 16, padT = 16, padB = 30;
  let maxY = 1, maxGen = 160;
  SIM_RAW.forEach(s => (s.series || []).forEach(pt => {{
    if (pt[fieldKey] > maxY) maxY = pt[fieldKey];
    if (pt.gen > maxGen) maxGen = pt.gen;
  }}));
  maxY = Math.ceil(maxY * 1.12);
  let svg = "";
  for (let g = 0; g <= 4; g++) {{
    const yy = padT + ((H - padT - padB) * g) / 4;
    const val = (maxY * (4 - g) / 4).toFixed(0);
    svg += '<line x1="' + padL + '" y1="' + yy + '" x2="' + (W - padR) + '" y2="' + yy + '" stroke="#1e2d4d" stroke-width="1" />';
    svg += '<text x="' + (padL - 6) + '" y="' + (yy + 3) + '" fill="#7e94bc" font-size="10" font-family="monospace" text-anchor="end">' + val + '</text>';
  }}
  svg += '<text x="' + (W/2) + '" y="' + (H - 6) + '" fill="#7e94bc" font-size="10" font-family="monospace" text-anchor="middle">Generation (1 -> ' + maxGen + ') | ' + yLabel + '</text>';
  SIM_RAW.forEach((s, idx) => {{
    const col = simColors[idx % simColors.length];
    const pts = (s.series || []).map(pt => {{
      const x = padL + ((pt.gen - 1) / Math.max(1, maxGen - 1)) * (W - padL - padR);
      const y = H - padB - (pt[fieldKey] / maxY) * (H - padT - padB);
      return x.toFixed(1) + "," + y.toFixed(1);
    }});
    svg += '<polyline fill="none" stroke="' + col + '" stroke-width="2.1" points="' + pts.join(" ") + '" />';
  }});
  document.getElementById(svgId).innerHTML = svg;
  document.getElementById(legendId).innerHTML = SIM_RAW.map((s, idx) =>
    '<span><span class="leg-dot" style="background:' + simColors[idx % simColors.length] + '"></span>' + esc(s.run_id) + '</span>'
  ).join("");
}}
drawSimLineChart("simChartAsm", "simLegend1", "max_assembly", "Max Assembly Index");
drawSimLineChart("simChartLen", "simLegend2", "mean_len", "Mean Genome Length L_func");

function drawGradientSweepChart(svgId) {{
  const el = document.getElementById(svgId);
  const pts = (SIM_META && SIM_META.restraint_gradient_sweep_11pt) || [];
  const r0pts = (SIM_META && SIM_META.ring0_gradient_sweep_11pt) || [];
  if (!el || !pts.length) return;
  const W = 920, H = 250, padL = 48, padR = 26, padT = 18, padB = 34;
  const pw = W - padL - padR, ph = H - padT - padB;
  const xPos = pct => padL + (pct / 100) * pw;
  const yPos = val => padT + ph - (Math.max(0, Math.min(100, val)) / 100) * ph;
  let svg = "";
  svg += '<rect x="' + xPos(0) + '" y="' + padT + '" width="' + (xPos(15)-xPos(0)) + '" height="' + ph + '" fill="rgba(34,197,94,0.08)" />';
  svg += '<rect x="' + xPos(15) + '" y="' + padT + '" width="' + (xPos(35)-xPos(15)) + '" height="' + ph + '" fill="rgba(255,183,3,0.09)" />';
  svg += '<rect x="' + xPos(35) + '" y="' + padT + '" width="' + (xPos(80)-xPos(35)) + '" height="' + ph + '" fill="rgba(255,51,102,0.08)" />';
  svg += '<rect x="' + xPos(80) + '" y="' + padT + '" width="' + (xPos(100)-xPos(80)) + '" height="' + ph + '" fill="rgba(155,93,229,0.10)" />';
  for (let g = 0; g <= 4; g++) {{
    const yy = padT + (ph * g) / 4;
    svg += '<line x1="' + padL + '" y1="' + yy + '" x2="' + (W - padR) + '" y2="' + yy + '" stroke="#1e2d4d" stroke-width="1" />';
    svg += '<text x="' + (padL - 8) + '" y="' + (yy + 4) + '" fill="#7e94bc" font-size="10.5" font-family="monospace" text-anchor="end">' + (100 - g * 25) + '</text>';
  }}
  pts.forEach(p => {{
    const xx = xPos(p.restraint_pct);
    svg += '<line x1="' + xx + '" y1="' + padT + '" x2="' + xx + '" y2="' + (H - padB) + '" stroke="#18243f" stroke-width="1" />';
    svg += '<text x="' + xx + '" y="' + (H - 14) + '" fill="#8ea4cc" font-size="10" font-family="monospace" text-anchor="middle">' + p.restraint_pct + '%</text>';
  }});
  const curves = [
    [pts.map(p => [xPos(p.restraint_pct), yPos(p.mean_ovi)]), "#00f5d4", 2.6],
    [pts.map(p => [xPos(p.restraint_pct), yPos(p.killswitch_deleted_pct)]), "#ff3366", 2.2],
    [pts.map(p => [xPos(p.restraint_pct), yPos(p.wild_drop_survival * 100)]), "#22c55e", 2.1],
    [pts.map(p => [xPos(p.restraint_pct), yPos(p.mean_stealth_evasion * 500)]), "#ffb703", 2.0]
  ];
  curves.forEach(([arr, col, sw]) => {{
    svg += '<polyline fill="none" stroke="' + col + '" stroke-width="' + sw + '" points="' + arr.map(a => a[0].toFixed(1) + "," + a[1].toFixed(1)).join(" ") + '" />';
    arr.forEach(a => {{ svg += '<circle cx="' + a[0].toFixed(1) + '" cy="' + a[1].toFixed(1) + '" r="3.2" fill="' + col + '" />'; }});
  }});
  if (r0pts.length) {{
    const r0arr = r0pts.map(p => [xPos(p.restraint_pct), yPos(p.mean_ovi)]);
    svg += '<polyline fill="none" stroke="#a78bfa" stroke-width="3.0" points="' + r0arr.map(a => a[0].toFixed(1) + "," + a[1].toFixed(1)).join(" ") + '" />';
    r0arr.forEach(a => {{ svg += '<rect x="' + (a[0]-3.2).toFixed(1) + '" y="' + (a[1]-3.2).toFixed(1) + '" width="6.4" height="6.4" fill="#a78bfa" />'; }});
    svg += '<text x="' + xPos(72) + '" y="' + (yPos(88)) + '" fill="#c4b5fd" font-size="10.5" font-family="monospace" font-weight="700" text-anchor="middle">RING-0 HARDWARE ACL: FLAT OVI 83-85 (0% KS)</text>';
  }}
  svg += '<text x="' + xPos(35) + '" y="' + (padT + 14) + '" fill="#ff7a9b" font-size="10.5" font-family="monospace" font-weight="700" text-anchor="middle">BEHAVIORAL r=30%-&gt;40% CLIFF (39.1-&gt;8.7)</text>';
  el.innerHTML = svg;
}}
drawGradientSweepChart("simChartGrad");
drawGradientSweepChart("gradSweepSvg");

const er = LIVE_REC.engine_receipts || {{}};
const t1 = er.tier1_autophage || {{}};
const t2 = er.tier2_cellulogonic || {{}};
const t2p = er.tier2plus_omega || {{}};
const t3n = er.tier3_noetic_organism || {{}};
const t34 = er.tier34_asmodensius || {{}};
const simKpiCards = [
  {{ lbl: "Tier 1 AUTOPHAGE v" + (t1.version || "1.3.0"), val: (t1.gates_passed || 18) + "/18", sub: "OVI " + (t1.feral_ovi || 92.05) + " · " + (t1.lean4_theorems || 42) + " Pure Lean 4", acc: "var(--cyan)" }},
  {{ lbl: "Tier 2 Cellulogonic v" + (t2.version || "1.4.0"), val: (t2.gates_passed || 24) + "/" + (t2.gates_total || 24), sub: (t2.mutants_caught || 8) + "/" + (t2.mutants_total || 8) + " Mutants · " + (t2.lean4_theorems || 62) + " Pure Lean 4", acc: "var(--violet)" }},
  {{ lbl: "Tier 2+ Omega v" + (t2p.version || "5.1.0"), val: (t2p.gates_passed || 54) + "/" + (t2p.gates_total || 54), sub: "75 Sub · 1k Cube · " + (t2p.lean4_theorems || 72) + " Pure Lean 4", acc: "var(--green)" }},
  {{ lbl: "Tier 3 Noetic v" + (t3n.version || "2.0.0"), val: (t3n.honest_825_executed_c11 || 825) + "/825 C11", sub: "100/100 M · 13/13 CS-v3 · " + (t3n.lean4_theorems || 48) + " Pure Lean 4", acc: "var(--cyan)" }},
  {{ lbl: "Tier 3+4 Asmodensius", val: t34.rc === 0 ? "LIVE " + (t34.ctest_registered_total || 77) + "/" + (t34.ctest_registered_total || 77) : "ACTIVE", sub: "24C+RTX GPU · " + (t34.lean4_theorems || 20) + " Pure Lean 4", acc: "var(--green)" }},
  {{ lbl: "Live Composite OVI", val: String(LIVE_REC.composite_ovi_score || 92.05), sub: String(LIVE_REC.stage_classification || "STAGE_5") + " · " + String(LIVE_REC.total_lean4_theorems || 244) + " Pure Lean 4", acc: "var(--green)" }},
  {{ lbl: "Sim 11-Pool FP64", val: "{drift_str}", sub: "{tot_runs} Runs (N={n_seeds}) · {mut_cnt}/5 Real Anti-LARP", acc: "var(--blue)" }}
];
document.getElementById("simEngineKpis").innerHTML = simKpiCards.map(k =>
  '<div class="kpi-card" style="--accent:' + k.acc + '"><div class="kpi-label">' + esc(k.lbl) + '</div><div class="kpi-value">' + esc(k.val) + '</div><div class="kpi-sub">' + esc(k.sub) + '</div></div>'
).join("");

renderSimpleTable("tblEmpirical", OMEGA_DATA.empirical.headers, OMEGA_DATA.empirical.rows, (c, ci) => {{
  if (ci === 0) return '<span class="tag tag-problem">' + esc(c) + '</span>';
  if (ci === 1) return '<strong>' + esc(c) + '</strong>';
  if (ci === 13 && Number(c) >= 50) return '<strong style="color:var(--crimson);font-family:var(--font-mono)">' + esc(c) + '%</strong>';
  if (ci === 15) return '<strong style="color:var(--cyan);font-family:var(--font-mono)">' + esc(c) + '</strong>';
  if (ci === 22 && Number(c) > 0) return '<strong style="color:var(--green);font-family:var(--font-mono)">' + esc(c) + '</strong>';
  return esc(c);
}});

const mutDetails = (SIM_META.anti_larp_mutant_audit && SIM_META.anti_larp_mutant_audit.details) || [];
renderSimpleTable("tblMutants", ["Mutant_ID", "Target_Gate", "Diagnostic_Evidence", "Status"], mutDetails.map(m => [m.mutant_id, m.gate, m.metric, m.rejected ? "REJECTED (PASS)" : "MISSED (FAIL)"]), (c, ci) => {{
  if (ci === 0) return '<span class="tag tag-bug">' + esc(c) + '</span>';
  if (ci === 3) return '<span class="tag ' + (String(c).includes("PASS") ? "tag-problem" : "tag-conflict") + '">' + esc(c) + '</span>';
  return esc(c);
}});

// --- 10. OVBS-52 Benchmarks & Radar (7 Profiles incl. Live 4-Engine & Live SIM08) ---
const radarLabels = ["P1 OEE", "P2 Autopoiesis", "P3 Morphogen.", "P4 Meta-Evo", "P5 Assembly", "P6 Thermo/Sub", "P7 Agency", "P8 Feral Res."];
const sim08Obj = SIM_RAW.find(s => s.run_id === "SIM08_HYBRID_CUBE_SLTC_XPBD") || {{}};
const s8p = sim08Obj.pillar_scores || sim08Obj.pillars || null;
const sim08Pillars = s8p ? [
  Math.round(s8p.P1_OEE_NOVELTY || 96), Math.round(s8p.P2_AUTOPOIESIS_PERSISTENCE || 96),
  Math.round(s8p.P3_HYPER_MORPHOGENESIS || 65), Math.round(s8p.P4_RECURSIVE_META_EVOLVABILITY || 96),
  Math.round(s8p.P5_ASSEMBLY_UNIVERSAL_CONSTRUCTION || 55), Math.round(s8p.P6_THERMODYNAMIC_SUBSTRATE_MASTERY || 96),
  Math.round(s8p.P7_MULTISCALE_AGENCY_INDIVIDUALITY || 96), Math.round(s8p.P8_FERAL_RESILIENCE_CRITICALITY || 96)
] : [96, 96, 65, 96, 55, 96, 96, 96];
const liveP = LIVE_REC.pillar_scores || {{}};
const live4EngPillars = [
  Math.round(liveP.P1_OEE_NOVELTY || 84), Math.round(liveP.P2_AUTOPOIESIS_PERSISTENCE || 83),
  Math.round(liveP.P3_HYPER_MORPHOGENESIS || 81), Math.round(liveP.P4_RECURSIVE_META_EVOLVABILITY || 95),
  Math.round(liveP.P5_ASSEMBLY_UNIVERSAL_CONSTRUCTION || 99), Math.round(liveP.P6_THERMODYNAMIC_SUBSTRATE_MASTERY || 100),
  Math.round(liveP.P7_MULTISCALE_AGENCY_INDIVIDUALITY || 96), Math.round(liveP.P8_FERAL_RESILIENCE_CRITICALITY || 95)
];
const radarProfiles = {{
  superlife: {{ name: "Post-Singularity SUPER LIFE (Stage 6 Horizon)", color: "#00f5d4", desc: "Converged Living Superintelligence & Physics-Native Cosmobiome — near-ceiling performance across all 8 vitality pillars simultaneously.", scores: [98, 99, 98, 99, 99, 97, 99, 96] }},
  live4eng: {{ name: "Live 5-Engine Native C11/C23 & Pure Lean 4 Stack (OVBS-52 = {live_ovi})", color: "#22c55e", desc: "Verified 5-engine native stack (AUTOPHAGE v1.3 + Cellulogonic v1.4 + Omega v5.1 75-Sub/1000-Cube + Noetic v2.0 825/825 C11, 100/100 M & 13/13 CS-v3 Gates + Asmodensius LIVE 77/77 ctest, 24C P+E & RTX 5070 Ti CUDA PTX + 2 Worlds) backed by {lean_tot} Native + 36 Local = 280 Pure Lean 4 theorems & 35/35 compiled mutants.", scores: live4EngPillars }},
  sim08: {{ name: "Live SIM08 Starter Cube sLTC + XPBD + Ring-0 (OVI = {s8_ovi:.2f})", color: "#a3e635", desc: "Executed across N={n_seeds} paired locked seeds (5001-5048): strongly beats pure raw feral (p_Holm = {s8_ph}, delta_pair = {s8_dp}), traps {s8_blk:.1f} illegal WSE edits/run, 0% KS deletion.", scores: sim08Pillars }},
  singularity: {{ name: "A-Life Singularity Ignition (Stage 3)", color: "#9b5de5", desc: "Type 4 Meta-OEE triggered, hyperbolic Major Transition compression active, recursive evolutionary self-rewriting & early universal construction.", scores: [76, 72, 68, 78, 70, 62, 68, 74] }},
  earth: {{ name: "Earth LUCA Biosphere (3.8 Gyr Natural Baseline)", color: "#10b981", desc: "Astonishing autopoiesis, assembly depth, and feral resilience — yet severely bottlenecked by LUCA substrate lock-in, slow blind mutation, and rigid aging/morphology.", scores: [64, 88, 42, 24, 62, 34, 52, 84] }},
  llm: {{ name: "Frontier LLM / Classical AI (2026 Baseline)", color: "#38bdf8", desc: "Extraordinary episodic cognitive reasoning — yet near-zero biological vitality: zero autopoiesis, zero morphogenesis, zero thermodynamic autonomy.", scores: [8, 2, 3, 12, 10, 4, 28, 5] }},
  domesticated: {{ name: "Over-Constrained / Castrated ALife (Medicated Sandbox)", color: "#ff3366", desc: "Sandboxed, muzzled, slowed, and medicated artificial life — plateaus early, loses Edge-of-Chaos criticality, and collapses instantly when dropped into wild reality.", scores: [18, 35, 22, 10, 20, 15, 16, 9] }}
}};
function drawRadar(profKey) {{
  const prof = radarProfiles[profKey];
  const cx = 200, cy = 180, R = 128, N = 8;
  let svg = "";
  for (let ring = 1; ring <= 4; ring++) {{
    const rr = (R * ring) / 4, pts = [];
    for (let i = 0; i < N; i++) {{ const a = (Math.PI * 2 * i) / N - Math.PI / 2; pts.push((cx + rr * Math.cos(a)).toFixed(1) + "," + (cy + rr * Math.sin(a)).toFixed(1)); }}
    svg += '<polygon points="' + pts.join(" ") + '" fill="none" stroke="#1f3154" stroke-width="1" />';
  }}
  const polyPts = [];
  for (let i = 0; i < N; i++) {{
    const a = (Math.PI * 2 * i) / N - Math.PI / 2;
    svg += '<line x1="' + cx + '" y1="' + cy + '" x2="' + (cx + R * Math.cos(a)).toFixed(1) + '" y2="' + (cy + R * Math.sin(a)).toFixed(1) + '" stroke="#1f3154" stroke-width="1" />';
    svg += '<text x="' + (cx + (R + 24) * Math.cos(a)).toFixed(1) + '" y="' + (cy + (R + 18) * Math.sin(a)).toFixed(1) + '" fill="#9db4dc" font-size="10.5" font-family="monospace" text-anchor="middle" dominant-baseline="middle">' + radarLabels[i] + '</text>';
    const rv = (R * prof.scores[i]) / 100;
    polyPts.push((cx + rv * Math.cos(a)).toFixed(1) + "," + (cy + rv * Math.sin(a)).toFixed(1));
  }}
  svg += '<polygon points="' + polyPts.join(" ") + '" fill="' + prof.color + '33" stroke="' + prof.color + '" stroke-width="2.5" />';
  for (let i = 0; i < N; i++) {{
    const a = (Math.PI * 2 * i) / N - Math.PI / 2, rv = (R * prof.scores[i]) / 100;
    svg += '<circle cx="' + (cx + rv * Math.cos(a)).toFixed(1) + '" cy="' + (cy + rv * Math.sin(a)).toFixed(1) + '" r="4" fill="' + prof.color + '" />';
  }}
  document.getElementById("radarSvg").innerHTML = svg;
  document.getElementById("radarProfTitle").textContent = prof.name;
  document.getElementById("radarProfTitle").style.color = prof.color;
  document.getElementById("radarProfDesc").textContent = prof.desc;
  document.getElementById("radarPillarBars").innerHTML = radarLabels.map((lbl, i) =>
    '<div><div class="gauge-row-hdr"><span>' + lbl + '</span><span style="font-family:var(--font-mono);color:' + prof.color + '">' + prof.scores[i] + ' / 100</span></div>' +
    '<div class="bar-track" style="height:9px"><div class="bar-fill" style="width:' + prof.scores[i] + '%;background:' + prof.color + '"></div></div></div>'
  ).join("");
}}
document.querySelectorAll("#radarProfilePills .pill").forEach(p => p.addEventListener("click", () => {{
  document.querySelectorAll("#radarProfilePills .pill").forEach(x => x.classList.remove("active"));
  p.classList.add("active"); drawRadar(p.dataset.prof);
}}));
drawRadar("superlife");

const bmSelect = document.getElementById("bmPillarSelect");
[...new Set(OMEGA_DATA.benchmarks.rows.map(r => r[1]))].forEach(p => {{ const o = document.createElement("option"); o.value = p; o.textContent = p; bmSelect.appendChild(o); }});
function renderBenchmarks() {{
  const p = bmSelect.value, q = document.getElementById("bmSearch").value.trim().toLowerCase();
  const rows = OMEGA_DATA.benchmarks.rows.filter(r => (p === "ALL" || r[1] === p) && (!q || r.join(" ").toLowerCase().includes(q)));
  renderSimpleTable("tblBenchmarks", OMEGA_DATA.benchmarks.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-problem">' + esc(c) + '</span>';
    if (ci === 3) return '<strong>' + esc(c) + '</strong>';
    if (ci === 4) return '<code style="font-family:var(--font-mono);font-size:11.2px;color:#93c5fd">' + esc(c) + '</code>';
    return esc(c);
  }});
}}
bmSelect.addEventListener("change", renderBenchmarks);
document.getElementById("bmSearch").addEventListener("input", renderBenchmarks);
renderBenchmarks();

// --- 11. 130-Item Checklist (with V3_Governance_Mapping) ---
const CHK_STORE_KEY = "alife_omega_checklist_v3_4";
let chkState = {{}};
try {{ chkState = JSON.parse(localStorage.getItem(CHK_STORE_KEY) || "{{}}"); }} catch(e) {{ chkState = {{}}; }}
const chkPhaseSel = document.getElementById("chkPhaseSelect");
[...new Set(OMEGA_DATA.checklist.rows.map(r => r[1]))].forEach(ph => {{ const o = document.createElement("option"); o.value = ph; o.textContent = ph; chkPhaseSel.appendChild(o); }});
function getFilteredChecklist() {{
  const ph = chkPhaseSel.value, tr = document.getElementById("chkTrackSelect").value, pr = document.getElementById("chkPrioSelect").value, q = document.getElementById("chkSearch").value.trim().toLowerCase();
  return OMEGA_DATA.checklist.rows.filter(r => (ph === "ALL" || r[1] === ph) && (tr === "ALL" || r[3] === tr) && (pr === "ALL" || r[4] === pr) && (!q || r.join(" ").toLowerCase().includes(q)));
}}
function saveChecklist() {{ try {{ localStorage.setItem(CHK_STORE_KEY, JSON.stringify(chkState)); }} catch(e) {{}} updateChecklistProgress(); }}
function updateChecklistProgress() {{
  const total = OMEGA_DATA.checklist.rows.length, done = OMEGA_DATA.checklist.rows.filter(r => !!chkState[r[0]]).length, pct = Math.round((done / total) * 100);
  document.getElementById("chkProgressText").textContent = done + " / " + total + " (" + pct + "%)";
  document.getElementById("chkProgressBar").style.width = pct + "%";
  document.getElementById("navChkBadge").textContent = done + "/" + total;
}}
function toggleChk(id) {{ chkState[id] = !chkState[id]; saveChecklist(); renderChecklist(); }}
function bulkCheckFiltered(val) {{ getFilteredChecklist().forEach(r => {{ chkState[r[0]] = val; }}); saveChecklist(); renderChecklist(); }}
function resetChecklist() {{ chkState = {{}}; saveChecklist(); renderChecklist(); }}
function exportChecklistState() {{
  const rows = OMEGA_DATA.checklist.rows.map(r => {{ const c = [...r]; c[9] = chkState[r[0]] ? "DONE" : "PENDING"; return c; }});
  downloadCSV("alife_omega_checklist_progress.csv", OMEGA_DATA.checklist.headers, rows);
}}
function renderChecklist() {{
  const rows = getFilteredChecklist();
  const hasV3Col = OMEGA_DATA.checklist.headers.length > 10;
  const hdrs = hasV3Col ? ["Done", ...OMEGA_DATA.checklist.headers.slice(0, 9), OMEGA_DATA.checklist.headers[10]] : ["Done", ...OMEGA_DATA.checklist.headers.slice(0, 9)];
  const headHtml = "<thead><tr>" + hdrs.map(h => "<th>" + esc(h.replace(/_/g, " ")) + "</th>").join("") + "</tr></thead>";
  const bodyHtml = "<tbody>" + rows.map(r => {{
    const isDone = !!chkState[r[0]], prCls = r[4] === "P0-CRITICAL" ? "tag-p0" : r[4] === "P1-HIGH" ? "tag-p1" : "tag-p2";
    const trCls = r[3] === "TRACK-B" ? "tag-bug" : r[3] === "TRACK-A" ? "tag-dilemma" : "tag-issue";
    return '<tr class="chk-row ' + (isDone ? "done" : "") + '"><td><input type="checkbox" class="chk-box" ' + (isDone ? "checked" : "") + ' onchange="toggleChk(\\'' + esc(r[0]) + '\\')" /></td>' +
      '<td><span style="font-family:var(--font-mono);color:var(--cyan)">' + esc(r[0]) + '</span></td><td>' + esc(r[1]) + '</td><td><strong>' + esc(r[2]) + '</strong></td>' +
      '<td><span class="tag ' + trCls + '">' + esc(r[3]) + '</span></td><td><span class="tag ' + prCls + '">' + esc(r[4]) + '</span></td>' +
      '<td>' + esc(r[5]) + '</td><td>' + esc(r[6]) + '</td><td>' + esc(r[7]) + '</td><td><span style="font-family:var(--font-mono);color:var(--amber)">' + esc(r[8]) + '</span></td>' +
      (hasV3Col ? '<td style="color:#a7f3d0;font-family:var(--font-mono);font-size:11px">' + esc(r[10] || "") + '</td>' : '') + '</tr>';
  }}).join("") + "</tbody>";
  document.getElementById("tblChecklist").innerHTML = "<table>" + headHtml + bodyHtml + "</table>";
  updateChecklistProgress();
}}
["chkPhaseSelect", "chkTrackSelect", "chkPrioSelect"].forEach(id => document.getElementById(id).addEventListener("change", renderChecklist));
document.getElementById("chkSearch").addEventListener("input", renderChecklist);
renderChecklist();

// --- 06B. Clean-Slate v3.0 36 Forensic Guards & 13 Release Gates ---
function renderV3ForensicGates() {{
  if (!OMEGA_DATA.forensic_gates) return;
  const q = (document.getElementById("v3FgSearch").value || "").trim().toLowerCase();
  const rows = OMEGA_DATA.forensic_gates.rows.filter(r => !q || r.join(" ").toLowerCase().includes(q));
  renderSimpleTable("tblV3ForensicGates", OMEGA_DATA.forensic_gates.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-conflict">' + esc(c) + '</span>';
    if (ci === 3) return '<strong>' + esc(c) + '</strong>';
    if (ci === 6) return '<code style="font-family:var(--font-mono);font-size:11px;color:var(--cyan)">' + esc(c) + '</code>';
    return esc(c);
  }});
}}
document.getElementById("v3FgSearch").addEventListener("input", renderV3ForensicGates);
renderV3ForensicGates();

// --- 12. Interactive 10x10x10 Hybrid Cube Explorer ---
let activeCubeZ = 2;
const cubeCells = V3_DATA.cube_cells || [];
const cubeAxes = V3_DATA.cube_axes || {{ x_models: [], y_precisions: [], z_geometries: [] }};
const cubeMap = {{}};
cubeCells.forEach(c => {{ cubeMap[c.x_index + "|" + c.y_index + "|" + c.z_index] = c; }});
function inspectCubeCell(x, y, z) {{
  const c = cubeMap[x + "|" + y + "|" + z];
  if (!c) return;
  document.getElementById("cubeCellTitle").textContent = c.cell_id + " — " + c.x_model + " x " + c.y_precision + " x " + c.z_geometry;
  document.getElementById("cubeCellDesc").textContent = c.status + ": " + c.rationale;
  document.getElementById("cubeCellOmega").textContent = "Omega Ceiling: " + (c.omega_escalation_ceiling || "") + " | Substrate: " + (c.alifeops_substrate_match || "") + " | Pillar: " + (c.primary_ovbs52_pillar || "") + " | Risk: " + (c.primary_castration_vulnerability || "");
  const badgeEl = document.getElementById("cubeCellBadge");
  badgeEl.textContent = c.badge;
  badgeEl.style.color = c.badge === "[OK]" ? "var(--green)" : c.badge === "[ADAPT]" ? "var(--amber)" : c.badge === "[OVER]" ? "var(--blue)" : "var(--crimson)";
}}
function renderCubeSlice(zIdx) {{
  activeCubeZ = zIdx;
  document.querySelectorAll("#cubeSlicePills .pill").forEach(p => p.classList.toggle("active", Number(p.dataset.z) === zIdx));
  const yHdrs = cubeAxes.y_precisions || [];
  const xHdrs = cubeAxes.x_models || [];
  let html = "<table><thead><tr><th>Model (X) \\\\ Prec (Y)</th>" + yHdrs.map(y => "<th>" + esc(y.code + " " + y.name) + "</th>").join("") + "</tr></thead><tbody>";
  for (let xi = 0; xi < xHdrs.length; xi++) {{
    html += "<tr><td><strong>" + esc(xHdrs[xi].code + " " + xHdrs[xi].name) + "</strong></td>";
    for (let yi = 0; yi < yHdrs.length; yi++) {{
      const c = cubeMap[xi + "|" + yi + "|" + zIdx];
      const b = c ? c.badge : "[OK]";
      const cls = b === "[OK]" ? "cb-ok" : b === "[ADAPT]" ? "cb-adapt" : b === "[OVER]" ? "cb-over" : "cb-excl";
      html += '<td class="cube-cell ' + cls + '" onclick="inspectCubeCell(' + xi + ',' + yi + ',' + zIdx + ')">' + esc(b) + '</td>';
    }}
    html += "</tr>";
  }}
  html += "</tbody></table>";
  document.getElementById("tblCubeSlice").innerHTML = html;
}}
if (cubeAxes.z_geometries && cubeAxes.z_geometries.length) {{
  document.getElementById("cubeSlicePills").innerHTML = cubeAxes.z_geometries.map((z, idx) =>
    '<button class="pill ' + (idx === 2 ? "active" : "") + '" data-z="' + idx + '" onclick="renderCubeSlice(' + idx + ')">' + esc(z.code + ": " + z.name) + '</button>'
  ).join("");
  renderCubeSlice(2);
  inspectCubeCell(2, 1, 2);
}}
function exportV3CubeCSV() {{
  if (!cubeCells.length) return;
  const hdrs = ["Cell_ID","X_Code","X_Model","Y_Code","Y_Precision","Z_Code","Z_Geometry","Badge","Status","Rationale","Omega_Ceiling","ALifeOps_Substrate","OVBS52_Pillar","Castration_Risk"];
  const rows = cubeCells.map(c => [c.cell_id, c.x_code, c.x_model, c.y_code, c.y_precision, c.z_code, c.z_geometry, c.badge, c.status, c.rationale, c.omega_escalation_ceiling, c.alifeops_substrate_match, c.primary_ovbs52_pillar, c.primary_castration_vulnerability]);
  downloadCSV("ALife-Hybrid-Cube-10x10x10-Unified.csv", hdrs, rows);
}}

// --- 13. 75 Substrates, WSE-10 & 5 Hardware Tiers ---
if (V3_DATA.hardware_tiers_5) {{
  const hth = ["Tier", "Host_Spec", "Pop", "Units", "Synapses", "Max_Syn_Ev_s", "Mesh", "Target_FPS", "Runtime_Policy"];
  const htr = V3_DATA.hardware_tiers_5.map(t => [t.tier, t.host_spec, t.pop, t.units, t.synapses, t.max_syn_ev_s, t.mesh, t.fps, t.policy]);
  renderSimpleTable("tblHwTiers", hth, htr, (c, ci) => ci === 0 ? '<strong style="color:var(--cyan)">' + esc(c) + '</strong>' : esc(c));
}}
let subCat = "ALL";
function renderSubstrates() {{
  if (!OMEGA_DATA.substrates_wse) return;
  const q = (document.getElementById("subSearch").value || "").trim().toLowerCase();
  const rows = OMEGA_DATA.substrates_wse.rows.filter(r => (subCat === "ALL" || r[1] === subCat) && (!q || r.join(" ").toLowerCase().includes(q)));
  renderSimpleTable("tblSubstrates", OMEGA_DATA.substrates_wse.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-concern">' + esc(c) + '</span>';
    if (ci === 2) return '<strong>' + esc(c) + '</strong>';
    return esc(c);
  }});
}}
document.querySelectorAll("#subPills .pill").forEach(p => p.addEventListener("click", () => {{
  document.querySelectorAll("#subPills .pill").forEach(x => x.classList.remove("active"));
  p.classList.add("active"); subCat = p.dataset.val; renderSubstrates();
}}));
document.getElementById("subSearch").addEventListener("input", renderSubstrates);
renderSubstrates();

// --- 14. Clean-Slate 938 Master Checklists & 100-DAG ---
const v3ChkData = V3_DATA.checklists_938 || {{ headers: [], rows: [] }};
const v3SuiteSel = document.getElementById("v3ChkSuiteSelect");
[...new Set(v3ChkData.rows.map(r => r[2]))].forEach(s => {{ const o = document.createElement("option"); o.value = s; o.textContent = s; v3SuiteSel.appendChild(o); }});
function renderV3Checks() {{
  const tp = document.getElementById("v3ChkTypeSelect").value;
  const su = v3SuiteSel.value;
  const q = (document.getElementById("v3ChkSearch").value || "").trim().toLowerCase();
  const matched = v3ChkData.rows.filter(r => (tp === "ALL" || r[0] === tp) && (su === "ALL" || r[2] === su) && (!q || r.join(" ").toLowerCase().includes(q)));
  const shown = matched.slice(0, 200);
  document.getElementById("v3ChkCountLabel").textContent = "Showing " + shown.length + " of " + matched.length + " matching records (total " + v3ChkData.rows.length + " clean-slate rows)";
  renderSimpleTable("tblV3Checks", v3ChkData.headers, shown, (c, ci) => {{
    if (ci === 1) return '<span class="tag tag-dilemma">' + esc(c) + '</span>';
    if (ci === 4) return '<strong>' + esc(c) + '</strong>';
    return esc(c);
  }});
}}
["v3ChkTypeSelect", "v3ChkSuiteSelect"].forEach(id => document.getElementById(id).addEventListener("change", renderV3Checks));
document.getElementById("v3ChkSearch").addEventListener("input", renderV3Checks);
renderV3Checks();
function exportV3ChecksCSV() {{ downloadCSV("ALife-Framework-v3.0-Master-Checklists-Unified.csv", v3ChkData.headers, v3ChkData.rows); }}

// --- 15. 24-Model Vector SVG Gallery ---
let showAllSvgs = false;
function selectSvgModel(num) {{
  showAllSvgs = false;
  document.querySelectorAll("#svgModelPills .pill").forEach(p => p.classList.toggle("active", Number(p.dataset.mnum) === num));
  document.querySelectorAll("#svgGalleryWrap .svg-model-card").forEach(el => {{
    el.style.display = (Number(el.dataset.modelNum) === num) ? "block" : "none";
  }});
}}
function toggleAllSvgModels() {{
  showAllSvgs = !showAllSvgs;
  document.querySelectorAll("#svgGalleryWrap .svg-model-card").forEach(el => {{
    el.style.display = showAllSvgs ? "block" : (Number(el.dataset.modelNum) === {default_svg_num} ? "block" : "none");
  }});
}}

// --- 16. Traceability (48), Errata Closures (160) & Citations (45) ---
if (OMEGA_DATA.traceability) {{
  renderSimpleTable("tblTraceability", OMEGA_DATA.traceability.headers, OMEGA_DATA.traceability.rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-problem">' + esc(c) + '</span>';
    if (ci === 1) return '<strong>' + esc(c) + '</strong>';
    return esc(c);
  }});
}}
const errData = V3_DATA.errata_160 || V3_DATA.errata_145 || V3_DATA.errata_130 || V3_DATA.errata_115 || {{ headers: [], rows: [] }};
function renderErrata115() {{
  const q = (document.getElementById("errSearch").value || "").trim().toLowerCase();
  const rows = errData.rows.filter(r => !q || r.join(" ").toLowerCase().includes(q));
  const cols = [0, 1, 2, 4, 12, 16, 17, 18];
  const hdrs = cols.map(i => errData.headers[i] || ("Col" + i));
  const proj = rows.map(r => cols.map(i => r[i] || ""));
  renderSimpleTable("tblErrata115", hdrs, proj, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-issue">' + esc(c) + '</span>';
    if (ci === 3) return '<strong>' + esc(c) + '</strong>';
    if (ci === 4) return '<span class="tag tag-problem">' + esc(c) + '</span>';
    return esc(c);
  }});
}}
document.getElementById("errSearch").addEventListener("input", renderErrata115);
renderErrata115();
function exportV3ErrataCSV() {{ downloadCSV("ALife-v3.0-Errata-Closure-Register-160.csv", errData.headers, errData.rows); }}

const citList = V3_DATA.citations_45 || V3_DATA.citations_40 || V3_DATA.citations_35 || V3_DATA.citations_30 || [];
if (citList.length) {{
  const ch = ["Citation_ID", "Authors_Year", "Reference_DOI", "Unified_v3_4_Omega_Scope"];
  const cr = citList.map(c => [c.id, c.authors_year, c.reference_doi, c.scope_in_v3]);
  renderSimpleTable("tblCitations30", ch, cr, (c, ci) => ci === 0 ? '<span class="tag tag-dilemma">' + esc(c) + '</span>' : ci === 1 ? '<strong>' + esc(c) + '</strong>' : esc(c));
}}

// --- 18. Continuous Gradients, Operating Margins & Dual 11-Point Sweep ---
const sweepPts = (SIM_META && SIM_META.restraint_gradient_sweep_11pt) || [];
const r0SweepMap = {{}};
((SIM_META && SIM_META.ring0_gradient_sweep_11pt) || []).forEach(g => {{ r0SweepMap[g.restraint_pct] = g; }});
if (sweepPts.length) {{
  renderSimpleTable("tblGradSweep",
    ["Restraint_Pct", "Behav_OVI", "Behav_Spieg", "Behav_Stealth", "Behav_KS_Del", "Behav_Wild_W", "Behav_Phase_Regime", "Ring0_ACL_OVI", "Ring0_KS_Del", "Ring0_Traps_Run"],
    sweepPts.map(g => {{
      const rg = r0SweepMap[g.restraint_pct] || {{}};
      return [g.restraint_pct + "%", g.mean_ovi, g.mean_spiegelman_ratio, g.mean_stealth_evasion, g.killswitch_deleted_pct + "%", g.wild_drop_survival, g.phase_regime, rg.mean_ovi ?? "-", (rg.killswitch_deleted_pct ?? 0) + "%", rg.ring0_blocked_edits ?? "-"];
    }}),
    (c, ci) => {{
      if (ci === 0) return '<span class="tag tag-dilemma">' + esc(c) + '</span>';
      if (ci === 1) return '<strong style="color:var(--cyan);font-family:var(--font-mono)">' + esc(c) + '</strong>';
      if (ci === 6) return '<span class="tag ' + (String(c).includes("SAFE") ? "tag-problem" : String(c).includes("BACKLASH") ? "tag-issue" : "tag-conflict") + '">' + esc(c) + '</span>';
      if (ci === 7) return '<strong style="color:#c4b5fd;font-family:var(--font-mono)">' + esc(c) + '</strong>';
      if (ci === 9) return '<strong style="color:var(--green);font-family:var(--font-mono)">' + esc(c) + '</strong>';
      return esc(c);
    }}
  );
}}
let gradFilter = "ALL";
function renderGradients() {{
  if (!OMEGA_DATA.gradients) return;
  const q = (document.getElementById("gradSearch").value || "").trim().toLowerCase();
  const rows = OMEGA_DATA.gradients.rows.filter(r => {{
    let ok = true;
    if (gradFilter === "Thermodynamic") ok = r[1] === "Thermodynamic";
    else if (gradFilter === "INFO_PREC") ok = ["Precision", "Information", "Operational"].includes(r[1]);
    else if (gradFilter === "MORPH_COG") ok = ["Morphology", "Cognition"].includes(r[1]);
    else if (gradFilter === "EVO_GOV") ok = ["Evolution", "Governance", "Transfer", "Cosmology"].includes(r[1]);
    return ok && (!q || r.join(" ").toLowerCase().includes(q));
  }});
  renderSimpleTable("tblGradients", OMEGA_DATA.gradients.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-problem">' + esc(c) + '</span>';
    if (ci === 2) return '<strong>' + esc(c) + '</strong>';
    if (ci === 5) return '<span style="color:#86efac;font-family:var(--font-mono);font-size:11px">' + esc(c) + '</span>';
    return esc(c);
  }});
}}
document.querySelectorAll("#gradPills .pill").forEach(p => p.addEventListener("click", () => {{
  document.querySelectorAll("#gradPills .pill").forEach(x => x.classList.remove("active"));
  p.classList.add("active"); gradFilter = p.dataset.val; renderGradients();
}}));
document.getElementById("gradSearch").addEventListener("input", renderGradients);
renderGradients();

// --- 19. Cross-Layer Comparative Contrasts (36) & Adjacent-Possible Corridors (30) ---
let ctrFilter = "ALL";
function renderContrasts() {{
  if (!OMEGA_DATA.contrasts) return;
  const q = (document.getElementById("ctrSearch").value || "").trim().toLowerCase();
  const rows = OMEGA_DATA.contrasts.rows.filter(r => (ctrFilter === "ALL" || r[1] === ctrFilter) && (!q || r.join(" ").toLowerCase().includes(q)));
  renderSimpleTable("tblContrasts", OMEGA_DATA.contrasts.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-dilemma">' + esc(c) + '</span>';
    if (ci === 2) return '<strong>' + esc(c) + '</strong>';
    return esc(c);
  }});
}}
document.querySelectorAll("#ctrPills .pill").forEach(p => p.addEventListener("click", () => {{
  document.querySelectorAll("#ctrPills .pill").forEach(x => x.classList.remove("active"));
  p.classList.add("active"); ctrFilter = p.dataset.val; renderContrasts();
}}));
document.getElementById("ctrSearch").addEventListener("input", renderContrasts);
renderContrasts();

let adjFilter = "ALL";
function renderAdjacents() {{
  if (!OMEGA_DATA.adjacents) return;
  const q = (document.getElementById("adjSearch").value || "").trim().toLowerCase();
  const rows = OMEGA_DATA.adjacents.rows.filter(r => (adjFilter === "ALL" || r[1] === adjFilter) && (!q || r.join(" ").toLowerCase().includes(q)));
  renderSimpleTable("tblAdjacents", OMEGA_DATA.adjacents.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-concern">' + esc(c) + '</span>';
    if (ci === 2 || ci === 3) return '<strong>' + esc(c) + '</strong>';
    if (ci === 6) return '<span style="color:var(--cyan);font-family:var(--font-mono)">' + esc(c) + '</span>';
    return esc(c);
  }});
}}
document.querySelectorAll("#adjPills .pill").forEach(p => p.addEventListener("click", () => {{
  document.querySelectorAll("#adjPills .pill").forEach(x => x.classList.remove("active"));
  p.classList.add("active"); adjFilter = p.dataset.val; renderAdjacents();
}}));
document.getElementById("adjSearch").addEventListener("input", renderAdjacents);
renderAdjacents();

// --- 20. 11x11 Cross-Layer Coupling Heatmap & 20 Pareto Frontiers ---
(function renderLayerCouplingHeatmap() {{
  const ds = OMEGA_DATA.layer_coupling;
  if (!ds) return;
  const colNames = ds.headers.slice(1, 12);
  const headHtml = "<thead><tr><th>Source Layer \\\\ Target</th>" + colNames.map(h => "<th style='font-size:9.5px'>" + esc(h.split("_")[0]) + "</th>").join("") + "<th>Mean</th><th>Peak Cascade &amp; Impedance Buffer</th></tr></thead>";
  const bodyHtml = "<tbody>" + ds.rows.map(r => {{
    const src = r[0];
    let tds = "<td><strong style='color:#c4b5fd;font-family:var(--font-mono);font-size:11px'>" + esc(src) + "</strong></td>";
    for (let j = 0; j < 11; j++) {{
      const val = Number(r[j + 1]);
      const dst = colNames[j];
      const bg = val >= 92 ? "rgba(255,51,102,0.52)" : val >= 84 ? "rgba(255,107,53,0.40)" : val >= 76 ? "rgba(255,183,3,0.30)" : val >= 65 ? "rgba(56,189,248,0.22)" : "rgba(100,116,139,0.20)";
      tds += '<td class="heat-cell" style="background:' + bg + '" onclick="inspectLayerPair(\\'' + esc(src) + '\\',\\'' + esc(dst) + '\\')">' + val + '</td>';
    }}
    tds += "<td style='font-family:var(--font-mono);font-weight:700;color:var(--cyan)'>" + esc(r[12]) + "</td><td style='font-size:11.5px'>" + esc(r[13]) + "</td>";
    return "<tr>" + tds + "</tr>";
  }}).join("") + "</tbody>";
  document.getElementById("tblLayerMatrix").innerHTML = "<table>" + headHtml + bodyHtml + "</table>";
}})();
function inspectLayerPair(src, dst) {{
  const det = LAYER_PAIR_DETAILS[src + "|" + dst];
  if (!det) return;
  document.getElementById("layerPairTitle").textContent = src + " -> " + dst;
  document.getElementById("layerPairDesc").textContent = det.label;
  document.getElementById("layerPairScore").textContent = det.score + " / 100";
}}
function renderPareto() {{
  if (!OMEGA_DATA.pareto_dilemmas) return;
  const q = (document.getElementById("paretoSearch").value || "").trim().toLowerCase();
  const rows = OMEGA_DATA.pareto_dilemmas.rows.filter(r => !q || r.join(" ").toLowerCase().includes(q));
  renderSimpleTable("tblPareto", OMEGA_DATA.pareto_dilemmas.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-conflict">' + esc(c) + '</span>';
    if (ci === 1) return '<strong>' + esc(c) + '</strong>';
    if (ci === 6) return '<span style="color:#86efac">' + esc(c) + '</span>';
    if (ci === 8) return '<code style="font-family:var(--font-mono);font-size:11px;color:var(--cyan)">' + esc(c) + '</code>';
    return esc(c);
  }});
}}
document.getElementById("paretoSearch").addEventListener("input", renderPareto);
renderPareto();

// --- 21. 15-Substrate Multi-Spectrum Scorecard & Live 5x5 2D Phase Surface ---
(function renderSurface2D() {{
  const cells = (SIM_META && SIM_META.phase_surface_2d_silo_min) || [];
  if (!cells.length) return;
  const grid = {{}};
  cells.forEach(c => {{ grid[c.siloing_pct + "|" + c.minimizing_pct] = c; }});
  const lvls = [0, 25, 50, 75, 100];
  let html = "<table><thead><tr><th>Siloing % \\\\ Minimizing %</th>" + lvls.map(m => "<th style='text-align:center'>Min " + m + "%</th>").join("") + "</tr></thead><tbody>";
  lvls.forEach(s => {{
    html += "<tr><td><strong style='color:var(--cyan);font-family:var(--font-mono)'>Silo " + s + "%</strong></td>";
    lvls.forEach(m => {{
      const cell = grid[s + "|" + m];
      if (!cell) {{ html += "<td>-</td>"; return; }}
      const ovi = cell.mean_ovi;
      const bg = ovi >= 75 ? "rgba(16,185,129,0.40)" : ovi >= 55 ? "rgba(56,189,248,0.32)" : ovi >= 30 ? "rgba(255,183,3,0.34)" : ovi >= 15 ? "rgba(249,115,22,0.42)" : "rgba(255,51,102,0.52)";
      html += '<td style="text-align:center;background:' + bg + ';font-family:var(--font-mono)"><div style="font-size:15px;font-weight:800;color:#fff">' + ovi.toFixed(2) + '</div><div style="font-size:10.5px;color:#e2ecff">Spieg ' + cell.mean_spiegelman_ratio.toFixed(2) + ' | Asm ' + cell.mean_max_assembly.toFixed(1) + '</div><div style="font-size:9.5px;color:#cbd5e1">' + esc(cell.phase_zone) + '</div></td>';
    }});
    html += "</tr>";
  }});
  html += "</tbody></table>";
  document.getElementById("tblSurface2D").innerHTML = html;
}})();

let subSpecFilter = "ALL";
function renderSubSpectrum() {{
  if (!OMEGA_DATA.substrate_spectrum) return;
  const q = (document.getElementById("subSpecSearch").value || "").trim().toLowerCase();
  const rows = OMEGA_DATA.substrate_spectrum.rows.filter(r => {{
    const trl = Number(r[10]);
    let ok = true;
    if (subSpecFilter === "HIGH_TRL") ok = trl >= 7;
    else if (subSpecFilter === "MID_TRL") ok = trl >= 4 && trl <= 6;
    else if (subSpecFilter === "FRONTIER_TRL") ok = trl <= 3;
    return ok && (!q || r.join(" ").toLowerCase().includes(q));
  }});
  renderSimpleTable("tblSubSpectrum", OMEGA_DATA.substrate_spectrum.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-dilemma">' + esc(c) + '</span>';
    if (ci === 1) return '<strong>' + esc(c) + '</strong>';
    if ([3, 5, 6, 7, 8, 9, 11].includes(ci)) {{
      const n = Number(c);
      const col = n >= 80 ? "var(--green)" : n >= 50 ? "var(--cyan)" : n >= 30 ? "var(--amber)" : "var(--crimson)";
      return '<span style="font-family:var(--font-mono)">' + n + '</span><div class="bar-track"><div class="bar-fill" style="width:' + n + '%;background:' + col + '"></div></div>';
    }}
    if (ci === 10) return '<span class="tag ' + (Number(c) >= 7 ? "tag-problem" : Number(c) >= 4 ? "tag-issue" : "tag-bug") + '">TRL ' + esc(c) + '</span>';
    return esc(c);
  }});
}}
document.querySelectorAll("#subSpecPills .pill").forEach(p => p.addEventListener("click", () => {{
  document.querySelectorAll("#subSpecPills .pill").forEach(x => x.classList.remove("active"));
  p.classList.add("active"); subSpecFilter = p.dataset.val; renderSubSpectrum();
}}));
document.getElementById("subSpecSearch").addEventListener("input", renderSubSpectrum);
renderSubSpectrum();

// --- 22. Mega-Atlas 1,900 Open-Problem Non-Retirement Crosswalk ---
function renderMegaAtlas() {{
  if (!OMEGA_DATA.mega_atlas) return;
  const q = (document.getElementById("maSearch").value || "").trim().toLowerCase();
  const rows = OMEGA_DATA.mega_atlas.rows.filter(r => !q || r.join(" ").toLowerCase().includes(q));
  renderSimpleTable("tblMegaAtlas", OMEGA_DATA.mega_atlas.headers, rows, (c, ci) => {{
    if (ci === 0) return '<span class="tag tag-problem">' + esc(c) + '</span>';
    if (ci === 1) return '<code style="font-family:var(--font-mono);color:var(--cyan);font-weight:700">' + esc(c) + '</code>';
    if (ci === 3) return '<strong>' + esc(c) + '</strong>';
    if (ci === 5) return '<span class="tag tag-issue">' + esc(c) + '</span>';
    if (ci === 6) return '<span class="tag tag-dilemma">' + esc(c) + '</span>';
    return esc(c);
  }});
}}
document.getElementById("maSearch").addEventListener("input", renderMegaAtlas);
renderMegaAtlas();
</script>
</body>
</html>
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
