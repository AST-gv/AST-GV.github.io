lst=[]
while True:
    string=input()
    length=len(string)
    if string == '.':
        break
    for i in range(1,length+1):
        if length % i != 0:
            continue
        else:
            if string == string[:i] * int(length/i):
                lst.append(int(length/i))
                break
for element in lst:
    print(element)
