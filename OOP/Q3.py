class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = mileage

    @property
    def mileage(self):
        return self.__mileage

    def display(self):
         print(f"The car is: Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}")
    

TeslaY = Car("Tesla", "Y", 2020, 45.5)

TeslaY.display()
 
