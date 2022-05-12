def pair(head, tail):
    return lambda index: tail if index else head

# 2-e
def first(lst):
    return lst(0)


# 2-e
def rest(lst):
    return lst(1)


# 3-e
def make_list(*args):
    lst = None
    for x in reversed(args):
        lst = pair(x, lst)
    return lst


# 4-e
def list_to_string(lst):
    result = []
    while lst:
        result.append(str(first(lst)))
        lst = rest(lst)
    return ', '.join(result)


# 5-e
def list_range(low, high):
    return make_list(*list(range(low, high + 1)))


# 6-e
def foldl(f, lst, acc):
    while lst:
        acc = f(acc, first(lst))
        lst = rest(lst)
    return acc


# 7-e
list_sum = lambda lst: foldl(lambda x, y: x + y, lst, 0)
# 8-e
fact = lambda n: foldl(lambda x, y: x * y, list_range(1, n), 1)
# 9-e
list_to_py = lambda lst: foldl(lambda x, y: x + y, lst, 0)
# 10-e
list_reverse = lambda lst: foldl(lambda x, y: pair(x, y), lst, None)


lst = list_range(1, 10)

print(list_to_string(lst))

print(foldl(lambda x, y: x + y, lst, 0))
print(list_sum(list_range(1, 100)))
print(fact(5))
print(list_reverse(list_range(1, 100)))
