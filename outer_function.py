def outer_function(x):
    def inner_function(factor):
        return x * factor
    print(inner_function(10))


outer_function(5)
