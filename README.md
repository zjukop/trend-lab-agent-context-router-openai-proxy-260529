# Agent Context Router

OpenAI-compatible proxy that routes compact instruction packs to coding-agent requests.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
agent-context-router --task "fix tests" --sources AGENTS.md CLAUDE.md README.md
```

## What this starter includes

- Minimal CLI
- Naive instruction-pack compiler (chunking lines)
- Simple task router (keyword-based)
- JSON output suitable for plugging into a proxy layer later

## Run tests

```bash
pytest -q
```
