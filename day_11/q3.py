# wap to sum all the integer value present in a list using function

def total_sum( list1 ):
    sum = 0
    for i in list1:
        print(f" sum = {sum} + {i}")
        sum = sum + i # sum = 0 + 1 = 1 -> sum = 1
                    # sum = 1 + 2 = 3 -> sum = 3
                    # sum = 3 + 1 = 4 -> sum = 4
    return sum
        


x = [1,2,1, 10, 20, 2, 77, 889, 1] 

print(total_sum(x))
