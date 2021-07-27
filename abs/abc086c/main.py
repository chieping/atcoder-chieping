N = int(input())

T, X, Y = 0, 0, 0
ans = 'Yes'

def can_reach(t, x, y):
    global T, X, Y
    dist = abs(X-x) + abs(Y-y)
    if dist <= t-T and (dist - (t-T)) % 2 == 0:
        T, X, Y = t, x, y
        return True
    else:
        return False

for _ in range(N):
    t, x, y = map(int, input().split())
    if not can_reach(t, x, y):
        ans = 'No'
        break

print(ans)
