#---------------------------------------------------------------
#                    Problem 1
#---------------------------------------------------------------
print('Problem 1')
# Create a car class with attributes like brand and model. 
# Then create and instance of this class.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car1 = Car("Toyota", "Corolla")
print(my_car1.brand)
print(my_car1.model)
print('')

my_car2 = Car("Honda", "Civic")
print(my_car2.brand)
print(my_car2.model)
print('')
#---------------------------------------------------------------
#                    Problem 2
#---------------------------------------------------------------
print('Problem 2')
# Add a method to the Car class that displays the full name of
# the car (brand and model)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} + {self.model}"
    
my_car1 = Car("Honda", "Civic")
print(my_car1.brand)
print(my_car1.model)
print(my_car1.full_name())
print('')
#---------------------------------------------------------------
#                    Problem 3
#---------------------------------------------------------------
print('Problem 3')
# Create an ElectricCar class that inherits from the Car class 
# and has an additional attribute
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_electric_car1 = ElectricCar("Tesla", "Model S", "85 kWh")
print(my_electric_car1.brand)
print(my_electric_car1.model)
print(my_electric_car1.battery_size)
print(my_electric_car1.full_name())
print('')
#---------------------------------------------------------------
#                    Problem 4
#---------------------------------------------------------------
# Modify the Car class to encapsulate the brand attribute, 
# making it private, and provide a getter method for it.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} + {self.model}"
    def get_brand(self):
        return self.__brand + ' !'

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
print('Problem 4')
my_electric_car1 = ElectricCar("Tesla", "S5", "86 kWh")
# print(my_electric_car1.brand) # will give error because brand is private and accessible through get_brand() method
print(my_electric_car1.model)
print(my_electric_car1.get_brand())
#---------------------------------------------------------------
#                    Problem 5
#---------------------------------------------------------------
# Demonstrate polymorphism by defining a method fuel_type in both
#  Car and ElectricCar classes, but with different behaviors.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def get_brand(self):
        return self.brand + '!'
    def get_full_name(self):
        return f"{self.brand} + {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

print('Problem 5')
my_car1 = Car("Honda", "Civic")
print(my_car1.brand)
print(my_car1.model)
print(my_car1.fuel_type())

my_electric_car1 = ElectricCar("Tesla", "S5", "85kWh")
print(my_electric_car1.brand)
print(my_electric_car1.model)
print(my_electric_car1.fuel_type())
print('')
#---------------------------------------------------------------
#                    Problem 6
#---------------------------------------------------------------
# Add a class variable to Car that keeps track of the number of cars created.
class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return f"{self.brand}"
    def full_name(self):
        return f"{self.brand} + {self.model}"
print("Problem 6")
my_car1 = Car("Honda", "Civic")
print(my_car1.brand)
print(my_car2.model)
print("Total: ", Car.total_car)
my_car2 = Car("Toyota", "Corolla")
print(my_car2.brand)
print(my_car2.model)
print("Total: ", Car.total_car)
my_car3 = Car("Tesla", "S5")
print(my_car3.brand)
print(my_car3.model)
print("Total: ", Car.total_car)
#---------------------------------------------------------------
#                    Problem 7
#---------------------------------------------------------------
# Add a static method to the Car class that returns a general description of a car.
class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1
    
    def full_name(self):
        return f"{self.brand} + {self.model}"
    def fuel_tyepe(self):
        return f"Petrol or diesel"
    def get_brand(self):
        return f"{self.brand}"
    @staticmethod
    def get_description():
        return "Cars are a mean of transport"

print("Problem 7")
my_car1 = Car("Honda", "Civic")
print(my_car1.brand)
print(my_car1.model)
print("Total cars: ", Car.total_cars)
print(Car.get_description())
# Class can access get_description() method which is a static method but 
# objects can't access this method
print('')
#---------------------------------------------------------------
#                     Problem 8
#---------------------------------------------------------------
# Use a property decorator in the Car class to make the model attribute read-only.
class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_cars += 1

    def get_brand(self):
        return f"{self.brand}"
    
    def full_name(self):
        return f"{self.brand} + {self.__model}"
    @staticmethod
    def get_description(self):
        return f"{self.brand}" 
    # Class can access get_description() method which is a static method but 
    # objects can't access this method

    @property
    def model(self):
        return self.__model
    # The Python property decorator makes attributes in a class act like read-only properties.
    # Essentially, it lets you access methods as if they were attributes, without needing to write parentheses.

print('Problem 8')
my_car1 = Car('Honda', 'Civic')
print(my_car1.brand)
print(my_car1.model)
print(my_car1.full_name)
print(my_car1.get_description)
print(my_car1.model)
print('')
#---------------------------------------------------------------
#                     Problem 9
#---------------------------------------------------------------
# Demonstrate the use of isinstance() to check if my_tesla is an
# instance of Car and ElectricCar.
class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def full_name(self):
        return f"{self.brand} + {self.model}"
    def get_description(self):
        return "Cars are a means of transport."
    def fuel_type(self):
        return "Petrol or diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

print('Problem 9')
my_electric_car1 = ElectricCar("Tesla", "S5", "85 kWh")
print('Is my_electic_car1 an instance of the Car class?: ', isinstance(my_electric_car1, Car))
print('Is my_electric_car1 an instance of the ElectricCar class?', isinstance(my_electric_car1, ElectricCar))
print('')
#---------------------------------------------------------------
#                     Problem 10
#---------------------------------------------------------------
# Create two classes Battery and Engine, and let the ElectricCar 
# class inherit from both and Car class as well, demonstrating multiple inheritance.
class Battery:
    def battery_info(self):
        return "This is battery."
class Engine:
    def engine_info(self):
        return "This is engine."
class ElectricCar(Battery, Engine, Car):
    pass

my_electric_car1 = ElectricCar("Tesla", "S5")
print("Problem 10")
print(my_electric_car1.battery_info())
print(my_electric_car1.engine_info())