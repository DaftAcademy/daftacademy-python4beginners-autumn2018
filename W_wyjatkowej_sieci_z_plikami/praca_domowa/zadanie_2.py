'''
Pamiętasz firmę ConfWord dla której sprawdzałeś statystyki kilka tygodni temu?
Okazało się że firmowa baza danych klientów wyciekła do internetu.

By firma ConfWorld dalej funkcjonowała musisz przekazać klientom
informacje na temat wycieku, ale nie chcesz siać paniki.
W pierwszej kolejności należy zresetować hasła klientom którzy nie zmieniali hasła od czasu ataku

Napisz program by znaleźć takie osoby. Wyciek danych nastąpił 10.11.2017 w samo południe
Twoja baza danych jest aktualna (załóżmy dzień 20.11.2018 00:00)

Na domiar złego okazało się że Twoi klienci używali bardzo słabych haseł.
By w przyszłości nikt nie łamał haseł Twoich klientów,
wykożystując listę dancyh najczęściej używanych haseł w internecie,
napisz kolejną część programu który w 2-giej kolejności:
    znajdzie wszystkich użytkowników którzy mają hasło figurujące na tej liście
    znajdzie top 10 występujących haseł w serwisie figurujących na liście top500 w PLAIN TEXT
    znajdzie wszystkich bezpiecznych użytkowników
        (hasło nie na figuruje liście oraz zmienili hasło od ataku)

Dane:
    hasła w bazie są hashowane algorytmem SHA1
    lista 500 najczęstszych haseł w internecie -> top_500_most_common_passwords.txt
    baza danych która wyciekła do internetu   -> confwrld_user_data_dump_10.11.2017.csv
    aktualna baza klientów                    -> confwrld_user_database.csv
    wszystkie daty są z tej samej strefy czasowej

Wymagania szczegółowe:
    ConfData
        Struktura przechwująca dane
    ConfData.weak_pass_users(pass_list)
        Zwraca listę ludzi którzy mają słabe hasło figurujące na liście słaych haseł
        pass_list = [["pass1", "pass1_hash"], ["pass1", "pass1_hash"], ...]
    ConfData.common_pass(pass_list, n=10) = ["pass1", "pass2", ..... ]
        Zwraca listę ludzi którzy mają najczęściej występujące hasła
        pass_list = [["pass1", "pass1_hash"], ["pass1", "pass1_hash"], ...]
    ConfData.pwned_users(pass_list, hack_time) = ["mail1", "mail2", ..... ]
        Zwraca listę ludzi których musimy poinformować o wycieku ich hasła
        hack_time -> objekt Datetime reprezentujący czas wycieku
    ConfData.safe_users(pass_list, hack_time) = ["mail1", "mail2", ..... ]
        Zwraca listę ludzi którzy nie figurowali w wycieku i mają bezpieczne hasła
        hack_time -> objekt Datetime reprezentujący czas wycieku

Do dyzpozycji jest tylko próbka danych które firma ConfWord przekazała do analizy
Napisz program tak by działał dla dowolych danych i czasu wycieku

'''


class ConfData():
    pass