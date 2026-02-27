from polynomial import Polynomial
from number import Number
from function_calculate import FunctionCalculate
from errors import InputError
from polynomial_mult import Karatsuba


def input_polynomial() -> list:
    raw_polynomial = input("Введите коэффиценты полинома через пробел: ")
    return raw_polynomial.split()


def run():
    try:
        polynomial = Polynomial()
        polynomial.polynomial = input_polynomial()
        x = Number(input("Введите значение x: "))

        result_direct = FunctionCalculate.direct(polynomial.polynomial, x)
        result_gorner = FunctionCalculate.gorner(polynomial.polynomial, x)

        print(f"Значение полинома в точке x по прямой схеме: {result_direct}")
        print(f"Значение полинома в точке x по схеме Горнера: {result_gorner}")

        result_mult_direct = polynomial * polynomial
        result_mult_karatsuba = Karatsuba.execute(polynomial, polynomial)
    
        print(f"Значение полинома в точке x по прямой схеме умножения: {result_mult_direct.polynomial}")
        print(f"Значение полинома в точке x по схеме Карацубы: {result_mult_karatsuba.polynomial}")

        res = FunctionCalculate.gorner(result_mult_karatsuba.polynomial)
        print(res)
    except InputError as e:
        print(e)


if __name__ == "__main__":
    run()
