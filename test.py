#05.12
numList = list(map(int, input().split()))
ans = [0, 0]
for idx, item in enumerate(numList):
    if item >= ans[0]:
        ans[0] = item
        ans[1] = idx
print(*ans)
