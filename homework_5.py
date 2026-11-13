
class Distance:
    conversion_dict = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def convert(self):
        return self.value * Distance.conversion_dict[self.unit]

    def __add__(self, other):
        result = self.convert() + other.convert()
        return Distance(result, "m")

    def __sub__(self, other):
        result = self.convert() - other.convert()
        return Distance(result, "m")

    def __eq__(self, other):
        return self.convert() == other.convert()

    def __lt__(self, other):
        return self.convert() < other.convert()

    def __gt__(self, other):
        return self.convert() > other.convert()


# Создаем объекты
d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(1000, "cm")

# Проверяем вывод
print("Первое расстояние:", d1)
print("Второе расстояние:", d2)
print("Третье расстояние:", d3)

# Сложение и вычитание
print("Сложение:", d1 + d2)
print("Вычитание:", d2 - d1)

# Сравнение
print("Равны:", d1 == d3)
print("Первое меньше второго:", d1 < d2)
print("Первое больше второго:", d1 > d2)
