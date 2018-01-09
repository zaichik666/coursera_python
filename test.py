#05.14
numList = list(map(int, input().split()))
ans = 0
for item in numList:
    if item % 2 == 1 and ans == 0:
        ans = item
    elif item % 2 == 1 and item < ans:
        ans = item
print(ans)
