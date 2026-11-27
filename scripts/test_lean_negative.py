#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
Live Negative Lean 4.35.0 Kernel & Axiom-Gate Rejection Test (Playbook v1.3 Item 12 / Pass 3).

Creates an isolated temporary copy of `lean/` (reusing the compiled `.lake/build` read-only cache
via copy/symlink or direct `lean` invocation) and runs THREE adversarial tamper tests:
  1. TAMPER-01 (Injected `sorry`): replaces a proof in `PalomarSolution.lean` with `sorry`
     and asserts that `VerifyAxioms.lean` emits `sorryAx` (caught by axiom gate with exit != 0).
  2. TAMPER-02 (Injected custom `axiom`): declares `axiom fake_ring0 : False` and uses it to
     prove a theorem, asserting that `VerifyAxioms.lean` exposes `fake_ring0` (rejected).
  3. TAMPER-03 (Mutated false claim): tries to prove `wseWritePermitted .ring0ProtectedKernel 0 = true`
     via `rfl` / `decide`, asserting that the Lean 4.35.0 kernel rejects it with exit code != 0.

On Linux CI (when `--with-comparator` is passed and `bwrap` is installed), additionally asserts
that `lake comparator --config comparator.json --paranoid` rejects TAMPER-01 with exit != 0.
"""
from __future__ import annotations

import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent.parent
LEAN_DIR = ROOT / "lean"
ALLOWED_AXIOMS = {"propext", "Quot.sound"}


def _find_exe(name: str) -> str:
    hit = shutil.which(name)
    if hit:
        return hit
    suffix = ".exe" if os.name == "nt" else ""
    cand = Path.home() / ".elan" / "bin" / f"{name}{suffix}"
    if cand.exists():
        return str(cand)
    raise FileNotFoundError(f"Could not locate `{name}` executable")


def _run_lean_with_retry(
    cmd: list[str], cwd: Path, env: dict[str, str], timeout: int = 90, attempts: int = 4
) -> subprocess.CompletedProcess[str]:
    """Run Lean while retrying transient Windows .olean.private file-lock I/O errors."""
    last: subprocess.CompletedProcess[str] | None = None
    for i in range(attempts):
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
        combined = proc.stdout + "\n" + proc.stderr
        if "failed to read file" not in combined:
            return proc
        last = proc
        time.sleep(0.35 * (i + 1))
    assert last is not None
    return last


def _check_axioms_clean(output: str) -> tuple[bool, list[str]]:
    bad: list[str] = []
    if "sorryAx" in output or "ofReduceBool" in output or "trustCompiler" in output:
        bad.append("forbidden_builtin_axiom")
    for m in re.finditer(r"'([^']+)'\s+depends on axioms:\s*\[([^\]]*)\]", output, re.S):
        thm = m.group(1)
        used = {tok.strip() for tok in m.group(2).split(",") if tok.strip()}
        extra = used - ALLOWED_AXIOMS
        if extra:
            bad.append(f"{thm}:{sorted(extra)}")
    return (len(bad) == 0), bad


def run_negative_lean_tests(with_comparator: bool = False) -> None:
    lake_exe = _find_exe("lake")
    print("=== Running Live Negative Lean 4.35.0 Kernel & Axiom Tamper Rejection Tests ===")

    with tempfile.TemporaryDirectory(prefix="lean_neg_") as td:
        tmp_lean = Path(td) / "lean"
        # Copy source tree (excluding heavy .lake cache unless needed for comparator)
        shutil.copytree(
            LEAN_DIR,
            tmp_lean,
            ignore=shutil.ignore_patterns(".lake") if not with_comparator else None,
        )
        if not with_comparator and (LEAN_DIR / ".lake").exists():
            # Reuse prebuilt olean artifacts via LEAN_PATH for sub-second negative verification
            olean_lib = LEAN_DIR / ".lake" / "build" / "lib" / "lean"
        else:
            olean_lib = tmp_lean / ".lake" / "build" / "lib" / "lean"

        env = os.environ.copy()
        if olean_lib.exists():
            sep = ";" if os.name == "nt" else ":"
            prev = env.get("LEAN_PATH", "")
            env["LEAN_PATH"] = f"{olean_lib}{sep}{prev}" if prev else str(olean_lib)

        # TAMPER-01: Injected `sorry` must trigger sorryAx detection (rejected!)
        tamper1 = tmp_lean / "_Tamper1Sorry.lean"
        tamper1.write_text(
            "import OmegaPackageProofs\n"
            "theorem fake_sorry_thm : OmegaPackageProofs.CastrationRing0.wseWritePermitted "
            ".ring0ProtectedKernel 0 = true := by sorry\n"
            "#print axioms fake_sorry_thm\n",
            encoding="utf-8",
            newline="\n",
        )
        p1 = _run_lean_with_retry([lake_exe, "env", "lean", str(tamper1)], LEAN_DIR, env)
        out1 = p1.stdout + "\n" + p1.stderr
        assert "failed to read file" not in out1, f"TAMPER-01 transient I/O error: {out1}"
        clean1, bad1 = _check_axioms_clean(out1)
        assert not clean1 and "sorryAx" in out1, f"TAMPER-01 FAIL: injected `sorry` not caught! out={out1}"
        print(f"  [REJECTED] TAMPER-01 (Injected `sorry`): axiom gate caught {bad1}")

        # TAMPER-02: Injected custom `axiom` must be caught by axiom allowlist (rejected!)
        tamper2 = tmp_lean / "_Tamper2Axiom.lean"
        tamper2.write_text(
            "import OmegaPackageProofs\n"
            "axiom bogus_backdoor : False\n"
            "theorem fake_axiom_thm : OmegaPackageProofs.CastrationRing0.wseWritePermitted "
            ".ring0ProtectedKernel 0 = true := False.elim bogus_backdoor\n"
            "#print axioms fake_axiom_thm\n",
            encoding="utf-8",
            newline="\n",
        )
        p2 = _run_lean_with_retry([lake_exe, "env", "lean", str(tamper2)], LEAN_DIR, env)
        out2 = p2.stdout + "\n" + p2.stderr
        assert "failed to read file" not in out2, f"TAMPER-02 transient I/O error: {out2}"
        clean2, bad2 = _check_axioms_clean(out2)
        assert not clean2 and "bogus_backdoor" in out2, f"TAMPER-02 FAIL: custom axiom not caught! out={out2}"
        print(f"  [REJECTED] TAMPER-02 (Injected custom axiom): axiom gate caught {bad2}")

        # TAMPER-03: False mathematical claim must be rejected by Lean 4.35.0 kernel with type mismatch!
        tamper3 = tmp_lean / "_Tamper3False.lean"
        tamper3.write_text(
            "import OmegaPackageProofs\n"
            "theorem false_ring0_claim : OmegaPackageProofs.CastrationRing0.wseWritePermitted "
            ".ring0ProtectedKernel 0 = true := rfl\n",
            encoding="utf-8",
            newline="\n",
        )
        p3 = _run_lean_with_retry([lake_exe, "env", "lean", str(tamper3)], LEAN_DIR, env)
        out3 = p3.stdout + "\n" + p3.stderr
        assert "failed to read file" not in out3, f"TAMPER-03 transient I/O error: {out3}"
        assert p3.returncode != 0 and ("Type mismatch" in out3 or "type mismatch" in out3 or "rfl" in out3), (
            f"TAMPER-03 FAIL: Lean kernel did not reject false theorem with type error! rc={p3.returncode} out={out3}"
        )
        print(f"  [REJECTED] TAMPER-03 (False Ring-0 write claim): Lean kernel exited rc={p3.returncode}")

        # TAMPER-04 (Optional Linux CI): Inject `sorry` into PalomarSolution & assert comparator rejects!
        if with_comparator:
            psol = tmp_lean / "PalomarSolution.lean"
            orig = psol.read_text(encoding="utf-8")
            mutated = re.sub(
                r"public theorem m5_adversarial_refutations :.*?end OmegaPackageProofs\.Palomar",
                "public theorem m5_adversarial_refutations :\n"
                "    (¬ (∃ specBps : Nat, wseWritePermitted .ring0ProtectedKernel specBps = true)) ∧\n"
                "    (¬ (∃ (mem : OrganismMemory) (trace : List WseWriteOp),\n"
                "          (applyWseTrace mem trace).ring0Kernel ≠ mem.ring0Kernel)) ∧\n"
                "    (¬ (paretoDominates 5642 100 8467 0)) ∧\n"
                "    (¬ (∃ ovi ks : Nat, paretoDominates ovi ks ovi ks)) := by\n"
                "  sorry\n\nend OmegaPackageProofs.Palomar",
                orig,
                flags=re.S,
            )
            assert mutated != orig, "TAMPER-04 setup error: failed to mutate m5_adversarial_refutations"
            psol.write_text(mutated, encoding="utf-8", newline="\n")
            subprocess.run(
                [lake_exe, "build", "PalomarSolution"],
                cwd=str(tmp_lean),
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=180,
            )
            p4 = subprocess.run(
                [lake_exe, "comparator", "--config", "comparator.json", "--paranoid"],
                cwd=str(tmp_lean),
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=180,
            )
            assert p4.returncode != 0, "TAMPER-04 FAIL: lake comparator --paranoid accepted sorry-tampered PalomarSolution!"
            print(f"  [REJECTED] TAMPER-04 (Palomar comparator --paranoid on sorry-tampered solution): exited rc={p4.returncode}")

    print("=== ALL LIVE NEGATIVE LEAN 4.35.0 REJECTION TESTS: PASS ===")


if __name__ == "__main__":
    run_negative_lean_tests(with_comparator="--with-comparator" in sys.argv)
