# Operations, Backup, Mirror & Preservation Runbook (Build Standard A35)

## 1. Dual-Drive Atomic Mirror (`Z: <-> I:`)

The canonical working repository resides on the dedicated ReFS Dev Drive (`Z:\[Vibe Coded (AI)]\ANTIGRAVITY\alife-singularity-omega-package`) and is mirrored atomically to the secondary SSD archive (`I:\A-Life God Plan\A-Life Master Folder Build`).

### Mirror & Verification Procedure
1. Rebuild and verify `Z:` locally (`just build`).
2. Mirror all package directories and files to `I:` (excluding `.git`, `lean/.lake`, `paper/build`, and transient caches), preserving the 17 Clean-Slate v3.0 files at the root of `I:` as well as in their structured subdirectories.
3. Run Gate 18 byte-for-byte SHA-256 verification:
   ```powershell
   uv run --no-project --with openpyxl --with xlwt --with xlrd --with pyyaml --with jsonschema --with scipy --with pypdf `
     python scripts/audit_omniscient_integrity.py --mirror-root "I:\A-Life God Plan\A-Life Master Folder Build"
   ```
   Confirm `0` SHA-256 mismatches across every manifested file.

## 2. Offline Git Bundle Backup

Create a self-contained single-file Git archive (`git bundle`) for cold offline backup:
```bash
git bundle create alife-singularity-omega-v3.4.0.bundle --all
git bundle verify alife-singularity-omega-v3.4.0.bundle
```

## 3. Offsite Remote Mirror & Archival Preservation
- **Primary Remote:** `https://github.com/0thernes/alife-singularity-omega-package`
- **Backup Mirror Remote:** Configure `git remote add backup <url>` and run `git push backup --mirror` (or `just mirror`).
- **Permanent Preservation:** See [`PRESERVATION.md`](PRESERVATION.md) for Zenodo (`.zenodo.json`) and Software Heritage (SWHID) archival steps.
