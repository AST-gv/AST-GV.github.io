rowA,colA=map(int,input().split())
lstA=[[0]*colA for _ in range(rowA)]
for i in range(rowA):
    row_data=list(map(int, input().split()))
    for j in range(colA):
        lstA[i][j]=row_data[j]
rowB,colB=map(int,input().split())
lstB=[[0]*colB for _ in range(rowB)]
for i in range(rowB):
    row_data = list(map(int, input().split()))
    for j in range(colB):
        lstB[i][j] = row_data[j]
rowC,colC=map(int,input().split())
lstC=[[0]*colC for _ in range(rowC)]
for i in range(rowC):
    row_data =list(map(int, input().split()))
    for j in range(colC):
        lstC[i][j] = row_data[j]
if colA!=rowB or rowA!=rowC or colB!=colC:
    print('Error!')
else:
    lst = [[0] * colB for _ in range(rowA)]
    for i in range(rowA):
        for j in range(colB):
            lst[i][j]=sum(lstA[i][k]*lstB[k][j] for k in range(colA))+lstC[i][j]
            print(lst[i][j],end=' ')
        print('')

