#05.11
numList = list(map(int, input().split()))
n = 0
for i in numList:
    if i > 0:
        n += 1
print(n)
