from person import Person
class BD:
    person_list = dict()

    def show_all(self):
        for key in self.person_list:
            print(self.person_list[key])
    
    def add(self, person: Person) -> bool:
        key = person.get_name() + ' ' + person.get_surname()
        if key in self.person_list:
            return False
        self.person_list[key] = person
        return True

    def remove_by_key(self, key: str):
        pass

    def remove_by_phone_number(self, phone: str):
        pass

    def search(self, ddmm=default, mm=default, sign=default, name=default, surname=default, phone_number=default):
        pass

    def change_field(self, key: str):
        pass
    
