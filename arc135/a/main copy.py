from collections import deque
X = int(input())
MOD = 998244353
q = deque()
q.append(X)
ans = 1
while len(q) > 0:
    n = q.pop()
    if n > 3:
        if n % 2 == 0:
            m = n // 2
            q.append(m)
            q.append(m)
        else:
            m = n // 2
            q.append(m+1)
            q.append(m)
    else:
        ans *= n
        ans %= MOD

print(ans)

