#05.21
i = 0
ans = 'NO'
tmpDown = []
tmpUp = []
Vertical = [1, 2, 3, 4, 5, 6, 7, 8]
Horizontal = [1, 2, 3, 4, 5, 6, 7, 8]
while i < 8:
    x, y = tuple(map(int, input().split()))
    y0_Down = y + x
    y0_Up = y - x
    if tmpDown.count(y0_Down) == 0 and tmpUp.count(y0_Up) == 0:
        tmpDown.append(y0_Down)
        tmpUp.append(y0_Up)
    if Vertical.count(x) != 0 and Horizontal.count(y) != 0:
        Vertical.remove(x)
        Horizontal.remove(y)
    else:
        ans == 'YES'
    i += 1
print(ans)
