def fun1(): 
    return 7

# var1 = fun1()
# print(var1)
# fun1()
# print(fun1())

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return(num * factorial(num-1))
    
print(factorial(5))