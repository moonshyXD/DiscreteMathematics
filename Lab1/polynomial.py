from dataclasses import dataclass


@dataclass
class Polynomial:
    def __init__(self):
        self._coefficients = []

    @property
    def coefficients(self):
        return self._coefficients

    def add_coefficient(self, coefficient: float):
        self.coefficients.append(coefficient)

    def change_coefficent(self, index: int, coefficent: float):
        self.coefficients[index] = coefficent
