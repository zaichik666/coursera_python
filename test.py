#05.18
nList = list(map(int, input().split()))
a = b = c = d = 0
for n in nList:
    if n >= a:
        b = a
        a = n
    if n < a and n > b:
        b = n
    if n <= c:
        d = c
        c = n
    if n > c and n < d:
        d = n
if a * b > c * d:
    print(b, a)
else:
    print(c, d)
