from person import Person
from BD import BD
from FileWorker import FileWorker

p1 = Person()
p1.set_name('Max')
p1.set_surname('Moshkov')
p1.set_birthday_date('10.11.1770')
p1.add_phone('tel_1_1', '89026810084')
p1.add_phone('tel_2_1', '89023000910')

p2 = Person()
p2.set_name('Maxim')
p2.set_surname('Moshkov')
p2.set_birthday_date('25.05.1975')
p2.add_phone('tel_1_2', '89026810085')
p2.add_phone('tel_2_2', '89023000910')

bd = BD()
bd.add(p1)
bd.add(p2)

print(bd)

people = bd.get_all()
for p in people:
    print(p)

print()

print(bd.search(name='Max'))
print(bd.search(surname='Moshkov'))
print(bd.search(sign='=', age='43'))
print(bd.search(ddmm='10.11'))
print(bd.search(mm='05'))
print()
print(bd.search(phone_number='89023000910'))
print()
bd.remove_by_key('MaxMoshkov')
people = bd.get_all()

for p in people:
    print(p)

print('\n\n\nFROM FILE:::')
fileworker = FileWorker()
bd = fileworker.read_from_file()
p2 = Person()
p2.set_name('Kek')
p2.set_surname('Lolov')
p2.set_birthday_date('19.08.1975')
p2.add_phone('tel_1_3', '89026811185')
p2.add_phone('tel_2_3', '89023001910')
bd.add(p2)
fileworker.rewrite_file(bd)
print(bd)
