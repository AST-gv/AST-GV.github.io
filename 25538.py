a = int(input())
bi_string = f'{a:b}'
length=len(bi_string)
for i in range(length):
    if bi_string[i] != bi_string[length-i-1]:
        print("No")
        break
else:
    print("Yes")