#Python OOP basic concepts, data types and their use / Article by Gina Rubik 

#Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, 
#which can have attributes (data) and methods (functions). 


#1.Class: is a blueprint for creating objects. It defines a data structure and methods to operate on that data.

class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")

#2.Object: is an instance of a class which represents a real-world entity and has attributes and methods.
        
    laptop1 = Laptop("HP", "DELL")
    laptop2 = Laptop("EliteBook", "Inspiron")

    laptop1.display_info()  # Output: HP EliteBook
    laptop2.display_info()  # Output: DELL Inspiron 
   

#3.Encapsulation: refers to bundling data (attributes) and methods that operate on the data within a single unit (class).
#It helps in hiding the internal details of an object and exposing only what is necessary.
    
class Laptop:
    def __init__(self, brand, model):
        self._brand = brand  # Protected attribute
        self._model = model  # Protected attribute
        self._battery_percentage = 100  # Protected attribute

    def display_info(self):
        print(f"{self._brand} {self._model}, Battery: {self._battery_percentage}%")

    def use_laptop(self, hours):
        # Simulate battery usage
        self._battery_percentage -= hours * 5

        if self._battery_percentage <= 10:
            self._battery_percentage = 10
            print("Low Battery Warning: Charge your laptop!")

    # Protected method
    def _check_warranty(self):
        print(f"{self._brand} {self._model} - Warranty status: Valid")

# Example usage: Laptop class has protected attributes _brand, _model, and _battery_percentage, as well as a protected method _check_warranty. 
#Instances of this class (hp_laptop and dell_laptop) represent HP EliteBook and Dell Inspiron laptops, respectively. 
#The usage of the laptops demonstrates the encapsulation of data and behavior within the class.
            
hp_laptop = Laptop("HP", "EliteBook")
dell_laptop = Laptop("DELL", "Inspiron")

hp_laptop.display_info()  # Output: HP EliteBook, Battery: 100%
dell_laptop.display_info()  # Output: DELL Inspiron, Battery: 100%

hp_laptop.use_laptop(3)
dell_laptop.use_laptop(5)

hp_laptop.display_info()  # Output: HP EliteBook, Battery: 85%
dell_laptop.display_info()  # Output: DELL Inspiron, Battery: 75%


#4.Inheritance: allows a class (subclass/derived class) to inherit attributes and methods from another class (superclass/base class).
#It promotes code reusability and establishes an "is-a" relationship between classes. 

class GamerLaptop(Laptop):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

electric_car = GamerLaptop("ACME", "GamerPro", "100 kWh")
electric_car.display_info()  # Output: ACME, GamerPro

#5. Polymorphism: allows objects of different types to be treated as objects of a common type. It can be achieved through method overloading or method overriding.

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def animal_sounds(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

animal_sounds(dog)  # Output: Woof!
animal_sounds(cat)  # Output: Meow!








