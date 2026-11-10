class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Геттеры
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Сеттеры
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным.")

    def make_sound(self):
        print("Животное издаёт звук.")


class Dog(Animal):
    def make_sound(self):
        print("Собака: Гав-гав!")


class Cat(Animal):
    def make_sound(self):
        print("Кошка: Мяу-мяу!")


# Создание объектов
dog = Dog("Бобик", 3)
kitty = Cat("Китти", 1)

# Демонстрация полиморфизма
dog.make_sound()
kitty.make_sound()

# Изменение приватных атрибутов через сеттеры
kitty.set_age(2)
kitty.set_name("Мурка")

# Получение обновлённых значений через геттеры
print("Имя кошки:", kitty.get_name())
print("Возраст кошки:", kitty.get_age())
