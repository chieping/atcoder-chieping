from collections import deque

K = int(input())
cnt = 0

Q = deque()
for i in range(1, 10):
    Q.append(i)

while len(Q):
    i = Q.popleft()
    cnt += 1
    if cnt == K:
        print(i)
        break
    r = i % 10
    if r > 0: Q.append(i*10+r-1)
    Q.append(i*10+r)
    if r < 9: Q.append(i*10+r+1)
