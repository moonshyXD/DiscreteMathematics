from polynomial import Polynomial


class FunctionCalculate:
    @staticmethod
    def gorner(coefficents: Polynomial, x: float):
        result = 0
        for i in range(len(coefficents) - 1):
            result += x * coefficents[i] + coefficents[i + 1]

        return result

    @staticmethod
    def direct(coefficents: Polynomial, x: float):
        result = 0
        n = len(coefficents)
        for i in range(n):
            result += x * coefficents[i] * 10 ** (n - i)

        return result
