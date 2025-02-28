class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"year: {self.year}")
Car = Car("AUDI", "Q7", 2019)
print(Car.display_info())
