def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1} раз".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper


@counter
def wel_wel(x):
    match x:
        case 1:
            return "By My Shaggy Bark"
        case 2:
            return "kraB yggahS yM yB"
        case _:
            return "Frome See To Shore"


for i in range(0, 10):
    print(wel_wel(i))
