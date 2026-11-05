from person import Person
from rect import Rectangle
from datetime import date

person = Person("James Doe", date(2020, 2, 20))

print(person.initials())
person2 = Person("james doe deo", date(2020, 2, 20))

print(person2.initials())

rect = Rectangle("2", 5)
