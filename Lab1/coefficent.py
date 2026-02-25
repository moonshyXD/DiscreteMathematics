from errors import InputError


class Coefficent:
    def __init__(self, x: float):
        self._x = x

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: str):
        try:
            self._x = float(value)
        except ValueError:
            raise InputError("Введиенное значение должно быть числом")
