# dictionary : key value pair, mutable : add, remove, delete, no duplicate

# key - value

info = {
    'name': 'David',
    'age': 20,
    'eligible' : True
}
# print(info)
# print(info.values())
# print(info.keys())
# print(info.items())

# variable_name[key] = New_value

# info['age'] = 25
# print(info)

# info.update({'age': 100})

# info['DOB'] = 2004
# print(info)

# info.clear()

# info.pop('name')
# print(info)



# copy
info = {
    'name': 'David',
    'age': 20,
    'eligible' : True
}

new_dict = info.copy()
print(new_dict)


