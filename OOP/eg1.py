class Student:
    """ purpose""" # docstring
    college = "Sagarmatha College" # class attribute
    
    def __init__(self, x, y):
        print("A new student is being added !!!!!")
        self.name = x
        self.roll = y
        
    def marks(self):
        print("result")
        
    def show_info(self, contact):
        self.contact = contact
        print(self.contact)
        print(self.name)
        print(self.roll)
    
B1 = Student("Sam", 1)
B1.name = "xenium"
print(B1.name)
B1.show_info(123)
# setattr(objectname, attr, value)
# setattr(B1, 'age', 20)



# class Math:
#     """ this class is meant for solving math"""
#     @staticmethod
#     def add(a, b):
#         return a + b
    
#     @staticmethod
#     def sub(a,b):
#         return a-b

# print(Math.add(1,2))
# print(Math.sub(1,2))
        
   
# # 

