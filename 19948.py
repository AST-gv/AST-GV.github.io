n, m = map(int,input().split())
lst = sorted(map(int,input().split()))
minus = sorted([lst[i+1] - lst[i] for i in range(n - 1)], reverse = True)
print(lst[-1] - lst[0] - sum(minus[:m - 1]))