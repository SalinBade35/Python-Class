# # file open:

# pointer_var = open('filename.txt') # opens by default in read mode
# pointer_var = open('filename.txt', 'modes') # opens in specified mode

# # file close

# pointer_var.close()

# # file modes
# 'r' - read mode, not write
# 'w' = write mode, existing contents are cleared first then is overwritten
# 'a' = append mode, existing content as it is, lastly the contents are added
# 'x' = create mode, if already exists then shows error else creates the file 

# 'b' - binary mode 
# 't' - text file


# file = open('nf1.txt', 'x')

# file.write(' hello namaste ')
# # print(file.read())

# file.close()



# with open('nf1.txt', 'w') as f1:
#     f1.write("new content overwritten")

# with open('nf1.txt', 'r') as f2:
#     print(f2.read())

f = open('nf1.txt')
print(f.read(4))
print(f.read(2))

print(f.tell())
print(f.seek(0))
print(f.tell())

# for line in f:
#     print(line)

print(f.readlines())