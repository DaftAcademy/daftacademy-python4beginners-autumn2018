# Zadanie 5
# Napisz 2 funkcje:
# Jedna o nazwie prime ma sprawdzić czy zadana liczba <n> jest liczbą pierwszą
# zwracając True/False
# Druga funkcja twins ma sprawdzić czy danae liczbay <n>, <k> są liczbami bliźniaczymi.
# Funkcja może przyjmować też jeden parametr
# Jeżeli podana liczba jest liczbą bliźniaczą zwróć jej bliźniaka,
# Jeżli nie jest bliźniacza to zwróć False
# Obie funkcje mają przyjmować liczby naturalne. Podanie innej liczby niż
# naturalna w wymaganym parametrze ma skutkować zwróceniem None

# Definicja 1: Liczba Pierwsza to liczba naturalna większa od 1,
# która ma dokładnie dwa dzielniki naturalne: jedynkę i siebie samą
# Definicja 2: Liczby bliźniacze to takie dwie liczby pierwsze, których różnica
# wynosi 2.

# Przydatne linki:
# https://stackoverflow.com/questions/18833759/python-prime-number-checker


assert prime(101) == True
assert prime("22") == None

assert twins(101) == 103
assert twins(79) == False
assert twins(5, 7) == True
