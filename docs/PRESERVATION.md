# Long-Term Preservation & Archival Strategy

To ensure permanent scholarly discoverability and bit-level verifiability of `alife-singularity-omega-package` (`v3.5.0`), this repository implements a four-tier preservation stack:

1. **Cryptographic Content Addressing (Local & Release):**
   - `CHECKSUMS.sha256` & `MANIFEST_SHA256.txt`: SHA-256 hashes of every package deliverable.
   - `data/MANIFEST.sha256`: Dedicated dataset integrity lock (Build Standard `B39`).
   - `.github/workflows/release.yml`: Publishes `SHA256SUMS` and SLSA v1 build provenance (`actions/attest-build-provenance`) on every `v*` Git tag.
2. **Dual-Drive Local Cold Mirror:**
   - Synchronized byte-for-byte between ReFS Dev Drive `Z:\[Vibe Coded (AI)]\ANTIGRAVITY\alife-singularity-omega-package` and secondary SSD `I:\A-Life God Plan\A-Life Master Folder Build`, verified by Gate 18 (`0` SHA-256 mismatches).
3. **FAIR Machine-Readable Descriptors:**
   - [`CITATION.cff`](../CITATION.cff) (CFF v1.2.0), [`CITATION.bib`](../CITATION.bib), [`.zenodo.json`](../.zenodo.json), [`croissant.json`](../croissant.json) (MLCommons Croissant 1.0), and [`ro-crate-metadata.json`](../ro-crate-metadata.json) (RO-Crate 1.1).
4. **External Permanent Archives (Post-Push Registration):**
   - **GitHub + Zenodo:** Enabling GitHub-Zenodo integration on tag `v3.5.0` automatically mints a permanent Zenodo DOI using `.zenodo.json`. *(No DOI is fabricated prior to actual Zenodo minting.)*
   - **Software Heritage (SWHID):** Triggering Save Code Now on `https://github.com/0thernes/alife-singularity-omega-package` post-push archives the exact Git commit tree permanently.
   - **arXiv Submission Readiness:** `dist/arxiv_submission.tar.gz` is pre-verified by clean-room extraction and compilation in `scripts/build_paper_and_figures.py`.
