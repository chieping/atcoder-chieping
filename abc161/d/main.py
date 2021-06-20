from collections import deque

K = int(input())

remain = K

Q = deque(list(range(1, 10)))

while True:
    n = Q.popleft()
    remain -= 1

    if remain == 0:
        print(n)
        break
    
    n1 = int(str(n)[-1])
    if not n1 - 1 < 0:
        Q.append(n * 10 + (n1 - 1))
    Q.append(n * 10 + n1)
    if not n1 + 1 > 9:
        Q.append(n * 10 + (n1 + 1))
