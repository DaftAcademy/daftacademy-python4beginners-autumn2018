'''
Pamiętasz firmę ConfWord dla której sprawdzałeś statystyki kilka tygodni temu?
Okazało się że firmowa baza danych klientów wyciekła do internetu.

By firma ConfWorld dalej funkcjonowała musisz przekazać klientom
informacje na temat wycieku, ale nie chcesz siać paniki.
W pierwszej kolejności należy zresetować hasła klientom którzy nie zmieniali hasła od czasu ataku i mają słabe hasło
(figurujące na liście słabych haseł)

Napisz program by znaleźć takie osoby. Wyciek danych nastąpił 10.11.2017 w samo południe
Twoja baza danych jest aktualna (załóżmy dzień 20.11.2018 00:00)

Na domiar złego okazało się że Twoi klienci używali bardzo słabych haseł.
By w przyszłości nikt nie łamał haseł Twoich klientów,
wykorzystując listę danych najczęściej używanych haseł w internecie,
napisz kolejną część programu który w 2-giej kolejności:
    znajdzie wszystkich użytkowników którzy mają hasło figurujące na tej liście
    znajdzie top 10 występujących haseł w serwisie figurujących na liście top500 w PLAIN TEXT
    znajdzie wszystkich bezpiecznych użytkowników
        (hasło nie na figuruje liście oraz zmienili hasło od ataku)

Dane:
    hasła w bazie są hashowane algorytmem SHA1
    lista 500 najczęstszych haseł w internecie -> top_500_most_common_passwords.txt
    baza danych która wyciekła do internetu   -> confwrld_user_data_dump_10.11.2017.csv
    aktualna baza klientów                               -> confwrld_user_database.csv
    wszystkie daty są z tej samej strefy czasowej

Wymagania szczegółowe:
    ConfData
        Struktura przechowująca dane (dowolnie)

    ConfData.weak_pass_users(pass_list)
        Przyjmuje:
            pass_list -> struktura z wczytanymi hasłami i jej hashami
        Zwraca:
            ["mail1", "mail2", ..... ]
            Zwraca listę ludzi którzy mają słabe hasło figurujące na liście słabych haseł

    ConfData.common_pass(pass_list, n=10)
        Przyjmuje:
            pass_list -> struktura z wczytanymi hasłami i jej hashami
            n -> liczba haseł jakie chcemy otrzymać
        Zwraca:
            [["pass1", "pass1_hash"], ["pass1", "pass1_hash"], ...]
            listę list haseł i ich hashy SHA1

    ConfData.pwned_users(pass_list, hack_time)
        Przyjmuje:
            pass_list -> struktura z wczytanymi hasłami i jej hashami
            hack_time -> obiekt Datetime reprezentujący czas wycieku
        Zwraca:
            ["mail1", "mail2", ..... ]
            listę ludzi których musimy poinformować o wycieku ich hasła (tylko tych ze słabymi hasłami)

    ConfData.safe_users(pass_list, hack_time)
        Przyjmuje:
            pass_list -> struktura z wczytanymi hasłami i jej hashami
            hack_time -> obiekt Datetime reprezentujący czas wycieku
        Zwraca:
            ["mail1", "mail2", ..... ]
            listę ludzi którzy nie figurowali w wycieku i mają bezpieczne hasła

Do dyspozycji jest tylko próbka danych które firma ConfWord przekazała do analizy
Napisz program tak by działał dla dowolnych danych i czasu wycieku

'''
import hashlib
import csv
from collections import defaultdict, OrderedDict
from datetime import datetime


class ConfData():

    # Najważniejsze funkcje (ale nie wszystkie !) które trzeba uzupełnić

    def __init__(self, database_file):
        pass

    def weak_pass_users(self, pass_list):
        pass

    def common_pass(self, pass_list, n=10):
        pass

    def pwned_users(self, pass_list, hack_time):
        pass

    def safe_users(self, pass_list, hack_time):
        pass

    @staticmethod
    def read_passwords(database_file):
        pass
