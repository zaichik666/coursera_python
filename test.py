#06.04
S, N = tuple(map(int, input().split()))
b = []
for i in range(N):
    el = int(input())
    b.append(el)
b.sort()
ans = 0
b_sum = 0
for i in range(N):
    b_sum += b[i]
    if b_sum <= S:
        ans += 1
print(ans)
