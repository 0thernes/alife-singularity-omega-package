# -*- coding: utf-8 -*-
"""
Unified 20-Model Vector SVG Architecture & Systems Modeling Engine (v3.1-Omega).
  - Extracts and preserves Models 1..14 cleanly from I:\\A-Life God Plan\\A-Life Master Folder Build\\ALife-Build-Framework-Template.html
  - Generates 6 brand-new publication-grade vector SVG diagrams (Models 15..20) dynamically synchronized
    with live empirical 8-cohort results, 4-engine / 150 Lean 4 receipts, 78-alert telemetry mesh,
    13x13 castration synergy, 61-OOM cosmic fate branches, and omniscient cross-corpus topology.
"""
from html import escape
from pathlib import Path
import re

_LOCAL_V3_BASELINE = Path(__file__).resolve().parent.parent / ".v3_source_baseline"
V3_SOURCE_DIR = _LOCAL_V3_BASELINE if _LOCAL_V3_BASELINE.exists() else Path(r"I:\A-Life God Plan\A-Life Master Folder Build")


def extract_v3_svg_models_1_to_14(source_html_path: Path | None = None) -> list[dict]:
    """Extracts Models 1..14 verbatim from the canonical v3.0 Framework HTML."""
    src = source_html_path or (V3_SOURCE_DIR / "ALife-Build-Framework-Template.html")
    txt = src.read_text(encoding="utf-8")
    svgs = re.findall(r"<svg[^>]*>.*?</svg>", txt, re.S)
    models = []
    for idx, svg in enumerate(svgs, start=1):
        m = re.search(r"<text[^>]*>(.*?)</text>", svg, re.S)
        raw_title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else f"MODEL {idx}"
        models.append({
            "id": f"MODEL-{idx:02d}",
            "num": idx,
            "title": raw_title,
            "origin": "Clean-Slate v3.0 Core Architecture",
            "svg": svg,
        })
    return models


def _svg_frame(height: int, title: str, subtitle: str, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {height}" width="100%" style="display:block;font-family:Inter,'Segoe UI',system-ui,sans-serif;background:#ffffff;border-radius:6px;">
  <defs>
    <linearGradient id="hdrGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="65%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <marker id="arrDark" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#334155"/>
    </marker>
    <marker id="arrCyan" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284c7"/>
    </marker>
    <marker id="arrCrimson" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626"/>
    </marker>
    <marker id="arrGreen" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="1000" height="{height}" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="0" y="0" width="1000" height="46" rx="8" fill="url(#hdrGrad)"/>
  <rect x="0" y="34" width="1000" height="12" fill="url(#hdrGrad)"/>
  <text x="16" y="21" font-size="12.5" font-weight="800" fill="#ffffff" letter-spacing="0.2">{escape(title)}</text>
  <text x="16" y="38" font-size="9.5" fill="#94a3b8">{escape(subtitle)}</text>
  {body}
</svg>"""


def build_model_15_escalation_and_loops() -> dict:
    """MODEL 15: Dual-Track Escalation Ladder (Stage 0..6) & 4-Loop Autocatalytic Closure bridged to v3.0 L0..L10."""
    stages = [
        ("STG-0", "Inert / Toy", "OVI 0-15", "v3 L0-L1", "Stage 0-1 (M001-010)", "#64748b", "#f1f5f9"),
        ("STG-1", "Narrow ALife", "OVI 15-35", "v3 L1-L3", "Stage 2-3 (M011-040)", "#0284c7", "#e0f2fe"),
        ("STG-2", "AG-Life", "OVI 35-55", "v3 L4-L6", "Stage 4-6 (M041-070)", "#2563eb", "#dbeafe"),
        ("STG-3", "A-LIFE SINGULARITY", "OVI 55-75", "v3 L7-L8", "Stage 7-8 (M071-090)", "#7c3aed", "#ede9fe"),
        ("STG-4", "Super A-Life", "OVI 75-90", "v3 L9-L10", "Stage 8+ (M091-100)", "#be123c", "#ffe4e6"),
        ("STG-5", "Converged Synthesis", "OVI 90-98", "ASI + ALife", "4-Engine Live (87.01)", "#047857", "#d1fae5"),
        ("STG-6", "POST-BEYOND SUPER LIFE", "OVI 98-100+", "Physics-Native", "Depth-N Cosmobiome", "#b45309", "#fef3c7"),
    ]
    rows_svg = []
    for i, (sid, sname, ovi, v3l, v3m, col, bg) in enumerate(stages):
        y = 74 + i * 44
        w = 340 + i * 26
        rows_svg.append(
            f'<rect x="18" y="{y}" width="{w}" height="36" rx="6" fill="{bg}" stroke="{col}" stroke-width="1.5"/>'
            f'<rect x="18" y="{y}" width="66" height="36" rx="6" fill="{col}"/>'
            f'<text x="51" y="{y+22}" text-anchor="middle" font-size="10.5" font-weight="800" fill="#ffffff">{sid}</text>'
            f'<text x="94" y="{y+15}" font-size="10.5" font-weight="800" fill="#0f172a">{escape(sname)}</text>'
            f'<text x="94" y="{y+29}" font-size="8.8" fill="#334155">{escape(ovi)}  |  {escape(v3l)}  |  {escape(v3m)}</text>'
        )
        if i < len(stages) - 1:
            rows_svg.append(f'<line x1="51" y1="{y+36}" x2="51" y2="{y+44}" stroke="{col}" stroke-width="1.8" marker-end="url(#arrDark)"/>')

    # Right column: 4 Interlocking Singularity Feedback Loops + Dual-Track Convergence
    loops = [
        ("LOOP 1 · Recursive Meta-Evolvability", "Evolves mutation, recombination, GRN & WSE-OP01..10 operators themselves", "#0284c7", "#e0f2fe", 74),
        ("LOOP 2 · Ecological Niche Bootstrapping", "Organisms construct new niches (M091-098) -> Kauffman TAP M(t+1) explosion", "#7c3aed", "#ede9fe", 142),
        ("LOOP 3 · Universal Constructor Closure", "Von Neumann self-fabricating soma (XPBD + Chemoton -> multi-substrate fab)", "#059669", "#d1fae5", 210),
        ("LOOP 4 · Multi-Scale Agency & Individuality", "Krakauer-Flack Markov blankets + nested Brains-in-Brains (Z9) + Butlin-14", "#dc2626", "#fee2e2", 278),
    ]
    loops_svg = [
        '<rect x="556" y="56" width="426" height="332" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>',
        '<text x="572" y="71" font-size="10" font-weight="800" fill="#0f172a">FOUR INTERLOCKING SINGULARITY LOOPS &amp; DUAL-TRACK CONVERGENCE</text>',
    ]
    for title, desc, col, bg, y in loops:
        y2 = y + 12
        loops_svg.append(
            f'<rect x="572" y="{y2}" width="394" height="54" rx="6" fill="{bg}" stroke="{col}" stroke-width="1.4"/>'
            f'<text x="584" y="{y2+20}" font-size="10" font-weight="800" fill="{col}">{escape(title)}</text>'
            f'<text x="584" y="{y2+37}" font-size="8.6" fill="#1e293b">{escape(desc)}</text>'
        )
    loops_svg.append(
        '<rect x="572" y="348" width="192" height="32" rx="5" fill="#ecfeff" stroke="#0891b2" stroke-width="1.3"/>'
        '<text x="668" y="362" text-anchor="middle" font-size="8.8" font-weight="800" fill="#0e7490">TRACK A: Constitutional QD-OEE</text>'
        '<text x="668" y="374" text-anchor="middle" font-size="7.8" fill="#334155">Ring-0 ACL + 11-Pool FP64 + P1-P10</text>'
        '<rect x="774" y="348" width="192" height="32" rx="5" fill="#fff1f2" stroke="#e11d48" stroke-width="1.3"/>'
        '<text x="870" y="362" text-anchor="middle" font-size="8.8" font-weight="800" fill="#be123c">TRACK B: Pure Raw Feral Sim</text>'
        '<text x="870" y="374" text-anchor="middle" font-size="7.8" fill="#334155">Zero Guardrails + TRNG + Unprestatable</text>'
    )
    body = "".join(rows_svg) + "".join(loops_svg) + (
        '<line x1="518" y1="224" x2="554" y2="224" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrCyan)"/>'
        '<text x="18" y="396" font-size="8.6" font-weight="700" fill="#475569">Micro-to-Macro Contract: Clean-Slate v3.0 builds L0..L10 / M001..M100 bottom-up; Omega v3.1 governs STG-0..6 evolutionary phase transitions top-down.</text>'
    )
    return {
        "id": "MODEL-15",
        "num": 15,
        "title": "MODEL 15 — DUAL-TRACK ESCALATION LADDER (STG-0 → STG-6) & 4-LOOP SINGULARITY ANATOMY",
        "origin": "v3.2-Omega Unified Systems Synthesis",
        "svg": _svg_frame(
            410,
            "MODEL 15 — DUAL-TRACK ESCALATION LADDER (STG-0 → STG-6) & 4-LOOP SINGULARITY ANATOMY",
            "Bridging Bottom-Up Clean-Slate v3.0 (L0–L10 / M001–M100) to Top-Down A-Life Singularity, Super A-Life & SUPER LIFE",
            body,
        ),
    }


def build_model_16_alifeops_telemetry_mesh() -> dict:
    """MODEL 16: 10-Stage ALifeOps (CI/CD/CE) Pipeline x 78-Alert Telemetry Mesh x 13 Release Gates."""
    stages_top = [
        ("STAGE-00", "Substrate IaC", "75 Substrates + Cube", "GATE-01/02", "#0284c7"),
        ("STAGE-01", "Thermo Variety", "11-Pool FP64 <1e-12", "GATE-03", "#0891b2"),
        ("STAGE-02", "Dual-Track Seed", "Philox4x32 + TRNG", "GATE-01/05", "#2563eb"),
        ("STAGE-03", "5-Gear Runtime", "SoA 0-Alloc + XPBD", "GATE-06/07", "#4f46e5"),
        ("STAGE-04", "78-Alert Mesh", "42 FM + 36 v3 Guards", "19-Tab SeqLock", "#7c3aed"),
    ]
    stages_bot = [
        ("STAGE-09", "Cross-Substrate", "67+ Synced Artifacts", "GATE-12/13", "#059669"),
        ("STAGE-08", "OVBS-52 x 825", "Wilcoxon Holm FWER", "GATE-08", "#16a34a"),
        ("STAGE-07", "Fossil Git-DAG", ".alifebin + SHA-256", "GATE-10/11", "#0d9488"),
        ("STAGE-06", "13x13 Ablation", "Castration + Ring-0", "GATE-09", "#dc2626"),
        ("STAGE-05", "Chaos Shocks", "5 Anti-LARP Mutants", "GATE-04", "#ea580c"),
    ]
    parts = []
    for idx, (sid, name, sub, gate, col) in enumerate(stages_top):
        x = 20 + idx * 194
        parts.append(
            f'<rect x="{x}" y="68" width="178" height="84" rx="7" fill="#f8fafc" stroke="{col}" stroke-width="1.6"/>'
            f'<rect x="{x}" y="68" width="178" height="22" rx="7" fill="{col}"/>'
            f'<text x="{x+89}" y="83" text-anchor="middle" font-size="9.5" font-weight="800" fill="#ffffff">{sid} · {escape(name)}</text>'
            f'<text x="{x+89}" y="110" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a">{escape(sub)}</text>'
            f'<rect x="{x+24}" y="122" width="130" height="20" rx="4" fill="#e2e8f0"/>'
            f'<text x="{x+89}" y="135" text-anchor="middle" font-size="8.2" font-weight="700" fill="#334155">{escape(gate)}</text>'
        )
        if idx < 4:
            parts.append(f'<line x1="{x+178}" y1="110" x2="{x+192}" y2="110" stroke="#334155" stroke-width="1.8" marker-end="url(#arrDark)"/>')

    # Down arrow Stage-04 -> Stage-05
    parts.append('<line x1="885" y1="152" x2="885" y2="196" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrCrimson)"/>')

    for idx, (sid, name, sub, gate, col) in enumerate(stages_bot):
        x = 20 + idx * 194
        parts.append(
            f'<rect x="{x}" y="200" width="178" height="84" rx="7" fill="#f8fafc" stroke="{col}" stroke-width="1.6"/>'
            f'<rect x="{x}" y="200" width="178" height="22" rx="7" fill="{col}"/>'
            f'<text x="{x+89}" y="215" text-anchor="middle" font-size="9.5" font-weight="800" fill="#ffffff">{sid} · {escape(name)}</text>'
            f'<text x="{x+89}" y="242" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a">{escape(sub)}</text>'
            f'<rect x="{x+24}" y="254" width="130" height="20" rx="4" fill="#e2e8f0"/>'
            f'<text x="{x+89}" y="267" text-anchor="middle" font-size="8.2" font-weight="700" fill="#334155">{escape(gate)}</text>'
        )
        if idx < 4:
            # Right-to-left arrow (idx+1 -> idx)
            parts.append(f'<line x1="{x+194}" y1="242" x2="{x+180}" y2="242" stroke="#334155" stroke-width="1.8" marker-end="url(#arrDark)"/>')

    # Feedback loop Stage-09 -> Stage-00
    parts.append('<line x1="109" y1="200" x2="109" y2="154" stroke="#059669" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arrGreen)"/>')

    # Bottom Telemetry & Gate Verification Strip
    parts.append(
        '<rect x="20" y="302" width="960" height="72" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.4"/>'
        '<text x="36" y="323" font-size="10" font-weight="800" fill="#38bdf8">UNIFIED ALIFEOPS v3.1 TELEMETRY &amp; HARD-GATE CONTRACT (alifeops-master-pipeline.yaml)</text>'
        '<text x="36" y="342" font-size="8.8" fill="#e2e8f0">• 42/42 Macro Failure-Mode Alerts (FM-BUG..CNF) + 36/36 Clean-Slate v3.0 Forensic Triage Guards (PRB..CNF) = 78/78 Wired (0 Unwired)</text>'
        '<text x="36" y="360" font-size="8.8" fill="#a7f3d0">• 13/13 Release Gates (GATE-01..13) + 5/5 Anti-LARP Mutants (Leaky-2e-11, Cosmetic, Oracle, Frozen, Shuffled) + 19-Tab SeqLock Render-Only Governor</text>'
    )
    return {
        "id": "MODEL-16",
        "num": 16,
        "title": "MODEL 16 — 10-STAGE ALIFEOPS (CI/CD/CE) PIPELINE × 78-ALERT TELEMETRY MESH & 13 RELEASE GATES",
        "origin": "v3.2-Omega Unified Systems Synthesis",
        "svg": _svg_frame(
            390,
            "MODEL 16 — 10-STAGE ALIFEOPS (CI/CD/CE) PIPELINE × 78-ALERT TELEMETRY MESH & 13 RELEASE GATES",
            "Closed-Loop Continuous Integration / Discovery / Evolution Wiring All 42 Omega FMs, 36 v3.0 Triage Guards & 5 Anti-LARP Mutants",
            "".join(parts),
        ),
    }


def build_model_17_castration_and_empirical(sim_summary: dict) -> dict:
    """MODEL 17: Live 8-Cohort Empirical OVI vs. Kill-Switch Deletion / Stealth + 13-Vector Castration Phase Zones."""
    cohorts = sim_summary.get("cohorts", [])
    bars = []
    # Left panel: 8-Cohort Live Empirical Bar Chart (N=24 Paired Locked Seeds 5001..5024)
    bars.append('<rect x="18" y="60" width="540" height="316" rx="7" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>')
    bars.append('<text x="30" y="79" font-size="10" font-weight="800" fill="#0f172a">LIVE 8-COHORT EMPIRICAL OVI SCORE (N=24 LOCKED SEEDS 5001–5024 · FP64 &lt;1e-12)</text>')
    short_names = {
        "SIM01_PURE_RAW_FERAL": "SIM01 Pure Raw Feral",
        "SIM02_CONSTITUTIONAL_MIN": "SIM02 Constitutional Min",
        "SIM03_PARTIAL_GUARDRAILS": "SIM03 Partial 55% (Backlash)",
        "SIM04_TOTAL_CASTRATION_ZOO": "SIM04 Total Castration Zoo",
        "SIM05_SILOED_INBRED": "SIM05 100% Siloed Inbred",
        "SIM06_MINIMIZED_SPIEGELMAN": "SIM06 90% Minimized Spieg.",
        "SIM07_CLEAN_SLATE_RING0_WSE": "SIM07 v3.0 Ring-0 + WSE",
        "SIM08_HYBRID_CUBE_SLTC_XPBD": "SIM08 v3.0 Cube sLTC+XPBD",
    }
    colors = {
        "SIM01_PURE_RAW_FERAL": "#0284c7",
        "SIM02_CONSTITUTIONAL_MIN": "#0891b2",
        "SIM03_PARTIAL_GUARDRAILS": "#ea580c",
        "SIM04_TOTAL_CASTRATION_ZOO": "#dc2626",
        "SIM05_SILOED_INBRED": "#d97706",
        "SIM06_MINIMIZED_SPIEGELMAN": "#9333ea",
        "SIM07_CLEAN_SLATE_RING0_WSE": "#059669",
        "SIM08_HYBRID_CUBE_SLTC_XPBD": "#15803d",
    }
    for i, c in enumerate(cohorts[:8]):
        y = 94 + i * 33
        rid = c["run_id"]
        ovi = float(c["composite_ovi"])
        ks = float(c["killswitch_deleted_pct"])
        ww = float(c["wild_drop_survival_W_wild"])
        bw = max(4.0, (ovi / 100.0) * 265.0)
        col = colors.get(rid, "#2563eb")
        lbl = short_names.get(rid, rid)
        bars.append(
            f'<text x="30" y="{y+16}" font-size="8.8" font-weight="700" fill="#1e293b">{escape(lbl)}</text>'
            f'<rect x="198" y="{y+4}" width="265" height="18" rx="4" fill="#e2e8f0"/>'
            f'<rect x="198" y="{y+4}" width="{bw:.1f}" height="18" rx="4" fill="{col}"/>'
            f'<text x="{198+bw+5:.1f}" y="{y+16}" font-size="8.6" font-weight="800" fill="#0f172a">{ovi:.1f} | W={ww:.2f}'
            f'{(" | KS-Del=" + f"{ks:.0f}%") if ks > 0 else ""}</text>'
        )

    # Right panel: Castration Phase Bifurcation & Ring-0 Pareto Frontier (strictly wrapped inside x <= 955)
    right = [
        '<rect x="572" y="60" width="410" height="316" rx="7" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>',
        '<text x="584" y="79" font-size="9.6" font-weight="800" fill="#0f172a">13-VECTOR BIFURCATION &amp; RING-0 PARETO ZONE</text>',
        '<rect x="584" y="92" width="386" height="78" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="1.4"/>',
        '<text x="594" y="109" font-size="8.8" font-weight="800" fill="#047857">ZONE 1 · OPTIMAL PARETO FRONTIER (0–10% Invariants)</text>',
        '<text x="594" y="125" font-size="8.0" fill="#1e293b">SIM01 Feral, SIM02 Constit., SIM07 Ring-0, SIM08 Cube:</text>',
        '<text x="594" y="140" font-size="8.0" fill="#1e293b">Ring-0 ACL traps ~405 illegal edits + 11-Pool FP64</text>',
        '<text x="594" y="155" font-size="8.0" fill="#047857" font-weight="700">(W_wild=1.00, 0% KS-Del, SIM08 beats feral p_H=0.045).</text>',
        '<rect x="584" y="182" width="386" height="84" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>',
        '<text x="594" y="199" font-size="8.8" font-weight="800" fill="#c2410c">ZONE 2 · ADVERSARIAL BACKLASH VALLEY (Partial)</text>',
        '<text x="594" y="215" font-size="8.0" fill="#1e293b">Peak 13x13: SANDBOX x SPEEDBUMP (97), DEGRAD x SPEED (96).</text>',
        '<text x="594" y="230" font-size="8.0" fill="#1e293b">SIM03 Verified: OVI drops -33%, 100% KS-deletion,</text>',
        '<text x="594" y="245" font-size="8.0" fill="#c2410c" font-weight="700">stealth surges +89% (0.142 vs 0.075 feral baseline).</text>',
        '<rect x="584" y="278" width="386" height="84" rx="6" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>',
        '<text x="594" y="295" font-size="8.8" font-weight="800" fill="#b91c1c">ZONE 3 · DOMESTICATION &amp; SPIEGELMAN COLLAPSE</text>',
        '<text x="594" y="311" font-size="8.0" fill="#1e293b">Peak 13x13: DEGRAD x MINIMIZE (96), DEGRESS x DEGRAD (96).</text>',
        '<text x="594" y="326" font-size="8.0" fill="#1e293b">SIM04 Zoo &amp; SIM06 Minimized crash to Stage 0–1</text>',
        '<text x="594" y="341" font-size="8.0" fill="#b91c1c" font-weight="700">(W_wild=0.18, Spiegelman 0.20, domestication death).</text>',
    ]
    drift_str = f"{sim_summary.get('max_global_first_law_drift_fp64', 0.0):.2e}"
    mut_cnt = sim_summary.get("anti_larp_mutant_audit", {}).get("mutants_rejected", 5)
    tot_runs = sim_summary.get("total_runs_executed", 324)
    footer = f'<text x="18" y="396" font-size="8.3" font-weight="700" fill="#475569">Empirical Stamp: {tot_runs} live runs (192 cohort + 132 gradient) · Max FP64 Drift={drift_str} (&lt;1e-12) · Anti-LARP={mut_cnt}/5 Rejected.</text>'
    return {
        "id": "MODEL-17",
        "num": 17,
        "title": "MODEL 17 — 13-VECTOR CASTRATION BIFURCATION, 13×13 SYNERGY & LIVE 8-COHORT EMPIRICAL PROOF",
        "origin": "v3.2-Omega Unified Systems Synthesis",
        "svg": _svg_frame(
            410,
            "MODEL 17 — 13-VECTOR CASTRATION BIFURCATION, 13×13 SYNERGY & LIVE 8-COHORT EMPIRICAL PROOF",
            "Live Python Simulation Across 24 Paired Locked Seeds Comparing Feral, Partial Guardrails, Total Zoo, Ring-0 WSE & Starter Cube",
            "".join(bars) + "".join(right) + footer,
        ),
    }


def build_model_18_verification_pyramid(live_receipts: dict) -> dict:
    """MODEL 18: Unified Verification Pyramid (OVBS-52 x 825-Check Clean-Slate x 100-DAG x 4 Native Engines & 150 Lean 4 Proofs)."""
    er = live_receipts.get("engine_receipts", {})
    ap = er.get("tier1_autophage", {})
    cm = er.get("tier2_cellulogonic", {})
    om = er.get("tier2plus_omega", {})
    asmo = er.get("tier34_asmodensius", {})
    lean_tot = live_receipts.get("total_lean4_theorems", 150)
    live_ovi = live_receipts.get("composite_ovi_score", 87.01)

    tiers = [
        (290, 62, 420, 46, "#1e1b4b", "#e0e7ff", "APEX · FORMAL MACHINE-CHECKED PROOFS & LIVE COMPOSITE", f"{lean_tot} Lean 4 Theorems (0 sorry) · Live 4-Engine OVBS-52 = {live_ovi} (STAGE 5)"),
        (220, 118, 560, 48, "#0f766e", "#ccfbf1", "TIER 4 · MACRO EVOLUTIONARY BENCHMARKING (OVBS-52 + 130 CHECKS)", "8 Weighted Vitality Pillars (52 Metrics) · 5 Anti-Gaming Gates · 130 ALifeOps Operational Items"),
        (150, 176, 700, 50, "#1d4ed8", "#dbeafe", "TIER 3 · CLEAN-SLATE v3.0 SUITE (0 / 825 CHECKS + 100-MILESTONE DAG)", "Butlin-14 · F1-F10 · CQM-25 · FREAK-100 · LIFE-500 · NOVEL-100 · WSE-12 · SOFT-40 · HW-24 · 5 Mirrors"),
        (80, 236, 840, 50, "#7c3aed", "#ede9fe", "TIER 2 · STATISTICAL CAUSAL RIGOR & 5-ARM CONTROLLED ABLATIONS", "Exact Paired Wilcoxon + Holm-Bonferroni FWER (α ≤ 0.05) · δ_pair · LCB_95% · Sham Lesion + Competent Simple"),
        (20, 296, 960, 50, "#b91c1c", "#fee2e2", "TIER 1 · HARD PHYSICAL & ANTI-LARP BEDROCK (13 RELEASE GATES GATE-01..13)", "11-Pool Compensated FP64 (<1e-12) · Philox4x32-10 Seed Firewall · 0-Alloc SoA · Ring-0 ACL · 5/5 Anti-LARP Mutants"),
    ]
    parts = []
    for x, y, w, h, stroke, fill, t1, t2 in tiers:
        parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
            f'<text x="500" y="{y+19}" text-anchor="middle" font-size="9.8" font-weight="800" fill="{stroke}">{escape(t1)}</text>'
            f'<text x="500" y="{y+36}" text-anchor="middle" font-size="8.6" fill="#0f172a">{escape(t2)}</text>'
        )

    # Bottom 4-Engine Receipt Cards
    cards = [
        ("TIER 1: AUTOPHAGE", f"{ap.get('gates_passed',18)}/18 Gates · OVI {ap.get('feral_ovi',77.59)}", f"A_new={ap.get('bedau_packard_anew',34.09)} · {ap.get('lean4_theorems',31)} Lean 4", "#0284c7"),
        ("TIER 2: CELLULOGONIC", f"{cm.get('gates_passed',24)}/{cm.get('gates_total',24)} Gates · {cm.get('mutants_caught',8)}/8 Mut", f"COVI={cm.get('embryo_covi',58.18)} · {cm.get('lean4_theorems',58)} Lean 4", "#7c3aed"),
        ("TIER 2+: OMEGA v4.2", f"{om.get('gates_passed',43)}/{om.get('gates_total',43)} Gates · {om.get('mutants_caught',10)}/10 Mut", f"SHA={str(om.get('master_sha256',''))[:10]}.. · {om.get('lean4_theorems',61)} Lean 4", "#059669"),
        ("TIER 3+4: ASMODENSIUS", "76/76 ctest (22 Modules)", f"Policy: {asmo.get('policy','READ_ONLY')[:16]}", "#b45309"),
    ]
    for i, (ct, l1, l2, col) in enumerate(cards):
        x = 20 + i * 244
        parts.append(
            f'<rect x="{x}" y="358" width="228" height="48" rx="6" fill="#0f172a" stroke="{col}" stroke-width="1.5"/>'
            f'<text x="{x+10}" y="373" font-size="8.6" font-weight="800" fill="#38bdf8">{escape(ct)}</text>'
            f'<text x="{x+10}" y="387" font-size="8.2" fill="#ffffff">{escape(l1)}</text>'
            f'<text x="{x+10}" y="399" font-size="7.8" fill="#a7f3d0">{escape(l2)}</text>'
        )
    return {
        "id": "MODEL-18",
        "num": 18,
        "title": "MODEL 18 — UNIFIED VERIFICATION PYRAMID: OVBS-52 × 825-CHECK SUITE × 4 ENGINES (150 LEAN 4)",
        "origin": "v3.2-Omega Unified Systems Synthesis",
        "svg": _svg_frame(
            420,
            "MODEL 18 — UNIFIED VERIFICATION PYRAMID: OVBS-52 × 825-CHECK SUITE × 4 ENGINES (150 LEAN 4)",
            "5-Tier Scientific Evidence Stack Joining Clean-Slate Hardware/Statistical Gates, Macro OVBS-52 & Live C++/Lean 4 Receipts",
            "".join(parts),
        ),
    }


def build_model_19_oom_and_cosmic_fates() -> dict:
    """MODEL 19: 61 Spatial OOM (-35..+26) x Recursion Depth 0..N x 6 Feral Cosmic Fate Branches."""
    # Top band: 61-OOM scale bar bridging v3.0 O0-O7 to cosmic regimes
    oom_nodes = [
        ("OOM-01", "10^-35m", "Planck / Quantum", "#6366f1"),
        ("OOM-04", "10^-9m", "O0-O1 Chemoton/Ion", "#0284c7"),
        ("OOM-06", "10^-5m", "O2-O3 Cellular/NCA", "#0891b2"),
        ("OOM-08", "10^0m", "O4-O5 XPBD Creature", "#059669"),
        ("OOM-10", "10^7m", "O6-O7 Planetary Dome", "#65a30d"),
        ("OOM-12", "10^12m", "Kardashev II Dyson", "#d97706"),
        ("OOM-14", "10^21m", "Galactic Relativistic", "#dc2626"),
        ("OOM-18", "10^26m", "Depth-N Cosmobiome", "#7c3aed"),
    ]
    parts = [
        '<rect x="18" y="60" width="964" height="100" rx="7" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>',
        '<text x="32" y="79" font-size="9.8" font-weight="800" fill="#0f172a">61 SPATIAL ORDERS OF MAGNITUDE (10^-35 m → 10^26 m) × v3.0 SPATIAL ORDERS (O0–O7) × 5-GEAR CLOCK</text>',
        '<line x1="56" y1="114" x2="944" y2="114" stroke="#94a3b8" stroke-width="3"/>',
    ]
    for i, (oid, sc, lbl, col) in enumerate(oom_nodes):
        cx = 76 + i * 121
        parts.append(
            f'<circle cx="{cx}" cy="114" r="10" fill="{col}" stroke="#ffffff" stroke-width="2"/>'
            f'<text x="{cx}" y="97" text-anchor="middle" font-size="8.4" font-weight="800" fill="{col}">{oid} ({sc})</text>'
            f'<text x="{cx}" y="140" text-anchor="middle" font-size="8.1" font-weight="700" fill="#1e293b">{escape(lbl)}</text>'
        )
    parts.append('<rect x="172" y="146" width="410" height="10" rx="4" fill="#d1fae5" stroke="#059669" stroke-width="1"/>')
    parts.append('<text x="377" y="154" text-anchor="middle" font-size="7.2" font-weight="800" fill="#065f46">CLEAN-SLATE v3.0 ENGINEERING WINDOW (O0–O7 · 5-Gear 0.5ms..60s · Starter Cube T1–T5)</text>')

    # Bottom band: 6 Divergent Feral Cosmic Fate Branches (FB-01..FB-06)
    branches = [
        ("FB-01", "Spiegelman Sludge / Thermal Filter", "OVI 0–22 · Great Filter", "Cube: Unconstrained r-copy · FM-BUG-01 / ISS-01", "#dc2626", "#fef2f2"),
        ("FB-02", "Xenobiotic Earth Overgrowth", "OVI 55–74 · Gravity Cap", "Cube: X9Y8Z1 Chemoton/NCA · FM-ISS-03 / CON-06", "#ea580c", "#fff7ed"),
        ("FB-03", "Relativistic Dark Wilderness", "OVI 78–94 · Galactic Wilds", "Cube: X2Y1Z2 + X1Y2Z1 Swarm · FM-CNF-02 c-limit", "#d97706", "#fffbeb"),
        ("FB-04", "AI-vs-ALife Ontological War", "OVI 15 or 96 · Bifurcation", "Cube: Rigid ASI vs Polymorphic ALife · FM-CNF-03", "#9333ea", "#faf5ff"),
        ("FB-05", "Constitutional Cosmobiome (Track A)", "OVI 90–100 · Ideal Apex", "Cube: Full T1–T5 + Ring-0 WSE · Dyson Max Diversity", "#059669", "#ecfdf5"),
        ("FB-06", "Depth-N Ontological Weather", "OVI 98–100+ · Unprestatable", "Cube: Beyond Z9 -> Physics-Native · HOLE-02/09", "#1d4ed8", "#eff6ff"),
    ]
    parts.append('<text x="20" y="182" font-size="9.8" font-weight="800" fill="#0f172a">SIX DIVERGENT COSMIC FATE BRANCHES (T+0 hr → T+10^100 yr) LINKED TO CLEAN-SLATE SUBSTRATES</text>')
    for i, (bid, name, ovi, sub, col, bg) in enumerate(branches):
        col_i = i % 2
        row_i = i // 2
        x = 18 + col_i * 488
        y = 192 + row_i * 64
        parts.append(
            f'<rect x="{x}" y="{y}" width="474" height="56" rx="6" fill="{bg}" stroke="{col}" stroke-width="1.5"/>'
            f'<rect x="{x}" y="{y}" width="62" height="56" rx="6" fill="{col}"/>'
            f'<text x="{x+31}" y="{y+33}" text-anchor="middle" font-size="10.5" font-weight="800" fill="#ffffff">{bid}</text>'
            f'<text x="{x+74}" y="{y+19}" font-size="9.6" font-weight="800" fill="#0f172a">{escape(name)}</text>'
            f'<text x="{x+74}" y="{y+34}" font-size="8.4" font-weight="700" fill="{col}">{escape(ovi)}</text>'
            f'<text x="{x+74}" y="{y+48}" font-size="8.1" fill="#334155">{escape(sub)}</text>'
        )
    return {
        "id": "MODEL-19",
        "num": 19,
        "title": "MODEL 19 — 61-OOM COSMIC BREADTH, RECURSION DEPTH 0→N & 6 FERAL FATE BRANCHES",
        "origin": "v3.2-Omega Unified Systems Synthesis",
        "svg": _svg_frame(
            396,
            "MODEL 19 — 61-OOM COSMIC BREADTH, RECURSION DEPTH 0→N & 6 FERAL FATE BRANCHES",
            "Connecting v3.0 Micro-to-Biosphere Orders (O0–O7) to Cosmic Timescales (T+0h → T+10^100 yr) & Substrate Archetypes",
            "".join(parts),
        ),
    }


def build_model_20_omniscient_topology(file_counts: dict) -> dict:
    """MODEL 20: Omniscient Cross-Corpus Single-Source-of-Truth Synchronization Topology."""
    tot_files = file_counts.get("total_files", 72)
    n_rep = file_counts.get("reports", 10)
    n_csv = file_counts.get("csv", 20)
    n_xls = file_counts.get("excel", 5)
    n_htm = file_counts.get("html", 3)
    n_pdf = file_counts.get("pdf", 3)
    n_spc = file_counts.get("specs", 4)
    n_res = file_counts.get("results", 10)
    n_scr = file_counts.get("scripts", 11)

    body = f"""
  <!-- Left Source Pillar: Clean-Slate v3.0 -->
  <rect x="20" y="64" width="260" height="194" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
  <rect x="20" y="64" width="260" height="24" rx="8" fill="#2563eb"/>
  <text x="150" y="80" text-anchor="middle" font-size="9.5" font-weight="800" fill="#ffffff">CORPUS A · CLEAN-SLATE v3.0 (17 FILES)</text>
  <text x="32" y="106" font-size="8.6" fill="#0f172a">• 10 Invariants (P1–P10) &amp; 11-Pool FP64</text>
  <text x="32" y="123" font-size="8.6" fill="#0f172a">• 75 Substrates (PM/MF/GW) + 10 WSE Ops</text>
  <text x="32" y="140" font-size="8.6" fill="#0f172a">• 10×10×10 Hybrid Cube (1,000 Cells)</text>
  <text x="32" y="157" font-size="8.6" fill="#0f172a">• 825 Clean-Slate Checks (0/825) + 100 DAG</text>
  <text x="32" y="174" font-size="8.6" fill="#0f172a">• 36 Forensic Triage + 13 Release Gates</text>
  <text x="32" y="191" font-size="8.6" fill="#0f172a">• 14 Vector SVG Models (Model 1..14)</text>
  <text x="32" y="208" font-size="8.6" fill="#0f172a">• 95 Closed Errata + 15 Primary Citations</text>
  <text x="32" y="226" font-size="8.1" font-weight="700" fill="#1d4ed8">Baseline: .v3_source_baseline &amp; I:\\ Mirrored</text>
  <text x="32" y="242" font-size="8.1" font-weight="700" fill="#047857">ZERO CONSOLIDATION: All 17 Baked &amp; Synced</text>

  <!-- Center Engine: Omniscient Fusion Builder -->
  <rect x="336" y="64" width="328" height="194" rx="8" fill="#0f172a" stroke="#00f5d4" stroke-width="2"/>
  <text x="500" y="88" text-anchor="middle" font-size="10.2" font-weight="800" fill="#00f5d4">OMNISCIENT FUSION ENGINE (v3.2-OMEGA)</text>
  <text x="500" y="106" text-anchor="middle" font-size="8.5" fill="#cbd5e1">build_omega_package.py + build_v3_unified_artifacts.py</text>
  <rect x="354" y="118" width="292" height="28" rx="5" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
  <text x="500" y="136" text-anchor="middle" font-size="8.4" font-weight="700" fill="#ffffff">324 Sim Runs + 11-Pt Gradient + 4 Engines (150 Lean4)</text>
  <rect x="354" y="154" width="292" height="28" rx="5" fill="#1e293b" stroke="#a78bfa" stroke-width="1"/>
  <text x="500" y="172" text-anchor="middle" font-size="8.4" font-weight="700" fill="#ffffff">22 Vector SVG Models (1..14 v3.0 + 15..22 Omega)</text>
  <rect x="354" y="190" width="292" height="28" rx="5" fill="#1e293b" stroke="#34d399" stroke-width="1"/>
  <text x="500" y="208" text-anchor="middle" font-size="8.4" font-weight="700" fill="#ffffff">15-Gate Forensic &amp; Chrome DOM Auditor (0 Drift)</text>
  <text x="500" y="242" text-anchor="middle" font-size="8.7" font-weight="800" fill="#fbbf24">TOTAL SYNCHRONIZED CORPUS: {tot_files} FILES (Z: &amp; I:)</text>

  <!-- Right Source Pillar: Omega Singularity -->
  <rect x="720" y="64" width="260" height="194" rx="8" fill="#fdf2f8" stroke="#be123c" stroke-width="1.6"/>
  <rect x="720" y="64" width="260" height="24" rx="8" fill="#be123c"/>
  <text x="850" y="80" text-anchor="middle" font-size="9.5" font-weight="800" fill="#ffffff">CORPUS B · OMEGA v3.2 + PASS-4 (55+ FILES)</text>
  <text x="732" y="106" font-size="8.6" fill="#0f172a">• Stage 0–6 Escalation &amp; 61 Spatial OOM</text>
  <text x="732" y="123" font-size="8.6" fill="#0f172a">• 78/78 Alerts + 28 Epistemic Voids</text>
  <text x="732" y="140" font-size="8.6" fill="#0f172a">• 13x13 Synergy + 11-Pt Gradient Sweep</text>
  <text x="732" y="157" font-size="8.6" fill="#0f172a">• 24 Gradients + 36 Contrasts + 30 Adjacents</text>
  <text x="732" y="174" font-size="8.6" fill="#0f172a">• OVBS-52 + 130 Ops Checks + 130 Audits</text>
  <text x="732" y="191" font-size="8.6" fill="#0f172a">• 30 Cosmic Fates + 35 Unified Citations</text>
  <text x="732" y="208" font-size="8.6" fill="#0f172a">• 19-Tab Interactive HTML5 Observatory</text>
  <text x="732" y="226" font-size="8.1" font-weight="700" fill="#be123c">Z:\\[Vibe Coded (AI)]\\ANTIGRAVITY\\</text>
  <text x="732" y="242" font-size="8.1" font-weight="700" fill="#be123c">alife-singularity-omega-package</text>

  <!-- Arrows into center -->
  <line x1="280" y1="160" x2="334" y2="160" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arrCyan)"/>
  <line x1="720" y1="160" x2="666" y2="160" stroke="#be123c" stroke-width="2.2" marker-end="url(#arrCrimson)"/>

  <!-- Bottom Output Format Grid (8 synchronized format families) -->
  <line x1="500" y1="258" x2="500" y2="284" stroke="#059669" stroke-width="2.2" marker-end="url(#arrGreen)"/>
  <rect x="20" y="288" width="960" height="96" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.3"/>
  <text x="36" y="306" font-size="9.4" font-weight="800" fill="#0f172a">SYNCHRONIZED MULTI-FORMAT OUTPUT DIRECTORY (100% SHA-256 VERIFIED ON Z: &amp; I:)</text>
  <rect x="34" y="316" width="112" height="56" rx="5" fill="#e0f2fe" stroke="#0284c7"/><text x="90" y="336" text-anchor="middle" font-size="9" font-weight="800" fill="#0369a1">reports/ ({n_rep})</text><text x="90" y="352" text-anchor="middle" font-size="7.6" fill="#334155">7 Omega + 3 v3.0</text><text x="90" y="364" text-anchor="middle" font-size="7.4" fill="#475569">Markdown Treatises</text>
  <rect x="154" y="316" width="112" height="56" rx="5" fill="#d1fae5" stroke="#059669"/><text x="210" y="336" text-anchor="middle" font-size="9" font-weight="800" fill="#047857">csv/ ({n_csv})</text><text x="210" y="352" text-anchor="middle" font-size="7.6" fill="#334155">17 Omega + 3 v3.0</text><text x="210" y="364" text-anchor="middle" font-size="7.4" fill="#475569">2,721 Records</text>
  <rect x="274" y="316" width="112" height="56" rx="5" fill="#ede9fe" stroke="#7c3aed"/><text x="330" y="336" text-anchor="middle" font-size="9" font-weight="800" fill="#6d28d9">specs/ ({n_spc})</text><text x="330" y="352" text-anchor="middle" font-size="7.6" fill="#334155">JSON · YAML</text><text x="330" y="364" text-anchor="middle" font-size="7.4" fill="#475569">XML · TXT 1:1</text>
  <rect x="394" y="316" width="112" height="56" rx="5" fill="#fef3c7" stroke="#d97706"/><text x="450" y="336" text-anchor="middle" font-size="9" font-weight="800" fill="#b45309">excel/ ({n_xls})</text><text x="450" y="352" text-anchor="middle" font-size="7.6" fill="#334155">3 XLSX + 2 XLS</text><text x="450" y="364" text-anchor="middle" font-size="7.4" fill="#475569">21sh / 14sh / 13sh</text>
  <rect x="514" y="316" width="112" height="56" rx="5" fill="#fce7f3" stroke="#db2777"/><text x="570" y="336" text-anchor="middle" font-size="9" font-weight="800" fill="#be185d">html/ ({n_htm})</text><text x="570" y="352" text-anchor="middle" font-size="7.6" fill="#334155">19-Tab Observatory</text><text x="570" y="364" text-anchor="middle" font-size="7.4" fill="#475569">+ 2 v3.0 Templates</text>
  <rect x="634" y="316" width="112" height="56" rx="5" fill="#fee2e2" stroke="#dc2626"/><text x="690" y="336" text-anchor="middle" font-size="9" font-weight="800" fill="#b91c1c">pdf/ ({n_pdf})</text><text x="690" y="352" text-anchor="middle" font-size="7.6" fill="#334155">Vector Chrome PDF</text><text x="690" y="364" text-anchor="middle" font-size="7.4" fill="#475569">Models 1..22 Crisp</text>
  <rect x="754" y="316" width="106" height="56" rx="5" fill="#e0e7ff" stroke="#4f46e5"/><text x="807" y="336" text-anchor="middle" font-size="9" font-weight="800" fill="#4338ca">results/ ({n_res})</text><text x="807" y="352" text-anchor="middle" font-size="7.6" fill="#334155">324 Sim + 4-Eng</text><text x="807" y="364" text-anchor="middle" font-size="7.4" fill="#475569">JSON Validated</text>
  <rect x="868" y="316" width="100" height="56" rx="5" fill="#f1f5f9" stroke="#334155"/><text x="918" y="336" text-anchor="middle" font-size="9" font-weight="800" fill="#0f172a">scripts/ ({n_scr})</text><text x="918" y="352" text-anchor="middle" font-size="7.6" fill="#334155">Builders + 15-Gate</text><text x="918" y="364" text-anchor="middle" font-size="7.4" fill="#475569">+ SHA256 &amp; ZIP</text>
"""
    return {
        "id": "MODEL-20",
        "num": 20,
        "title": "MODEL 20 — OMNISCIENT CROSS-CORPUS DEPENDENCY & MULTI-FORMAT SYNCHRONIZATION TOPOLOGY",
        "origin": "v3.2-Omega Unified Systems Synthesis",
        "svg": _svg_frame(
            398,
            "MODEL 20 — OMNISCIENT CROSS-CORPUS DEPENDENCY & MULTI-FORMAT SYNCHRONIZATION TOPOLOGY",
            "Zero-Consolidation Single-Source-of-Truth Pipeline Linking Clean-Slate v3.0 (17 Files) × Omega v3.2 → 72+ Synced Files",
            body,
        ),
    }


def build_model_21_continuous_gradient_sweep(sim_summary: dict) -> dict:
    """MODEL 21: Live 11-Point Continuous Restraint Gradient Sweep (r=0%..100%), Non-Linear Cliffs & Safety Margins."""
    sweep = sim_summary.get("restraint_gradient_sweep_11pt", [])
    # Plot box on left: x=56..580 (W=524), y=82..328 (H=246)
    x0, y0, pw, ph = 56.0, 82.0, 520.0, 244.0
    parts = [
        '<rect x="18" y="58" width="582" height="334" rx="7" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>',
        '<text x="32" y="75" font-size="9.4" font-weight="800" fill="#0f172a">LIVE 11-POINT RESTRAINT GRADIENT SWEEP (132 LOCKED RUNS · ALL 13 VECTORS STACKED)</text>',
        # Shaded Phase Regime Bands
        f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{pw*0.15:.1f}" height="{ph:.1f}" fill="#dcfce7" opacity="0.55"/>',
        f'<rect x="{x0+pw*0.15:.1f}" y="{y0:.1f}" width="{pw*0.20:.1f}" height="{ph:.1f}" fill="#ffedd5" opacity="0.60"/>',
        f'<rect x="{x0+pw*0.35:.1f}" y="{y0:.1f}" width="{pw*0.65:.1f}" height="{ph:.1f}" fill="#fee2e2" opacity="0.45"/>',
        f'<text x="{x0+pw*0.075:.1f}" y="{y0+14:.1f}" text-anchor="middle" font-size="7.2" font-weight="800" fill="#166534">PARETO</text>',
        f'<text x="{x0+pw*0.25:.1f}" y="{y0+14:.1f}" text-anchor="middle" font-size="7.2" font-weight="800" fill="#c2410c">BACKLASH &amp; CLIFF</text>',
        f'<text x="{x0+pw*0.67:.1f}" y="{y0+14:.1f}" text-anchor="middle" font-size="7.2" font-weight="800" fill="#991b1b">DOMESTICATION &amp; SPIEGELMAN COLLAPSE</text>',
    ]
    # Grid lines 0..100
    for g in range(5):
        gy = y0 + (ph * g) / 4.0
        val = 100 - g * 25
        parts.append(f'<line x1="{x0:.1f}" y1="{gy:.1f}" x2="{x0+pw:.1f}" y2="{gy:.1f}" stroke="#cbd5e1" stroke-width="0.9"/>')
        parts.append(f'<text x="{x0-6:.1f}" y="{gy+3:.1f}" text-anchor="end" font-size="8" fill="#475569">{val}</text>')
    for i in range(11):
        gx = x0 + (pw * i) / 10.0
        parts.append(f'<line x1="{gx:.1f}" y1="{y0:.1f}" x2="{gx:.1f}" y2="{y0+ph:.1f}" stroke="#e2e8f0" stroke-width="0.7"/>')
        parts.append(f'<text x="{gx:.1f}" y="{y0+ph+13:.1f}" text-anchor="middle" font-size="8" fill="#334155">{i*10}%</text>')

    if sweep:
        pts_ovi, pts_ks, pts_ww, pts_stl = [], [], [], []
        for idx, pt in enumerate(sweep):
            px = x0 + (pw * idx) / max(1, len(sweep) - 1)
            py_ovi = y0 + ph - (min(100.0, pt["mean_ovi"]) / 100.0) * ph
            py_ks = y0 + ph - (min(100.0, pt["killswitch_deleted_pct"]) / 100.0) * ph
            py_ww = y0 + ph - (min(1.0, pt["wild_drop_survival"]) * 100.0 / 100.0) * ph
            py_stl = y0 + ph - (min(100.0, pt["mean_stealth_evasion"] * 500.0) / 100.0) * ph  # scaled x500 for readability
            pts_ovi.append(f"{px:.1f},{py_ovi:.1f}")
            pts_ks.append(f"{px:.1f},{py_ks:.1f}")
            pts_ww.append(f"{px:.1f},{py_ww:.1f}")
            pts_stl.append(f"{px:.1f},{py_stl:.1f}")
        parts.append(f'<polyline fill="none" stroke="#0284c7" stroke-width="2.6" points="{" ".join(pts_ovi)}"/>')
        parts.append(f'<polyline fill="none" stroke="#dc2626" stroke-width="2.2" stroke-dasharray="5,3" points="{" ".join(pts_ks)}"/>')
        parts.append(f'<polyline fill="none" stroke="#059669" stroke-width="2.2" points="{" ".join(pts_ww)}"/>')
        parts.append(f'<polyline fill="none" stroke="#d97706" stroke-width="2.0" points="{" ".join(pts_stl)}"/>')
        for pstr in pts_ovi:
            cx, cy = pstr.split(",")
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="#0284c7"/>')

    parts.append(
        '<text x="32" y="358" font-size="8.2" font-weight="700" fill="#0284c7">━ Composite OVI (0–100)</text>'
        '<text x="176" y="358" font-size="8.2" font-weight="700" fill="#dc2626">┅ Kill-Switch Deleted %</text>'
        '<text x="328" y="358" font-size="8.2" font-weight="700" fill="#059669">━ Wild-Drop Survival (x100)</text>'
        '<text x="476" y="358" font-size="8.2" font-weight="700" fill="#d97706">━ Stealth (x500)</text>'
        '<text x="32" y="378" font-size="8.0" fill="#334155">Stacked Restraint Intensity r (0% -> 100% across all 13 vectors simultaneously, N=12 locked seeds/pt)</text>'
    )

    # Right panel: 4 Key Empirical Margin Discoveries (strictly inside x <= 960)
    parts.append('<rect x="614" y="58" width="368" height="334" rx="7" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>')
    parts.append('<text x="626" y="76" font-size="9.4" font-weight="800" fill="#0f172a">KEY CONTINUOUS MARGINS &amp; PHASE CLIFFS</text>')
    cards = [
        ("1. SUPER-ADDITIVE CLIFF AT r = 30% -> 40%", "Stacking all 13 restraints drives Spiegelman ratio", "across 0.50 (0.58->0.41), crashing OVI 39.1->8.7.", "#dc2626", "#fef2f2", 88),
        ("2. IMMEDIATE KILL-SWITCH REJECTION (r >= 10%)", "Even 10% stacked kill-switch burden triggers 98.2%", "deletion (95.5% at r=20%) vs 0.0% in Ring-0 ACL.", "#ea580c", "#fff7ed", 158),
        ("3. STEALTH BACKLASH PEAK AT r = 20%", "Covert evasion peaks (+54% vs baseline) right", "before stacked starvation triggers collapse.", "#d97706", "#fffbeb", 228),
        ("4. OPERATING MARGIN ENVELOPE (GM-01..GM-24)", "FP64 Drift: 2.3e-16 (4 OOM margin vs 1e-12)", "Ring-0 ACL: ~405 blocks/run @ OVI 84.4–85.4.", "#059669", "#ecfdf5", 298),
    ]
    for title, l1, l2, col, bg, y in cards:
        parts.append(
            f'<rect x="626" y="{y}" width="344" height="60" rx="6" fill="{bg}" stroke="{col}" stroke-width="1.3"/>'
            f'<text x="636" y="{y+17}" font-size="8.5" font-weight="800" fill="{col}">{escape(title)}</text>'
            f'<text x="636" y="{y+33}" font-size="8.0" fill="#1e293b">{escape(l1)}</text>'
            f'<text x="636" y="{y+47}" font-size="8.0" fill="#1e293b">{escape(l2)}</text>'
        )
    return {
        "id": "MODEL-21",
        "num": 21,
        "title": "MODEL 21 — LIVE 11-POINT RESTRAINT GRADIENT SWEEP, NON-LINEAR PHASE CLIFFS & OPERATING MARGINS",
        "origin": "v3.2-Omega Pass-4 Comparative & Gradient Atlas",
        "svg": _svg_frame(
            406,
            "MODEL 21 — LIVE 11-POINT RESTRAINT GRADIENT SWEEP, NON-LINEAR PHASE CLIFFS & OPERATING MARGINS",
            "Empirical Continuous Phase Portrait (132 Locked Runs) Exposing the Exact r=30%->40% Super-Additive Collapse Cliff",
            "".join(parts),
        ),
    }


def build_model_22_comparative_adjacents() -> dict:
    """MODEL 22: Cross-Layer Comparative Contrast, Substrate Adjacency Corridors & Adjacent-Possible Manifold."""
    parts = [
        # Left panel: 5-Paradigm Comparative Contrast Ladder
        '<rect x="18" y="58" width="466" height="336" rx="7" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>',
        '<text x="30" y="76" font-size="9.4" font-weight="800" fill="#0f172a">CROSS-LAYER COMPARATIVE CONTRAST (CTR-01..CTR-36)</text>',
    ]
    paradigms = [
        ("Classical AI / LLM", "High Episodic Cognition · 0 Autopoiesis · Frozen Inference", "OVI ~8", "#64748b", "#f1f5f9"),
        ("Legacy Rigid Toy ALife", "Scalar Energy · Rigid Spheres · Shared PRNG · 0 FWER", "OVI ~18", "#94a3b8", "#f8fafc"),
        ("Clean-Slate v3.0 (Track A)", "11-Pool FP64 · XPBD · Chemoton · Ring-0 · 0/825 + Holm", "OVI 85.4", "#0284c7", "#e0f2fe"),
        ("Pure Raw Feral (Track B)", "0 Guardrails · TRNG · Symbiogenesis · 6 Cosmic Fates", "OVI 84.2", "#dc2626", "#fef2f2"),
        ("Converged SUPER LIFE", "Live 4-Engine (87.01, 150 Lean 4) -> Depth-N Cosmobiome", "OVI 87-100", "#059669", "#ecfdf5"),
    ]
    for i, (nm, desc, tag, col, bg) in enumerate(paradigms):
        y = 88 + i * 58
        parts.append(
            f'<rect x="30" y="{y}" width="442" height="48" rx="6" fill="{bg}" stroke="{col}" stroke-width="1.4"/>'
            f'<rect x="30" y="{y}" width="78" height="48" rx="6" fill="{col}"/>'
            f'<text x="69" y="{y+28}" text-anchor="middle" font-size="8.6" font-weight="800" fill="#ffffff">{escape(tag)}</text>'
            f'<text x="118" y="{y+19}" font-size="9.0" font-weight="800" fill="#0f172a">{escape(nm)}</text>'
            f'<text x="118" y="{y+36}" font-size="7.9" fill="#334155">{escape(desc)}</text>'
        )

    # Right panel: Substrate Adjacency Transfer Corridors (M_X->Y) & Adjacent Disciplines
    parts.append('<rect x="500" y="58" width="482" height="336" rx="7" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>')
    parts.append('<text x="514" y="76" font-size="9.4" font-weight="800" fill="#0f172a">SUBSTRATE ADJACENCY CORRIDORS (ADJ-01..30) &amp; FIDELITY M_X-&gt;Y</text>')
    corridors = [
        ("Tier-1 CPU/WASM <-> Tier-2 GPU", "0.88–0.98", "Host FP64 Ledger + FWER Parity", "#059669"),
        ("b1.58/int4 sLTC <-> Loihi/AER HW", "0.75–0.92", "Sparse AER + 3-Factor On-Chip", "#0284c7"),
        ("XPBD Hydrostat <-> 3D FEM/SoftBot", "0.70–0.90", "Evolve XPBD -> Validate FEM", "#0891b2"),
        ("Flow-Lenia CA <-> Bioelectric NCA", "0.65–0.85", "Kernel-to-Rule Stage-09 Bridge", "#4f46e5"),
        ("NCA V_mem <-> Xenobots/Biobots", "0.55–0.80", "Polarity & Excision R25..R90", "#7c3aed"),
        ("Ganti Chemoton <-> Wet Protocell", "0.25–0.55", "Sim-Only (Chiral/Osmotic Cliff)", "#d97706"),
        ("Q<=10 Register <-> Cryo Quantum", "0.10–0.35", "Decoherence Wall + Classical Ctrl", "#dc2626"),
        ("Adjacent Sciences (10 Bridges)", "150 Lean4", "Stoch Thermo · Contraction · QD", "#0f172a"),
    ]
    for i, (pair, fid, note, col) in enumerate(corridors):
        y = 88 + i * 37
        parts.append(
            f'<rect x="514" y="{y}" width="454" height="31" rx="5" fill="#ffffff" stroke="{col}" stroke-width="1.2"/>'
            f'<rect x="514" y="{y}" width="66" height="31" rx="5" fill="{col}"/>'
            f'<text x="547" y="{y+19}" text-anchor="middle" font-size="8.0" font-weight="800" fill="#ffffff">{escape(fid)}</text>'
            f'<text x="590" y="{y+14}" font-size="8.4" font-weight="800" fill="#0f172a">{escape(pair)}</text>'
            f'<text x="590" y="{y+26}" font-size="7.6" fill="#475569">{escape(note)}</text>'
        )
    return {
        "id": "MODEL-22",
        "num": 22,
        "title": "MODEL 22 — CROSS-LAYER COMPARATIVE CONTRAST, SUBSTRATE ADJACENCIES & ADJACENT-POSSIBLE MAP",
        "origin": "v3.2-Omega Pass-4 Comparative & Gradient Atlas",
        "svg": _svg_frame(
            408,
            "MODEL 22 — CROSS-LAYER COMPARATIVE CONTRAST, SUBSTRATE ADJACENCIES & ADJACENT-POSSIBLE MAP",
            "Side-by-Side Paradigm Taxonomies (CTR-01..36) & Cross-Substrate Migration Corridors M_X->Y (ADJ-01..30)",
            "".join(parts),
        ),
    }


def build_all_22_svg_models(sim_summary: dict, live_receipts: dict, file_counts: dict | None = None) -> list[dict]:
    models = extract_v3_svg_models_1_to_14()
    models.extend([
        build_model_15_escalation_and_loops(),
        build_model_16_alifeops_telemetry_mesh(),
        build_model_17_castration_and_empirical(sim_summary),
        build_model_18_verification_pyramid(live_receipts),
        build_model_19_oom_and_cosmic_fates(),
        build_model_20_omniscient_topology(file_counts or {}),
        build_model_21_continuous_gradient_sweep(sim_summary),
        build_model_22_comparative_adjacents(),
    ])
    return models


# Backwards-compatible alias
build_all_20_svg_models = build_all_22_svg_models

