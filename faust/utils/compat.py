"""Compatibility utilities."""
from typing import Any, AnyStr

__all__ = ['DummyContext', 'want_bytes', 'want_str']


class DummyContext:

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...

    async def __aenter__(self) -> 'DummyContext':
        return self

    async def __aexit__(self, *exc_info: Any) -> None:
        ...

    def __enter__(self) -> 'DummyContext':
        return self

    def __exit__(self, *exc_info: Any) -> Any:
        ...


def want_bytes(s: AnyStr) -> bytes:
    """Convert string to bytes."""
    if isinstance(s, str):
        return s.encode()
    return s


def want_str(s: AnyStr) -> str:
    """Convert bytes to string."""
    if isinstance(s, bytes):
        return s.decode()
    return s
