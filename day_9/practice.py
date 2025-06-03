# wap to built a calculator

# + - *  /

def add(a,b):
    return a+b

def mul(a,b):
    return a+b

def div(a,b):
    return a+b

def sub(a,b):
    return a+b


a = int(input('a :'))
b = int(input('b: '))

print("option: ")
print(''' 
          1. +
          2. -
          3. *
          4. /''')

input = int(input('select: '))

if input == 1:
    print(add(a, b))
    
elif input == 2:
    print(sub(a, b))
    
elif input == 3:
    print(mul(a, b))

elif input == 4:
    print(div(a, b))
    
else:
    print('INVALID')
    
    

    
    

