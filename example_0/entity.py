from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class PPCEntity:
    name: str
    cpc: Decimal
    status: int
    children: list[PPCEntity] = field(default_factory=list)

    def add_child(self, child: PPCEntity) -> None:
        if child not in self.children:
            self.children.append(child)
