import math
# string data types

# literal assignment
first = "Allan"

last = "Mathenge"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)
fullname += " " + "Kamau"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = """
hey, how are you?

I was just checking in.
                            All good?

"""
print(multiline)

# Escaping special characters

sentence = 'I\'m back at work!\tHey\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                             "
multiline = "                                              " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$3".rjust(4))

# String index values
print("")
print(first[-5])
print(first[-4])
print(first[-3])
print(first[-2])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods  return Boolean

print(first.startswith("A"))
print(first.endswith("x"))

# Boolean data types
print("")
myvalue = True
x = bool(False)  # contructor
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# Integer type
price = 100
best_price = int(100)
print(type(price))
print(isinstance(best_price, int))

# Float type: have decimals
print("")
gpa = 3.28
y = float(1.14)
print(type(gpa))

# Complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print("")
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to an integer
print("")
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Throws error if you attempt to cast incorrect data
# zip_value = int("Allan")

x = 3
y = 8
y *= x
print(y)
