from person import Person
from BD import BD
from FileWorker import FileWorker

def show_menu():
    print('''_______________
Print' to show all.\n
'Search' to searching.\n
'Add' to add new person.\n
'Remove' to remove.\n
'Change' to any changes.\n
'Show age' to show person's age.\n
'quit' to quit.\n
_______________''')

def print_person(person: Person):
    print(person.get_name() + ' ' + person.get_surname())
    print('\t' + str(person.get_birthday_date()))
    print('\tPhones:')
    for phone in person.get_phones():
        print('\t\t' + phone + ' : ' + person.get_phones()[phone])
    print('_' * 50)

def show_list_person(people: dict):
    for person in people:
        print_person(people[person])


fileworker = FileWorker()
bd = fileworker.read_from_file()
comand = '0'
while 1:
    if comand == '0':
        show_menu()
    elif comand == 'Print':
        show_list_person(bd.person_list)
    elif comand == 'quit':
        break;
    comand = input("'0' to show menu again.\n")
