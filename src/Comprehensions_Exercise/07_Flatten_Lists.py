input_line = input().split("|")
opposite_list = input_line[::-1]

nums = [[num for num in item.split()] for item in opposite_list]

flat = [num for row in nums for num in row]
print(' '.join(flat))

'''
line = input()
flat = [el for x in line.split("|")[::-1] for el in x.split() if el != ""]
print(" ".join(flat))
'''