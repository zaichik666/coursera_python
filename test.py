#05.19
nList = list(map(int, input().split()))
min1 = min2 = 0
max0 = max1 = max2 = -30000
for n in nList:
    if n >= max0:
        max2 = max1
        max1 = max0
        max0 = n
    if n < max0 and n >= max1:
        max2 = max1
        max1 = n
    if n < max1 and n > max2:
        max2 = n
    if n <= min1:
        min2 = min1
        min1 = n
    if n > min1 and n < min2:
        min2 = n
if max0 == 0:
    print(max1, min1, max0)
elif max0 * max1 * max2 > max0 * min1 * min2:
    print(max1, max2, max0)
else:
    print(min1, min2, max0)
