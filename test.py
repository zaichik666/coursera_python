n = int(input())
clicksMax = list(map(int, input().split()))
k = int(input())
clicks = list(map(int, input().split()))
res = [0] * n
for click in clicks:
    res[click - 1] += 1
for i in range(n):
    if clicksMax[i] >= res[i]:
        print('NO')
    else:
        print('YES')
