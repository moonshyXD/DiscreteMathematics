from polynomial import Polynomial
from number import Number
from function_calculate import FunctionCalculate
from errors import InputError
from karatsuba import Karatsuba
from becnhamrk import run_benchmarks


def input_polynomial(prompt="Введите коэффициенты полинома через пробел: ") -> list:
    return input(prompt).split()


def main():
    while True:
        print("\n" + "-"*30)
        print("   МЕНЮ УПРАВЛЕНИЯ ПОЛИНОМАМИ")
        print("-"*30)
        print("1. Вычислить значение полинома в точке (x)")
        print("2. Перемножить два полинома (В лоб и Карацуба)")
        print("3. Перемножить два числа (Number)")
        print("4. Запустить бенчмарки (производительность)")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        try:
            if choice == "1":
                poly = Polynomial()
                poly.polynomial = input_polynomial()
                x = Number(input("Введите значение x: "))

                val_direct = FunctionCalculate.direct(poly.polynomial, x)
                val_gorner = FunctionCalculate.gorner(poly.polynomial, x)

                print(f"\nРезультат (Прямой метод): {val_direct}")
                print(f"Результат (Схема Горнера): {val_gorner}")

            elif choice == "2":
                p1 = Polynomial()
                p1.polynomial = input_polynomial("Коэффициенты 1-го полинома: ")
                p2 = Polynomial()
                p2.polynomial = input_polynomial("Коэффициенты 2-го полинома: ")

                res_direct = p1 * p2
                res_karatsuba = Karatsuba.execute(p1, p2)

                print(f"\nРезультат (В лоб):    {res_direct.polynomial}")
                print(f"Результат (Карацуба): {res_karatsuba.polynomial}")

            elif choice == "3":
                n1 = Number(input("Введите первое число: "))
                n2 = Number(input("Введите второе число: "))
                print(f"\nРезультат умножения: {n1.value * n2.value}")

            elif choice == "4":
                run_benchmarks()

            elif choice == "0":
                print("Завершение работы...")
                break
            else:
                print("Неверный выбор, попробуйте снова")

        except InputError as e:
            print(f"\nОшибка ввода: {e}")
        except Exception as e:
            print(f"\nПроизошла ошибка: {e}")


if __name__ == "__main__":
    main()
