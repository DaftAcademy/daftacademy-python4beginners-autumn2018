'''
W tym zadaniu zawsze będą poprawne dane.
Nie ma potrzeby obsługiwania sytuacji wyjątkowych.

Napisz klasę MyFraction.
Ta klasa ma reprezentować ułamek.
Ta klasa ma być mutowalna.
Ta klasa ma mieć dwa pola: `numerator` i `denominator`.

Instancję klasy powinno dać się utworzyć na następujące sposoby:
	MyFraction(1, 2)
	MyFraction(1, denominator=2)
	MyFraction(numerator=1, denominator=2)
	MyFraction(5) == MyFraction(5, 1)
	MyFraction(numerator=6) == MyFraction(numerator=6, denominator=1)
	MyFraction(MyFraction(1, 2)) == MyFraction(1, 2)

Dodatkowo mianownik ułamka powinien zawsze być najmniejszą możliwą liczbą.
Przykład:
	a = MyFraction(10, 30)
	assert 1 == a.numerator
	assert 3 == a.denominator

Ułamki powinno dać się do siebie dodać.
	MyFraction(5, 4) == MyFraction(2, 4) + MyFraction(3, 4)
Dodawanie int też powinno być możliwe.
	MyFraction(5, 4) == MyFraction(1, 4) + 1
	MyFraction(5, 4) == 1 + MyFraction(1, 4)


Instancje klasy MyFraction powinno dać się rzutować na string
Przykład:
	'MyFraction(numerator=1, denominator=2)' == str(MyFraction(1, 2))
	'MyFraction(numerator=1, denominator=2)' == repr(MyFraction(1, 2))


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
