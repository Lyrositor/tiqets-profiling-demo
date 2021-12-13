Tiqets Profiling Demo
=====================

A quick demo of the value of profiling and making simple optimizations to your code, for an internal Tiqets presentation.

This is not meant to be rigorous by any stretch of the imagination. The numbers are merely illustrative.

Benchmark times for a single run on my laptop:

| benchmark                          | time       |
|------------------------------------|------------|
| example_0 (baseline)               | 54.890144s |
| example_1 (less magic)             | 15.408645s |
| example_2 (better data structures) | 3.822141s  |
| example_3 (more direct access)     | 2.08018s   |
| example_4 (fewer loops)            | 1.77723s   |
| example_5 (no dataclasses)         | 1.770482s  |
| example_6 (Cython)                 | 0.516549s  |
| example_7 (typed Cython)           | 0.416739s  |
