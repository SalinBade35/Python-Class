# argument : is sth that we pass when calling a function
# parameter : is sth that we declare while declaring a function

def greet(name): # this name is a parameter
    print(f'namaste {name}')
  
  
  
    
# greet('hoti')  # salin value is argument


# arugment:
'''

1. no arugment, no return
2. with argument, no return 
3. with arugment, with return
4. no argument, with return

'''

#1. NO ARGUMENT, NO RETURN:

def greet1():
    print('Namaste, Jojolapa, Goodmorning')
    
# greet1()

#2. W/ ARGUMENT, NO RETURN

def greet_this_guy(name):
    print(f' Namaste, Jojolapa, Goodmorning {name}')

# greet_this_guy('Salin')

#3. W/ ARGUMENT, W/ RETURN

def add(x, y):
    print(f'x: {x}')
    print(f'y: {y}')
    return x + y

# add(2,5)  # output: 7

# print(add(2,5))

# print(  add(3, 10)  )

def student(grade):
    print('i secured following mark , dad!')
    
    if grade == 'A':
        var1 = 100
    elif grade == "B":
        var1 = 50 
    else:
        var1 = 'Failed'
    return var1


print(student('A'))


# 4. NO ARGUEMENT / WITH RETURN

def PI():
    return 3.1415

# print(PI())

var1 = PI()

# print(var1)

