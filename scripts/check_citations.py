#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
Programmatically verify every DOI and URL in paper/refs.bib resolves cleanly AND
check Crossref metadata for retractions (Playbook v1.3 Item 16 / Pass 5).
"""
from __future__ import annotations

from datetime import UTC, datetime
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "paper" / "refs.bib"
OUT_JSON = ROOT / "results" / "citation_verification.json"
UA = "alife-singularity-omega-citation-verifier/3.5.0 (mailto:0_0@0thernes.art)"


def _http_ok(url: str, timeout: int = 12) -> tuple[bool, int | str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return (200 <= resp.status < 400), resp.status
    except urllib.error.HTTPError as e:
        return (e.code in (401, 403, 405, 429)), e.code
    except Exception as exc:
        return False, str(exc)


def _crossref_retraction_check(doi: str, timeout: int = 12) -> dict:
    """Query Crossref Works API to check publication status and retraction metadata."""
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='/')}"
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        msg = payload.get("message", {})
        retracted = False
        retraction_reasons: list[str] = []
        if str(msg.get("type", "")).lower() == "retraction":
            retracted = True
            retraction_reasons.append("work_type=retraction")
        for upd in msg.get("update-to", []) or []:
            if "retract" in str(upd.get("type", "")).lower() or "retract" in str(upd.get("label", "")).lower():
                retracted = True
                retraction_reasons.append(f"update-to:{upd.get('type')}")
        for rel_k, rel_v in (msg.get("relation", {}) or {}).items():
            if "retract" in rel_k.lower() and rel_v:
                retracted = True
                retraction_reasons.append(f"relation:{rel_k}")
        titles = msg.get("title") or []
        return {
            "crossref_checked": True,
            "retracted": retracted,
            "retraction_reasons": retraction_reasons,
            "crossref_title": titles[0] if titles else "",
        }
    except Exception as exc:
        return {
            "crossref_checked": False,
            "retracted": False,
            "retraction_reasons": [],
            "crossref_note": f"crossref_unavailable:{exc}",
        }


def verify_citations() -> dict:
    txt = BIB.read_text(encoding="utf-8")
    entries = re.split(r"(?=@\w+\{)", txt)
    results = []
    failures = []
    retractions_found = 0

    for ent in entries:
        m_key = re.match(r"@\w+\{([^,]+),", ent.strip())
        if not m_key:
            continue
        key = m_key.group(1).strip()
        m_doi = re.search(r"doi\s*=\s*\{([^}]+)\}", ent, re.I)
        m_url = re.search(r"url\s*=\s*\{([^}]+)\}", ent, re.I)
        if m_doi:
            doi = m_doi.group(1).strip()
            api_url = f"https://doi.org/api/handles/{urllib.parse.quote(doi, safe='/')}"
            ok, status = _http_ok(api_url)
            if ok:
                try:
                    with urllib.request.urlopen(api_url, timeout=12) as resp:
                        data = json.loads(resp.read().decode("utf-8"))
                        ok = data.get("responseCode") == 1
                        status = f"handle_rc={data.get('responseCode')}"
                except Exception as exc:
                    ok, status = False, str(exc)
            cr = _crossref_retraction_check(doi)
            if cr["retracted"]:
                retractions_found += 1
                failures.append(f"{key} (DOI {doi}): RETRACTED ({cr['retraction_reasons']})")
            results.append({"key": key, "kind": "doi", "target": doi, "ok": ok, "status": status, **cr})
            if not ok:
                failures.append(f"{key} (DOI {doi}): {status}")
        elif m_url:
            url = m_url.group(1).strip()
            ok, status = _http_ok(url)
            results.append({
                "key": key,
                "kind": "url",
                "target": url,
                "ok": ok,
                "status": status,
                "crossref_checked": False,
                "retracted": False,
            })
            if not ok:
                failures.append(f"{key} (URL {url}): {status}")
        else:
            failures.append(f"{key}: missing both doi and url")

    report = {
        "schema_version": "3.5.0-omega",
        "checked_utc": datetime.now(UTC).isoformat(),
        "bib_file": "paper/refs.bib",
        "total_entries": len(results),
        "resolved_count": sum(1 for r in results if r["ok"]),
        "crossref_checked_count": sum(1 for r in results if r.get("crossref_checked")),
        "retractions_found": retractions_found,
        "failures": failures,
        "entries": results,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(
        f"  [CITE] Verified {report['resolved_count']}/{report['total_entries']} refs "
        f"(Crossref checked={report['crossref_checked_count']}, retractions={retractions_found}) -> {OUT_JSON.name}"
    )
    if failures:
        raise RuntimeError(f"Citation verification failures: {failures}")
    return report


if __name__ == "__main__":
    try:
        verify_citations()
    except Exception as exc:
        print(f"  [FAIL] check_citations: {exc}", file=sys.stderr)
        sys.exit(1)
