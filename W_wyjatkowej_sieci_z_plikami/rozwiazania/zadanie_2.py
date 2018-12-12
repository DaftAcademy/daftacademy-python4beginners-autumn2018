'''
Pamiętasz firmę ConfWord dla której sprawdzałeś statystyki kilka tygodni temu?
Okazało się że firmowa baza danych klientów wyciekła do internetu.

By firma ConfWorld dalej funkcjonowała musisz przekazać klientom
informacje na temat wycieku, ale nie chcesz siać paniki.
W pierwszej kolejności należy zresetować hasła klientom którzy nie zmieniali
hasła od czasu ataku i mają słabe hasło (figurujące na liście słabych haseł)

Napisz program by znaleźć takie osoby. Wyciek danych nastąpił 10.11.2017 w południe
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
    baza danych która wyciekła do internetu    -> confwrld_user_data_dump_10.11.2017.csv
    aktualna baza klientów                     -> confwrld_user_database.csv
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
            pass_list -> struktura z wczytanymi hasłami i jej hashami w postaci:
                        [["pass1", "pass1_hash"], ["pass1", "pass1_hash"], ...]
            n -> liczba haseł jakie chcemy otrzymać
        Zwraca:
            listę haseł posortowanych po częśtości wystąpienia.
            Jeśli częstotliwość jest taka sam dla kilku haseł, sortuje je alfabetycznie

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

Scafflod dla rozwiązania:

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




'''
import hashlib
import csv
from datetime import datetime
from collections import defaultdict, OrderedDict


class ConfData():
    def __init__(self, database_file='confwrld_user_database.csv'):
        # Treść zadania przewidywała dowolny format bazy danych.
        # Relacyjna baza SQL wygląda podobnie do listy rekordów które są listami
        # Dlatego też w zadaniu wzorcowym stworzyłem odwzorowanie tego wzorca
        self.database = self._read_database(database_file)

    def _read_database(self, database_file):
        db = list()
        # otwieramy plik za pomocą contextmanagera przez `with`
        with open(database_file, 'r') as f:
            # nasz plik CSV używa przecinka jako separator pól
            reader = csv.reader(f, delimiter=',')
            # pomijamy pierwszy wiersz, nagłówek zawierający nazwy kolumn
            next(reader)
            for row in reader:
                # dla każdego wiersza w pliku csvreader zwraca listę pól które
                # następnie w postaci listy dodajemy do naszej wynikowej bazy
                db.append([
                    row[0], row[1],
                    # daty zapisuję jako unix timestamp
                    # łatwiej będzie po porównywać daty (może być DateTime)
                    datetime.strptime(row[2], "%Y-%m-%dT%H:%M:%S").timestamp(),
                    datetime.strptime(row[3], "%Y-%m-%dT%H:%M:%S").timestamp(),
                ])
        return db

    @staticmethod
    def hash_password(password):
        # metoda hashująca hasło.
        # hashlib wymaga podania hasła jako Bytes stąd password.encode
        # hashlib zwraca hasha w postaci szesnastkowej by zapisać do str
        # wykonujemy na obiekcie hashlib.hexdigest()
        return hashlib.sha1(password.encode('utf-8')).hexdigest()

    @staticmethod
    def read_passwords(database_file="top_500_most_common_passwords.txt"):
        # funkcja ma zadanie zwrócić listę haseł w postaci
        # [["pass1", "pass1_hash"], ["pass1", "pass1_hash"], ...]
        pass_list = list()

        with open(database_file, 'r') as f:
            for row in f:
                # dla każdego hasła w pliku które jest zarazem wierszem w pliku
                # odcinamy znak nowej linii i następnie wpisujemy do listy
                # listę z hasłem i jego hashem
                p = row.rstrip('\n')
                pass_list.append([p, ConfData.hash_password(p)])
        return pass_list

    def week_pass_users(self, pass_list):
        # Zwraca listę ludzi którzy mają słabe hasło
        # figurujące na liście słabych haseł
        user_list = []
        # jako że potrzebujemy listę hashy do porównania, tworzymy taki helper
        hash_list = [x[1] for x in pass_list]
        for user in self.database:
            if user[1] in hash_list:
                # dodaj do wyniku tylko mail osób które mają słabe hasło
                user_list.append(user[0])

        return user_list

    def common_pass(self, pass_list, n=10):
        # przekształcamy listę haseł w `dict` będzie łatwiej przeszukiwalna
        pass_list_dict = dict([(x[1], x[0]) for x in pass_list])
        # używamy `defaultdict` jako tymczasowy słownik dla liczników
        _p = defaultdict(int)
        # dla każdego użytkownika w bazie danych
        for user in self.database:
            # jeśli jego hasło widniej na liście łatwych haseł
            if user[1] in pass_list_dict:
                # dodaj jego wystąpienie do słownika liczników
                _p[pass_list_dict[user[1]]] += 1
                # dodanie `+= 1` do wartości pod nieistniejącym kluczem
                # w defaultdict stworzy ten klucz i zainicjuje wartość przed
                # operacją, w tej sytuacji `int` o wartości `0`

        # sortujemy listę haseł i ich wystąpień po haśle alfabetycznie
        _p = OrderedDict(
            sorted(_p.items(), key=lambda x: x[0], reverse=False))

        # sortujemy listę haseł i ich wystąpień po ilości wystąpień (malejąco)
        # następnie tworzymy z nich listę haseł
        # takie dwa sortowania jedno po 2-gim umożliwiają posortowanie
        # haseł o tej samej ilości wystąpień, alfabetycznie
        return [x[0] for x in OrderedDict(
            sorted(_p.items(), key=lambda x: x[1], reverse=True)).items()][:n]

    def pwned_users(self, pass_list, hack_time):
        # jako że potrzebujemy listę hashy do porównania, tworzymy taki helper
        hash_list = [x[1] for x in pass_list]
        # tworzę unix timestamp z czasu ataku by porównywać z timestamp z bazy
        hack_time_ts = int(hack_time.timestamp())
        user_list = []

        for user in self.database:
            # dla każdego użytkownika ze słabym hasłem
            if user[1] in hash_list:
                # którego zmiana hasła nie nastąpiła przed atakiem
                if user[3] <= hack_time_ts:
                    # dodaj do listy osób zagrożonych
                    user_list.append(user[0])
        return user_list

    def safe_users(self, pass_list, hack_time):
        # jako że potrzebujemy listę hashy do porównania, tworzymy taki helper
        hash_list = [x[1] for x in pass_list]
        # tworzę unix timestamp z czasu ataku by porównywać z timestamp z bazy
        hack_time_ts = int(hack_time.timestamp())
        user_list = []

        for user in self.database:
            # dla każdego użytkownika ze mocnym hasłem
            # którego zmiana hasła miała miejsce po ataku
            if user[1] not in hash_list or user[3] > hack_time_ts:
                # dodaj do listy osób bezpiecznych
                user_list.append(user[0])

        # filtrujemy osoby w ten sposób by wyłuskać osoby które pomimo tego że
        # hasło zmieniły to jednak na słabe i należy je powiadomić o tym że
        # muszą je zmienić
        return user_list

