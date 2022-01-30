from collections import deque
N = int(input())
S = input()
q = deque([N])
for i in range(N-1, -1, -1):
    if S[i] == 'L':
        q.append(i)
    else:
        q.appendleft(i)
print(*q)
