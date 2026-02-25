from polynomial import Polynomial
from coefficent import Coefficent


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
            coefficent = Coefficent(token)
            self.polynomial.add_coefficient(coefficent)

    def input_coefficent(self):
        input_data = input()
        input_list = input_data.split()
        return input_list
