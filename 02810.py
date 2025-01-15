n = int(input())
lst=[]
cube = {x:x**3 for x in range(n+1)}
reserved_cube = {k:v for v,k in cube.items()}
for b in range(2,n):
   for c in range(b,n):
        for d in range(c,n):
            if (a := cube[b]+cube[c]+cube[d]) in reserved_cube:
                lst.append((reserved_cube[a],b,c,d))
lst.sort()
for element in lst:
    print(f'Cube = {element[0]}, Triple = ({element[1]},{element[2]},{element[3]})')
