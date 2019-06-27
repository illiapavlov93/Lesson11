def intercept(*args):
    def supress(f):
        def wrapper(a, b):
            try:
                res = f(a, b)
            except args as e:
                return e
            return res
        return wrapper
    return supress


@intercept(ZeroDivisionError)
def div(a, b):
    return a / b


print(div(10, 0))


@intercept(TypeError)
def div(a, b):
    return a / b


print(div(10, 'a'))
