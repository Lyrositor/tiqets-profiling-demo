cdef class PPCEntity:
    cdef readonly str name
    cdef readonly object cpc
    cdef readonly int status
    cdef readonly dict children

    cdef tuple get_diff_fields(self)