#06.03
n = int(input())
nList = list(map(int, input().split()))
nList.sort()
nCount = 0
if nList.count(n) >= 1:
    nCount = 1
for item in nList:
    if item > n and item >= n + 3:
        nCount += 1
        n = item
print(nCount)
