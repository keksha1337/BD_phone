import time
from datetime import date
class Person:
    def __init__(self, line='none'):
        if line == 'none':
            self.name = 'none'
            self.surname = 'none'
            self.birthday_date = 'none'
            self.phones = dict()
        else:
            line = line.split(';')
            self.name = line[0].title()
            self.surname = line[1].title()
            self.set_birthday_date(line[2])
            self.phones = dict()
            for number in line[3].split('@'):
                self.phones[number.split(':')[0]] = number.split(':')[1]
        
    def set_name(self, name: str):
        self.name = name.title()

    def set_surname(self, surname: str):
        self.surname = surname.title()

    def set_birthday_date(self, birthday_date: str):
        [dd, mm, yyyy] = birthday_date.split('.')
        self.birthday_date = date(int(yyyy), int(mm), int(dd))

    def add_phone(self, phone_name: str, phone_number: str) -> bool:
        if phone_name in self.phones:
            return False
        self.phones[phone_name] = phone_number
        return True

    def get_name(self) -> str:
        return self.name

    def get_surname(self) -> str:
        return self.surname

    def get_birthday_date(self) -> date:
        return self.birthday_date

    def get_phones(self) -> dict:
        return self.phones

    def change_phone_number(self, phone_name: str, phone_number: str):
        self.phones[phone_name] = phone_number

    def remove_phone(self, phone_name: str) -> bool:
        if not(phone_name in self.phones):
            return False
        self.phones.pop(phone_name)

    def get_age(self) -> int:
        return int((date.today() - self.birthday_date).days / 365.25)

    def __lt__(self, other):
        return (self.name + self.surname) < (other.name + other.surname)

    def __str__(self):
        result = self.name + ';' + self.surname + ';'
        try:
            result = result + str(self.birthday_date.day) + '.' + str(self.birthday_date.month) + '.' + str(self.birthday_date.year) + ';'
        except:
            result = result + "none;"
        for phone_name in self.phones:
            result = result + phone_name + ':' + self.phones[phone_name] + '@'
        result = result[:-1] + ';'
        return result
