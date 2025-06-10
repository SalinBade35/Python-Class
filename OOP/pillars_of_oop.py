# ============================================
# OOP: Four Pillars Explained with Vehicle Example
# ============================================

# ============================================
# 1. ABSTRACTION
# --------------------------------------------
# Definition:
#   Hiding complex internal details and showing only the essential features.
# Why Needed:
#   - Reduces complexity
#   - Focuses on what it does, not how it does it
#   - Promotes cleaner code and better interface design

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Abstract Base Class for all vehicles.
    It defines the essential methods that all vehicles must implement.
    """
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started with key")

class Scooter(Vehicle):
    def start(self):
        print("Scooter started with kick")

# Usage
v1 = Car()
v1.start()     # Output: Car started with key

v2 = Scooter()
v2.start()     # Output: Scooter started with kick


# ============================================
# 2. ENCAPSULATION
# --------------------------------------------
# Definition:
#   Bundling attributes and methods into one unit (class).
#   Restricting direct access to some attributes.

# Why Needed:
#   - Protects internal state
#   - Prevents unintended modifications

class CarEncapsulated:
    def __init__(self):
        self.__engine_status = "off"  # private attribute

    def start_engine(self):
        self.__engine_status = "on"

    def get_engine_status(self):
        return self.__engine_status

# Usage
c = CarEncapsulated()
c.start_engine()
print(c.get_engine_status())  # Output: on
# print(c.__engine_status)    # ❌ Will cause error (private attribute)


# ============================================
# 3. POLYMORPHISM
# --------------------------------------------
# Definition:
#   Ability to use the same method name in different classes,
#   with different behaviors.
# Why Needed:
#   - Code flexibility
#   - Consistent interfaces
#   - Less duplication

class Car:
    def move(self):
        print("Car is moving on four wheels")

class Scooter:
    def move(self):
        print("Scooter is moving on two wheels")

# Function that uses polymorphism
def test_drive(vehicle):
    vehicle.move()

# Usage
c = Car()
s = Scooter()

test_drive(c)  # Output: Car is moving on four wheels
test_drive(s)  # Output: Scooter is moving on two wheels


# ============================================
# 4. INHERITANCE
# --------------------------------------------
# Definition:
#   Allows one class to inherit attributes and methods from another class.
# Why Needed:
#   - Code reuse
#   - DRY principle
#   - Easier maintenance and extension

class VehicleBase:
    def horn(self):
        print("Beep beep!")

class CarInherit(VehicleBase):
    def start(self):
        print("Car starting...")

class ScooterInherit(VehicleBase):
    def start(self):
        print("Scooter starting...")

# Usage
car = CarInherit()
car.start()    # Output: Car starting...
car.horn()     # Output: Beep beep! (inherited)

scooter = ScooterInherit()
scooter.start()  # Output: Scooter starting...
scooter.horn()   # Output: Beep beep! (inherited)

# Super(): To reuse code from the parent class.
#        : To initialize parent attributes from child class.

class Parent:
    def __init__(self, a):
        self.a = a

class Child(Parent):
    def __init__(self, a, b):
        super().__init__(a)  # Call Parent’s constructor
        self.b = b

"""
=============================================
🧠 TYPES OF INHERITANCE IN PYTHON (OOP)
=============================================

Inheritance allows a class (child/derived) to inherit attributes and methods from another class (parent/base).

Types of inheritance:
    1️⃣ Single Inheritance
    2️⃣ Multiple Inheritance
    3️⃣ Multilevel Inheritance
    4️⃣ Hierarchical Inheritance
    5️⃣ Hybrid Inheritance
"""

# ---------------------------------------------------
# 1️⃣ SINGLE INHERITANCE
# One child class inherits from one parent class
# ---------------------------------------------------

class Vehicle:
    def show_type(self):
        print("I am a vehicle")

class Car(Vehicle):
    def brand(self):
        print("Brand: Tesla")

c = Car()
c.show_type()  # Inherited method
c.brand()

# ---------------------------------------------------
# 2️⃣ MULTIPLE INHERITANCE
# One child class inherits from multiple parent classes
# ---------------------------------------------------

class Engine:
    def engine_type(self):
        print("Electric Engine")

class Wheels:
    def wheel_count(self):
        print("4 wheels")

class ElectricCar(Engine, Wheels):
    def model(self):
        print("Model: Tesla Model S")

e = ElectricCar()
e.engine_type()
e.wheel_count()
e.model()

# ---------------------------------------------------
# 3️⃣ MULTILEVEL INHERITANCE
# Child inherits from Parent, and Grandchild inherits from Child
# ---------------------------------------------------

class Animal:
    def category(self):
        print("Category: Animal")

class Mammal(Animal):
    def subcategory(self):
        print("Subcategory: Mammal")

class Dog(Mammal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.category()
d.subcategory()
d.sound()

# ---------------------------------------------------
# 4️⃣ HIERARCHICAL INHERITANCE
# Multiple child classes inherit from a single parent
# ---------------------------------------------------

class Parent:
    def message(self):
        print("This is the parent class")

class Child1(Parent):
    def child1_method(self):
        print("Child1 functionality")

class Child2(Parent):
    def child2_method(self):
        print("Child2 functionality")

ch1 = Child1()
ch2 = Child2()

ch1.message()
ch2.message()

# ---------------------------------------------------
# 5️⃣ HYBRID INHERITANCE
# Combination of two or more types of inheritance
# (e.g., Multiple + Multilevel)
# ---------------------------------------------------

class A:
    def show_A(self):
        print("A class")

class B(A):
    def show_B(self):
        print("B class")

class C:
    def show_C(self):
        print("C class")

class D(B, C):  # Hybrid: D inherits from B (which inherits A) and C
    def show_D(self):
        print("D class")

d = D()
d.show_A()
d.show_B()
d.show_C()
d.show_D()

# -------------------------------
# ✅ END OF INHERITANCE TYPES
# -------------------------------



# ============================================
# Summary:
# --------------------------------------------
# Abstraction     → Hide details, show only essentials (via abstract class)
# Encapsulation   → Hide internal state, use getters/setters
# Polymorphism    → Same method name behaves differently across classes
# Inheritance     → Reuse parent class methods/attributes
