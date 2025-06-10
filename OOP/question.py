# class A:
#     def A(self):
#         print('A')
        
# A = A()
# A.A()

class A:

    def a(self, x, y):
        print('function 1 ')
        
    def a(self):
        print('function2')
        
b = A()
# b.a(1,2)
setattr(b, 'b', "value")
print(b.b)

# notes: Python is dynamically typed, and functions are objects that can be redefined. When you define multiple functions with the same name, the last definition simply overwrites the previous ones.

class MathTools:
    @staticmethod
    def add(a, b):
        return a + b

print(MathTools.add(1,2))


class Sam:
    def __init__(self, biscuit):
        print('hi biscuits first, this is your work')
        
    # def __init__(self):
    #     print('here is your work ')
        

Salin = Sam('here is you biscuit')

# this caused problem cause we can't overload functions in python


print("----------------------------\n")

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


print("-------------------------------------\n")

class A:
    def show_A(self):
        print("A class")

class B(A):
    def show(self):
        print("B class")
        
class C(A):
    def show(self):
        print("C class")

class D(C, B):  
    def show_D(self):
        print("D class")

d = D()
d.show()

# The output is C class because while inheriting, C comes first.
# Python follows the Metho Resolution Order(MRO) which goes from left to right in the class definition. The method from the first parent class listed will be executed. 

# To bypass MRO, and call function of B even though order is first C then B, we need to explicitly call B's method. It can be called as follows:
d=D()
B.show(d)
# This passes the object d as self parameter to class B's function show().Pthon does not check the MRO in thos case-it directly runs B.show() with d as the instance.

# We use explicit calling when we need to bypass MRO or super(). It is needed when both parent classes have same method name and we want to use a specific one.


