from contextlib import nullcontext
from decimal import Decimal
from importlib import import_module
from typing import Type, Any

import pendulum

from profiling import yappi_profile

STATUS_ACTIVE = 1
STATUS_INACTIVE = 2

EXAMPLES = ["example_0", "example_1", "example_2", "example_3", "example_4", "example_5", "example_6", "example_7"]

WITH_YAPPI_PROFILING = False


def run_benchmarks() -> None:
    print("Running benchmarks")
    for example in EXAMPLES:
        print(f"===== {example} =====")
        example_duration = profile_benchmark(example)
        print(f"{example}: {example_duration.total_seconds()}s")
    print("Done")


def profile_benchmark(benchmark_name: str) -> pendulum.Duration:
    benchmark_module: Any = import_module(benchmark_name)
    start = pendulum.now()
    with yappi_profile(f"profile_{benchmark_name}") if WITH_YAPPI_PROFILING else nullcontext():
        run_benchmark(benchmark_module)
    end = pendulum.now()
    return end - start


def run_benchmark(benchmark_module: Any) -> None:
    root_1 = setup_entities(
        benchmark_module.PPCEntity,
        i_cpc=Decimal("0.01"),
        j_cpc=Decimal("0.02"),
        k_cpc=Decimal("0.03"),
        i_status=STATUS_ACTIVE,
        j_status=STATUS_INACTIVE,
        k_status=STATUS_INACTIVE
    )
    root_2 = setup_entities(
        benchmark_module.PPCEntity,
        i_cpc=Decimal("0.04"),
        j_cpc=Decimal("0.09"),
        k_cpc=Decimal("0.02"),
        i_status=STATUS_ACTIVE,
        j_status=STATUS_ACTIVE,
        k_status=STATUS_ACTIVE
    )
    diff = benchmark_module.make_diff(root_1, root_2)
    with open("benchmark_diff.txt", "w") as f:
        benchmark_module.write_diff(f, diff)


def setup_entities(
    entity_cls: Type, i_cpc: Decimal, j_cpc: Decimal, k_cpc: Decimal, i_status: int, j_status: int, k_status: int
) -> Any:
    root = entity_cls(name="root", cpc=Decimal("0.05"), status=STATUS_ACTIVE)
    for i in range(100):
        child_i = entity_cls(name=f"child_i_{i}", cpc=i_cpc, status=i_status)
        root.add_child(child_i)
        for j in range(100):
            child_j = entity_cls(name=f"child_j_{j}", cpc=j_cpc, status=j_status)
            child_i.add_child(child_j)
            for k in range(100):
                child_k = entity_cls(name=f"child_k_{k}", cpc=k_cpc, status=k_status)
                child_j.add_child(child_k)
    return root


if __name__ == "__main__":
    run_benchmarks()
