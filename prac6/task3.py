def student(name, age):
    def func(key):
        if key == 'name':
            return name
        elif key == 'age':
            return age
    return func


def get(func, key):
    return func(key)


def replace(func, key, val):
    if key == 'name':
        return student(val, get(func, 'age'))
    elif key == 'age':
        return student(get(func, 'name'), val)


p1 = student(name='Иван', age=20)
p2 = replace(replace(p1, 'name', 'Алексей'), 'age', 21)


print(get(p2, 'name'))
