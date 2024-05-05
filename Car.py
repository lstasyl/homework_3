import random

class Car:
    def __init__(self, model, color):
        self.__fuel = random.randrange(0, 9)
        self.__trip_distance = 0
        self.__model = model
        self.__color = color

    def move(self, distance):
        if self.__fuel == 0:
            print(
                f"Паливо закінчилось у автомобіля {self.__color} {self.__model}. Гонка завершилась для цього автомобіля.")
            return
        else:
            self.__trip_distance += distance
            self.__fuel -= distance // 10  # Зменшення палива на 1 за кожні 10 одиниць відстані

    def get_trip_distance(self):
        return self.__trip_distance

    def get_fuel(self):
        return self.__fuel

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

# Створення трьох екземплярів класу Car
car1 = Car("Toyota", "Червоний")
car2 = Car("Honda", "Синій")
car3 = Car("Ford", "Зелений")

# Початок гонки
race_dist = 0
desired_dist = 100

while race_dist < desired_dist:
    for car in [car1, car2, car3]:
        if car.get_fuel() == 0:
            continue
        distance = random.randrange(0, 9)
        car.move(distance)
        race_dist = max(car.get_trip_distance() for car in [car1, car2, car3])

        if race_dist >= desired_dist:
            winning_car = max([car1, car2, car3], key=lambda x: x.get_trip_distance())
            print(f"Переміг автомобіль {winning_car.get_color()} {winning_car.get_model()} з результатом {winning_car.get_trip_distance()} км.")
            break

# Виведення результатів
for car in [car1, car2, car3]:
    print(f"Автомобіль {car.get_color()} {car.get_model()} проїхав {car.get_trip_distance()} км та має запас палива {car.get_fuel()}.")



