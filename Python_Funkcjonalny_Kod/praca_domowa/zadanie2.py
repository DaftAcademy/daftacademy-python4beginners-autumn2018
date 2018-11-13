# Zadanie 2
# Napisz funkcję reduce
# funkcja ma na celu sumowanie kolejnych par elementów zadanej listy
# i zwrócenie listy sum kolejnych par, jeżeli lista ma nieparzystą długość
# ostatni element zostaje przepisany od listy wynikowej na ostatniej pozycji


assert reduce([1, 2, 3, 4, 5, 6]) == [3, 7, 11]
assert reduce([1, 2, 3, 4, 5, 6, 7]) == [3, 7, 11, 7]
