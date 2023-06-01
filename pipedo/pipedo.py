from __future__ import annotations

from typing import Any, Callable

class Pipe:
    def __init__(self, obj: Any) -> None:
        self.obj = obj

    def do(self, f: Callable) -> Pipe:
        return Pipe(f(self.obj))

    def get(self) -> Any:
        return self.obj


def get(p: Pipe) -> Any:
    return p.get()
