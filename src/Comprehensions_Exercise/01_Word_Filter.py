words = input().split()
even_lengths = [word for word in words if len(word) % 2 == 0]
for w in even_lengths:
    print(w)
