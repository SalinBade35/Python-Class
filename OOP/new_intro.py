"""
===============================
🧠 PYTHON OOP CONCEPTS TUTORIAL
===============================

👉 Everything in Python is an object (list, string, int, etc.)

But to create your own custom object,
first, you need to build a **class**.

A class is a blueprint for creating objects.
It defines attributes and methods the object will have.

"""

# ---------------------------
# ✅ Class Syntax
# ---------------------------

"""
class ClassName:
    class_attribute = value

    def __init__(self, parameters):
        # instance attributes
        self.attr1 = param1
        self.attr2 = param2

    def method1(self):
        pass

    def method2(self, param):
        pass
"""

# ----------------------------------
# 🎓 Class Example: Student
# ----------------------------------

class Student:
    """
    Attributes:
    ----------
    - Class Attributes (shared by all instances)
    - Instance/Object Attributes (unique to each object)

    Priority:
    ----------
    If both class and instance attributes exist with the same name,
    instance attributes take precedence.
    """

    # Class Attributes (shared by all)
    nationality = 'Nepali'
    college = 'ABC'

    # Constructor Overloading: Only the last defined __init__ is valid
    def __init__(self, name, character):
        """
        Constructor: gets called when object is created
        `self` refers to the current instance (object)
        """
        print("Memory location of object:", self)
        self.name = name
        self.character = character

    def orientation_class(self):
        """Instance Method"""
        print("WELCOME STUDENTS")


# Object creation (will call the constructor)
S1 = Student("Salin", "Hardworking")
print("Name:", S1.name)
print("Nationality (Class Attribute):", S1.nationality)

"""
✅ Ways to Define Attributes in Python Classes

1. self.a = a
   ➤ Inside __init__ → constructor-based

2. self.b = b
   ➤ Inside another method → dynamic attribute creation

3. obj.b = value
   ➤ Outside the class → on-the-fly attribute assignment

4. setattr(obj, attr_name, value)
   ➤ Using built-in function
"""

# Example:
S1.roll = 101  # Dynamic attribute assignment
print("Roll:", S1.roll)

setattr(S1, 'section', 'A')
print("Section:", S1.section)

# -------------------------------
# 🔸 STATIC METHODS
# -------------------------------

"""
A @staticmethod:
- Doesn’t take self or cls
- Can be called using class name (no need to create object)
- Used when logic belongs to class but doesn’t need object state
"""

class MathTools:
    """Example of using static method for utility"""

    @staticmethod
    def add(a, b):
        return a + b

print("Sum:", MathTools.add(5, 10))  # Static method call

# -----------------------------------
# 🔹 DOCSTRINGS
# -----------------------------------

"""
A docstring is:
- A multi-line string inside a class/function/module
- Explains what it does
- Can be accessed using ClassName.__doc__ or help(ClassName)
"""

class Person:
    """
    A class to represent a person.

    Attributes:
    ----------
    name : str
    age : int

    Methods:
    -------
    greet(): Prints greeting message with the name.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """Prints a greeting message."""
        print(f"Hello, my name is {self.name}.")

print(Person.__doc__)  # Shows class docstring

# -----------------------------------------
# 🎯 Four Pillars of OOP in Python
# -----------------------------------------

"""
1️⃣ Abstraction
   - Hiding internal implementation and showing only what’s necessary
   - Achieved using abstract base classes

2️⃣ Encapsulation
   - Wrapping data and methods in a single unit
   - Hiding internal details using private attributes

3️⃣ Inheritance
   - One class (child) inherits attributes/methods of another (parent)

4️⃣ Polymorphism
   - Same method name behaves differently based on object
"""

# 1. Abstraction Example
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):   
        print("Car starts with key")

class Scooter(Vehicle):
    def start(self):
        print("Scooter starts with kick")

v1 = Car()
v1.start()

# 2. Encapsulation Example
class EncapsulatedCar:
    def __init__(self):
        self.__engine = "OFF"  # private attribute

    def start_engine(self):
        self.__engine = "ON"

    def get_engine_status(self):
        return self.__engine

car = EncapsulatedCar()
car.start_engine()
print("Engine:", car.get_engine_status())

# 3. Inheritance Example
class VehicleBase:
    def horn(self):
        print("Beep Beep!")

class InheritCar(VehicleBase):
    def start(self):
        print("InheritCar started")

ic = InheritCar()
ic.start()
ic.horn()

# 4. Polymorphism Example
class CarPoly:
    def move(self):
        print("Car is moving on 4 wheels")

class ScooterPoly:
    def move(self):
        print("Scooter is moving on 2 wheels")

def test_drive(vehicle):
    vehicle.move()

test_drive(CarPoly())
test_drive(ScooterPoly())

# -----------------------------------------
#  Decorator Example
# -----------------------------------------

"""
Decorators are used to modify the behavior of a function or method.
Can be used to log, authenticate, authorize, etc.
"""



def simple_decorator(func):
    def wrapper():
        print(">> Before calling function")
        func()
        print(">> After calling function")
    return wrapper

@simple_decorator
def greet():
    print("Hello from decorator function!")

greet()

