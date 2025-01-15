n,a,b,c = input().split()
n = int(n)
def moveone(numdisk,init,desti):
    print(f'{numdisk}:{init}->{desti}')
def move(n,init,temp,desti):
    if n == 1:
        moveone(1,init,desti)
    else:
        move(n-1,init,desti,temp)
        moveone(n,init,desti)
        move(n-1,temp,init,desti)
move(n,a,b,c)