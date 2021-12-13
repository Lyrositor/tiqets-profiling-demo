from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import IO

from .entity import PPCEntity


@dataclass
class PPCEntityDiff:
    old: PPCEntity
    new: PPCEntity
    children: list[PPCEntityDiff]

    def has_changed(self) -> bool:
        old_value = asdict(self.old)
        del old_value["children"]
        new_value = asdict(self.new)
        del new_value["children"]
        return old_value != new_value

    def __str__(self) -> str:
        return f"{self.new.name}: {'changed' if self.has_changed() else 'unchanged'}"


def make_diff(old_entity: PPCEntity, new_entity: PPCEntity) -> PPCEntityDiff:
    diff = PPCEntityDiff(old=old_entity, new=new_entity, children=[])
    for old_child in old_entity.children:
        for new_child in new_entity.children:
            if old_child.name == new_child.name:
                diff.children.append(make_diff(old_child, new_child))
                break
    return diff


def write_diff(f: IO, diff: PPCEntityDiff, indent: str = "") -> None:
    f.write(f"{indent}{diff}\n")
    for child_diff in diff.children:
        write_diff(f, child_diff, indent + "  ")