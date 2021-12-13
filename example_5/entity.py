from __future__ import annotations

from decimal import Decimal


class PPCEntity:
    __slots__ = ("name", "cpc", "status", "children")

    name: str
    cpc: Decimal
    status: int
    children: dict[str, PPCEntity]

    def __init__(self, name: str, cpc: Decimal, status: int):
        self.name = name
        self.cpc = cpc
        self.status = status
        self.children = {}

    def add_child(self, child: PPCEntity) -> None:
        self.children[child.name] = child
