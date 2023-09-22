# while value <= 10:
#     print(value) Iterates through the loop 10 times
#     value += 1

# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# value = 0
# while value <= 10:
#     print(value)
#     value += 1
# else:
#     print("Value is now equal to " + str(value) + ".")

# For loop iterate over sequence of data collections like lists, tuples, dictionaries, sets or individual chars of a string

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# for a in "Mississipi":
#     print(a)

# for x in names:
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2, 4):
#     print(x)
# for x in range(5, 101, 5):
#     print(x)
# else:
#     print('Gland that\'s over!')

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

names = ["Dave", "Sara", "John", "Peter"]
actions = ["codes", "eats", "sleeps"]

for action in actions:
    for name in names:
        print(name + " " + action + " " + "at" + " " + time + ".")
