N = int(input())
S = []
T = []
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))

res = dict()

for i, s, t in zip(range(1, N+1), S, T):
    if not s in res:
        res[s] = (t, -i)

values = sorted(res.values(), reverse=True)

print(-values[0][1])

