# r = Read
# a = Append
# w = Write
# x = Create

# **Read** -> Error is raised if the file does not exist

import os
f = open("names.txt")
# print(f.read()) - Reads everything in file
# print(f.read(9)) - Reads the first 9 characters
# print(f.readline()) - Reads the first line
# print(f.readline()) - Reads the second line
# print(f.readline()) - Reads the third line
# print(f.readline()) - Reads the forth line

for x in f:
    print(x)  # print every line contained in the file

f.close()

# Read- Is the default value after open command
try:
    f = open("names.txt")
    print(f.read())
except:
    print('The file you want to read does not exist!')
finally:
    f.close()

# Append - Creates the file if it does not exist
f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (Overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the contexts!")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing with "w" permission or creates a file if it does not exist

f = open("name_list.txt", "w")
f.write("I am the new file created -> name_list.txt")
f.close()

f = open("name_list.txt")
print(f.read())
f.close()

# Creates the specified file but returns an error if the file already exists. "x" command stands for create

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file. Avoid an error if the file exists

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
    print("dave.txt file was deleted")
else:
    print("The file you wish to delete does not exist!")

# "with" keyword

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
