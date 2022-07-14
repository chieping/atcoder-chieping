from collections import deque
a, N = map(int, input().split())
Q = deque()
Q.append((N, 0))
used = [False] * (10**6)

while len(Q):
    now, cnt = Q.popleft()
    if now == 1:
        print(cnt)
        exit()
    if now % a == 0 and not used[now//a]:
        used[now//a] = True
        Q.append((now//a, cnt+1))
    tmp = str(now)
    if len(tmp) > 1 and tmp[1] != '0':
        tmp = int(tmp[1:] + tmp[0])
        if not used[tmp]:
            used[tmp] = True
            Q.append((tmp, cnt+1))
print(-1)
