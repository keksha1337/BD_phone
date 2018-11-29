from person import Person
from BD import BD
p1 = Person()
p1.set_name('Max')
p1.set_surname('Moshkov')
p1.set_birthday_date('10.11.1770')
p1.add_phone('tel_1', '89026810084')
p1.add_phone('tel_2', '89023000910')

p2 = Person()
p2.set_name('Maxim')
p2.set_surname('Moshkov')
p2.set_birthday_date('25.05.1975')
p2.add_phone('tel_1', '89026810084')
p2.add_phone('tel_2', '89023000910')

bd = BD()
bd.add(p1)
bd.add(p2)
bd.show_all()
