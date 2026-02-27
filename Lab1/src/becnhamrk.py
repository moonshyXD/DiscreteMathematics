from polynomial import Polynomial
from karatsuba import Karatsuba
import time
import random
from function_calculate import FunctionCalculate
from number import Number


def generate_poly(length: int) -> Polynomial:
    p = Polynomial()
    p._coefficients = [random.uniform(1.0, 10.0) for _ in range(length)]
    return p


def run_benchmarks():
    print("\n" + "="*50)
    print("ЗАПУСК БЕНЧМАРКОВ")
    print("="*50)

    sizes_mult = [16, 32, 64, 128, 256, 512, 1024, 2048]
    print("\n### Сравнение умножения: В лоб vs Карацуба\n")
    print("| Длина (N) | В лоб (сек) | Карацуба (сек) | Победитель | Ускорение |")
    print("|" + "-"*11 + "|" + "-"*12 + "|" + "-"*16 + "|" + "-"*12 + "|" + "-"*11 + "|")

    for n in sizes_mult:
        p1, p2 = generate_poly(n), generate_poly(n)

        start = time.perf_counter()
        _ = p1 * p2
        t_direct = time.perf_counter() - start

        start = time.perf_counter()
        Karatsuba.execute(p1, p2)
        t_karatsuba = time.perf_counter() - start

        winner = "Карацуба" if t_karatsuba < t_direct else "В лоб"
        speedup = t_direct / t_karatsuba if t_karatsuba > 0 else 0
        print(f"| {n:<9} | {t_direct:<10.6f} | {t_karatsuba:<14.6f} | {winner:<10} | {speedup:<9.1f}x |")

    sizes_eval = [10, 100, 1000, 10000, 100000]
    print("\n### Сравнение вычисления значения: В лоб vs Горнер\n")
    print("| Степень (N) | В лоб (сек) | Горнер (сек) | Ускорение |")
    print("|" + "-"*13 + "|" + "-"*12 + "|" + "-"*14 + "|" + "-"*11 + "|")
    x_bench = Number(1.00001)

    for n in sizes_eval:
        p = generate_poly(n)
        start = time.perf_counter()
        FunctionCalculate.direct(p.polynomial, x_bench)
        t_direct = time.perf_counter() - start

        start = time.perf_counter()
        FunctionCalculate.gorner(p.polynomial, x_bench)
        t_gorner = time.perf_counter() - start

        speedup = t_direct / t_gorner if t_gorner > 0 else 0
        print(f"| {n:<11} | {t_direct:<10.6f} | {t_gorner:<12.6f} | {speedup:<9.1f}x |")
    print("\nБенчмарки завершены")
