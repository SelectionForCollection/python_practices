class Main:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def first(self):
        return self.x + self.y

    def second(self):
        return 'что?'


obj = Main(32, 2)
print(vars(obj))
while True:
    print('Введите название метода или же exit для завершения работы')
    s = input()
    if s == 'exit':
        break
    print(getattr(obj, s)())
