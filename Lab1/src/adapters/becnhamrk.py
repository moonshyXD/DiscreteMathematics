import time
import random
import sys
from domain.polynomial import Polynomial
from usecases.karatsuba import Karatsuba
from usecases.function_calculate import FunctionCalculate
from domain.number import Number

sys.setrecursionlimit(10000)


def generate_polynomial(length: int) -> Polynomial:
    p = Polynomial()
    p._coefficients = [random.uniform(0.1, 2.0) for _ in range(length)]
    return p


def benchmark_polynomial():
    sizes_mult = [128, 512, 1024, 2048, 4096]

    print("\n### Сравнение умножения: В лоб vs Карацуба\n")
    print("| Длина (N) | В лоб (сек) | Карацуба (сек) | Победитель | Ускорение |")

    for n in sizes_mult:
        p1, p2 = generate_polynomial(n), generate_polynomial(n)

        start = time.perf_counter()
        _ = p1 * p2
        t_direct = time.perf_counter() - start

        start = time.perf_counter()
        Karatsuba.execute(p1, p2)
        t_karatsuba = time.perf_counter() - start

        winner = "Карацуба" if t_karatsuba < t_direct else "В лоб"
        speedup = t_direct / t_karatsuba if t_karatsuba > 0 else 0

        print(f"| {n:<9} | {t_direct:<11.6f} | {t_karatsuba:<14.6f} | {winner:<10} | {speedup:.1f}")


def benchmark_numbers():
    sizes_eval = [1000, 10000, 100000, 500000, 1000000, 5000000, 10000000]

    print("\n### Сравнение вычисления значения: В лоб vs Горнер\n")
    print("| Степень (N) | В лоб (сек) | Горнер (сек) | Победитель | Ускорение |")

    x_bench = Number(1.0000001)

    for n in sizes_eval:
        p = generate_polynomial(n)
        coeffs = p._coefficients

        start = time.perf_counter()
        FunctionCalculate.direct(coeffs, x_bench)
        t_direct = time.perf_counter() - start

        start = time.perf_counter()
        FunctionCalculate.gorner(coeffs, x_bench)
        t_gorner = time.perf_counter() - start

        speedup = t_direct / t_gorner if t_gorner > 0 else 0
        winner = "Горнер" if t_gorner < t_direct else "В лоб"
        print(f"| {n:<11} | {t_direct:<11.6f} | {t_gorner:<12.6f} |{winner:<11} | {speedup:.1f}x")


def run_benchmarks():
    benchmark_polynomial()
    benchmark_numbers()
    print("\nБенчмарки завершены")