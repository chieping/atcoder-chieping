import sys
readline = sys.stdin.readline
A = [list(map(int, readline().split())) for _ in range(3)]
N = int(readline())
B = set([int(readline()) for _ in range(N)])

h1 = set(A[0])
h2 = set(A[1])
h3 = set(A[2])
v1 = {A[0][0], A[1][0], A[2][0]}
v2 = {A[0][1], A[1][1], A[2][1]}
v3 = {A[0][2], A[1][2], A[2][2]}
c1 = {A[0][0], A[1][1], A[2][2]}
c2 = {A[2][0], A[1][1], A[0][2]}

L = [h1, h2, h3, v1, v2, v3, c1, c2]
ans = False
for l in L:
    if len(B.intersection(l)) == 3:
        ans = True
print('Yes' if ans else 'No')
