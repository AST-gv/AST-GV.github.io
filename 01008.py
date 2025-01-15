n = int(input())
output= []
dict_Haab = {'pop':0, 'no':1, 'zip':2, 'zotz':3, 'tzec':4, 'xul':5, 'yoxkin':6, 'mol':7, 'chen':8, 'yax':9, 'zac':10, 'ceh':11, 'mac':12, 'kankin':13, 'muan':14, 'pax':15, 'koyab':16, 'cumhu':17, 'uayet':18}
dict_Tzolkin = {20:'ahau', 1:'imix', 2:'ik', 3:'akbal', 4:'kan', 5:'chicchan', 6:'cimi', 7:'manik', 8:'lamat', 9:'muluk', 10:'ok', 11:'chuen', 12:'eb', 13:'ben', 14:'ix', 15:'mem', 16:'cib', 17:'caban', 18:'eznab', 19:'canac'}
for _ in range(n):
    Haab_date, Haab_month, Haab_year = input().split()
    Haab_date = Haab_date[:-1]
    Haab_date = int(Haab_date)
    Haab_year = int(Haab_year)

    real_date = Haab_date + 20 * dict_Haab[Haab_month] + 365 * Haab_year

    Tzolkin_year = real_date // 260
    Tzolkin_date = real_date % 13 + 1
    Tzolkin_month = dict_Tzolkin[real_date % 20 + 1]
    output.append(f'{Tzolkin_date} {Tzolkin_month} {Tzolkin_year}')
print(n)
print(*output, sep='\n')
