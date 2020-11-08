from pyfiglet import figlet_format


def encrypt(text):
    result = figlet_format(text)
    return result


text = input()
print(encrypt(text))
