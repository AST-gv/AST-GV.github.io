from bisect import bisect_right

n = int(input())
price = sorted([int(x) for x in input().split()])
q = int(input())
money = [int(input()) for _ in range(q)]
output = []
for num in money:
    result = bisect_right(price, num)
    output.append(result)

print(*output, sep='\n')