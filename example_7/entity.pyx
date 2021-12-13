cdef class PPCEntity:
    def __init__(self, str name, object cpc, int status):
        self.name = name
        self.cpc = cpc
        self.status = status
        self.children = {}

    def add_child(self, PPCEntity child) -> None:
        self.children[child.name] = child

    cdef tuple get_diff_fields(self):
        return self.name, self.cpc, self.status, self.children
