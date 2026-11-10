
class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, работаю {self.occupation}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одногруппник, родился {self.birth_date}, учусь в группе {self.group_name}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг, родился {self.birth_date}, работаю {self.occupation}, моё хобби — {self.hobby}")


# Создаём 2 одногруппников
classmate1 = Classmate("Алмаз", "05.12.2000", "студент", "ПИ-1")
classmate2 = Classmate("Бектур", "10.03.2001", "студент", "ПИ-2")

# Создаём 2 друзей
friend1 = Friend("Байэль", "15.06.2002", "программист", "футбол")
friend2 = Friend("Данияр", "20.08.2001", "дизайнер", "рисование")


# Вызываем методы
classmate1.introduce()
classmate2.introduce()

friend1.introduce()
friend2.introduce()
