string=list(input())
def dxx(m):
    if 65<=ord(m)<=90:
        return chr(ord(m)+32)
    if 97<=ord(m)<=122:
        return chr(ord(m)-32)
string=[dxx(e) for e in string]
result=''.join(string)
print(result)

