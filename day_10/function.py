# function :
# block of code - sp. task - unique name - when called - it get executed

# two types:
"""
1. inbuilt function : print(), len(), type()

2. user defined function : defined and built by the user for their sp. need
"""


# def function_name(parameters):
#     # code :functions
    
# function_name(arguments)

def greet(name) : # parameter
    print(f"namaste {name}")
    
# greet('David') # argument


# function argument
"""
1. default argument
2. keyword argument
3. required argument
4. variable length argument
"""

# default argument

# def biodata(fname, lname = "JBR", address = 'Nepal'): # 3 params
#     print(f"bio  data\n fname : {fname}\n lname: {lname}\n address: {address}")
    
# biodata('lagankhel') 

# biodata('Makkhan Tole', 'Manandhar', 'abc')


# keyword argument:

# def biodata(fname = 'XYZ', lname = "JBR", address = 'Nepal'): # 3 params
#     print(f"bio  data\n fname : {fname}\n lname: {lname}\n address: {address}")
    
# biodata(address = 'lgn', fname = 'Salin') 



# required argument:

# def biodata( x, y, z): # 1 params
#     print(f"bio  data\n DOB: {DOB}\nfname : {fname}\n lname: {lname}\n address: {address}")
    
# biodata('JUDDHA', 'JBR', 'NEPAL', 1080 ) 

# def add(a,b,c,d,e,f):
#     var1 = a+b+c+d+e+f
#     print(var1)

# add(1,1,1,1,1,1)

# variable length argument
# args and kwargs 

# args: - position argument
# def functionname(*params_for_agrs) :
    # code
    
    
# def greet(*name):
#     print(f"hello {name}")
    
# greet('Salin', 'David', 'Symphony', 'ram', 'sita', 'gita')
     
    
   
    
# kwargs: keyword argument
# def functionname(**params_for_kwargs) :
    # code




def name(**name):
   print("hello", name)

name(team1 = "che", team2= "RM", team3 = "hafjkld")




    
    
     



