from collections import deque

money = int(input())
price = deque(sorted(map(int, input().split())))
count_weapon = 0
while price:
    while money >= price[0] :
        count_weapon += 1
        money -= price.popleft()
        if not price:
            break
    if count_weapon > 0 and len(price) > 1:
        count_weapon -= 1
        money += price.pop()
    else:
        break

print(count_weapon)