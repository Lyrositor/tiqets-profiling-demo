from decimal import Decimal


class PPCEntity:
    __slots__ = ("name", "cpc", "status", "children")

    name: str
    cpc: Decimal
    status: int
    children: dict

    def __init__(self, name: str, cpc: Decimal, status: int):
        self.name = name
        self.cpc = cpc
        self.status = status
        self.children = {}

    def add_child(self, child) -> None:
        self.children[child.name] = child
