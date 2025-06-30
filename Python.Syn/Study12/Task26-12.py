class Transport(object):

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def get_info(self):
        print(f'Название автомобиля: {self.name}. Скорость: {self.max_speed}. Пробег: {self.mileage}')

class Autobus(Transport):

        seating_capacity = 50

        def __index__(self, name, max_speed, mileage, seating_capacity):
            self.seating_capacity = seating_capacity

        def seating_capacity_unit(self):
            print(f"Вместимость одного автобуса {self.name} {self.seating_capacity} пассажиров")

car1 = Autobus("Renault Logan", 180, 12)

car1.seating_capacity_unit()