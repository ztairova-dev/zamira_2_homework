class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education = "высшее образование есть" if self.higher_education else "высшего образования нет"
        print(
            f"Меня зовут {self.name}, я родился {self.birth_date}, "
            f"по профессии {self.occupation}, {education}."
        )

person1 = Person("Александр", "12.05.2000", "программист", True)
person2 = Person("Мария", "23.08.2002", "дизайнер", False)
person3 = Person("Иван", "04.11.1998", "инженер", True)

people = [person1, person2, person3]

for person in people:
    print("Имя:", person.name)
    print("Дата рождения:", person.birth_date)
    print("Профессия:", person.occupation)
    print("Высшее образование:", person.higher_education)
    person.introduce()
    print()
