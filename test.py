#05.16
a = list(map(int, input().split()))
b = []
i = 0
while i < len(a):
    if i + 1 < len(a):
        b.append(a[i+1])
        b.append(a[i])

    else:
        b.append(a[i])
    i += 2
print(*b)
