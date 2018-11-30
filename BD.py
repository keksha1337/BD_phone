from person import Person
from datetime import date
class BD:
    person_list = dict()

    def get_all(self) -> list():
        return sorted(list(self.person_list.values()))
    
    def add(self, person: Person) -> bool:
        key = person.get_name() + person.get_surname()
        if key in self.person_list:
            return False
        self.person_list[key] = person
        return True

    def remove_by_key(self, key: str):
        self.person_list.pop(key)

    def search(self, ddmm='none', mm='none', sign='none', age='none', name='none', surname='none', phone_number='none') -> dict:
        result = self.person_list
        if name != 'none':
            result = self.search_by_name(result, name)
        if surname != 'none':
            result = self.search_by_surname(result, surname)
        if sign != 'none' and age != 'none':
            result = self.search_by_age(result, sign, age)
        if ddmm != 'none':
            result = self.search_by_birthday(result, ddmm)
        if mm != 'none':
            result = self.search_by_birthday_month(result, mm)
        if phone_number != 'none':
            result = self.search_by_phone(result, phone_number)
        return result

    def search_by_name(self, keys: dict, value: str) -> dict:
        result = dict()
        for person in keys:
            if self.person_list[person].get_name() == value:
                result[person] = self.person_list[person]
        return result

    def search_by_surname(self, keys: dict, value: str) -> dict:
        result = dict()
        for person in keys:
            if self.person_list[person].get_surname() == value:
                result[person] = self.person_list[person]
        return result

    def search_by_age(self, keys: dict, sign: str, age: str) -> dict:
        result = dict()
        age = int(age)
        for person in keys:
            if sign == '=' and self.person_list[person].get_age() == age:
                result[person] = self.person_list[person]
            elif sign == '<' and self.person_list[person].get_age() < age:
                result[person] = self.person_list[person]
            elif sign == '>' and self.person_list[person].get_age() > age:
                result[person] = self.person_list[person]
        return result

    def search_by_birthday(self, keys: dict, mmdd: str) -> dict:
        result= dict()
        date_birthday = date(2000, int(mmdd.split('.')[1]), int(mmdd.split('.')[0]))
        for person in keys:
            pers = self.person_list[person]
            if (pers.get_birthday_date().day == date_birthday.day and
                pers.get_birthday_date().month == date_birthday.month):
                result[person] = self.person_list[person]
        return result

    def search_by_birthday_month(self, keys: dict, mm: str) -> dict:
        result= dict()
        date_birthday = date(2000, int(mm), 1)
        for person in keys:
            pers = self.person_list[person]
            if pers.get_birthday_date().month == date_birthday.month:
                result[person] = self.person_list[person]
        return result

    def search_by_phone(self, keys: dict, phone_number: str) -> dict:
        result = dict()
        for person in keys:
            for phone in self.person_list[person].get_phones():
                if self.person_list[person].get_phones()[phone] == phone_number:
                    result[person] = self.person_list[person]
                    break;
        return result

    def change_field(self, key: str, person: Person):
        self.person_list[key] = person

    def __str__(self):
        result = ''
        for person in self.person_list:
            result = result + str(self.person_list[person]) + '\n'
        return result
