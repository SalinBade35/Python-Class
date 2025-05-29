# nested loop: it mean loop inside loop

# table = 3
# dishes = ['rice', 'dal', 'curry']

# for table in range(1, table+1):
#     print('serving table', table)
#     for dish in dishes:
#         print('-', dish)
        
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} X {j} = {i*j}")

        
