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


class MyFraction:
    def __init__(self, numerator, denominator=1):
        if isinstance(numerator, MyFraction):
            self.numerator = numerator.numerator
            self.denominator = numerator.denominator
        else:
            self.numerator = numerator
            self.denominator = denominator
        self._reduce()

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

    def __add__(self, other):
        g, h = self._inner_add(other)
        return MyFraction(g, h)

    def __eq__(self, other):
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __iadd__(self, other):
        self.numerator, self.denominator = self._inner_add(other)
        self._reduce()
        return self

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return '{}(numerator={}, denominator={})'.format(
            self.__class__.__name__,
            self.numerator,
            self.denominator
        )
