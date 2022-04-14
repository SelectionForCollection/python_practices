import re


class Add:
    n = ""

    def __init__(self, a, b):
        self.n = "(" + a.toString() + " + " + b.toString() + ")"

    def toString(self):
        return self.n


class Num:
    def __init__(self, value):
        self.value = str(value)

    def __add__(self, other):
        return Num(self.value + str(other.value))

    def toString(self):
        return self.value


class Mul:
    n = ""

    def __init__(self, a, b):
        self.n = "(" + a.toString() + " * " + b.toString() + ")"

    def toString(self):
        return self.n


class PrintVisitor:

    def visit(self, f_ast):
        return f_ast.toString()


class CalcVisitor:

    def visit(self, f_ast):
        return eval(f_ast.toString())


class StackVisitor:
    n = ""

    def visit(self, f_ast):
        n = re.sub("[)( ]", "", f_ast.toString())
        self.n = n

    def get_code(self):
        flag = True
        result = []
        stack = []
        for element in self.n:
            if element not in '+-*/':
                if flag:
                    result.append("PUSH " + element)
                else:
                    result.append(result.pop() + element)
                flag = False
            else:
                flag = True
                stack.append(element)
        for e in reversed(stack):
            if e == "+":
                e = "ADD"
            elif e == "*":
                e = "MUL"
            result.append(e)
        return '\n'.join(result)


ast = Mul(Num(123), Mul(Num(12), Add(Num(7), Mul(Num(3), Num(2)))))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code())
