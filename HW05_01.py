from itertools import permutations

lst = [''.join(p) for p in permutations('ABC')]
print(lst)

import itertools

# ABC => ABC, ACB, BAC, BCA, CAB, CBA
s = input() # "AB"
s = set(s)
s = sorted(s)
perm = list(itertools.permutations(s))

result=[''.join(row) for row in perm]

print(result)
