from itertools import permutations
n = int(input())
lst = [int(x) for x in input().split()]
permutation = set(permutations(lst))
for perm in permutation:
    print(*perm, sep=' ')