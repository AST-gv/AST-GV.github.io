n=input()
s=0
for i in range(int(n)):
    string=input()
    s1=string.count('###')
    s2=string.count('### ###')
    s+=s1/2-s2
print(int(s))
