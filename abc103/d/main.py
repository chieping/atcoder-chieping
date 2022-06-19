import sys
input = sys.stdin.readline
N, M = map(int, input().split())
AB = []
for _ in range(M):
    a, b = map(int, input().split())
    AB.append((a-1, b-1))
AB.sort(key=lambda x: (x[1], x[0]))
ans = 0
lastB = 0
for a, b in AB:
    if a < lastB:
        continue
    else:
        lastB = b
        ans += 1
print(ans)
