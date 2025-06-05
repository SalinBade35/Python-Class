# wap to count the total number of upper case and lower cases present in  a sentence.

def counter( sentence ):
    upper = 0
    lower = 0
    
    for i in sentence:
        if i.isupper():  
            upper += 1
        elif i.islower():
            lower += 1
            
    print(f' uppercases : {upper}\n lowercase : {lower}')
    

counter('i AM happy')

# var1 = 'i am happy'
#         0123456789
        
# print(var1[2]) # a
# print(var1[4]]) # whitespace