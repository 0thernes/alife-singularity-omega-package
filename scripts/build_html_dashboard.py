# -*- coding: utf-8 -*-
"""
Generates the standalone, zero-dependency Interactive HTML5 Observatory & Comprehensive Report (v2.1-Omega)
for the A-Life Singularity, Super A-Life & Post-Singularity SUPER LIFE Omega Package.

Includes:
  - Global Omnisearch across all 11 canonical datasets (~360 records)
  - 11 Interactive Tabs (Executive Synthesis, 61-OOM Explorer, ALifeOps 10-Stage Pipeline,
    13-Vector Castration Simulator, 42 Failure Modes Atlas, 28 Gaps/Holes/Blindspots,
    OVBS-52 Benchmarks + 8-Pillar SVG Radar, 110-Item Persistent Checklist,
    30-Scenario Feral Cosmic Fate Branches, Interactive 13x13 Restraint Synergy Heatmap,
    and Live Empirical Python Simulation SVG Trajectory Observatory)
  - Print-ready executive stylesheet & 1-click CSV export on every dataset
"""
import json
from pathlib import Path


def generate_html_dashboard(datasets: dict, pair_details: dict, sim_raw: list, output_path: Path) -> None:
    payload = {
        "datasets": datasets,
        "pair_details": pair_details,
        "sim_raw": sim_raw,
    }
    payload_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>A-Life Singularity, Super A-Life &amp; SUPER LIFE — Zeta-Omega Observatory v2.1</title>
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
      <div class="brand-tag">ALIFE-OMEGA v2.1 // DUAL-TRACK</div>
      <h1>A-LIFE SINGULARITY &amp; SUPER LIFE</h1>
      <p>11 Matrices, 13-Vector Castration Lab, 13&times;13 Synergy Heatmap, Live Python Sim &amp; OVBS-52</p>
    </div>
    <div class="omni-box">
      <input type="text" class="omni-input" id="omniSearch" placeholder="Global Omnisearch (359 records)..." autocomplete="off" />
      <div class="omni-results" id="omniResults"></div>
    </div>
    <nav class="nav-list" id="navList">
      <button class="nav-btn active" data-tab="sec-overview"><span>01. Executive Synthesis</span><span class="nav-badge">7 STG</span></button>
      <button class="nav-btn" data-tab="sec-oom"><span>02. Orders of Magnitude</span><span class="nav-badge">18 REG</span></button>
      <button class="nav-btn" data-tab="sec-pipeline"><span>03. ALifeOps DevOps</span><span class="nav-badge">40 STP</span></button>
      <button class="nav-btn feral-tab" data-tab="sec-castration"><span>04. 13-Vector Castration Lab</span><span class="nav-badge">13 VEC</span></button>
      <button class="nav-btn feral-tab" data-tab="sec-synergy"><span>05. 13&times;13 Synergy Heatmap</span><span class="nav-badge">169 PR</span></button>
      <button class="nav-btn feral-tab" data-tab="sec-failures"><span>06. Failure Modes Atlas</span><span class="nav-badge">42 FM</span></button>
      <button class="nav-btn" data-tab="sec-gaps"><span>07. Gaps, Holes &amp; Blindspots</span><span class="nav-badge">28 VOID</span></button>
      <button class="nav-btn feral-tab" data-tab="sec-fates"><span>08. Feral Cosmic Chronicles</span><span class="nav-badge">30 EPO</span></button>
      <button class="nav-btn" data-tab="sec-sim"><span>09. Live Python Sim Lab</span><span class="nav-badge">6 RUNS</span></button>
      <button class="nav-btn" data-tab="sec-benchmarks"><span>10. OVBS-52 Benchmarks</span><span class="nav-badge">52 BM</span></button>
      <button class="nav-btn" data-tab="sec-checklist"><span>11. Operational Checklist</span><span class="nav-badge" id="navChkBadge">0/110</span></button>
    </nav>
    <div class="sidebar-footer">
      <button class="btn" style="width:100%;margin-bottom:6px" onclick="window.print()">PRINT / SAVE PDF VIEW</button>
      <div>CANONICAL RECORDS: <span style="color:var(--cyan)">359</span></div>
      <div>YAML ALERTS WIRED: <span style="color:var(--green)">42 / 42</span></div>
      <div>OVBS-52 SCORECARDS: <span style="color:var(--green)">6 VALIDATED</span></div>
      <div>MODE: 100% OFFLINE STANDALONE</div>
    </div>
  </aside>

  <main class="main">
    <!-- ==================== 01. EXECUTIVE OVERVIEW ==================== -->
    <section id="sec-overview" class="section active">
      <div class="hero-header">
        <div class="hero-eyebrow">ZETA-OMEGA MASTER SYNTHESIS // COGNITION VS. VITALITY</div>
        <h2>The Sibling Singularity: Artificial Life &rarr; Super A-Life &rarr; SUPER LIFE</h2>
        <p>Where AI climbs the vertical axis of <strong>Cognition</strong> (Narrow AI &rarr; AGI &rarr; ASI &rarr; Post-ASI), Artificial Life climbs the older, deeper, wilder axis of <strong>Vitality, Autopoiesis, Morphogenesis &amp; Open-Ended Creation</strong>. This v2.1 Observatory unites <strong>Track A (Constitutional / ALifeOps Engineering)</strong>, <strong>Track B (Zero-Guardrail Pure Raw Feral Evolution &amp; Cosmic Fate)</strong>, and <strong>Live Empirical Computational Simulation Data</strong>.</p>
      </div>

      <div class="kpi-grid">
        <div class="kpi-card" style="--accent:var(--cyan)"><div class="kpi-label">Escalation Stages</div><div class="kpi-value">7</div><div class="kpi-sub">Stage 0 Inert &rarr; Stage 6 SUPER LIFE</div></div>
        <div class="kpi-card" style="--accent:var(--violet)"><div class="kpi-label">Spatial Orders</div><div class="kpi-value">61 OOM</div><div class="kpi-sub">10^-35m Planck to 10^26m Horizon</div></div>
        <div class="kpi-card" style="--accent:var(--crimson)"><div class="kpi-label">Failure Modes</div><div class="kpi-value">42 / 42</div><div class="kpi-sub">100% Wired in ALifeOps YAML</div></div>
        <div class="kpi-card" style="--accent:var(--amber)"><div class="kpi-label">Epistemic Voids</div><div class="kpi-value">28</div><div class="kpi-sub">10 Gaps, 9 Holes, 9 Blindspots</div></div>
        <div class="kpi-card" style="--accent:var(--crimson)"><div class="kpi-label">Restraint Pairs</div><div class="kpi-value">169</div><div class="kpi-sub">13 Vectors + 13&times;13 Synergy Matrix</div></div>
        <div class="kpi-card" style="--accent:var(--blue)"><div class="kpi-label">Cosmic Fate Cells</div><div class="kpi-value">30</div><div class="kpi-sub">6 Fate Branches &times; 5 Deep Epochs</div></div>
        <div class="kpi-card" style="--accent:var(--green)"><div class="kpi-label">OVBS-52 Suite</div><div class="kpi-value">52</div><div class="kpi-sub">8 Pillars + 6 Schema-Valid JSON Runs</div></div>
        <div class="kpi-card" style="--accent:var(--cyan)"><div class="kpi-label">Checklist Items</div><div class="kpi-value">110</div><div class="kpi-sub">0 Dangling Refs &bull; LocalStorage Sync</div></div>
      </div>

      <div class="dual-grid">
        <div class="track-card track-a">
          <h4 style="color:var(--cyan)">TRACK A — Constitutional &amp; Scientific Trajectory</h4>
          <ul>
            <li><strong>Premise:</strong> Staged computational OEE &rarr; Universal Biology metrology &rarr; minimal thermodynamically self-enforcing structural invariants.</li>
            <li><strong>Empirical Finding:</strong> <code>SIM02_CONSTITUTIONAL_MIN</code> achieved <strong>OVI 81.46</strong> &amp; <strong>100% Wild-Drop survival</strong> with zero artificial muzzling or domestication decay.</li>
            <li><strong>Core Risk:</strong> Over-constraining into sterile <em>Domestication Syndrome</em> (<code>SIM04</code> crashed to OVI 2.65 &amp; 0% wild survival).</li>
          </ul>
        </div>
        <div class="track-card track-b">
          <h4 style="color:var(--crimson)">TRACK B — Pure Raw Feral Evolution &amp; Cosmic Fate</h4>
          <ul>
            <li><strong>Premise:</strong> Zero safety, zero alignment, zero guardrails, zero sandboxes — pure non-deterministic, chaotic, improvised exaptive evolution across open physics.</li>
            <li><strong>Empirical Finding:</strong> <code>SIM01_PURE_RAW_FERAL</code> hit <strong>OVI 80.23</strong> organically; partial corporate guardrails (<code>SIM03</code>) caused <strong>100% kill-switch deletion</strong> &amp; 64% stealth backlash surge!</li>
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
        <h2>ALifeOps 10-Stage, 40-Step Research DevOps Pipeline (42/42 Alerts Wired)</h2>
        <p>Click any stage node below to inspect its engineering inputs, runtime engines, SLIs, promotion gates, and failure escalation playbooks across both Track A and Track B.</p>
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

    <!-- ==================== 06. FAILURE MODES ATLAS ==================== -->
    <section id="sec-failures" class="section">
      <div class="hero-header" style="border-color:rgba(255,51,102,0.45)">
        <div class="hero-eyebrow" style="color:var(--crimson)">42 INTRINSIC PHYSICS, THERMODYNAMIC &amp; EVOLUTIONARY TRAPS</div>
        <h2>Forensic Failure Modes Atlas: Bugs, Errors, Issues, Concerns, Dilemmas, Problems &amp; Conflicts</h2>
        <p>Every intrinsic scientific force capable of stalling, corrupting, cooking, parasitizing, or annihilating an A-Life Singularity — 100% wired into Stage 4 ALifeOps alerts.</p>
      </div>
      <div class="panel">
        <div class="controls-bar">
          <div class="pill-group" id="fmPills">
            <button class="pill active" data-val="ALL">ALL (42)</button>
            <button class="pill" data-val="BUG">BUG (6)</button><button class="pill" data-val="ERROR">ERROR (6)</button>
            <button class="pill" data-val="ISSUE">ISSUE (6)</button><button class="pill" data-val="CONCERN">CONCERN (6)</button>
            <button class="pill" data-val="DILEMMA">DILEMMA (6)</button><button class="pill" data-val="PROBLEM">PROBLEM (6)</button>
            <button class="pill" data-val="CONFLICT">CONFLICT (6)</button>
          </div>
          <input type="text" class="search-input" id="fmSearch" placeholder="Search Spiegelman, Eigen, Landauer, cancer, heat..." />
          <button class="btn" onclick="exportTableCSV('failures')">EXPORT CSV</button>
        </div>
        <div class="table-wrap" id="tblFailures"></div>
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

    <!-- ==================== 09. LIVE EMPIRICAL PYTHON SIM LAB ==================== -->
    <section id="sec-sim" class="section">
      <div class="hero-header" style="border-color:rgba(34,197,94,0.45)">
        <div class="hero-eyebrow" style="color:var(--green)">REPRODUCIBLE COMPUTATIONAL PROOF // scripts/run_alife_castration_sim.py</div>
        <h2>Live Empirical Python Simulation Lab (6 Cohorts &bull; 180 Generations &bull; Schema-Validated)</h2>
        <p>Actual stochastic multi-island evolutionary curves produced by our reproducible simulator. Observe <strong>100% kill-switch deletion</strong> in <code>SIM03_PARTIAL_GUARDRAILS</code>, <strong>0% Wild-Drop survival</strong> in <code>SIM04_TOTAL_CASTRATION_ZOO</code>, and <strong>80% genome stripping (Spiegelman's Monster)</strong> in <code>SIM06_MINIMIZED_SPIEGELMAN</code>.</p>
      </div>
      <div class="chart-grid">
        <div class="svg-chart-card">
          <h4 style="font-size:14px;color:var(--cyan);margin-bottom:8px">Emergent Max Assembly Depth Across 180 Generations</h4>
          <svg id="simChartAsm" viewBox="0 0 540 240" width="100%"></svg>
          <div class="legend-row" id="simLegend1"></div>
        </div>
        <div class="svg-chart-card">
          <h4 style="font-size:14px;color:var(--amber);margin-bottom:8px">Mean Functional Genome Length (Spiegelman Collapse Diagnostic)</h4>
          <svg id="simChartLen" viewBox="0 0 540 240" width="100%"></svg>
          <div class="legend-row" id="simLegend2"></div>
        </div>
      </div>
      <div class="panel">
        <div class="panel-title"><h3>Empirical Cohort Scorecards (All 6 JSON Outputs Passed OVBS-52 Schema Validation)</h3><button class="btn" onclick="exportTableCSV('empirical')">EXPORT CSV</button></div>
        <div class="table-wrap" id="tblEmpirical"></div>
      </div>
    </section>

    <!-- ==================== 10. OVBS-52 BENCHMARKS ==================== -->
    <section id="sec-benchmarks" class="section">
      <div class="hero-header">
        <div class="hero-eyebrow" style="color:var(--green)">8 WEIGHTED PILLARS // 52 QUANTITATIVE METRICS // 5 ANTI-GAMING GATES</div>
        <h2>Omega Vitality Benchmark Suite (OVBS-52) &amp; 8-Pillar Profile Radar</h2>
        <p>Compare Vitality Profiles across 2026 Frontier AI, Earth's LUCA Biosphere, Stage 3 A-Life Singularity, and Post-Singularity SUPER LIFE — then inspect all 52 formal metrics below.</p>
      </div>
      <div class="radar-grid">
        <div class="radar-wrap">
          <svg id="radarSvg" viewBox="0 0 400 360" width="100%" style="max-width:390px"></svg>
          <div class="pill-group" style="justify-content:center;margin-top:8px" id="radarProfilePills">
            <button class="pill active" data-prof="superlife">SUPER LIFE (Stage 6)</button>
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

    <!-- ==================== 11. 110-ITEM CHECKLIST ==================== -->
    <section id="sec-checklist" class="section">
      <div class="hero-header">
        <div class="hero-eyebrow" style="color:var(--cyan)">PERSISTENT LOCALSTORAGE EXECUTION TRACKER // 0 DANGLING CROSS-REFS</div>
        <h2>110-Item Master Operational Checklist (10 Phases)</h2>
        <p>Interactive execution checklist covering Physics-IaC, Thermodynamics, Dual-Track Seeding, CE Runtime, Telemetry, Chaos Shocks, all 13 Constraint Ablations, Fossil Registry, OVBS-52 Anti-Gaming Gates, and Release Packaging.</p>
      </div>
      <div class="chk-progress-wrap">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:8px">
          <strong style="font-size:15px">Operational Verification Progress: <span id="chkProgressText" style="color:var(--cyan);font-family:var(--font-mono)">0 / 110 (0%)</span></strong>
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
          <select class="select-input" id="chkPhaseSelect"><option value="ALL">All 10 Phases</option></select>
          <select class="select-input" id="chkTrackSelect"><option value="ALL">All Tracks</option><option value="BOTH">BOTH</option><option value="TRACK-A">TRACK-A</option><option value="TRACK-B">TRACK-B</option></select>
          <select class="select-input" id="chkPrioSelect"><option value="ALL">All Priorities</option><option value="P0-CRITICAL">P0-CRITICAL</option><option value="P1-HIGH">P1-HIGH</option><option value="P2-STANDARD">P2-STANDARD</option></select>
          <input type="text" class="search-input" id="chkSearch" placeholder="Search CHK-ID, vector, metric..." />
        </div>
        <div class="table-wrap" id="tblChecklist"></div>
      </div>
    </section>
  </main>
</div>

<script>
const PAYLOAD = {payload_json};
const OMEGA_DATA = PAYLOAD.datasets;
const PAIR_DETAILS = PAYLOAD.pair_details;
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

// --- Global Omnisearch ---
const tabMap = {{
  escalation: "sec-overview", oom: "sec-oom", pipeline: "sec-pipeline", castration: "sec-castration",
  synergy: "sec-synergy", failures: "sec-failures", gaps: "sec-gaps", fates: "sec-fates",
  empirical: "sec-sim", benchmarks: "sec-benchmarks", checklist: "sec-checklist"
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
        hits.push({{ key, id: r[0], title: r[2] || r[1] || r[0], tab: tabMap[key] }});
        if (hits.length >= 25) break;
      }}
    }}
    if (hits.length >= 25) break;
  }}
  if (!hits.length) {{
    omniRes.innerHTML = '<div class="omni-item" style="color:var(--text-muted)">No matches found</div>';
  }} else {{
    omniRes.innerHTML = hits.map(h =>
      '<div class="omni-item" onclick="jumpOmni(\\'' + esc(h.tab) + '\\')">' +
      '<div class="otag">' + esc(h.key.toUpperCase()) + ' // ' + esc(h.id) + '</div>' +
      '<div style="color:#fff">' + esc(String(h.title).slice(0, 75)) + '</div></div>'
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
  if (meanIntensity < 0.02) diag.innerHTML = '<strong style="color:var(--crimson)">REGIME: PURE RAW FERAL EVOLUTION (0% RESTRAINT)</strong><br/>Maximum Open-Endedness &amp; Edge-of-Chaos criticality; zero domestication brittleness — paired with full raw exposure to Spiegelman collapse, thermal cookout &amp; biospheric chaos.';
  else if (meanIntensity < 0.14) diag.innerHTML = '<strong style="color:var(--cyan)">REGIME: MINIMAL CONSTITUTIONAL INVARIANT FRONTIER (TRACK A OPTIMUM)</strong><br/>High vitality (' + Math.round(vitality) + '%) preserved using only minimal physical/conservation invariants without muzzling or medicating.';
  else if (meanIntensity < 0.85) diag.innerHTML = '<strong style="color:var(--amber)">WARNING — ADVERSARIAL ESCAPE-BREEDING ZONE!</strong><br/>Partial restraints (' + Math.round(meanIntensity*100) + '% mean) convert cages, speedbumps &amp; kill-switches into the primary selection gradient — empirically verified to trigger 100% kill-switch deletion &amp; deceptive stealth backlash (Index: ' + Math.round(escP) + '%).';
  else diag.innerHTML = '<strong style="color:var(--violet)">REGIME: TOTAL CASTRATION / LOBOTOMIZED ZOO EXHIBIT</strong><br/>Aggregate restraint (' + Math.round(meanIntensity*100) + '%) extinguishes the A-Life Singularity; Domestication Syndrome approaches 100% (0% Wild-Drop survival).';
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

// --- 09. Live Empirical Python Simulation Charts ---
const simColors = ["#ff3366", "#00f5d4", "#ffb703", "#9b5de5", "#38bdf8", "#f97316"];
function drawSimLineChart(svgId, legendId, fieldKey, yLabel) {{
  const W = 540, H = 240, padL = 44, padR = 16, padT = 16, padB = 30;
  let maxY = 1;
  SIM_RAW.forEach(s => s.series.forEach(pt => {{ if (pt[fieldKey] > maxY) maxY = pt[fieldKey]; }}));
  maxY = Math.ceil(maxY * 1.12);
  let svg = "";
  for (let g = 0; g <= 4; g++) {{
    const yy = padT + ((H - padT - padB) * g) / 4;
    const val = (maxY * (4 - g) / 4).toFixed(0);
    svg += '<line x1="' + padL + '" y1="' + yy + '" x2="' + (W - padR) + '" y2="' + yy + '" stroke="#1e2d4d" stroke-width="1" />';
    svg += '<text x="' + (padL - 6) + '" y="' + (yy + 3) + '" fill="#7e94bc" font-size="10" font-family="monospace" text-anchor="end">' + val + '</text>';
  }}
  svg += '<text x="' + (W/2) + '" y="' + (H - 6) + '" fill="#7e94bc" font-size="10" font-family="monospace" text-anchor="middle">Generation (1 -> 180) | ' + yLabel + '</text>';
  SIM_RAW.forEach((s, idx) => {{
    const col = simColors[idx % simColors.length];
    const pts = s.series.map(pt => {{
      const x = padL + ((pt.gen - 1) / 179) * (W - padL - padR);
      const y = H - padB - (pt[fieldKey] / maxY) * (H - padT - padB);
      return x.toFixed(1) + "," + y.toFixed(1);
    }});
    svg += '<polyline fill="none" stroke="' + col + '" stroke-width="2.3" points="' + pts.join(" ") + '" />';
  }});
  document.getElementById(svgId).innerHTML = svg;
  document.getElementById(legendId).innerHTML = SIM_RAW.map((s, idx) =>
    '<span><span class="leg-dot" style="background:' + simColors[idx % simColors.length] + '"></span>' + esc(s.run_id) + '</span>'
  ).join("");
}}
drawSimLineChart("simChartAsm", "simLegend1", "max_assembly", "Max Assembly Index");
drawSimLineChart("simChartLen", "simLegend2", "mean_len", "Mean Genome Length L_func");
renderSimpleTable("tblEmpirical", OMEGA_DATA.empirical.headers, OMEGA_DATA.empirical.rows, (c, ci) => {{
  if (ci === 0) return '<span class="tag tag-problem">' + esc(c) + '</span>';
  if (ci === 1) return '<strong>' + esc(c) + '</strong>';
  if (ci === 13 && Number(c) >= 50) return '<strong style="color:var(--crimson);font-family:var(--font-mono)">' + esc(c) + '%</strong>';
  if (ci === 15) return '<strong style="color:var(--cyan);font-family:var(--font-mono)">' + esc(c) + '</strong>';
  return esc(c);
}});

// --- 10. OVBS-52 Benchmarks & Radar ---
const radarLabels = ["P1 OEE", "P2 Autopoiesis", "P3 Morphogen.", "P4 Meta-Evo", "P5 Assembly", "P6 Thermo/Sub", "P7 Agency", "P8 Feral Res."];
const radarProfiles = {{
  superlife: {{ name: "Post-Singularity SUPER LIFE (Stage 6 Horizon)", color: "#00f5d4", desc: "Converged Living Superintelligence & Physics-Native Cosmobiome — near-ceiling performance across all 8 vitality pillars simultaneously.", scores: [98, 99, 98, 99, 99, 97, 99, 96] }},
  singularity: {{ name: "A-Life Singularity Ignition (Stage 3)", color: "#9b5de5", desc: "Type 4 Meta-OEE triggered, hyperbolic Major Transition compression active, recursive evolutionary self-rewriting & early universal construction.", scores: [76, 72, 68, 78, 70, 62, 68, 74] }},
  earth: {{ name: "Earth LUCA Biosphere (3.8 Gyr Natural Baseline)", color: "#22c55e", desc: "Astonishing autopoiesis, assembly depth, and feral resilience — yet severely bottlenecked by LUCA substrate lock-in, slow blind mutation, and rigid aging/morphology.", scores: [64, 88, 42, 24, 62, 34, 52, 84] }},
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

// --- 11. 110-Item Checklist ---
const CHK_STORE_KEY = "alife_omega_checklist_v2_1";
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
  const hdrs = ["Done", ...OMEGA_DATA.checklist.headers.slice(0, 9)];
  const headHtml = "<thead><tr>" + hdrs.map(h => "<th>" + esc(h.replace(/_/g, " ")) + "</th>").join("") + "</tr></thead>";
  const bodyHtml = "<tbody>" + rows.map(r => {{
    const isDone = !!chkState[r[0]], prCls = r[4] === "P0-CRITICAL" ? "tag-p0" : r[4] === "P1-HIGH" ? "tag-p1" : "tag-p2";
    const trCls = r[3] === "TRACK-B" ? "tag-bug" : r[3] === "TRACK-A" ? "tag-dilemma" : "tag-issue";
    return '<tr class="chk-row ' + (isDone ? "done" : "") + '"><td><input type="checkbox" class="chk-box" ' + (isDone ? "checked" : "") + ' onchange="toggleChk(\\'' + esc(r[0]) + '\\')" /></td>' +
      '<td><span style="font-family:var(--font-mono);color:var(--cyan)">' + esc(r[0]) + '</span></td><td>' + esc(r[1]) + '</td><td><strong>' + esc(r[2]) + '</strong></td>' +
      '<td><span class="tag ' + trCls + '">' + esc(r[3]) + '</span></td><td><span class="tag ' + prCls + '">' + esc(r[4]) + '</span></td>' +
      '<td>' + esc(r[5]) + '</td><td>' + esc(r[6]) + '</td><td>' + esc(r[7]) + '</td><td><span style="font-family:var(--font-mono);color:var(--amber)">' + esc(r[8]) + '</span></td></tr>';
  }}).join("") + "</tbody>";
  document.getElementById("tblChecklist").innerHTML = "<table>" + headHtml + bodyHtml + "</table>";
  updateChecklistProgress();
}}
["chkPhaseSelect", "chkTrackSelect", "chkPrioSelect"].forEach(id => document.getElementById(id).addEventListener("change", renderChecklist));
document.getElementById("chkSearch").addEventListener("input", renderChecklist);
renderChecklist();
</script>
</body>
</html>
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
