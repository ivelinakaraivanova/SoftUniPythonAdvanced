import re

with open('D:/Iva/Python Advanced/Materials/Exercises/08-File-Handling-Lab-Resources/Words Count/words.txt', 'r') as word_file:
    words = word_file.read().split()

with open('D:/Iva/Python Advanced/Materials/Exercises/08-File-Handling-Lab-Resources/Words Count/text.txt', 'r') as input_file:
    text = input_file.read()

words_occurrences = {}

for word in words:
    matches = re.findall(rf'[\s-]({word})[\s,.!?]', text, re.MULTILINE + re.IGNORECASE)
    words_occurrences[word.lower()] = len(matches)

with open('D:/Iva/Python Advanced/Materials/Exercises/08-File-Handling-Lab-Resources/Words Count/output.txt', 'w') as output_file:
    for word, occurrences in sorted(words_occurrences.items(), key=lambda x: -x[1]):
        print(f'{word} - {occurrences}', file=output_file)
