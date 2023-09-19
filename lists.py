users = ['Allan', 'Mary', 'Sarah']

data = ['Allan', 42, True]

emptylist = []

print('Allan' in emptylist)
print(data[0])
print(users[-2])
print(users.index('Sarah'))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))
users.append('Paul')
print(users)

users += ['Jason']
print(users)
users.extend(['Robert', 'Jim'])
print(users)

# users.extend(data)
# print(users)

# inserting data in specific position in a list
users.insert(0, 'Bob')
print(users)

# At the second position
users[2:2] = ['Eddie', 'Alex']
print(users)

# Replace values aka slice
users[1:3] = ['Robert', 'JPJ']
print(users)

# Remove methods
users.remove('Bob')
print(len(users))

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['allan']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 34, 24, 1, 45]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)

print(type(nums))

mylist = list([0, 'Neil', True])
print(mylist)

# Tuples

mytuple = tuple(('Dave', 42, True))  # using constructor
anothertuple = (1, 2, 2, 2, 3, 7, 4)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(*one, two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.index(2))
