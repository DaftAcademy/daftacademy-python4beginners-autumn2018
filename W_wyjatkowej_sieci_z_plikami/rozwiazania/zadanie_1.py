'''
Dla modelowej lub swojej klasy MyFraction dodaj walidację wejścia i przetwarzania.
Tym razem oczekujemy że MyFraction będzie obsługiwać nie tylko dodawanie ale również:
    odejmowanie
    mnożenie
    dzielenie
Oraz i przekazywanie obiektów MyFraction jako licznik czy mianownik dla nowego obiektu MyFraction.
Przykład:
    MyFraction(1, 2) * MyFraction(1, 2) = MyFraction(1, 4)
    MyFraction(numerator=1, denominator=MyFraction(1, 2)) == 2
    MyFraction(2, 3) / MyFraction(1, 3) = 2

Klasa MyFraction powinna też wykonywać działania z liczbami zmiennoprzecinkowymi ale:
    nie musi ich przyjmować jako argumenty
    wynik operacji z operandem typu float jest typu float
    MyFraction można przedstawić w notacji zmiennoprzecinkowej
Przykład:
    0.5 + MyFraction(1, 2) = 1.0
    float(MyFraction(3, 20)) = 0.15

Dodatkowo wejście może nie być poprawne.
Z tego powodu klasa MyFraction powinna walidować wejściowe parametry i ich poprawność.

By to osiągnąć zaimplementuj następujące wyjątki:
    InvalidOperandError
    InvalidInputOperandError
    OperationNotSupportedError

Przykład:
    MyFraction(5, 4) + "10"   #  <- ten test ma rzucić wyjątkiem InvalidOperand
    MyFraction(5, [12])       #  <- ten test ma rzucić wyjątkiem InvalidInputOperand
    MyFraction(99, 100)**2    #  <- ten test ma rzucić wyjątkiem OperationNotSupported

Pamiętaj jednak że wszystkie dotychczasowej operacje na MyFraction z Zadania 3.1 powinny
wciąż działać.
'''

import math


class GenericMyFractionError(Exception):
    pass


class InvalidOperandError(GenericMyFractionError):
    pass


class InvalidInputOperandError(GenericMyFractionError):
    pass


class OperationNotSupportedError(GenericMyFractionError):
    pass


class MyFraction:
    numerator = 0
    denominator = 1

    def __init__(self, numerator, denominator=1):

        self._supported_input(numerator)
        self._supported_input(denominator)
        if denominator == 0:
            raise InvalidInputOperandError
        if isinstance(numerator, MyFraction):
            self.numerator = numerator.numerator
            self.denominator = numerator.denominator
            self /= denominator
        elif isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator
        elif isinstance(numerator, int) and isinstance(denominator, MyFraction):
            self.numerator = numerator
            self.denominator = 1
            self /= denominator
        else:
            self.numerator = 0
            self.denominator = denominator
        self._reduce()

    def _supported_operand(self, other):
        if not isinstance(other, (int, float, MyFraction)) or isinstance(other, bool):
            raise InvalidOperandError

    def _supported_input(self, other):
        if not isinstance(other, (int, MyFraction)) or isinstance(other, bool):
            raise InvalidInputOperandError

    def _reduce(self):
        nd_gcd = math.gcd(
            self.numerator, self.denominator
        )
        self.numerator //= nd_gcd
        self.denominator //= nd_gcd

    def _inner_add(self, other):
        other = MyFraction(other)
        # a/b + c/d = (a*d + c*b)/(b*d) = g/h
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        g = a * d + c * b
        h = b * d
        return g, h

    def _inner_sub(self, other):
        other = MyFraction(other)
        # a/b - c/d = (a*d - c*b)/(b*d) = g/h
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        g = a * d - c * b
        h = b * d
        return g, h

    def _inner_mul(self, other):
        other = MyFraction(other)
        # a/b * c/d = a*c / b*d = g/h
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        g = a * c
        h = b * d
        return g, h

    def _inner_truediv(self, other):
        other = MyFraction(other)
        # a/b / c/d = a*d / b*c = g/h
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        g = a * d
        h = b * c
        return g, h

    def __invert__(self):
        self.numerator, self.denominator = self.denominator, self.numerator

    def __float__(self):
        return float(self.numerator) / float(self.denominator)

    def __int__(self):
        return int(float(self))

    def __eq__(self, other):
        return (
            self.numerator == other.numerator and
            self.denominator == other.denominator
        )

    def __repr__(self):
        return '{}(numerator={}, denominator={})'.format(
            self.__class__.__name__,
            self.numerator,
            self.denominator
        )

    def __floordiv__(self, other):
        raise OperationNotSupportedError("Operator // is not yet supported")

    def __pow__(self, other):
        raise OperationNotSupportedError("Operator ** is not yet supported")

    def __lshift__(self, other):
        raise OperationNotSupportedError("Operator << is not yet supported")

    def __rshift__(self, other):
        raise OperationNotSupportedError("Operator >> is not yet supported")

    def __add__(self, other):
        self._supported_operand(other)
        if isinstance(other, float):
            return other + float(self)
        g, h = self._inner_add(other)
        return MyFraction(g, h)

    def __iadd__(self, other):
        self._supported_operand(other)
        if isinstance(other, float):
            return other + float(self)
        self.numerator, self.denominator = self._inner_add(other)
        self._reduce()
        return self

    def __sub__(self, other):
        self._supported_operand(other)
        if isinstance(other, float):
            return float(self) - other
        g, h = self._inner_sub(other)
        return MyFraction(g, h)

    def __isub__(self, other):
        self._supported_operand(other)
        if isinstance(other, float):
            return float(self) - other
        self.numerator, self.denominator = self._inner_sub(other)
        self._reduce()
        return self

    def __radd__(self, other):
        self._supported_operand(other)
        return self + other

    def __rsub__(self, other):
        self._supported_operand(other)
        if isinstance(other, float):
            return other - float(self)
        return MyFraction(other) - self

    def __mul__(self, other):
        self._supported_operand(other)
        if isinstance(other, float):
            return other * float(self)
        g, h = self._inner_mul(other)
        return MyFraction(g, h)

    def __imul__(self, other):
        self._supported_operand(other)
        if isinstance(other, float):
            return other * float(self)
        self.numerator, self.denominator = self._inner_mul(other)
        self._reduce()
        return self

    def __rmul__(self, other):
        self._supported_operand(other)
        return self * other

    def __truediv__(self, other):
        self._supported_operand(other)
        if isinstance(other, float):
            return float(self) / other
        g, h = self._inner_truediv(other)
        return MyFraction(g, h)

    def __itruediv__(self, other):
        self._supported_operand(other)
        if isinstance(other, float):
            return float(self) / other
        self.numerator, self.denominator = self._inner_truediv(other)
        self._reduce()
        return self

    def __rtruediv__(self, other):
        self._supported_operand(other)
        if isinstance(other, float):
            return other / float(self)
        return MyFraction(other) / self
