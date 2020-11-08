numbers = [int(x) for x in input().split()]

positive_numbers = [x for x in numbers if x > 0]
negative_numbers = [x for x in numbers if x < 0]
sum_positives = sum(positive_numbers)
sum_negatives = sum(negative_numbers)


print(sum_negatives)
print(sum_positives)

if abs(sum_negatives) > sum_positives:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")