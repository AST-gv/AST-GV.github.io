from functools import lru_cache

@lru_cache(maxsize = 4)
def eight_queens(row, lst, memo):
    if row == -1:
        temp = ''
        lst.sort(key=lambda x:x[0])
        for element in lst:
            temp += f'{element[1] + 1}'
        memo.append(temp)
        return
    for i in range(8):
        for location in lst:
            if location[1] == i or abs(location[0] - row) == abs(location[1] - i):
                break
        else:
            eight_queens(row - 1, lst + [(row, i)], memo)

memo = []
eight_queens(7, [], memo)
memo.sort()
for _ in range(int(input())):
    print(memo[int(input()) - 1])