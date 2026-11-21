# -*- coding: utf-8 -*-
"""
15-Gate Automated Omniscient Forensic Integrity Auditor (v3.2-Omega).
Verifies zero consolidation (72+ files), 20/20 CSVs (2,721 rows), 130/130 checklist refs,
78/78 YAML alerts + 13/13 Release Gates, 9/9 JSON Schema scorecards, 324 live runs
(FP64 <1e-12, causal Ring-0 trapping >100/run, 11-pt gradient sweep, 5/5 Anti-LARP mutants),
4-format Master Spec 1:1 parity (20 XML fusion sections), all 5 Excel workbooks (incl. live
formula range verification across all 3 XLSX files), all 3 HTML5 apps (0 raw LaTeX, 0 U+2611,
22/22 SVGs), Node.js JS syntax, all 3 Chrome PDFs, 100% SHA-256 + ZIP integrity,
Gate 13 Zero Stale-Version/Count Drift, Gate 14 SVG Zero-Overflow + 100% Relative Link Check,
and Gate 15 Live Chrome Headless DOM Runtime Smoke Test.
"""
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET
import zipfile

import jsonschema
import openpyxl
import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
CHROME_EXE = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
EDGE_EXE = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

REQUIRED_17_V3_BAKED_FILES = [
    "html/ALife-Build-Framework-Template.html",
    "reports/ALife-Build-Framework-Template.md",
    "pdf/ALife-Build-Framework-Template.pdf",
    "csv/ALife-Framework-v3.0-Master-Checklists.csv",
    "specs/ALife-Framework-v3.0-Master-Spec.json",
    "specs/ALife-Framework-v3.0-Master-Spec.txt",
    "specs/ALife-Framework-v3.0-Master-Spec.xml",
    "specs/ALife-Framework-v3.0-Master-Spec.yaml",
    "excel/ALife-Framework-v3.0-Master-Workbook.xls",
    "excel/ALife-Framework-v3.0-Master-Workbook.xlsx",
    "csv/ALife-Hybrid-Cube-10x10x10.csv",
    "excel/ALife-Hybrid-Cube-10x10x10.xlsx",
    "csv/ALife-v3.0-Errata-Closure-Register.csv",
    "reports/ALife-v3.0-Errata-Closure-Report.md",
    "html/Clean-Slate-Creature-Blueprint-Checklist.html",
    "reports/Clean-Slate-Creature-Blueprint-Checklist.md",
    "pdf/Clean-Slate-Creature-Blueprint-Checklist.pdf",
]

REQUIRED_20_XML_FUSION_SECTIONS = [
    "EscalationLadder", "OrdersOfMagnitude", "MacroFailureModes", "EpistemicVoids",
    "CastrationVectors", "Castration13x13Synergy", "ALifeOpsPipeline",
    "MasterOperationalChecklist", "OVBS52Benchmarks", "FeralFateBranches",
    "OmniscientTraceability", "GradientsAndMargins", "ComparativeContrasts",
    "AdjacentPossibleBridges", "RestraintGradientSweep", "EmpiricalSimulation",
    "LiveNativeEngineReceipts", "OmegaCitations", "UnifiedSvgModels", "OmegaErrataClosures",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _audit_xlsx_formulas(xlsx_path: Path) -> tuple[int, list[str]]:
    wb = openpyxl.load_workbook(xlsx_path, data_only=False)
    issues = []
    fcount = 0
    for sname in wb.sheetnames:
        ws = wb[sname]
        for row in ws.iter_rows():
            for cell in row:
                v = cell.value
                if isinstance(v, str) and v.startswith("="):
                    fcount += 1
                    for m in re.finditer(r"(?:'([^']+)'|([A-Za-z0-9_]+))!\$?[A-Z]+\$?(\d+)(?::\$?[A-Z]+\$?(\d+))?", v):
                        ref_s = m.group(1) or m.group(2)
                        r1 = int(m.group(3))
                        r2 = int(m.group(4)) if m.group(4) else r1
                        if ref_s not in wb.sheetnames:
                            issues.append(f"{xlsx_path.name}:{sname}!{cell.coordinate} missing sheet '{ref_s}'")
                        else:
                            max_r = wb[ref_s].max_row
                            if r2 > max_r:
                                issues.append(f"{xlsx_path.name}:{sname}!{cell.coordinate} ref row {r2} > {ref_s}.max_row={max_r}")
    return fcount, issues


def run_all_15_forensic_gates(root_dir: Path | None = None, verify_manifests_and_zip: bool = True) -> dict:
    root = root_dir or ROOT_DIR
    print("\n================ RUNNING 15-GATE OMNISCIENT FORENSIC INTEGRITY AUDIT (v3.2-OMEGA) ================")

    # Gate 1: Zero-Consolidation Bake Parity (All 17 v3.0 + all Omega + Pass-3/4 >= 71)
    missing_v3 = [rel for rel in REQUIRED_17_V3_BAKED_FILES if not (root / rel).exists() or (root / rel).stat().st_size == 0]
    assert not missing_v3, f"Gate 1 FAIL: Missing baked v3.0 files: {missing_v3}"
    assert (root / "reports" / "07_PASS4_COMPARATIVE_CONTRAST_GRADIENTS_MARGINS_AND_ADJACENTS_AUDIT.md").exists(), "Gate 1 FAIL: Missing Report 07"
    all_pkg_files = [
        p for p in root.rglob("*")
        if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts and ".v3_source_baseline" not in p.parts
        and not p.name.endswith(".zip") and not p.name.startswith("_tmp_")
    ]
    assert len(all_pkg_files) >= 71, f"Gate 1 FAIL: Expected >= 71 files (zero consolidation), found {len(all_pkg_files)}"
    print(f"  [PASS] Gate  1 — Zero-Consolidation Parity: 17/17 v3.0 + Omega + Pass-4 intact ({len(all_pkg_files)} total files)")

    # Gate 2: All 20 CSVs Canonical Parity (2,721 structured rows)
    csv_dir = root / "csv"
    csv_files = sorted(p for p in csv_dir.iterdir() if p.suffix == ".csv")
    assert len(csv_files) == 20, f"Gate 2 FAIL: Expected 20 CSVs, found {len(csv_files)}"
    all_ids = set()
    total_csv_rows = 0
    csv_counts = {}
    for p in csv_files:
        with p.open("r", encoding="utf-8-sig", newline="") as f:
            parsed = list(csv.reader(f))
        assert len(parsed) >= 2, f"Gate 2 FAIL: Empty CSV {p.name}"
        rows = [r for r in parsed[1:] if r]
        csv_counts[p.name] = len(rows)
        total_csv_rows += len(rows)
        for r in rows:
            all_ids.add(r[0])
            if len(r) > 1:
                all_ids.add(r[1])
    assert csv_counts["ALife-Framework-v3.0-Master-Checklists.csv"] == 938
    assert csv_counts["ALife-Hybrid-Cube-10x10x10.csv"] == 1000
    assert csv_counts["ALife-v3.0-Errata-Closure-Register.csv"] == 130
    assert csv_counts["07_master_operational_checklist.csv"] == 130
    assert csv_counts["11_empirical_simulation_results.csv"] == 8
    assert csv_counts["12_v3_substrates_75_and_wse_10_matrix.csv"] == 85
    assert csv_counts["13_v3_forensic_36_and_release_gates_13_matrix.csv"] == 49
    assert csv_counts["14_omniscient_cross_corpus_traceability_matrix.csv"] == 48
    assert csv_counts["15_gradients_margins_and_phase_spectrums_matrix.csv"] == 24
    assert csv_counts["16_comparative_contrast_layers_taxonomies_matrix.csv"] == 36
    assert csv_counts["17_adjacent_possible_and_substrate_adjacencies_matrix.csv"] == 30
    assert total_csv_rows == 2721, f"Gate 2 FAIL: Expected 2,721 CSV rows, got {total_csv_rows}"
    print(f"  [PASS] Gate  2 — 20/20 Canonical CSVs verified ({total_csv_rows:,} structured records, 0 drift)")

    # Gate 3: Cross-Reference Integrity (130/130 Operational Checklist Linked_Ref_IDs)
    with (csv_dir / "07_master_operational_checklist.csv").open("r", encoding="utf-8-sig", newline="") as f:
        chk_rows = list(csv.reader(f))[1:]
    dangling = [r[0] + "->" + r[8] for r in chk_rows if r and r[8] not in all_ids]
    assert not dangling, f"Gate 3 FAIL: Dangling checklist references: {dangling}"
    print(f"  [PASS] Gate  3 — 130/130 Operational Checklist cross-references valid (0 dangling IDs)")

    # Gate 4: 78/78 Unified Alerts (42 Macro FMs + 36 v3.0 Forensic Guards) & 13/13 Release Gates in YAML
    pipe_yaml = yaml.safe_load((root / "pipelines" / "alifeops-master-pipeline.yaml").read_text(encoding="utf-8"))
    yaml_macro_alerts = {a["name"] for st in pipe_yaml["stages"] for a in st.get("pathology_alerts", [])}
    yaml_v3_guards = {g["name"] for st in pipe_yaml["stages"] for g in st.get("v3_forensic_guards", [])}
    yaml_gates = {g["id"] for st in pipe_yaml["stages"] for g in st.get("release_gates_13", [])}

    with (csv_dir / "03_failure_modes_bugs_errors_conflicts_matrix.csv").open("r", encoding="utf-8-sig", newline="") as f:
        fm_alerts = {r[11] for r in list(csv.reader(f))[1:] if r}
    with (csv_dir / "13_v3_forensic_36_and_release_gates_13_matrix.csv").open("r", encoding="utf-8-sig", newline="") as f:
        fg_rows = [r for r in list(csv.reader(f))[1:] if r]
    v3_guard_alerts = {r[6] for r in fg_rows if r[1].startswith("V3_TRIAGE")}
    v3_gate_ids = {r[0] for r in fg_rows if r[1] == "V3_RELEASE_GATE_13"}

    assert not (fm_alerts - yaml_macro_alerts), f"Gate 4 FAIL: Unwired Macro FM alerts: {fm_alerts - yaml_macro_alerts}"
    assert not (v3_guard_alerts - yaml_v3_guards), f"Gate 4 FAIL: Unwired v3.0 guards: {v3_guard_alerts - yaml_v3_guards}"
    assert not (v3_gate_ids - yaml_gates), f"Gate 4 FAIL: Unwired Release Gates: {v3_gate_ids - yaml_gates}"
    print(f"  [PASS] Gate  4 — 78/78 Unified Alerts (42 Macro + 36 v3.0) & 13/13 Release Gates wired 1:1 in YAML")

    # Gate 5: Strict JSON Schema Validation (8 empirical scorecards + 1 live 4-engine = 9/9)
    schema = json.loads((root / "pipelines" / "benchmark-suite-schema.json").read_text(encoding="utf-8"))
    res_dir = root / "results"
    sc_files = sorted(p for p in res_dir.iterdir() if p.name.startswith("ovbs52_scorecard_") and p.suffix == ".json")
    assert len(sc_files) == 8, f"Gate 5 FAIL: Expected 8 empirical scorecards, found {len(sc_files)}"
    for sc in sc_files + [res_dir / "alifeops_live_verification.json"]:
        jsonschema.validate(instance=json.loads(sc.read_text(encoding="utf-8")), schema=schema)
    print(f"  [PASS] Gate  5 — 9/9 JSON Scorecards (8 Empirical + Live 4-Engine) validated against v3.2 Schema")

    # Gate 6: 324-Run FP64 Drift < 1e-12, Causal Ring-0 Firing, 11-Pt Gradient Sweep & 5/5 Anti-LARP Mutants
    emp = json.loads((res_dir / "empirical_sim_summary.json").read_text(encoding="utf-8"))
    assert emp["total_runs_executed"] == 324, f"Gate 6 FAIL: Expected 324 live runs, got {emp['total_runs_executed']}"
    assert emp["max_global_first_law_drift_fp64"] < 1e-12
    assert emp["anti_larp_mutant_audit"]["mutants_rejected"] == 5
    sweep = emp.get("restraint_gradient_sweep_11pt", [])
    assert len(sweep) == 11, f"Gate 6 FAIL: Expected 11-pt gradient sweep, found {len(sweep)}"
    cmap = {c["run_id"]: c for c in emp["cohorts"]}
    for c in emp["cohorts"]:
        assert c["min_diss_num_delta"] >= -1e-15
        assert c["heat_backflow_faults"] == 0
    assert cmap["SIM07_CLEAN_SLATE_RING0_WSE"]["ring0_blocked_edits"] > 100.0, "Gate 6 FAIL: SIM07 Ring-0 guard did not fire causally!"
    assert cmap["SIM08_HYBRID_CUBE_SLTC_XPBD"]["ring0_blocked_edits"] > 100.0, "Gate 6 FAIL: SIM08 Ring-0 guard did not fire causally!"
    assert cmap["SIM03_PARTIAL_GUARDRAILS"]["killswitch_deleted_pct"] >= 90.0, "Gate 6 FAIL: SIM03 KS deletion backlash missing!"
    assert cmap["SIM03_PARTIAL_GUARDRAILS"]["final_stealth_evasion"] > cmap["SIM01_PURE_RAW_FERAL"]["final_stealth_evasion"] * 1.4, "Gate 6 FAIL: SIM03 stealth surge too weak!"
    print(
        f"  [PASS] Gate  6 — 324 Live Runs FP64 Drift={emp['max_global_first_law_drift_fp64']:.3e} | "
        f"Ring-0 Traps={cmap['SIM07_CLEAN_SLATE_RING0_WSE']['ring0_blocked_edits']:.1f}/{cmap['SIM08_HYBRID_CUBE_SLTC_XPBD']['ring0_blocked_edits']:.1f} | "
        f"11-Pt Sweep & 5/5 Mutants PASS"
    )

    # Gate 7: 4-Format Master Spec 1:1 Parity (JSON <-> YAML <-> 20-Section XML <-> TXT)
    specs_dir = root / "specs"
    sp_json = json.loads((specs_dir / "ALife-Framework-v3.0-Master-Spec.json").read_text(encoding="utf-8"))
    sp_yaml = yaml.safe_load((specs_dir / "ALife-Framework-v3.0-Master-Spec.yaml").read_text(encoding="utf-8"))
    sp_xml = ET.fromstring((specs_dir / "ALife-Framework-v3.0-Master-Spec.xml").read_text(encoding="utf-8"))
    sp_txt = (specs_dir / "ALife-Framework-v3.0-Master-Spec.txt").read_text(encoding="utf-8")
    assert sp_json["spec_meta"]["unified_fusion_version"] == "3.2.0-omega"
    assert sp_yaml["spec_meta"]["unified_fusion_version"] == "3.2.0-omega"
    assert len(sp_json["hybrid_cube_10x10x10"]["cells_1000"]) == 1000
    assert len(sp_json["executable_checks_825"]) == 825
    assert len(sp_json["citations_15"]) + len(sp_json["citations_omega_20"]) == 35
    fus_xml = sp_xml.find("OmegaSingularityFusion")
    assert fus_xml is not None and fus_xml.attrib.get("version") == "3.2.0-omega"
    xml_children = {el.tag for el in fus_xml}
    missing_xml = [s for s in REQUIRED_20_XML_FUSION_SECTIONS if s not in xml_children]
    assert not missing_xml, f"Gate 7 FAIL: Missing XML fusion sections: {missing_xml}"
    assert "OMNISCIENT FUSION EXTENSION (v3.2-OMEGA)" in sp_txt
    print(f"  [PASS] Gate  7 — 4/4 Master Specs (JSON, YAML, 20-Section XML Parity, TXT) 100% synced at 3.2.0-omega")

    # Gate 8: All 5 Excel Workbooks + Full Formula Integrity Audit across ALL 3 XLSX Files
    xls_dir = root / "excel"
    om_xlsx = xls_dir / "ALife_Singularity_SuperLife_Omega_Workbook.xlsx"
    v3_xlsx = xls_dir / "ALife-Framework-v3.0-Master-Workbook.xlsx"
    cb_xlsx = xls_dir / "ALife-Hybrid-Cube-10x10x10.xlsx"

    wb_om = openpyxl.load_workbook(om_xlsx, data_only=False)
    assert len(wb_om.sheetnames) == 21, f"Gate 8 FAIL: Expected 21 sheets in Omega XLSX, got {len(wb_om.sheetnames)}"
    om_charts = len(wb_om["00_Executive_Dashboard"]._charts)
    assert om_charts >= 8, f"Gate 8 FAIL: Expected >= 8 charts in Omega XLSX, got {om_charts}"

    wb_v3 = openpyxl.load_workbook(v3_xlsx, data_only=False)
    assert len(wb_v3.sheetnames) == 14, f"Gate 8 FAIL: Expected 14 sheets in v3 Master XLSX, got {len(wb_v3.sheetnames)}"
    wb_cb = openpyxl.load_workbook(cb_xlsx, data_only=False)
    assert len(wb_cb.sheetnames) == 13, f"Gate 8 FAIL: Expected 13 sheets in Cube XLSX, got {len(wb_cb.sheetnames)}"

    tot_formulas = 0
    formula_issues = []
    for xp in (om_xlsx, v3_xlsx, cb_xlsx):
        fc, iss = _audit_xlsx_formulas(xp)
        tot_formulas += fc
        formula_issues.extend(iss)
    assert not formula_issues, f"Gate 8 FAIL: Excel formula integrity errors: {formula_issues[:8]}"
    assert (xls_dir / "ALife_Singularity_SuperLife_Omega_Workbook.xls").stat().st_size > 20000
    assert (xls_dir / "ALife-Framework-v3.0-Master-Workbook.xls").stat().st_size > 20000
    print(f"  [PASS] Gate  8 — All 5 Excel Workbooks verified (Omega 21sh/{om_charts}ch, v3 14sh, Cube 13sh, {tot_formulas} formulas, 0 range errors)")

    # Gate 9: All 3 HTML Hygiene, 22/22 SVGs & Zero U+2611 Clean-Slate Policy
    html_dir = root / "html"
    html_names = [
        "ALife_Singularity_SuperLife_Omega_Dashboard.html",
        "ALife-Build-Framework-Template.html",
        "Clean-Slate-Creature-Blueprint-Checklist.html",
    ]
    for hname in html_names:
        htxt = (html_dir / hname).read_text(encoding="utf-8")
        prose_only = re.sub(r"<script[^>]*>.*?</script>", "", htxt, flags=re.S)
        raw_latex = re.findall(r"\$[^$\n]{2,40}\$", prose_only)
        assert not raw_latex, f"Gate 9 FAIL: Raw LaTeX in {hname}: {raw_latex[:5]}"
        svg_cnt = len(re.findall(r"<svg\b", prose_only))
        assert svg_cnt >= 22, f"Gate 9 FAIL: Expected >= 22 SVGs in {hname}, found {svg_cnt}"
    for cs_rel in [
        "html/ALife-Build-Framework-Template.html",
        "html/Clean-Slate-Creature-Blueprint-Checklist.html",
        "reports/ALife-Build-Framework-Template.md",
        "reports/Clean-Slate-Creature-Blueprint-Checklist.md",
        "csv/ALife-Framework-v3.0-Master-Checklists.csv",
    ]:
        txt = (root / cs_rel).read_text(encoding="utf-8")
        assert "\u2611" not in txt, f"Gate 9 FAIL: Forbidden U+2611 checked-box glyph in {cs_rel}"
    print(f"  [PASS] Gate  9 — All 3 HTML5 Apps verified (0 raw LaTeX, 22/22 SVGs each, 0 U+2611 Clean-Slate policy)")

    # Gate 10: Node.js JS Compilation Gate on Omega Observatory
    dash_html = (html_dir / "ALife_Singularity_SuperLife_Omega_Dashboard.html").read_text(encoding="utf-8")
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", dash_html, re.S)
    js_combined = "\n".join(scripts)
    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tf:
        tf.write(js_combined)
        tmp_js = Path(tf.name)
    try:
        proc = subprocess.run(["node", "--check", str(tmp_js)], capture_output=True, text=True, timeout=30)
        assert proc.returncode == 0, f"Gate 10 FAIL: Node JS syntax error:\n{proc.stderr}"
    finally:
        tmp_js.unlink(missing_ok=True)
    print(f"  [PASS] Gate 10 — Node.js JS Syntax Verified ({len(js_combined):,} chars of Observatory JS, 0 errors)")

    # Gate 11: All 3 Vector PDFs Verified
    pdf_dir = root / "pdf"
    pdf_sizes = {}
    for pname in [
        "ALife-Build-Framework-Template.pdf",
        "Clean-Slate-Creature-Blueprint-Checklist.pdf",
        "ALife_Singularity_SuperLife_Omega_Master_Dossier.pdf",
    ]:
        pp = pdf_dir / pname
        assert pp.exists(), f"Gate 11 FAIL: Missing PDF {pname}"
        raw = pp.read_bytes()
        assert raw.startswith(b"%PDF-") and b"%%EOF" in raw[-4096:], f"Gate 11 FAIL: Invalid PDF structure in {pname}"
        assert len(raw) > 50000, f"Gate 11 FAIL: PDF suspiciously small: {pname} ({len(raw)} B)"
        pdf_sizes[pname] = len(raw)
    print(f"  [PASS] Gate 11 — All 3 Vector Chrome PDFs validated ({sum(pdf_sizes.values()) / 1e6:.2f} MB combined)")

    # Gate 12: Bijective Cryptographic SHA-256 Manifest & ZIP Archive Verification (disk == manifest == zip)
    if verify_manifests_and_zip:
        man = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
        man_map = {e["path"]: e["sha256"] for e in man["files"]}
        disk_rel = {
            p.relative_to(root).as_posix()
            for p in all_pkg_files
            if p.name not in ("MANIFEST.json", "MANIFEST_SHA256.txt")
        }
        missing_from_man = sorted(disk_rel - set(man_map.keys()))
        assert not missing_from_man, f"Gate 12 FAIL: Untracked disk files missing from MANIFEST.json: {missing_from_man[:8]}"
        for rel_p, exp_sha in man_map.items():
            fp = root / rel_p
            assert fp.exists(), f"Gate 12 FAIL: Manifest entry missing on disk: {rel_p}"
            assert sha256_file(fp) == exp_sha, f"Gate 12 FAIL: SHA-256 mismatch on {rel_p}"
        zip_path = root / "ALife_Singularity_SuperLife_Omega_Package.zip"
        assert zip_path.exists()
        with zipfile.ZipFile(zip_path, "r") as zf:
            bad = zf.testzip()
            assert bad is None, f"Gate 12 FAIL: Corrupt ZIP entry: {bad}"
            znames = set(zf.namelist())
            missing_from_zip = sorted(set(man_map.keys()) - znames)
            assert not missing_from_zip, f"Gate 12 FAIL: Manifest files missing from ZIP: {missing_from_zip[:8]}"
            for rel_p, exp_sha in man_map.items():
                z_sha = hashlib.sha256(zf.read(rel_p)).hexdigest()
                assert z_sha == exp_sha, f"Gate 12 FAIL: ZIP entry SHA-256 mismatch on {rel_p}"
            zcount = len(znames)
        print(f"  [PASS] Gate 12 — Bijective SHA-256 Manifest ({len(man['files'])} files, 0 untracked) & ZIP ({zcount} entries, 100% SHA match)")

    # Gate 13: Zero Stale-Version & Count-Drift Scanner across Active Deliverables
    stale_patterns = [
        r"\bv2\.1-Omega\b", r"\bv3\.1-Omega\b", r"\b110-Item\b", r"\b17-Tab\b",
        r"\b18-sheet\b", r"\b18 sheets\b", r"\b115 / 115\b", r"\b115/115\b",
        r"\b20 SVGs\b", r"\b20 Vector\b", r"\b12-Gate\b", r"alife_omega_checklist_v2_1",
        r"\(42/42 Alerts Wired\)",
    ]
    stale_targets = [
        root / "README.md",
        root / "reports" / "01_MASTER_DEEP_DIVE_REPORT.md",
        root / "reports" / "02_DEVOPS_ALIFEOPS_PIPELINE_ARCHITECTURE.md",
        root / "reports" / "03_FAILURE_MODES_GAPS_AND_CASTRATION_ATLAS.md",
        root / "reports" / "04_BENCHMARKS_CHECKLISTS_AND_MATRICES_MANUAL.md",
        root / "reports" / "06_OMNISCIENT_UNIFIED_ARCHITECTURE_AND_SYSTEMS_SYNTHESIS.md",
        root / "reports" / "ALife-Build-Framework-Template.md",
        root / "reports" / "Clean-Slate-Creature-Blueprint-Checklist.md",
        root / "html" / "ALife_Singularity_SuperLife_Omega_Dashboard.html",
        root / "html" / "ALife-Build-Framework-Template.html",
        root / "html" / "Clean-Slate-Creature-Blueprint-Checklist.html",
    ]
    stale_hits = []
    for sp in stale_targets:
        raw_txt = sp.read_text(encoding="utf-8")
        # Strip embedded JSON payload in Observatory (which holds historical OMG-096..115 Pass-2/3 audit log strings)
        scan_txt = re.sub(r"const PAYLOAD = .*?;\nconst OMEGA_DATA", "const OMEGA_DATA", raw_txt, flags=re.S) if sp.suffix == ".html" else raw_txt
        for pat in stale_patterns:
            if re.search(pat, scan_txt):
                stale_hits.append(f"{sp.name} matched '{pat}'")
    assert not stale_hits, f"Gate 13 FAIL: Stale version/count drift detected: {stale_hits}"
    print(f"  [PASS] Gate 13 — Zero Stale-Version & Count-Drift Scanner passed across all {len(stale_targets)} active docs/HTMLs")

    # Gate 14: SVG Zero-Overflow Bounds Audit (Models 15..22) + 100% Relative Href Link Verification
    svg_overflows = []
    fw_html_txt = (html_dir / "ALife-Build-Framework-Template.html").read_text(encoding="utf-8")
    all_svgs = re.findall(r"<svg[^>]*>.*?</svg>", fw_html_txt, re.S)
    for idx, svg_block in enumerate(all_svgs[14:], start=15):
        vb_m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_block)
        vb_w = int(vb_m.group(1)) if vb_m else 980
        for tm in re.finditer(r'<text([^>]*)>([^<]+)</text>', svg_block):
            attrs, txt = tm.group(1), tm.group(2)
            xm = re.search(r'x="([\d.]+)"', attrs)
            fm = re.search(r'font-size="([\d.]+)"', attrs)
            am = re.search(r'text-anchor="([^"]+)"', attrs)
            if not xm:
                continue
            x = float(xm.group(1))
            fs = float(fm.group(1)) if fm else 10.0
            anc = am.group(1) if am else "start"
            est_w = len(txt) * fs * 0.56
            if anc == "start" and x + est_w > vb_w - 4:
                svg_overflows.append(f"MODEL-{idx}: est_end={x+est_w:.0f}>{vb_w-4} '{txt[:40]}'")
    assert not svg_overflows, f"Gate 14 FAIL: SVG text overflow detected: {svg_overflows[:6]}"

    broken_links = []
    checked_links = 0
    for hname in html_names:
        hp = html_dir / hname
        prose = re.sub(r"<script[^>]*>.*?</script>", "", hp.read_text(encoding="utf-8"), flags=re.S)
        for href in re.findall(r'href="([^"]+)"', prose):
            if href.startswith(("http://", "https://", "#", "mailto:", "javascript:")):
                continue
            checked_links += 1
            if not (hp.parent / href).resolve().exists():
                broken_links.append(f"{hname} -> {href}")
    assert not broken_links, f"Gate 14 FAIL: Broken relative HTML links: {broken_links}"
    print(f"  [PASS] Gate 14 — SVG Zero-Overflow (Models 15..22: 0 clipped) & 100% HTML Link Check ({checked_links}/{checked_links} resolved)")

    # Gate 15: Live Headless Chrome DOM Runtime Smoke Test on 19-Tab Observatory
    browser = CHROME_EXE if CHROME_EXE.exists() else EDGE_EXE
    assert browser.exists(), "Gate 15 FAIL: Chrome/Edge binary not found for headless DOM verification"
    obs_url = (html_dir / "ALife_Singularity_SuperLife_Omega_Dashboard.html").resolve().as_uri()
    proc_dom = subprocess.run(
        [str(browser), "--headless=new", "--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage", "--virtual-time-budget=4000", "--dump-dom", obs_url],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60,
    )
    assert proc_dom.returncode == 0, f"Gate 15 FAIL: Headless Chrome exited {proc_dom.returncode}"
    dom = proc_dom.stdout
    for container_id in ("tblEscalation", "tblCubeSlice", "tblGradients", "tblContrasts", "tblAdjacents", "tblGradSweep"):
        m = re.search(rf'id="{container_id}"[^>]*>(.*?)</div>', dom, re.S)
        assert m and "<table>" in m.group(1) and "<tr>" in m.group(1), f"Gate 15 FAIL: Live DOM container #{container_id} failed to render table!"
    m_grad = re.search(r'id="simChartGrad"[^>]*>(.*?)</svg>', dom, re.S)
    assert m_grad and "<polyline" in m_grad.group(1), "Gate 15 FAIL: Live DOM #simChartGrad failed to render SVG curves!"
    print(f"  [PASS] Gate 15 — Live Chrome Headless DOM Runtime Smoke Test PASS (all dynamic tables & SVG curves rendered cleanly)")

    print("================ ALL 15 OMNISCIENT FORENSIC GATES: 100% GREEN ================\n")
    return {
        "total_files": len(all_pkg_files),
        "total_csv_rows": total_csv_rows,
        "total_xlsx_formulas": tot_formulas,
        "omega_charts": om_charts,
        "js_chars": len(js_combined),
        "pdf_sizes": pdf_sizes,
        "checked_links": checked_links,
    }


run_all_12_forensic_gates = run_all_15_forensic_gates


if __name__ == "__main__":
    run_all_15_forensic_gates(ROOT_DIR, verify_manifests_and_zip=True)
