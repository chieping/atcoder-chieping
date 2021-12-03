N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

a = max(1-A, 1-B)
b = min(N-A, N-B)
c = max(1-A, B-N)
d = min(N-A, B-1)

for i in range(P, Q+1):
    j1 = -1
    j2 = -1
    if (A+a) <= i <= (A+b):
        j = B + (i - A) - 1
        j1 = j
    if (A+c) <= i <= (A+d):
        j = B - (i - A) - 1
        j2 = j
    for i in range(R-1, S):
        if i == j1 or i == j2:
            print('#', end='')
        else:
            print('.', end='')
    print()
