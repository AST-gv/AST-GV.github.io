h = int(input())
m = int(input())
s = [0] * m
c = [0] * m
benefit = [0] * m
for i in range(m):
    s[i], c[i] = map(float, input().split())
    benefit[i] = (s[i] * c[i], 5 / s[i])
time = 2 * h - 0.5 * m
benefit.sort(reverse=True)
improvement = 0
for j in range(m):
    if time < benefit[j][1]:
        improvement += time * benefit[j][0]
        break
    time -= benefit[j][1]
    improvement += benefit[j][0] * benefit[j][1]
print(round(improvement, 1))