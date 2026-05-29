from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List


def compile_packs(text: str, max_lines: int = 20) -> Dict[str, str]:
    """Split large instruction text into small packs."""
    lines = [ln for ln in text.splitlines() if ln.strip()]
    packs: Dict[str, str] = {}
    for i in range(0, len(lines), max_lines):
        key = f"pack_{i // max_lines + 1}"
        packs[key] = "\n".join(lines[i : i + max_lines])
    return packs or {"pack_1": ""}


def route_pack(task: str, packs: Dict[str, str]) -> str:
    """Very small heuristic router."""
    lowered = task.lower()
    if any(k in lowered for k in ("test", "pytest", "ci")):
        return next(iter(packs))
    if any(k in lowered for k in ("refactor", "design", "arch")):
        return list(packs)[min(1, len(packs) - 1)]
    return next(iter(packs))


def read_sources(paths: List[str]) -> str:
    chunks = []
    for p in paths:
        path = Path(p)
        if path.exists():
            chunks.append(path.read_text(encoding="utf-8"))
    return "\n\n".join(chunks)


def main() -> None:
    parser = argparse.ArgumentParser(description="Agent Context Router starter")
    parser.add_argument("--task", required=True, help="Task description")
    parser.add_argument("--sources", nargs="+", default=["README.md"], help="Instruction files")
    args = parser.parse_args()

    corpus = read_sources(args.sources)
    packs = compile_packs(corpus)
    selected = route_pack(args.task, packs)

    result = {
        "task": args.task,
        "selected_pack": selected,
        "pack_text": packs[selected],
        "pack_count": len(packs),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
