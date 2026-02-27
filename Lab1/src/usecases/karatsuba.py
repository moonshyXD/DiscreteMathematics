from domain.polynomial import Polynomial


class Karatsuba:
    @staticmethod
    def execute(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        c1 = poly1._coefficients
        c2 = poly2._coefficients

        if not c1 or not c2:
            res = Polynomial()
            res._coefficients = [0.0]
            return res

        result_poly = Karatsuba._karatsuba_rec(poly1, poly2)

        coeffs = result_poly._coefficients
        while len(coeffs) > 1 and coeffs[-1] == 0.0:
            coeffs.pop()

        return result_poly

    @staticmethod
    def _karatsuba_rec(poly1: Polynomial, poly2: Polynomial) -> Polynomial:
        c1 = poly1._coefficients
        c2 = poly2._coefficients

        if len(c1) <= 1 or len(c2) <= 1:
            return poly1 * poly2

        n = max(len(c1), len(c2))
        m = n // 2

        c1_padded = c1 + [0.0] * (n - len(c1))
        c2_padded = c2 + [0.0] * (n - len(c2))

        a0 = Polynomial(c1_padded[:m])
        a1 = Polynomial(c1_padded[m:])
        b0 = Polynomial(c2_padded[:m])
        b1 = Polynomial(c2_padded[m:])

        p0 = Karatsuba._karatsuba_rec(a0, b0)
        p2 = Karatsuba._karatsuba_rec(a1, b1)
        p1 = Karatsuba._karatsuba_rec(a0 + a1, b0 + b1)
        mid = p1 - p0 - p2

        mid_shifted = Polynomial()
        mid_shifted._coefficients = [0.0] * m + mid._coefficients

        p2_shifted = Polynomial()
        p2_shifted._coefficients = [0.0] * (2 * m) + p2._coefficients

        result = p0 + mid_shifted + p2_shifted

        return result
