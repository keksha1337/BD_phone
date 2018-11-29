from person import Person
p = Person()
p.set_name('Max')
p.set_surname('Moshkov')
p.set_birthday_date('25.01.1999')
p.add_phone('tel_1', '89026810084')
print(p.get_name(), p.get_surname(), p.get_age(),
      p.get_birthday_date(), p.get_phones(), sep='\n')

