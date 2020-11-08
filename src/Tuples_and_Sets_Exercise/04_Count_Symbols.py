text = input()

occurrences = {}

for ch in text:
    if ch not in occurrences:
        occurrences[ch] = 1
    else:
        occurrences[ch] += 1

sorted_occurrences = sorted(occurrences.items(), key=lambda x: x[0])

for ch, times in sorted_occurrences:
    print(f"{ch}: {times} time/s")
