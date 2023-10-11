class Just_not_cool_error(Exception):
    pass


x = 2
try:
    raise Just_not_cool_error('This just isn\'t cool, man!')
    # raise Exception('I am a custom exception!')
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed!")
except NameError:
    print('NameError means something is undefined!')
except ZeroDivisionError:
    print('Please do not devide by zero')
except Exception as error:
    print(error)
else:
    print('No Errors')
finally:
    print('I am going to print with or without an Error!')
