x = 10


def my_function():
    x = 20
    print(x)  # local x
    print(globals()['x'])  # global x


my_function()
