class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
   
    def info_return(self):
        return(f"The car is: Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}")

    def display(self):
        print(self.info_return())

class ElectricCar(Car):
    def __init__(self, brand, model, year, mileage, battery_capacity):
        super().__init__(brand, model, year, mileage)
        self.battery_capacity = battery_capacity

    def display(self):

        print(self.info_return() + f" Battery Capacity: {self.battery_capacity}% ")

car1 = Car("Tesla", "Y", 2020, 45.5,)
car2 = ElectricCar("Tesla", "X", 2021, 505, 55.5)

car1.display()
print(" ")
car2.display()