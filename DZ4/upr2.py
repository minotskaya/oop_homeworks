arr = map(int, input().split())

def my_decorator(foo):
    def wrapper(arr):
        c = foo(arr)
        if c == 0:
            return 'нет('
        elif c > 10:
            return 'Очень много'
        else:
            return c
    return wrapper

@my_decorator
def foo(arr):
    c = 0
    for item in arr:
        if item % 2 == 0:
            c += 1
    return c

print(foo(arr))
