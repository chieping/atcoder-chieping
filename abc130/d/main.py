N, K = map(int, input().split())
A = list(map(int, input().split()))
# 逆に、Kを超えない連続部分列を考え、全体からそれを引く
# 全体は、始点=終点のnCr(N, 1) + nCr(N, 2)
cnt = 0
r = 0
Sum = 0
for l in range(N):
    while r < N and Sum + A[r] < K:
        Sum += A[r]
        r += 1
    cnt += r - l
    if r == l:
        r += 1
    else:
        Sum -= A[l]
ans = N + (N*(N-1)//2) - cnt
print(ans)
