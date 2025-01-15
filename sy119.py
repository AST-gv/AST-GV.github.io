def hanoi(n, start, via, desti):
    global zhc
    if n == 0:
        return zhc
    hanoi(n - 1, start, desti, via)
    lst.append(f'{start}->{desti}')
    zhc += 1
    hanoi(n - 1, via, start, desti)

lst = []
zhc = 0
hanoi(int(input()), 'A', 'B', 'C')
print(zhc)
print(*lst, sep='\n')

