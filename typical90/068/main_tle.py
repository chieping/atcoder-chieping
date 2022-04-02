from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
Q = int(input())
events = [list(map(int, input().split())) for _ in range(Q)]
rule = [[] for _ in range(N)]
for t, x, y, v in events:
    x, y = x-1, y-1
    if t == 0:
        rule[x].append((y, v))
        rule[y].append((x, v))
    elif t == 1:
        ans = 'Ambiguous'
        q = deque()
        done = [False] * N
        q.append((x, v))
        done[x] = True
        while len(q):
            x, v = q.popleft()
            if x == y:
                ans = v
                break
            for pair, Sum in rule[x]:
                if not done[pair]:
                    q.append((pair, Sum-v))
                    done[pair] = True
        print(ans)
