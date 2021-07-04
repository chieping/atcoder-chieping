N, K = map(int, input().split())
A = list(map(int, input().split()))

AS = sorted(A)

base = K // N
remainder = K % N

if remainder > 0:
    s = AS[remainder - 1]
    for i in range(N):
        if A[i] <= s:
            print(base + 1)
        else:
            print(base)
else:
    for i in range(N):
        print(base)
        


