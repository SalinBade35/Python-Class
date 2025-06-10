# # class classname:
# #     pass

# # objectname = classname()


# # class Details:
# #     def __init__(self, animal, group):
# #         self.animal = animal
# #         self.group = group
        
  
    
# # obj1 = Details("dog", 'mammal')

# # print(obj1.animal)


    


# class Student:
#     def __init__(self, n, r, g):
#         self.name = n
#         self.roll = r
#         self.grade = g
        
#         print(f'name = {self.name} ' )
#         print('roll = ', self.roll) 
#         print('grade = ', self.grade)   

    
# S1 = Student('Salin', '79', '10') # object is declared



# # class
# # object 
# # __init__
# # method/ function
# # attributes




# """
# encapsulation: TO HIDE UNDERLYING COMPLEXITY, PROVIDING EASE TO USER
# inheritance  : PARENT CLASS - CHILD CLASS 
# polymorphism : SAME NAME OF METHODS AND ATTRIBUTE

# CLASS : BLUEPRINT
# OBJECT : INSTANCE OF CLASS

# METHOD : AKA FUNCTIONS
# """


# class Animal:
#     def speak(self):
#         print("Animal can speak")
        
# class Dog(Animal):
#     def speak(self):
#         print("bark")
        
        

    
    
    
# Husky = Dog()
# Husky.speak()



    

class Student:
    name = None
    
    def __init__(x, mark):
        x. sum= 0
        x.l = len(mark)
        for i in mark:
            x.sum += i
    
    def show(x):
        print(x.sum/ x.l)
    
salin = Student([18, 19, 17, 20])
salin.show()
salin.name = "sa"
setattr(salin, 'roll', 35)
print(salin.roll)
