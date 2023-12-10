'''This program so the existance e in real life. '''


import random

print("Please Enter number of samples you want! :")
k = int(input())
L = []

for i in range(k):
    L.append([])

for i in range(k):
    random_index = random.randint(0, k-1)
    L[random_index].append(0)

#print(L)

empty = [x for x in L if len(x) == 0]

#print(empty)

total_buckets = len(L)
empty_ratio = len(empty) / total_buckets

print(f"Ratio of empty sublists to total buckets: {empty_ratio}")
if empty_ratio != 0:
    reciprocal_ratio = 1 / empty_ratio
    print(f"Reciprocal of the ratio: {reciprocal_ratio}")
else:
    print("Reciprocal ratio is undefined when the ratio is 0.")
