from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class PPCEntity:
    name: str
    cpc: Decimal
    status: int
    children: dict[str, PPCEntity] = field(default_factory=dict)

    def add_child(self, child: PPCEntity) -> None:
        self.children[child.name] = child
