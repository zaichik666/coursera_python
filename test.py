#05.13
def IsAscending(A):
    i = 1
    length = len(A)
    while (i < length) and (A[i - 1] < A[i]):
        i += 1
    n = i // length
    n1 = abs(n - 1)
    print('YES' * n, 'NO' * n1, sep='')


numList = list(map(int, input().split()))
IsAscending(numList)
