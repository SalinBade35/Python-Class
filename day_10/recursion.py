# recursion

# factorial number 
# 3! = 3*2*1 = 6
# 5! = 5*4*3*2*1= 120
# 100! = 100 * 99 * 98 * ........... 1= ..
# 1! = 1
# 0! = 1
def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return(n * factorial(n -1)) 
  
              
# print(factorial(5))

# recursion: direct, indirect


def a1():
    print('i am a1')
    
    
def a2():
    print('i am a2')
    a1()
    




a2()


