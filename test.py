#05.22
i = 0
ans = 'NO'
tmpDown = []
tmpUp = []
Vertical = []
Horizontal = []
while i < 8:
    x, y = tuple(map(int, input().split()))
    if Vertical.count(x) == 0 and Horizontal.count(y) == 0:
        Vertical.append(x)
        Horizontal.append(y)
    else:
        ans = 'YES'
    y0_Down = y + x
    y0_Up = y - x
    if tmpDown.count(y0_Down) == 0 and tmpUp.count(y0_Up) == 0:
        tmpDown.append(y0_Down)
        tmpUp.append(y0_Up)
    else:
        ans = 'YES'
    i += 1
print(ans)
