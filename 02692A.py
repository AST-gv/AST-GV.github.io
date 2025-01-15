n=int(input())
lst=[['']*3 for _ in range(3)]
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L']
lis=[]
dic={char:0 for char in alphabet}
def evenresult(left,right):
    if sum(dic[element] for element in left)==sum(dic[element] for element in right):
        return 1
    else:
        return 0
def upresult(left,right):
    if sum(dic[element] for element in left)>sum(dic[element] for element in right):
        return 1
    else:
        return 0
def downresult(left,right):
    if sum(dic[element] for element in left)<sum(dic[element] for element in right):
        return 1
    else:
        return 0
for _ in range(n):
    for i in range(3):
        qwe = input().split()
        for j in range(3):
            lst[i][j]=qwe[j]
    for letter in alphabet:
        dic[letter] = 1
        for i in range(3):
            if lst[i][2]=='even':
                if evenresult(lst[i][0],lst[i][1])==0:
                    break
            if lst[i][2]=='up':
                if upresult(lst[i][0],lst[i][1])==0:
                    break
            if lst[i][2]=='down':
                if downresult(lst[i][0],lst[i][1])==0:
                    break
        else:
            lis.append(f"{letter} is the counterfeit coin and it is heavy.")
        dic[letter] = -1
        for i in range(3):
            if lst[i][2]=='even':
                if evenresult(lst[i][0],lst[i][1])==0:
                    dic[letter] = 0
                    break
            if lst[i][2]=='up':
                if upresult(lst[i][0],lst[i][1])==0:
                    dic[letter] = 0
                    break
            if lst[i][2]=='down':
                if downresult(lst[i][0],lst[i][1])==0:
                    dic[letter] = 0
                    break
        else:
            lis.append(f"{letter} is the counterfeit coin and it is light.")
            dic[letter] = 0
for element in lis:
    print(element)



