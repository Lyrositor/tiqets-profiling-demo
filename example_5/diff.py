from __future__ import annotations
from typing import IO

from .entity import PPCEntity


class PPCEntityDiff:
    __slots__ = ["old", "new", "children"]

    old: PPCEntity
    new: PPCEntity
    children: list[PPCEntityDiff]

    def __init__(self, old: PPCEntity, new: PPCEntity):
        self.old = old
        self.new = new
        self.children = []

    def has_changed(self) -> bool:
        for k in self.new.__slots__:
            if k != "children" and getattr(self.old, k) != getattr(self.new, k):
                return True
        return False

    def __str__(self) -> str:
        return f"{self.new.name}: {'changed' if self.has_changed() else 'unchanged'}"


def make_diff(old_entity: PPCEntity, new_entity: PPCEntity) -> PPCEntityDiff:
    diff = PPCEntityDiff(old=old_entity, new=new_entity)
    for old_child in old_entity.children.values():
        new_child = new_entity.children[old_child.name]
        diff.children.append(make_diff(old_child, new_child))
    return diff


def write_diff(f: IO, diff: PPCEntityDiff, indent: str = "") -> None:
    f.write(f"{indent}{diff}\n")
    for child_diff in diff.children:
        write_diff(f, child_diff, indent + "  ")