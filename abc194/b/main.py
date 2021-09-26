N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append((a, i))
    B.append((b, i))

A.sort()
B.sort()

if A[0][1] != B[0][1]:
    print(max(A[0][0], B[0][0]))
else:
    print(min(max(A[1][0], B[0][0]), max(A[0][0], B[1][0]), A[0][0] + B[0][0]))
