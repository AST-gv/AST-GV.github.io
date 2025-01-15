t=int(input())
for _ in range(t):print(min((n := int(input()))*min(col := list(map(int, input().split()))) + sum(row := list(map(int, input().split()))),(sum(col)+n*min(row))))

