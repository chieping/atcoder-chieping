from collections import defaultdict
N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
M = defaultdict(int)
#尺取り法
ans = 0
cr = 1
cnt = 0
for i in range(1, N+1):
    while cr <= N:
        if M[A[cr]] == 0 and cnt == K:
            break
        if M[A[cr]] == 0:
            cnt += 1
        M[A[cr]] += 1
        cr += 1
    ans = max(ans, cr - i)
    if M[A[i]] == 1:
        cnt -= 1
    M[A[i]] -= 1
print(ans)
