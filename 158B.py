from collections import Counter
from math import ceil
n = int(input())
lst = map(int,input().split())
dic = Counter(lst)
zhc = dic[3] + dic[4]
if dic[2] % 2 == 0:
    zhc += dic[2] // 2
    if dic[3] < dic[1]:
        zhc += ceil((dic[1] - dic[3]) / 4)
else:
    zhc += dic[2] // 2 + 1
    if dic[3] + 2 < dic[1]:
        zhc += ceil((dic[1] - dic[3] - 2) / 4)
print(zhc)