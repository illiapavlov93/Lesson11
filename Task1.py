def supress(f):
    def wrapper(a, b):
        try:
            res = f(a, b)
        except ZeroDivisionError as e:
            return e
        return res
    return wrapper


@supress
def div(a, b):
    return a / b


print(div(10, 0))
