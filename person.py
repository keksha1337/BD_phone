import time
from datetime import date
class Person:
    name = 'none'
    surname = 'none'
    birthday_date = 'none'
    phones = dict()

    def set_name(self, name: str):
        self.name = name

    def set_surname(self, surname: str):
        self.surname = surname

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