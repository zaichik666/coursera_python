# 05.09
n = int(input())
value = 0
for i in range(1, n + 1):
    if i == 1:
        s = 1
        value = 1
    else:
        s = s * i
        value += s
print(value)
