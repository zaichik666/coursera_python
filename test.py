# 05.06
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(j + 1, sep='', end='')
    print()
