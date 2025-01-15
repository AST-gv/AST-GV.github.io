n = int(input())
if n % 5 == 0 and n % 3 != 0:
    print(((3 * n) // 5-1) * 5)
else:
    print(((3 * n) // 5) * 5)