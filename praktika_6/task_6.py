class Avtobus:
    def __init__(self, max_passengers, max_speed):
        self.speed = 0
        self.max_passengers = max_passengers
        self.max_speed = max_speed
        self.passenger_names = []
        self.seats = {i: None for i in range(1, max_passengers + 1)}

    def has_free_seats(self):
        return any(seat is None for seat in self.seats.values())

    def board_passenger(self, name, count=1):
        boarded = 0
        for seat, passenger in self.seats.items():
            if passenger is None:
                self.seats[seat] = name if count == 1 else f"{name}_{boarded+1}"
                self.passenger_names.append(self.seats[seat])
                boarded += 1
                if boarded == count:
                    break
        if boarded < count:
            print(
                f"Посажено только {boarded} пассажиров из {count}, свободных мест больше нет."
            )

    def disembark_passenger(self, name):
        removed = 0
        for seat, passenger in list(self.seats.items()):
            if passenger == name or passenger.startswith(name + "_"):
                self.seats[seat] = None
                if passenger in self.passenger_names:
                    self.passenger_names.remove(passenger)
                removed += 1
        if removed == 0:
            print(f"Пассажир(ы) с именем '{name}' не найдены.")
        else:
            print(f"Высажено {removed} пассажир(ов) с именем '{name}'.")

    def increase_speed(self, value):
        self.speed += value
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        print(f"Текущая скорость увеличена до: {self.speed} км/ч")

    def decrease_speed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0
        print(f"Текущая скорость уменьшена до: {self.speed} км/ч")

    def show_info(self):
        print("-" * 30)
        print(f"Скорость: {self.speed} км/ч")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Макс. пассажиров: {self.max_passengers}")
        print(f"Пассажиры: {self.passenger_names}")
        print(f"Свободные места: {'Да' if self.has_free_seats() else 'Нет'}")
        print(f"Места: {self.seats}")
        print("-" * 30)


# Создание базы автобусов
bus_fleet = [Avtobus(10, 90), Avtobus(15, 100), Avtobus(20, 120)]

# Посадка пассажиров
bus_fleet[0].board_passenger("Иван", 3)
bus_fleet[1].board_passenger("Мария", 5)
bus_fleet[2].board_passenger("Алексей", 2)

# Изменение скорости
bus_fleet[0].increase_speed(30)
bus_fleet[1].increase_speed(50)
bus_fleet[2].increase_speed(80)

# Вывод полной информации по каждому автобусу
print("Информация по всем автобусам:")
for i, bus in enumerate(bus_fleet):
    print(f"АВТОБУС #{i+1}")
    bus.show_info()


# Поиск автобусов по параметрам
def find_buses(fleet, min_seats=None, max_speed=None):
    result = []
    for bus in fleet:
        conditions = True
        if min_seats is not None:
            conditions &= bus.max_passengers >= min_seats
        if max_speed is not None:
            conditions &= bus.max_speed <= max_speed
        if conditions:
            result.append(bus)
    return result


# Пример поиска: автобусы с минимум 15 местами и максимальной скоростью не более 100
print("Поиск подходящих автобусов:")
found_buses = find_buses(bus_fleet, min_seats=15, max_speed=100)
for i, bus in enumerate(found_buses):
    print(f"Подходящий автобус #{i+1}")
    bus.show_info()
