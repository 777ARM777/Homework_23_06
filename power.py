def power_of(n):
    def power(number):
        return number**n
    return power


x = power_of(5)
print(x(2))
x = power_of(3)
print(x(5))
x = power_of(2)
print(x(12))

