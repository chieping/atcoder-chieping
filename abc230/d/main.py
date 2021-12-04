N, D = map(int, input().split())
ans = 0
walls = []
for i in range(N):
    l, r = map(int, input().split())
    walls.append((r, l))
# 最後に壊した列
last = 0
walls.sort()
for r, l in walls:
    if l <= last:
        continue
    last = r+D-1
    ans += 1
print(ans)
