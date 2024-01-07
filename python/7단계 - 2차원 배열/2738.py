N, M = map(int, input().split())
A, B = [], []

for i in range(N):
    elements = list(map(int, input().split()))
    A.append(elements)
for i in range(N):
    elements = list(map(int, input().split()))
    B.append(elements)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()