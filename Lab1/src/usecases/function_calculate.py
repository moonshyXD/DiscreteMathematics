from domain.number import Number
from domain.polynomial import Polynomial


class FunctionCalculate:
    @staticmethod
    def gorner(coefficents: Polynomial, x: Number | None = Number(10.0)):
        result = coefficents[0]
        for i in range(1, len(coefficents)):
            result = result * x.value + coefficents[i]

        return result

    @staticmethod
    def direct(coefficents: Polynomial, x: Number | None = Number(10.0)):
        result = 0
        n = len(coefficents)
        for i in range(n):
            result += coefficents[i] * (x.value ** (n - 1 - i))

        return result
