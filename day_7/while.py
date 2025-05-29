# while loop
name = input('name:  ')

while name == '':
    print('entre name please!!!!!')
    name = input('name:  ')
    
print(f"your name is {name}")

age = int(input("entre you age:"))

while age < 0: # jaba samma yo condn true hunxa taba samma tala ko code execute
    print('warning: INVALID !!!!')
    age = int(input("entre you age:"))
    
print(f'DOB is {2025 - age}')
