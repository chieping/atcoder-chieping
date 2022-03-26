import sys
input = sys.stdin.readline
N, K = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for l in range(K+1):
    for r in range(K-l+1):
        if l + r > N:
            continue
        d = K - l - r
        now = 0
        S = []
        for i in range(l):
            now += V[i]
            S.append(V[i])
        for i in range(N-r, N):
            now += V[i]
            S.append(V[i])
        S.sort()
        for i in range(d):
            if i >= len(S):
                break
            if S[i] > 0:
                break
            now -= S[i]
        ans = max(ans, now)
print(ans)
