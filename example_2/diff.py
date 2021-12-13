from __future__ import annotations
from dataclasses import dataclass, fields
from typing import IO

from .entity import PPCEntity


@dataclass
class PPCEntityDiff:
    old: PPCEntity
    new: PPCEntity
    children: list[PPCEntityDiff]

    def has_changed(self) -> bool:
        old_values = {
            field.name: getattr(self.old, field.name) for field in fields(self.old) if field.name != "children"
        }
        new_values = {
            field.name: getattr(self.new, field.name) for field in fields(self.new) if field.name != "children"
        }
        return old_values != new_values

    def __str__(self) -> str:
        return f"{self.new.name}: {'changed' if self.has_changed() else 'unchanged'}"


def make_diff(old_entity: PPCEntity, new_entity: PPCEntity) -> PPCEntityDiff:
    diff = PPCEntityDiff(old=old_entity, new=new_entity, children=[])
    for old_child in old_entity.children.values():
        new_child = new_entity.children[old_child.name]
        diff.children.append(make_diff(old_child, new_child))
    return diff


def write_diff(f: IO, diff: PPCEntityDiff, indent: str = "") -> None:
    f.write(f"{indent}{diff}\n")
    for child_diff in diff.children:
        write_diff(f, child_diff, indent + "  ")