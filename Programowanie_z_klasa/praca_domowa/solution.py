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

# your code goes below
