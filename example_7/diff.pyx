from .entity cimport PPCEntity


cdef class PPCEntityDiff:
    cdef PPCEntity old
    cdef PPCEntity new
    cdef list children

    def __cinit__(self, PPCEntity old, PPCEntity new):
        self.old = old
        self.new = new
        self.children = []

    cdef bint has_changed(self):
        return self.old.get_diff_fields() != self.new.get_diff_fields()

    def __str__(self):
        return f"{self.new.name}: {'changed' if self.has_changed() else 'unchanged'}"


cpdef PPCEntityDiff make_diff(PPCEntity old_entity, PPCEntity new_entity):
    cdef PPCEntityDiff diff = PPCEntityDiff.__new__(PPCEntityDiff, old_entity, new_entity)
    cdef PPCEntity old_child
    cdef PPCEntity new_child
    for old_child in old_entity.children.values():
        new_child = new_entity.children[old_child.name]
        diff.children.append(make_diff(old_child, new_child))
    return diff


cpdef void write_diff(f, PPCEntityDiff diff, str indent = ""):
    f.write(f"{indent}{diff}\n")
    for child_diff in diff.children:
        write_diff(f, child_diff, indent + "  ")