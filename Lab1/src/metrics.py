import time
import random
from polynomial import Polynomial
from polynomial_mult import Karatsuba
from function_calculate import FunctionCalculate
from number import Number


def generate_poly(length: int) -> Polynomial:
    p = Polynomial()
    p._coefficients = [random.uniform(1.0, 10.0) for _ in range(length)]
    return p


def run_multiplication_benchmark():
    sizes = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

    print("### Сравнение умножения: В лоб vs Карацуба\n")
    print("| Длина (N) | В лоб умножение (сек) | Схема Карацубы (сек) | Победитель | Ускорение (в раз) |")

    for n in sizes:
        p1 = generate_poly(n)
        p2 = generate_poly(n)

        start = time.perf_counter()
        p3 = p1 * p2
        t_direct = time.perf_counter() - start

        start = time.perf_counter()
        Karatsuba.execute(p1, p2)
        t_karatsuba = time.perf_counter() - start

        winner = "Карацуба" if t_karatsuba < t_direct else "В лоб"
        speedup = t_direct / t_karatsuba if t_karatsuba > 0 else 0
        if abs(t_karatsuba - t_direct) < 0.0001:
            winner = "Равны"

        print(f"| {n:<9} | {t_direct:<21.6f} | {t_karatsuba:<20.6f} | {winner:<10} | {speedup:<10.1f}")


def run_evaluation_benchmark():
    sizes = [10, 100, 1000, 10000, 50000, 100000]

    print("\n### Сравнение вычисления значения: В лоб vs Горнер\n")
    print("| Степень (N) | В лоб вычисление (сек) | Схема Горнера (сек) | Ускорение (в раз) |")

    x = Number(1.00001) 

    for n in sizes:
        p = generate_poly(n)

        start = time.perf_counter()
        FunctionCalculate.direct(p.polynomial, x)
        t_direct = time.perf_counter() - start

        start = time.perf_counter()
        FunctionCalculate.gorner(p.polynomial, x)
        t_gorner = time.perf_counter() - start

        speedup = t_direct / t_gorner if t_gorner > 0 else 0
        print(f"| {n:<11} | {t_direct:<22.6f} | {t_gorner:<19.6f} | {speedup:<20.1f}")

if __name__ == "__main__":
    print("Запуск тестов производительности... (это может занять несколько секунд)\n")
    run_multiplication_benchmark()
    run_evaluation_benchmark()
