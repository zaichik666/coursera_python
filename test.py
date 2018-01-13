#06.01
def merge(A, B):
    i = j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i < len(A):
        C.extend(A[i:len(A)])
    if j < len(B):
        C.extend(B[j:len(B)])
    return C

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = merge(a, b)
print(*c)
