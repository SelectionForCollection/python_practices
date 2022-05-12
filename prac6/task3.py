def Add(x, y):
    return ('Add', x, y)


def Mul(x, y):
    return ('Mul', x, y)


def Num(x):
    return ('Num', x)


def calc(ast):
    match ast:
        case ('Add', x, y):
            return calc(x) + calc(y)
        case ('Mul', x, y):
            return calc(x) * calc(y)
        case ('Num', x):
            return x


ast = Add(Num(7), Mul(Num(3), Num(2)))

print(ast)
print(calc(ast))
