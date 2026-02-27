from errors import InputError


class Number:
    def __init__(self, value: float):
        self.value = value

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: str):
        try:
            self._value = float(value)
        except ValueError:
            raise InputError("Введиенное значение должно быть числом")
