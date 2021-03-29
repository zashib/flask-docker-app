def fun_a(x):
    return x ** 2


def fun_b(x):
    return 2 * x + 1


def fun_c(x):
    return x - 1


def fun_d(x):
    return x / 10


def fun_e(x):
    return x + 10


def fun_f(x):
    return x / 2


# sequence of function names
SEQUENCE = [name for (name, obj) in vars().items() if hasattr(obj, "__class__")
            and obj.__class__.__name__ == "function"]

if __name__ == '__main__':
    print(SEQUENCE)
