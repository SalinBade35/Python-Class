# # sequence data type: list, tuple, range


# # list :
# # it a collection of data 
# # nature: 

# '''   
#  1. mutable : it can change
#  2. ordered : it has index value
#  3. duplicates: values can repeat
#  4. to declare a list:
 
#  variable_name = [] # square bracket, this declares the empty list
# '''
# # list_var = []



# # fruits = ['apple', 'banana', 'kiwi', 'orange', 'tomato', 'papaya', 'apple'] 
           
# # accessing the list

# # using indexes

# # print(fruits)
# # print(fruits[1])


# # slicing list

# #print(fruits[0:7:2])  # 0: starts from 0th index value
#                       # 7: till 6th index 
#                       # 1: gap
                      
# # print(fruits[ : : -1])   # from first to last with gap 1

# # modifying the list:


# # fruits = ['apple', 'banana', 'kiwi', 'orange', 'tomato', 'papaya', 'apple'] 

# # fruits[1] = 'coconut'
# # fruits[3] = 'watermelon'
# # print(fruits[1])

# # print(fruits)

# # checking the values in list using if statement

# # fruits = ['apple', 'banana', 'kiwi', 'orange', 'tomato', 'papaya', 'apple'] 

# # if 'Banana' in fruits:
# #     print('yes we have apple in the list')
# # else:
# #     print('no we do not have it in the list')

# # mutable = change + delete + add + replace

# # adding the item in the list
# # fruits = ['apple', 'banana', 'kiwi', 'orange', 'tomato']

# # # fruits.append('papaya')  # append() : to add the value in the existing one
# # # print(fruits)

# # fruits.insert(0, "beetroot")
# # print(fruits)

# # removing items from the list
# fruits = ['apple', 'banana', 'kiwi', 'orange', 'tomato']

# # fruits.pop()
# # print(fruits)

# # del fruits

# # # fruits.clear()
# # fruits.remove('apple')
# # print(fruits)

# # fruits.remove('orange')
# # print(fruits)


# # unpacking the list:

# # team1 = ['david', 'sam', 'tom', '123', '456']
# # x, y, z, a, b = team1

# # print(z)
# # print(b)

# x = [1,2,3]
# y = [4, 5, 6]

# z = x + y
# print(z)
# # x.extend(y)
# # print(x)

# # x = [1,2,3,4,5,6]

# sorting
attendance1 = ['dave', 'ashraya', 'sam', 'xenium', 'tulku']

attendance1.sort(reverse=1)
# print(attendance1)

# var2 = sorted(attendance1)
# print(var2)

# sort : values lai sort garera same variable mai values store garxa
# sorted: assigns sorted  values to new var



# list1 = list(range(100))
# print(list1)


# tuple : 
# nature: immutable, ordered
# tuple = ()

# fruits = ('apple', 'banana', 'kiwi', 'orange', 'tomato')
# print(len(fruits))

# print(fruits[0])

# x = () 



# list vs tuple : tuple is faster 

# range(n)

# 0 to n-1

# range(5) : 0 - 4
# range(100): 0 - 99




fruits = [1,2,3]
print(dir(fruits))

print(help(fruits))

