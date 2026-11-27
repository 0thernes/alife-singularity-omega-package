# SPDX-License-Identifier: Apache-2.0
"""
Unit, Negative, Contract, Determinism & Round-1/Round-2 Regression Test Suite
for alife-singularity-omega-package (v3.5.0) — Build Standard A09, B03, B05-B09.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
import re
import subprocess
import sys

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from reference.ovbs52_oracle import (
    oracle_classify_stage,
    oracle_composite_ovi_rounded,
)


def test_semver_parity_across_all_manifests() -> None:
    """Build Standard A08: single version source across VERSION, CHANGELOG, CITATION.cff, pyproject.toml, formalization.yaml."""
    ver = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    assert re.fullmatch(r"\d+\.\d+\.\d+", ver), f"Invalid semver in VERSION: {ver}"
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert re.search(rf"^## \[?v?{re.escape(ver)}\]?", changelog, re.M)
    citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    assert str(citation["version"]) == ver
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert f'version = "{ver}"' in pyproject
    formal = yaml.safe_load((ROOT / "lean" / "formalization.yaml").read_text(encoding="utf-8"))
    assert str(formal["release_version"]) == ver


def test_repo_yaml_validates_against_build_standard_schema() -> None:
    """Contract test: repo.yaml validates strictly against repo-standard.schema.json (Draft 2020-12)."""
    schema = json.loads((ROOT / "repo-standard.schema.json").read_text(encoding="utf-8"))
    repo_manifest = yaml.safe_load((ROOT / "repo.yaml").read_text(encoding="utf-8"))
    jsonschema.validate(instance=repo_manifest, schema=schema)
    assert repo_manifest["standard"] == "1.2.0"
    assert len(repo_manifest["items"]) == 90


def test_fair_metadata_json_files_valid() -> None:
    """Contract test: .zenodo.json, croissant.json, ro-crate-metadata.json, codemeta.json parse cleanly."""
    for rel in (".zenodo.json", "croissant.json", "ro-crate-metadata.json", "codemeta.json"):
        txt = (ROOT / rel).read_text(encoding="utf-8")
        data = json.loads(txt)
        assert isinstance(data, dict)
        assert "0thernes LLC" not in txt
        assert "0009-0006-8168-9648" in txt


def test_regression_h01_zero_unformed_llc_in_active_corpus() -> None:
    """Regression H-01 (OMG-146): Zero unformed '0thernes LLC' identity claims anywhere in active prose/config/code."""
    skip_dirs = {".git", "__pycache__", ".lake", "paper/build", ".v3_source_baseline", ".pytest_cache"}
    allowed_doc_files = {"ERRATA.md", "HARDENING_LOG.md", "CHANGELOG.md", "UPGRADING.md", "AGENTS.md"}
    allowed_paths = {
        "docs/faq.md",
        "docs/ACADEMIC_REVIEW.md",
        "docs/reviews/2026-11-25-three-cycle-redteam-hardening.md",
        "docs/reviews/2026-11-26-round2-3-cycle-hardening-audit.md",
        "scripts/omega_datasets_part6.py",
        "scripts/audit_omniscient_integrity.py",
        "tests/test_omega_package.py",
        "csv/ALife-v3.0-Errata-Closure-Register.csv",
        "reports/ALife-v3.0-Errata-Closure-Report.md",
        "llms-full.txt",
    }
    hits = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if any(seg in p.parts for seg in skip_dirs) or rel.startswith("paper/build/"):
            continue
        if p.name in allowed_doc_files or rel in allowed_paths:
            continue
        if p.suffix.lower() not in {".md", ".tex", ".py", ".json", ".yaml", ".yml", ".cff", ".toml", ".txt", ".lean"}:
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        if "0thernes LLC" in txt:
            hits.append(rel)
    assert not hits, f"Unformed '0thernes LLC' found in: {hits}"


def test_regression_h02_exact_theorem_arithmetic_310_plus_50_eq_360() -> None:
    """Regression H-02 (OMG-147): Native 5-engine theorem sum is 48+78+100+54+30=310, plus 50 local = 360."""
    live = json.loads((ROOT / "results" / "alifeops_live_verification.json").read_text(encoding="utf-8"))
    er = live["engine_receipts"]
    native_sum = (
        er["tier1_autophage"]["lean4_theorems"]
        + er["tier2_cellulogonic"]["lean4_theorems"]
        + er["tier2plus_omega"]["lean4_theorems"]
        + er["tier3_noetic_organism"]["lean4_theorems"]
        + er["tier34_asmodensius"]["lean4_theorems"]
    )
    assert native_sum == 310
    assert live["total_lean4_theorems"] == 310
    axioms = [ln.strip() for ln in (ROOT / "results" / "lean_package_axioms.txt").read_text(encoding="utf-8").splitlines() if ln.strip()]
    assert len(axioms) == 55  # 50 core + 5 Palomar
    assert native_sum + 50 == 360


def test_regression_h04_p8_submetric_pool_has_7_distinct_entries() -> None:
    """Regression H-04 (OMG-149): P8_FERAL_RESILIENCE_CRITICALITY has 7 tuple entries (no modulo wrap on BM-FRL-07)."""
    import ast

    tree = ast.parse((ROOT / "scripts" / "run_alifeops_suite.py").read_text(encoding="utf-8"))
    found_len = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id == "submetric_pools" and isinstance(node.value, ast.Dict):
                    for k, v in zip(node.value.keys, node.value.values, strict=True):
                        if isinstance(k, ast.Constant) and k.value == "P8_FERAL_RESILIENCE_CRITICALITY" and isinstance(v, ast.List):
                            found_len = len(v.elts)
    assert found_len == 7, f"Expected 7 P8 submetric tuples, got {found_len}"


def test_regression_h05_utf8_encoding_on_subprocess_runs() -> None:
    """Regression H-05 (OMG-150): Chrome & native runner subprocess.run calls specify encoding='utf-8'."""
    for rel in ("scripts/build_v3_unified_artifacts.py", "scripts/run_alifeops_suite.py"):
        txt = (ROOT / rel).read_text(encoding="utf-8")
        for m in re.finditer(r"subprocess\.run\((.*?)\)", txt, re.S):
            call = m.group(1)
            if "text=True" in call:
                assert 'encoding="utf-8"' in call or "encoding='utf-8'" in call, f"Missing utf-8 in {rel}"


def test_regression_h06_zero_r4_banned_files_and_sub_5mb_tracked() -> None:
    """Build Standard R4 & A24: zero banned governance/bot files; every Git-tracked file < 5.00 MB."""
    banned = [
        ".github/pull_request_template.md",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/PULL_REQUEST_TEMPLATE",
        "PULL_REQUEST_TEMPLATE.md",
        ".github/dependabot.yml",
        ".github/renovate.json",
        "renovate.json",
        ".coderabbit.yaml",
        ".github/copilot-instructions.md",
        ".github/FUNDING.yml",
    ]
    for b in banned:
        assert not (ROOT / b).exists(), f"R4 banned file present: {b}"

    proc = subprocess.run(
        ["git", "ls-files"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )
    oversized = []
    for rel in proc.stdout.splitlines():
        p = ROOT / rel
        if p.is_file() and p.stat().st_size > 5_242_880:
            oversized.append((rel, p.stat().st_size))
    assert not oversized, f"A24 violation (>5 MB git-tracked): {oversized}"


def test_regression_h07_mega_atlas_zero_retirements_and_25_targets() -> None:
    """Claim C8 / H-07: Mega-Atlas crosswalk has 25 rows and every row declares NO overarching retirement."""
    p = ROOT / "csv" / "21_mega_atlas_1900_open_problems_crosswalk.csv"
    assert p.exists(), "Run build_omega_package.py first to materialize csv/21"
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    assert len(rows) == 26  # 1 header + 25 rows
    for r in rows[1:]:
        assert "NO" in r[5].upper() or "OPEN" in r[5].upper(), f"Unexpected retirement status in {r[0]}: {r[5]}"


def test_determinism_and_live_receipt_oracle_agreement() -> None:
    """Build Standard B03 & B09: Live 5-engine OVBS-52 receipt matches independent 50-digit oracle & schema."""
    schema = json.loads((ROOT / "pipelines" / "benchmark-suite-schema.json").read_text(encoding="utf-8"))
    live = json.loads((ROOT / "results" / "alifeops_live_verification.json").read_text(encoding="utf-8"))
    jsonschema.validate(instance=live, schema=schema)
    expected = oracle_composite_ovi_rounded(live["pillar_scores"], gamma_pass=True, spiegelman_factor=1.0)
    assert abs(expected - live["composite_ovi_score"]) < 0.02
    assert oracle_classify_stage(expected) == live["stage_classification"]
    # Determinism check on oracle
    assert oracle_composite_ovi_rounded(live["pillar_scores"]) == expected


def test_lean_suite_zero_sorry_and_axiom_whitelist() -> None:
    """Claim C1: Zero sorry/admit/native_decide in lean/ and verbatim axiom block in README.md."""
    for lf in (ROOT / "lean").rglob("*.lean"):
        if ".lake" in lf.parts or lf.name == "PalomarChallenge.lean":
            continue
        txt = lf.read_text(encoding="utf-8")
        assert not re.search(r"\bsorry\b", txt), f"Found sorry in {lf}"
        assert not re.search(r"\badmit\b", txt), f"Found admit in {lf}"
        assert "native_decide" not in txt, f"Found native_decide in {lf}"

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_readme_axioms.py")],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout


def test_clean_slate_zero_checked_box_glyph_policy() -> None:
    """Clean-Slate 0/825 Policy: Zero U+2611 checked-box glyphs in all Clean-Slate templates."""
    for rel in (
        "html/ALife-Build-Framework-Template.html",
        "html/Clean-Slate-Creature-Blueprint-Checklist.html",
        "reports/ALife-Build-Framework-Template.md",
        "reports/Clean-Slate-Creature-Blueprint-Checklist.md",
        "csv/ALife-Framework-v3.0-Master-Checklists.csv",
    ):
        assert "\u2611" not in (ROOT / rel).read_text(encoding="utf-8"), f"Forbidden U+2611 in {rel}"


def test_regression_r2_paper_table2_matches_live_sim_and_stage5_sim08() -> None:
    """Round-2 Regression: Auto-generated paper/generated_tables.tex matches live empirical_sim_summary.json & SIM08 is Stage 5."""
    emp = json.loads((ROOT / "results" / "empirical_sim_summary.json").read_text(encoding="utf-8"))
    tex = (ROOT / "paper" / "generated_tables.tex").read_text(encoding="utf-8")
    cmap = {c["run_id"]: c for c in emp["cohorts"]}
    assert cmap["SIM08_HYBRID_CUBE_SLTC_XPBD"]["stage_classification"] == "STAGE_5_CONVERGED_SYNTHESIS"
    for c in emp["cohorts"]:
        assert c["run_id"] in tex
        assert f"{c['composite_ovi']:5.2f}" in tex
        assert "cohens_dz_vs_feral" in c and "ci95_low_vs_feral" in c and "composite_ovi_arith" in c


def test_regression_r2_citations_zero_retractions_and_rfc3161_tsr() -> None:
    """Round-2 Regression: Crossref 0-retraction citation receipt & RFC 3161 TSA token present."""
    cit = json.loads((ROOT / "results" / "citation_verification.json").read_text(encoding="utf-8"))
    assert cit["resolved_count"] == cit["total_entries"] >= 20
    assert cit["retractions_found"] == 0
    assert (ROOT / "SUBMISSION_READINESS.md").exists()
    tsr = ROOT / "data" / "timestamps" / "CHECKSUMS.sha256.tsr"
    assert tsr.exists() and tsr.stat().st_size > 100

