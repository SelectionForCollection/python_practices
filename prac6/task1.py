def deriv(f, dx=0.001):
    return lambda x: (f(x + dx) - f(x)) / dx


def f3(x):
    return x ** 3


print(deriv(lambda x: x ** 3)(5))
