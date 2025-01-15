from functools import lru_cache

@lru_cache(maxsize = None)
def find(nums):
    if len(nums) == 1:
        return abs(nums[0] - 24) < 0.0000001

    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            a = nums[i]
            b = nums[j]
            remaining_nums = []

            for k in range(len(nums)):
                if k != i and k != j:
                    remaining_nums.append(nums[k])

            if find(tuple(remaining_nums + [a + b])) or find(tuple(remaining_nums + [a * b])):
                return True

            if a > b and find(tuple(remaining_nums + [a - b])):
                return True

            if a < b and find(tuple(remaining_nums + [b - a])):
                return True

            if a != 0 and find(tuple(remaining_nums + [b / a])):
                return True

            if b != 0 and find(tuple(remaining_nums + [a / b])):
                return True
            return False

while True:
    card = [int(x) for x in input().split()]
    if sum(card) == 0:
        break
    print('YES' if find(tuple(card)) else 'NO')
