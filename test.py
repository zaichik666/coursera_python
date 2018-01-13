#06.02
def Intersection(A, B):
    i = j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
        elif A[i] == B[j]:
            C.append(A[i])
            i += 1
            j += 1
    return C


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = Intersection(a, b)
print(*c)
