N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort()
ans = 0

for a, b in AB:
    if M == 0: break
    c = min(b, M)
    ans += a * c
    M -= c
print(ans)