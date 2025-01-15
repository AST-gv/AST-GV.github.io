s = input()
output = 1
for i in range(len(s)):
    zhc = 1
    for j in range(i, len(s) - 1):
        if int(s[j]) + int(s[j + 1]) == 1:
            zhc += 1
            if zhc > output:
                output = zhc
        else:
            if zhc > output:
                output = zhc
            break
print(output)