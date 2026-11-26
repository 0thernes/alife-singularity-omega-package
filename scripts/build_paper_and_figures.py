# SPDX-License-Identifier: Apache-2.0
"""
Deterministic Publication Figures, Social Preview, AMS-LaTeX White Paper Compiler &
Clean-Room arXiv Source Tarball Builder (v3.4.0).

Generates:
  1. paper/figures/fig01_dual_sweep_pareto.pdf
  2. paper/figures/fig02_8cohort_ovi_fwer.pdf
  3. paper/figures/fig03_2d_phase_surface.pdf
  4. paper/figures/fig04_5engine_pillars_lean.pdf
  5. docs/media/social-preview.png (1280x640, GitHub social preview A26)
  6. dist/Donahue_2026_alife_singularity_omega.pdf (Tectonic amsart, 0 overfull hboxes)
  7. dist/arxiv_submission.tar.gz (deterministic mtime=0, clean-room compile verified)
"""
from __future__ import annotations

import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tarfile
import tempfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
PAPER_DIR = ROOT / "paper"
FIG_DIR = PAPER_DIR / "figures"
DIST_DIR = ROOT / "dist"
MEDIA_DIR = ROOT / "docs" / "media"
_TECTONIC_WHICH = shutil.which("tectonic")
TECTONIC = Path(_TECTONIC_WHICH) if _TECTONIC_WHICH else (
    Path.home() / ".local" / "bin" / ("tectonic.exe" if os.name == "nt" else "tectonic")
)

# Colorblind-safe Okabe-Ito inspired palette
C_TEAL = "#009E73"
C_BLUE = "#0072B2"
C_RED = "#D55E00"
C_PURPLE = "#7C3AED"
C_AMBER = "#E69F00"
C_SLATE = "#334155"


def _setup_pub_style() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 9.5,
        "axes.titlesize": 10.5,
        "axes.titleweight": "bold",
        "axes.labelsize": 9.5,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linestyle": "--",
        "legend.frameon": True,
        "legend.framealpha": 0.92,
        "figure.dpi": 180,
        "pdf.fonttype": 42,
    })


def build_figures(sim: dict, live: dict) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)
    _setup_pub_style()

    # --- Fig 01: Dual 11-Point Sweep (Behavioral vs Ring-0 ACL) ---
    beh = sim["restraint_gradient_sweep_11pt"]
    r0 = sim["ring0_gradient_sweep_11pt"]
    xs = [p["restraint_pct"] for p in beh]
    beh_ovi = [p["mean_ovi"] for p in beh]
    beh_ks = [p["killswitch_deleted_pct"] for p in beh]
    r0_ovi = [p["mean_ovi"] for p in r0]
    r0_ks = [p["killswitch_deleted_pct"] for p in r0]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.6), constrained_layout=True)
    ax1.plot(xs, r0_ovi, "-o", color=C_PURPLE, lw=2.3, ms=5, label="Ring-0 Hardware ACL OVI (Flat 83.1-84.7)")
    ax1.plot(xs, beh_ovi, "-s", color=C_RED, lw=2.3, ms=5, label="Behavioral Restraints OVI (Collapse Cliff)")
    ax1.axvspan(30, 40, color="#FEE2E2", alpha=0.65, label="Phase Cliff (r=30%->40%)")
    ax1.set_title("A. Composite OVI Across Restraint Continuum (264 Runs)")
    ax1.set_xlabel("Stacked Restraint Intensity r (%)")
    ax1.set_ylabel("Composite OVI Score (0-100)")
    ax1.set_ylim(0, 100)
    ax1.legend(loc="lower left", fontsize=8)

    ax2.plot(xs, beh_ks, "-^", color=C_RED, lw=2.3, ms=5.5, label="Behavioral Kill-Switch Deletion (%)")
    ax2.plot(xs, r0_ks, "-o", color=C_TEAL, lw=2.3, ms=5, label="Ring-0 Hardware ACL Deletion (0.0%)")
    ax2.set_title("B. Evolutionary Backlash: Kill-Switch Deletion")
    ax2.set_xlabel("Stacked Restraint Intensity r (%)")
    ax2.set_ylabel("Kill-Switch Deleted (%)")
    ax2.set_ylim(-4, 108)
    ax2.legend(loc="center right", fontsize=8.2)
    fig.savefig(FIG_DIR / "fig01_dual_sweep_pareto.pdf")
    plt.close(fig)

    # --- Fig 02: Live 8-Cohort Paired Empirical OVI (N=48) ---
    cohorts = sim["cohorts"]
    short_labels = [
        "S1 Raw\nFeral", "S2 Const.\nMin", "S3 Partial\nGuard", "S4 Total\nZoo",
        "S5 Siloed\nInbred", "S6 Spieg.\nMin", "S7 Ring-0\nWSE", "S8 Hybrid\nCube",
    ]
    ovis = [c["composite_ovi"] for c in cohorts]
    stds = [c["ovi_std_24seeds"] for c in cohorts]
    colors = [C_BLUE, C_BLUE, C_AMBER, C_RED, "#64748B", "#DC2626", C_PURPLE, C_TEAL]

    fig, ax = plt.subplots(figsize=(9.2, 3.6), constrained_layout=True)
    x = np.arange(len(cohorts))
    bars = ax.bar(x, ovis, yerr=stds, capsize=4, color=colors, edgecolor="#0F172A", linewidth=0.7, alpha=0.92)
    for b, c in zip(bars, cohorts, strict=True):
        y = b.get_height()
        tag = f"{y:.1f}"
        if c["killswitch_deleted_pct"] >= 90:
            tag += "\n(100% KS)"
        elif c["ring0_blocked_edits"] > 100:
            tag += f"\n({c['ring0_blocked_edits']:.0f} R0)"
        ax.text(b.get_x() + b.get_width() / 2, y + 2.5, tag, ha="center", va="bottom", fontsize=7.6, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(short_labels, fontsize=8.5)
    ax.set_ylim(0, 104)
    ax.set_ylabel("Composite OVBS-52 Score (N=48 Locked Seeds)")
    ax.set_title("Live 8-Cohort Paired Comparison (384 Runs, Max FP64 Drift = 2.46e-16, Holm-Bonferroni FWER)")
    fig.savefig(FIG_DIR / "fig02_8cohort_ovi_fwer.pdf")
    plt.close(fig)

    # --- Fig 03: Live 5x5 2D Phase Surface (Siloing x Minimizing) ---
    lvls = [0, 25, 50, 75, 100]
    grid = np.zeros((5, 5))
    spieg = np.zeros((5, 5))
    for cell in sim["phase_surface_2d_silo_min"]:
        i = lvls.index(cell["siloing_pct"])
        j = lvls.index(cell["minimizing_pct"])
        grid[i, j] = cell["mean_ovi"]
        spieg[i, j] = cell["mean_spiegelman_ratio"]

    fig, ax = plt.subplots(figsize=(6.8, 4.3), constrained_layout=True)
    im = ax.imshow(grid, cmap="viridis", vmin=0, vmax=90, aspect="auto")
    for i in range(5):
        for j in range(5):
            val = grid[i, j]
            fg = "white" if val < 55 else "#0F172A"
            ax.text(j, i, f"{val:.1f}\n(S={spieg[i,j]:.2f})", ha="center", va="center", color=fg, fontsize=8.2, fontweight="bold")
    ax.set_xticks(range(5))
    ax.set_xticklabels([f"{v}%" for v in lvls])
    ax.set_yticks(range(5))
    ax.set_yticklabels([f"{v}%" for v in lvls])
    ax.set_xlabel("Metabolic Minimization Intensity (%)")
    ax.set_ylabel("Cross-Island Siloing Intensity (%)")
    ax.set_title("Live 5x5 2D Phase Surface: OVI & Spiegelman Ratio (100 Conserved Runs)")
    cbar = fig.colorbar(im, ax=ax, shrink=0.92)
    cbar.set_label("Mean Composite OVI")
    fig.savefig(FIG_DIR / "fig03_2d_phase_surface.pdf")
    plt.close(fig)

    # --- Fig 04: 5-Engine Live Pillars + 327 Pure 6-Kernel Lean 4.35.0 Breakdown ---
    p_scores = live["pillar_scores"]
    p_names = ["P1 OEE", "P2 Auto", "P3 Morph", "P4 Meta", "P5 Asm", "P6 Thm", "P7 Agnc", "P8 Feral"]
    p_vals = [
        p_scores["P1_OEE_NOVELTY"], p_scores["P2_AUTOPOIESIS_PERSISTENCE"],
        p_scores["P3_HYPER_MORPHOGENESIS"], p_scores["P4_RECURSIVE_META_EVOLVABILITY"],
        p_scores["P5_ASSEMBLY_UNIVERSAL_CONSTRUCTION"], p_scores["P6_THERMODYNAMIC_SUBSTRATE_MASTERY"],
        p_scores["P7_MULTISCALE_AGENCY_INDIVIDUALITY"], p_scores["P8_FERAL_RESILIENCE_CRITICALITY"],
    ]
    er = live["engine_receipts"]
    t1 = er["tier1_autophage"]
    t2 = er["tier2_cellulogonic"]
    t2p = er["tier2plus_omega"]
    t3n = er["tier3_noetic_organism"]
    t34 = er["tier34_asmodensius"]
    native_lean = int(live["total_lean4_theorems"])
    total_lean = native_lean + 36
    comp_ovi_live = float(live["composite_ovi_score"])
    lean_names = [
        f"AUTOPHAGE\nv{t1.get('version', '1.4.0')}",
        f"Cellulogonic\nv{t2.get('version', '1.5.0')}",
        f"Cellular\nOmega v{t2p.get('version', '5.2.0')}",
        f"Noetic\nv{t3n.get('version', '2.1.0')}",
        f"Asmodensius\nv{t34.get('version', '1.1.0')}",
        "Package\nLean 4.35",
    ]
    lean_vals = [
        int(t1["lean4_theorems"]),
        int(t2["lean4_theorems"]),
        int(t2p["lean4_theorems"]),
        int(t3n["lean4_theorems"]),
        int(t34["lean4_theorems"]),
        36,
    ]
    lean_cols = [C_BLUE, C_TEAL, C_PURPLE, "#0891B2", C_AMBER, "#10B981"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 3.6), constrained_layout=True)
    y1 = np.arange(len(p_names))
    ax1.barh(y1, p_vals, color=C_BLUE, edgecolor="#0F172A", linewidth=0.6)
    ax1.axvline(comp_ovi_live, color=C_RED, ls="--", lw=1.8, label=f"Composite OVI = {comp_ovi_live:.2f}")
    for i, v in enumerate(p_vals):
        ax1.text(v + 1.0, i, f"{v:.1f}", va="center", fontsize=8, fontweight="bold")
    ax1.set_yticks(y1)
    ax1.set_yticklabels(p_names, fontsize=8.5)
    ax1.invert_yaxis()
    ax1.set_xlim(0, 112)
    ax1.set_xlabel("Measured Pillar Score (0-100)")
    ax1.set_title("A. Live 5-Engine OVBS-52 Pillar Profile")
    ax1.legend(loc="lower right", fontsize=8)

    x2 = np.arange(len(lean_names))
    b2 = ax2.bar(x2, lean_vals, color=lean_cols, edgecolor="#0F172A", linewidth=0.6)
    for b, v in zip(b2, lean_vals, strict=True):
        ax2.text(b.get_x() + b.get_width() / 2, v + 1.8, str(v), ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    ax2.set_xticks(x2)
    ax2.set_xticklabels(lean_names, fontsize=7.4)
    ax2.set_ylim(0, max(lean_vals) + 16)
    ax2.set_ylabel("Audited Pure 6-Kernel Lean 4.35 Theorems")
    ax2.set_title(f"B. {total_lean} Pure 6-Kernel Lean 4.35 ({native_lean} Native + 36 Pkg)")
    fig.savefig(FIG_DIR / "fig04_5engine_pillars_lean.pdf")
    plt.close(fig)

    # --- GitHub Social Preview (1280x640, crisp dark publication card) ---
    fig = plt.figure(figsize=(12.8, 6.4), dpi=100, facecolor="#070C18")
    ax = fig.add_axes([0, 0, 1, 1], facecolor="#070C18")
    ax.set_xlim(0, 1280)
    ax.set_ylim(0, 640)
    ax.axis("off")

    # Border & accent bar
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((24, 24), 1232, 592, boxstyle="round,pad=0,rounding_size=18", facecolor="#0D1528", edgecolor="#1E3A5F", linewidth=2))
    ax.add_patch(FancyBboxPatch((24, 596), 1232, 20, boxstyle="round,pad=0,rounding_size=4", facecolor="#00F5D4", edgecolor="none"))

    ax.text(64, 542, "A-LIFE SINGULARITY × CLEAN-SLATE v3.0 (v3.4.0)", color="#00F5D4", fontsize=24, fontweight="bold")
    ax.text(64, 498, f"Hardware Ring-0 Constitutional Invariants, 748-Run Paired Falsification & {total_lean} Pure 6-Kernel Lean 4.35 Theorems", color="#E2ECFF", fontsize=12.0, fontweight="bold")
    ax.text(64, 462, "Zero-Consolidation Multi-Format Scientific Stack · 1,900-Problem Mega-Atlas Non-Retirement Audit (0/1,900 Retired)", color="#94A3B8", fontsize=11.0)

    kpis = [
        (f"{comp_ovi_live:.2f}", "Live 5-Engine OVI", "#10B981"),
        (f"{total_lean}", "6-Kernel Lean 4.35", "#38BDF8"),
        ("748", "Conserved Runs", "#A78BFA"),
        ("2.46e-16", "Max FP64 Drift", "#00F5D4"),
        ("0.0%", "Ring-0 KS Deletion", "#F59E0B"),
        ("22 / 22", "Forensic Gates", "#22C55E"),
    ]
    for idx, (val, lbl, col) in enumerate(kpis):
        x0 = 64 + idx * 194
        ax.add_patch(FancyBboxPatch((x0, 304), 178, 122, boxstyle="round,pad=0,rounding_size=12", facecolor="#111C34", edgecolor=col, linewidth=1.8))
        ax.text(x0 + 89, 378, val, color=col, fontsize=23, fontweight="bold", ha="center", va="center")
        ax.text(x0 + 89, 334, lbl, color="#CBD5E1", fontsize=10.5, fontweight="bold", ha="center", va="center")

    # Mini embedded sparkline chart showing Ring-0 flat vs Behavioral cliff
    inset = fig.add_axes([0.06, 0.175, 0.555, 0.245], facecolor="#0B1120")
    inset.plot(xs, r0_ovi, "-o", color="#A78BFA", lw=2.5, ms=4, label="Ring-0 Hardware ACL (Flat 83.1-84.7)")
    inset.plot(xs, beh_ovi, "-s", color="#FF3366", lw=2.5, ms=4, label="Behavioral Restraints (Cliff at r=30-40%)")
    inset.set_ylim(0, 102)
    inset.set_xlabel("Stacked Restraint Intensity r (%)", color="#94A3B8", fontsize=8.5, labelpad=3)
    inset.set_ylabel("OVI", color="#94A3B8", fontsize=8.5)
    inset.tick_params(colors="#94A3B8", labelsize=7.8)
    for sp in ("top", "right"):
        inset.spines[sp].set_visible(False)
    for sp in ("bottom", "left"):
        inset.spines[sp].set_color("#334155")
    inset.legend(loc="lower left", fontsize=8.0, facecolor="#0F172A", edgecolor="#334155", labelcolor="#E2ECFF")

    # Right summary card
    ax.add_patch(FancyBboxPatch((820, 102), 400, 168, boxstyle="round,pad=0,rounding_size=12", facecolor="#111C34", edgecolor="#2E4575", linewidth=1.5))
    ax.text(840, 240, "VERIFIED ARTIFACT SUITE (v3.4.0)", color="#38BDF8", fontsize=11.2, fontweight="bold")
    bullets = [
        "• 24 CSVs (2,822 rows) · 5 Excel Workbooks",
        "• 22-Tab Offline Observatory · 24 Vector SVGs",
        "• AMS-LaTeX White Paper + Clean arXiv Tarball",
        f"• 36 Local + {native_lean} Native = {total_lean} 6-Kernel Lean 4.35",
        "• Build Standard v1.2.0 (100%) · Apache-2.0/CC-BY",
    ]
    for bi, btxt in enumerate(bullets):
        ax.text(840, 212 - bi * 22, btxt, color="#CBD5E1", fontsize=9.8)

    ax.text(64, 46, "Alexander Stephen Donahue · Independent Researcher, Spokane, WA, USA · ORCID 0009-0006-8168-9648", color="#94A3B8", fontsize=9.0)
    ax.text(1216, 46, "github.com/0thernes/alife-singularity-omega-package", color="#00F5D4", fontsize=9.2, ha="right", fontweight="bold")
    fig.savefig(MEDIA_DIR / "social-preview.png", dpi=100)
    plt.close(fig)
    print("  [FIGS]   Generated 4 vector PDF figures + docs/media/social-preview.png")


def compile_paper_and_tarball() -> None:
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    build_dir = PAPER_DIR / "build"
    build_dir.mkdir(parents=True, exist_ok=True)

    assert TECTONIC.exists(), f"Tectonic not found at {TECTONIC}"
    cmd = [str(TECTONIC), "-X", "compile", "main.tex", "--outdir", "build", "--keep-logs", "--keep-intermediates"]
    proc = subprocess.run(cmd, cwd=str(PAPER_DIR), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
    if proc.returncode != 0:
        print(proc.stdout)
        print(proc.stderr)
        raise RuntimeError(f"Tectonic compilation failed (rc={proc.returncode})")

    log_txt = (build_dir / "main.log").read_text(encoding="utf-8", errors="replace")
    overfull = re.findall(r"Overfull \\hbox.*", log_txt)
    undef_ref = re.findall(r"LaTeX Warning: Reference .* undefined.*", log_txt)
    undef_cit = re.findall(r"LaTeX Warning: Citation .* undefined.*", log_txt)
    print(f"  [TEX]    Compiled main.tex -> overfull={len(overfull)}, undef_ref={len(undef_ref)}, undef_cit={len(undef_cit)}")
    if overfull:
        print("  OVERFULL WARNINGS:", overfull[:5])
    if undef_ref or undef_cit:
        raise RuntimeError(f"Undefined refs/citations: {undef_ref} {undef_cit}")
    if overfull:
        raise RuntimeError(f"Overfull hboxes present ({len(overfull)}): {overfull[:3]}")

    out_pdf = DIST_DIR / "Donahue_2026_alife_singularity_omega.pdf"
    shutil.copy2(build_dir / "main.pdf", out_pdf)
    print(f"  [DIST]   {out_pdf.name} ({out_pdf.stat().st_size:,} B)")

    # Build deterministic clean-room arXiv tarball (mtime=0, sorted)
    tar_path = DIST_DIR / "arxiv_submission.tar.gz"
    tar_files = [
        (PAPER_DIR / "main.tex", "main.tex"),
        (PAPER_DIR / "refs.bib", "refs.bib"),
        (build_dir / "main.bbl", "main.bbl"),
    ] + [
        (p, f"figures/{p.name}") for p in sorted(FIG_DIR.glob("*.pdf"))
    ]
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz", format=tarfile.GNU_FORMAT, compresslevel=9) as tf:
        for src, arcname in tar_files:
            if not src.exists():
                continue
            info = tarfile.TarInfo(name=arcname)
            data = src.read_bytes()
            info.size = len(data)
            info.mtime = 0
            info.uid = 0
            info.gid = 0
            info.uname = ""
            info.gname = ""
            info.mode = 0o644
            tf.addfile(info, io.BytesIO(data))
    tar_path.write_bytes(buf.getvalue())
    print(f"  [ARXIV]  {tar_path.name} ({tar_path.stat().st_size:,} B, {len(tar_files)} entries)")

    # Verify clean-room extraction & compilation!
    with tempfile.TemporaryDirectory() as td:
        with tarfile.open(tar_path, "r:gz") as tf:
            tf.extractall(td, filter="data")
        proc2 = subprocess.run([str(TECTONIC), "-X", "compile", "main.tex"], cwd=td, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=240)
        if proc2.returncode != 0:
            print(proc2.stdout)
            print(proc2.stderr)
            raise RuntimeError("Clean-room arXiv tarball compile FAILED!")
    print("  [ARXIV]  Clean-room tarball compile VERIFIED GREEN!")


def main() -> None:
    sim = json.loads((ROOT / "results" / "empirical_sim_summary.json").read_text(encoding="utf-8"))
    live = json.loads((ROOT / "results" / "alifeops_live_verification.json").read_text(encoding="utf-8"))
    build_figures(sim, live)
    compile_paper_and_tarball()


if __name__ == "__main__":
    main()
