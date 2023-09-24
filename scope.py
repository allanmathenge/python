# Global scope

name = "Allan"
count = 1


def another():
    color = "Blue"
    global count
    count += 1
    print(count)

    def greeting():
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting()


another()
