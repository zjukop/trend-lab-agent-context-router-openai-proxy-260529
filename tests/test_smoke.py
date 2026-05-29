from agent_context_router.main import compile_packs, route_pack


def test_smoke_compile_and_route() -> None:
    text = "\n".join(f"line {i}" for i in range(45))
    packs = compile_packs(text, max_lines=20)
    assert len(packs) == 3
    selected = route_pack("fix failing pytest", packs)
    assert selected in packs
