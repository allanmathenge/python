# Lambda function is a single function that returns a value

from functools import reduce
def squared(num): return num * num
# squared = lambda num: num * num print(squared(2))


print(squared(2))


def add_two(num): return num + 2
# add_two = lambda num: num + 2 print(add_two(12))


print(add_two(12))


def sum_total(num1, num2): return num1 + num2
# sum = lambda num1, num2: num1 + num2 print(sum(5, 5))


print(sum_total(5, 5))


def sum_total(a, b): return a + b
# sum = lambda a, b: a + b print(sum(4, 5))


print(sum_total(4, 5))

#####################################


def fun_builder(x):
    return lambda num: num + x


add_ten = fun_builder(10)
add_twenty = fun_builder(20)

print(add_ten(7))
print(add_twenty(7))

#####################################

# Higher order functions --> takes in one or more functions as arguments or a function that returns another function as result


numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

########################################


odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))


numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))

names = ['Allan Mathenge', 'Sara Ito', 'John Jacob jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
