phone_book = {}

while True:
    line = input()
    if line.isdigit():
        n = int(line)
        break
    name, phone_number = line.split('-')
    phone_book[name] = phone_number


for _ in range(n):
    search_name = input()
    if search_name not in phone_book:
        print(f"Contact {search_name} does not exist.")
    else:
        print(f"{search_name} -> {phone_book[search_name]}")
