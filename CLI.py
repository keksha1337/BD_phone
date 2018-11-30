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

def search():
    ddmm = 'none'
    mm = 'none'
    sign = 'none'
    age = 'none'
    name = 'none'
    surname = 'none'
    phone_number = 'none'
    ch = 'none'
    while ch != '2':
        print("'1' - add parametr.\n'2' - search.\n")
        ch = input()
        if ch == '1':
            print(''''Name' to add name.\n
'Surname' to add surname.\n
'Phone' to add phone number.\n
'Birthday' to add birthday.\n
'Month' to add birthday's month.\n
'Sign' ('<' '>' '=') to add filter by age.\n''')
            param = input()
            value = input('Input value:\t')
            if param == 'Name':
                name = value
            elif param == 'Surname':
                surname = value
            elif param == 'Phone':
                phone_number = value
            elif param == 'Birthday':
                ddmm = value
            elif param == 'Month':
                mm = value
            elif param == 'Sign':
                sign = value
                age = input('Input age:\t')
        if ch == '2':
            show_list_person(bd.search(ddmm=ddmm,mm=mm,sign=sign,name=name,surname=surname,phone_number=phone_number))        

fileworker = FileWorker()
bd = fileworker.read_from_file()
comand = '0'
while 1:
    if comand == '0':
        show_menu()
    elif comand == 'Print':
        show_list_person(bd.person_list)
    elif comand == 'Search':
        search()
    elif comand == 'quit':
        break;
    comand = input("'0' to show menu again.\n")
