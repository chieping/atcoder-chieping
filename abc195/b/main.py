A, B, W = map(int, input().split())

m = 10**18
M = 0
for n in range(1000001):
    if A*n <= 1000*W <= B*n:
        m = min(m, n)
        M = max(M, n)

if M == 0:
    print('UNSATISFIABLE')
else:
    print(m, M)
