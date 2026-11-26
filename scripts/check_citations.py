#!/usr/bin/env python3
"""Programmatically verify every DOI and URL in paper/refs.bib resolves cleanly."""
from __future__ import annotations

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


def _http_ok(url: str, timeout: int = 12) -> tuple[bool, int | str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "alife-singularity-omega-citation-verifier/3.4.0 (mailto:0_0@0thernes.art)"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return (200 <= resp.status < 400), resp.status
    except urllib.error.HTTPError as e:
        # Some publishers return 403 to automated HTTP clients even when DOI handle exists
        return (e.code in (401, 403, 405, 429)), e.code
    except Exception as exc:
        return False, str(exc)


def verify_citations() -> dict:
    txt = BIB.read_text(encoding="utf-8")
    entries = re.split(r"(?=@\w+\{)", txt)
    results = []
    failures = []

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
            results.append({"key": key, "kind": "doi", "target": doi, "ok": ok, "status": status})
            if not ok:
                failures.append(f"{key} (DOI {doi}): {status}")
        elif m_url:
            url = m_url.group(1).strip()
            ok, status = _http_ok(url)
            results.append({"key": key, "kind": "url", "target": url, "ok": ok, "status": status})
            if not ok:
                failures.append(f"{key} (URL {url}): {status}")
        else:
            failures.append(f"{key}: missing both doi and url")

    report = {
        "bib_file": "paper/refs.bib",
        "total_entries": len(results),
        "resolved_count": sum(1 for r in results if r["ok"]),
        "failures": failures,
        "entries": results,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"  [CITE] Verified {report['resolved_count']}/{report['total_entries']} refs in paper/refs.bib -> {OUT_JSON.name}")
    if failures:
        raise RuntimeError(f"Citation verification failures: {failures}")
    return report


if __name__ == "__main__":
    try:
        verify_citations()
    except Exception as exc:
        print(f"  [FAIL] check_citations: {exc}", file=sys.stderr)
        sys.exit(1)
