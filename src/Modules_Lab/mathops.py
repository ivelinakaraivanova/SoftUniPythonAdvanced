import operator


def get_input(string):
    n1, sign, n2 = string.split()
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
    }[sign]
    return float(n1), operations, int(n2)


def exec(n1, oper, n2):
    return oper(n1, n2)
