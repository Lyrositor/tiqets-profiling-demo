from contextlib import contextmanager

import yappi

yappi.profile("wall")


@contextmanager
def yappi_profile(profile_name: str):
    yappi.clear_stats()
    yappi.start()
    try:
        yield
    finally:
        yappi.stop()
    stats = yappi.get_func_stats()
    stats.save(f"{profile_name}.pstat", type="pstat")