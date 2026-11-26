#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Convenience CLI entry point forwarding to scripts/build_paper_and_figures.py."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_paper_and_figures import main

if __name__ == "__main__":
    main()
