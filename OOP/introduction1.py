"""
everything can be object, but 
first we need to build class 

list, string, ... those were object

class: blueprint for creating objects

# creating class
class Classname:
    attribute1 = value1
    attribute2 = value2
    
    def __special_methods__(self, params):
        pass
        
    def Method1(self, params):
        pass
        
    def Method2(self, params):
        pass

"""

class Student:
    # attribute :
    """
    class attr: attr with this class has all same attribute (eg : name of college)
                : stored only once in meory hence efficient for common attr
                
    object attr : instance attr, every obj has different attr (eg: name of parents)
                : take different memory space
    
    obj attr > class attr : obj attr gets high priority
    """
    nationality = 'Nepali'
    college = 'ABC'
    name = None
    CGPA = None
    
    # constructors types: signature matters 
    
    # default constructor
    def __init__(self):
        print('New student is being added')
    
   
    # paramterized constructor
    def __init__(self, name, x):
        print(self)
        self.name = name # generally has same name (attr name and params)
        self.character = x
        
    """ methods are functions that belongs to objects"""
    def orientation_class(self):
        print('WELCOME STUDENTS') # you can also access attrs
    
S1= Student()
print(S1.roll) 

"""
__init__ function: 
executes when an object is created
always takes self as a parameter
self means reference to current object trying to use this method
both object and self shows same memory address

"""


"""
✅ Ways to Define Attributes in Python Classes

self.a = a      inside __init__	Constructor-based initialization
self.b = b      inside another method	Dynamic attribute creation
obj.b = value   Direct / dynamic attribute assignment (outside the class)	
setattr(object_name, attr_name, value)  Built in function

"""

"""
STATIC METHODS

A @staticmethod in Python is just like a global function, but grouped inside a class for organizational and logical purposes. It:
Doesn’t need self(so no instance or class is needed).
Can be called without creating an object.
Keeps related functions grouped with the class they belong to.

"""
class MathTools:
    @staticmethod
    def add(a, b):
        return a + b

print(MathTools.add(1,2))

"""
🧾 What is a Docstring?

A docstring is a string literal that you place right after the definition of a class, function, or module. It describes what the class/function/module does.

You write it using triple quotes (""" """ or ''' ''') inside the class body, immediately after the class line.

"""

class Person:
    """
    A class to represent a person.

    Attributes:
    ----------
    name : str
        The name of the person
    age : int
        The age of the person

    Methods:
    -------
    greet():
        Prints a greeting message with the person's name.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """Prints a greeting message."""
        print(f"Hello, my name is {self.name}.")


print(Person.__doc__) # prints those docstrings

# dunder function : consists double underscore __