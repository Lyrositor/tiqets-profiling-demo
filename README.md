Tiqets Profiling Demo
=====================

A quick demo of the value of profiling and making simple optimizations to your code, for an internal Tiqets presentation.

This is not meant to be rigorous by any stretch of the imagination. The numbers are merely illustrative.

Benchmark times for a single run on my laptop (without yappi profiling, as this creates distorted numbers due to the overhead from profiling):

| benchmark                          | time       |
|------------------------------------|------------|
| example_0 (baseline)               | 92.600269s |
| example_1 (less magic)             | 47.535969s |
| example_2 (better data structures) | 10.17423s  |
| example_3 (more direct access)     | 8.414011s  |
| example_4 (fewer loops)            | 7.316188s  |
| example_5 (no dataclasses)         | 5.798112s  |
| example_6 (Cython)                 | 5.512598s  |
| example_7 (typed Cython)           | 2.874036s  |
