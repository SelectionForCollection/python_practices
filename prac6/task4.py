def pair(head, tail):
    return lambda index: tail if index else head


def first(lst):
    return lst(0)


def rest(lst):
    return lst(1)


def make_list(*args):
    lst = None
    for x in reversed(args):
        lst = pair(x, lst)
    return lst


def list_to_string(lst):
    result = []
    while lst:
        result.append(str(first(lst)))
        lst = rest(lst)
    return ','.join(result)


def list_range(low, high):
    return make_list(*list(range(low, high + 1)))


def foldl(f, lst, acc):
    while lst:
        acc = f(acc, first(lst))
        lst = rest(lst)
    return acc


list_sum = lambda lst: foldl(lambda x, y: x + y, lst, 0)

fact = lambda n: foldl(lambda x, y: x * y, list_range(1, n), 1)  #8-e

lst = list_range(1, 10)
print(list_to_string(lst))

print(foldl(lambda x, y: x + y, lst, 0))
print(list_sum(list_range(1, 100)))
print(fact(5))
