
TRIP_COST = 20


class TransportCard:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0

    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")

        self.__balance += amount
        print(f"Карта пополнена на {amount} сом")

    def pay_for_trip(self):
        if self.__balance < TRIP_COST:
            raise ValueError("Недостаточно средств на карте")

        self.__balance -= TRIP_COST
        print("Поездка оплачена!")


# Создаём две транспортные карты
card1 = TransportCard("Айсулуу")
card2 = TransportCard("Алмаз")


# Пополняем баланс
card1.add_money(100)
card2.add_money(60)


# Оплачиваем поездки
card1.pay_for_trip()
card1.pay_for_trip()

card2.pay_for_trip()


# Выводим информацию
print("\nИнформация о картах:")

print("Владелец:", card1.get_owner())
print("Баланс:", card1.get_balance())

print("Владелец:", card2.get_owner())
print("Баланс:", card2.get_balance())


# Проверяем обработку ошибок
try:
    card2.add_money(-50)
except ValueError as error:
    print("Ошибка:", error)

try:
    card2.pay_for_trip()
    card2.pay_for_trip()
except ValueError as error:
    print("Ошибка:", error)
