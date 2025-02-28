class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary
    def display_info(self):
        print(f"name: {self.name}, age: {self._age}, salary: {self.__salary}")

person = Person ("Gladys",24,80000)
print(person.name)
print(person._age)
print(person.__salary)

