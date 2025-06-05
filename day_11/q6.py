# prime or not

def is_it_prime( n ) :
    if n < 2:  #- infinity to 1
        return False
    
    for i in range(2, int(n**0.5)+1): #2 to infinity 
        if n % i == 0:
            return False
    return True

# print(is_it_prime(100))

def prime1(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

if prime1(10):
    print("prime")
else:
    print("nope")