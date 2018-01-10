#05.17
a = list(map(int, input().split()))
i = len(a) - 1
b = [a[i]]
b.extend(a[:i])
print(*b)
