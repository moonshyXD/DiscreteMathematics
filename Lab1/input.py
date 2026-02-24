from polynomial import Polynomial
from errors import InputError


class InputPolynom:
    def __init__(self):
        self._polynomial = Polynomial

    @property
    def polynomial(self):
        return self._polynomial

    @polynomial.setter
    def polynomial(self):
        raw_polynomial = self.input_coefficent()
        for token in raw_polynomial:
            try:
                token = self.validate_token(token)
                self.polynomial.add_coefficient(token)
            except InputError as e:
                print(e)

    def validate_token(self, token: str):
        try:
            return float(token)
        except:
            raise InputError("Введены неверные коэффиценты. Допустимо только int/float")

    def greet_message():
        print("Веедите коэффиценты полинома через пробел:\n")

    def input_coefficent(self):
        input_data = input()
        input_list = input_data.split()
        return input_list
