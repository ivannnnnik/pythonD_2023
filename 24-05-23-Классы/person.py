class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def get_full_name(self):
        return f"{self.name} {self.surname}"

person_1 = Person('Иван', 'Иванов')

print(person_1.name)
print(person_1.surname)
print(person_1.get_full_name)