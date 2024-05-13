from datetime import date

class Person:
    def __init__(self, age, name, birthday):
        self.age = age
        self.name = name

    def calculate_age(self):
        self.birthday = date.today()

    
class People(Person):
    pass




person1 = People(12, 'brandon',)

print(person1.age, person1.name, person1.birthday)