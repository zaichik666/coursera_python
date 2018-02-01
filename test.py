nums = list(map(int, input().split()))
res = [0] * 101
for num in nums:
    res[num] += 1
for nowRes in range(101):
    print((str(nowRes) + ' ') * res[nowRes], end='')
