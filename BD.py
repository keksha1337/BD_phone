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
