from typing import Any
from number import Number


class Polynomial:
    def __init__(self, data: int | list | None = None):
        if data is None:
            self._coefficients = []
        elif isinstance(data, int):
            self._coefficients = [None for _ in range(data)]
        elif isinstance(data, list):
            self._coefficients = data.copy()

    @property
    def polynomial(self):
        return self._coefficients

    @polynomial.setter
    def polynomial(self, input_list: list):
        self._coefficients = []
        for token in input_list:
            if token != "":
                coefficent = Number(token)
                self._coefficients.append(coefficent.value)

    def add_coefficient(self, coefficient: float):
        self._coefficients.append(coefficient)

    def change_coefficient(self, index: int, coefficient: float):
        self._coefficients[index] = coefficient

    def __len__(self):
        return len(self._coefficients)

    def __mul__(self, other: Any) -> 'Polynomial':
        if not isinstance(other, Polynomial):
            return NotImplemented

        l1 = self._coefficients
        l2 = other._coefficients

        if not l1 or not l2:
            return Polynomial()

        res_length = len(l1) + len(l2) - 1
        res_coeffs = [0.0] * res_length

        for i in range(len(l1)):
            for j in range(len(l2)):
                v1 = l1[i] if l1[i] is not None else 0.0
                v2 = l2[j] if l2[j] is not None else 0.0
                res_coeffs[i + j] += v1 * v2

        result = Polynomial()
        result._coefficients = res_coeffs
        return result

    def __add__(self, other: Any) -> 'Polynomial':
        if not isinstance(other, Polynomial):
            return NotImplemented

        l1 = self._coefficients
        l2 = other._coefficients
        length = max(len(l1), len(l2))
        res_coeffs = [0.0] * length

        for i in range(length):
            v1 = l1[i] if i < len(l1) and l1[i] is not None else 0.0
            v2 = l2[i] if i < len(l2) and l2[i] is not None else 0.0
            res_coeffs[i] = v1 + v2

        result = Polynomial()
        result._coefficients = res_coeffs
        return result

    def __sub__(self, other: Any) -> 'Polynomial':
        if not isinstance(other, Polynomial):
            return NotImplemented

        l1 = self._coefficients
        l2 = other._coefficients
        length = max(len(l1), len(l2))
        res_coeffs = [0.0] * length

        for i in range(length):
            v1 = l1[i] if i < len(l1) and l1[i] is not None else 0.0
            v2 = l2[i] if i < len(l2) and l2[i] is not None else 0.0
            res_coeffs[i] = v1 - v2

        result = Polynomial()
        result._coefficients = res_coeffs
        return result

    def __repr__(self):
        return f"Polynomial({self._coefficients})"
