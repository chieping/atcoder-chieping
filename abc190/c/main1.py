N, M = map(int, input().split())
A = []
B = []
for _ in range(M):
    a, bits = map(int, input().split())
    a -= 1
    bits -= 1
    A.append(a)
    B.append(bits)
K = int(input())
C = []
D = []
for _ in range(K):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    C.append(c)
    D.append(d)

def check(balls):
    ret = 0
    for i in range(M):
        if balls[A[i]] > 0 and balls[B[i]] > 0:
            ret += 1
    return ret

ans = 0

for bits in range(1<<K):
    balls = [0] * N
    for i in range(K):
        bit = bits & (1<<i)
        if bit:
            # right
            balls[D[i]] += 1
        else:
            # left
            balls[C[i]] += 1
    ans = max(ans, check(balls))

print(ans)
