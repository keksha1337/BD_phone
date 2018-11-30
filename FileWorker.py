from BD import BD
from person import Person
class FileWorker:
    def read_from_file(self) -> BD:
        bd = BD()
        f = open('text.txt', 'r')
        for line in f:
            person = Person(line[0:-1])
            bd.add(person)
        f.close()
        return bd

    def write_to_end(self, person: Person):
        f = open('text.txt', 'a')
        f.write('\n' + str(person))
        f.close()

    def rewrite_file(self, bd: BD):
        f = open('text.txt', 'w')
        for person in bd.person_list:
            f.write(str(bd.person_list[person]) + '\n')
        f.close()
