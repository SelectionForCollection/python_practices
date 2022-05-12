""" >>> deriv(lambda x: x ** 3)(5) 75.00014999664018 """

def deriv(f, dx=0.001):
    return lambda x: (f(x + dx) - f(x)) / dx


print(deriv(lambda x: x ** 3)(5))
