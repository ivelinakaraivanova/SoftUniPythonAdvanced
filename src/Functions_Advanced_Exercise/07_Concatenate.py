def concatenate(*args):
    result = ''
    for s in args:
        result += s
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
