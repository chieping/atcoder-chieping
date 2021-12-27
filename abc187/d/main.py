N = int(input())
A = []
T = []
effect = []
Avote = 0
Tvote = 0
for i in range(N):
    a, t = map(int, input().split())
    A.append(a)
    Avote += a
    T.append(t)
    effect.append((a*2+t, a+t, i))

effect.sort(reverse=True)

ans = 0
i = 0
while Avote >= Tvote:
    Tvote += effect[i][1]
    Avote -= A[effect[i][2]]
    ans += 1
    i += 1

print(ans)
