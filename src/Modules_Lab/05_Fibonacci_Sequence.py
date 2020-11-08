import fibonacci

sequence = []

while True:
    split_line = input().split()
    command = split_line[0]
    if command == 'Stop':
        break
    elif command == "Create":
        n = int(split_line[2])
        sequence = fibonacci.create_sequence(n)
        print(' '.join([str(x) for x in sequence]))
    elif command == "Locate":
        number = int(split_line[1])
        try:
            pos = sequence.index(number)
            print(f"The number - {number} is at index {pos}")
        except ValueError:
            print(f"The number {number} is not in the sequence")
