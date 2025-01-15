n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
a = max(lst)
zhc = [0] * a
zhc[0] = 1
zhc[1] = 2
for i in range(2,a):
    zhc[i] = (zhc[i-2] + 2 * zhc[i-1]) % 32767
for num in lst:
    print(zhc[num - 1])
