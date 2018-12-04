from collections import OrderedDict
import csv
from datetime import date
from decimal import Decimal


in_filename = 'personal_data.csv'
out_filename = 'clean_personal_data.csv'


def get_csv_lines():
    with open(in_filename, encoding='Windows-1250') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            yield row


def save_csv(data):
    first_row = next(data)
    field_names = first_row.keys()
    with open(out_filename, 'w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=field_names)
        csv_writer.writeheader()
        csv_writer.writerow(first_row)
        for row in data:
            csv_writer.writerow(row)


class PersonalDataCleaner:
    """
    Cleaner of personal data. 
    
    Usage:
      Pass an iterable of dicts to `clean` method, which 
      will yield dicts with cleaned data.
    """
    
    STRINGS_REPRESENTING_TRUE = {'1', 'prawda', 'tak', 'ma', 'true'}
    STRINGS_REPRESENTING_FALSE = {'0', 'fałsz', 'nie', 'nie ma', 'false'}
    
    def __init__(self):
        map_string_to_true = {
            k: True
            for k in self.STRINGS_REPRESENTING_TRUE
        }
        map_string_to_false = {
            k: False
            for k in self.STRINGS_REPRESENTING_FALSE
        }
        self.map_string_to_bool = {
            **map_string_to_true,
            **map_string_to_false,
        }

    def clean(self, rows):
        for row in rows:
            # czyszczenie wspólne dla wszystkich kolumn
            clean_row = self._clean_all_items(row)

            # czyszczenie wyspecjalizowane
            clean_row['first_name'] = (
                self._clean_name(clean_row['first_name'])
            )
            clean_row['last_name'] = (
                self._clean_name(clean_row['last_name'])
            )
            clean_row['id_number'] = (
                self._clean_id_number(clean_row['id_number'])
            )
            clean_row['employment_start_date'] = (
                self._clean_date(clean_row['employment_start_date'])
            )
            clean_row['monthly_salary'] = (
                self._clean_monetary_value(clean_row['monthly_salary'])
            )
            clean_row['department'] = (
                self._clean_department(clean_row['department'])
            )
            clean_row['multisport'] = (
                self._clean_multisport(clean_row['multisport'])
            )
    
            yield clean_row
            
    def _clean_all_items(self, row):
        clean_row = OrderedDict()
        for key, value in row.items():
            clean_value = value.strip()
            clean_value = clean_value or None
            clean_row[key] = clean_value
        return clean_row

    def _clean_name(self, name):
        if name is None:
            return None
        return name.title()

    def _clean_id_number(self, id_number):
        return id_number

    def _clean_date(self, date_string):
        if date_string is None:
            return None

        # YYYY-MM-DD{T}HH:MM:SS --> YYYY-MM-DD
        date_string = date_string.partition('T')[0]
    
        # YYYY/MM/DD --> YYYY-MM-DD
        date_string = date_string.replace('/', '-')
    
        # convert to `date` object (exception on wrong format)
        year, month, day = date_string.split('-')
        date_obj = date(year=int(year), month=int(month), day=int(day))
    
        return date_obj

    def _clean_monetary_value(self, amount):
        if amount is None:
            return None
        amount = amount.replace(' ', '')
        amount = amount.replace(',', '.')
        return Decimal(amount).quantize(Decimal('0.01'))

    def _clean_department(self, department):
        return department

    def _clean_multisport(self, something):
        if something is None:
            return None
        something = something.lower()
        return self.map_string_to_bool[something]


if __name__ == '__main__':
    data = get_csv_lines()
    cleaned_data = PersonalDataCleaner().clean(data)
    save_csv(cleaned_data)

