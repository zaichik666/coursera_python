#05.15
nList = list(map(int, input().split()))
n = int(input())
i = 0
while i < len(nList) and n <= nList[i]:
    i += 1
print(i + 1)
