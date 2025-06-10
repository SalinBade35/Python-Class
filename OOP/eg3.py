
# # 3. Inheritance Example

# """
# class Parent:
#     # code
    
# class Child(Parent):
#     # code
# """

# class Vehicle:
#     def horn(self):
#         print("Beep Beep!")

# class Car(Vehicle):
#     def start(self):
#         print("InheritCar started")

# A = Car()

# A.start()
# A.horn()


# def simple_decorator(func):
#     def wrapper():
#         print(">> Before calling function")
#         func()
#         print(">> After calling function")
#     return wrapper

# @simple_decorator
# def greet():
#     print("Hello from decorator function!")

# greet()