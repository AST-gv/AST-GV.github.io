lst=[]
string=''
reserved=''
tem=''
def change(m,n):
    if 64 < ord(m) < 91 :
        return chr((ord(m)-65-(n)+26)%26+65)
    if 96 < ord(m) < 123:
        return chr((ord(m)-97-(n)+26)%26+97)
def judge(a):
    if (ord('a') <= ord(a) <= ord('z')) or ( ord('A') <= ord(a) <= ord('Z')):
        return True
    else:
        return False
while True:
    try:
        str_list=input()
        sum1 = 0
        tem = ''
        string=''
        str_list = '\0' + str_list
        for i in range(1,len(str_list)):
            if judge(str_list[i]) == True:
                if judge(str_list[i-1]) == False:
                    sum1+=1
                    tem = ''
                tem = change(str_list[i], sum1) + tem
                if i == len(str_list)-1:
                    string = string+tem
                else:
                    if judge(str_list[i+1]) == False :
                        string += tem
            if judge(str_list[i])  == False:
                string = string+str_list[i]
        lst.append(string[0:])
    except:
        break
for i in range(0,len(lst)):
    print(lst[i])
