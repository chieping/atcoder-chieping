N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = T.copy()

min_idx = T.index(min(T))

for i in range(min_idx, N):
    j = i + 1
    if j > N-1:
        j = 0
    ans[j] = min(ans[i] + S[i], ans[j])
for i in range(0, min_idx):
    j = i + 1
    if j > N-1:
        j = 0
    ans[j] = min(ans[i] + S[i], ans[j])

for a in ans:
    print(a)
