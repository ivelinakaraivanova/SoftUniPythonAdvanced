no_vowels_list = [s for s in input() if s not in ['a', 'o', 'u', 'e', 'i']]
no_vowels = ''
for s in no_vowels_list:
    no_vowels += s
print(no_vowels)
