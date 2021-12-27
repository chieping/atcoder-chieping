N = int(input())
effect = []
diff = 0
for i in range(N):
    a, t = map(int, input().split())
    diff += a
    effect.append(a*2+t)
effect.sort(reverse=True)

ans = 0
i = 0
while diff >= 0:
    diff -= effect[i]
    ans += 1
    i += 1

print(ans)
