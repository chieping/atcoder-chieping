N, Q = map(int, input().split())
front = [-1] * (N+1)
back = [-1] * (N+1)
for _ in range(Q):
    Q = list(map(int, input().split()))

    if Q[0] == 1:
        x, y = Q[1:]
        front[y] = x
        back[x] = y
        
    elif Q[0] == 2:
        x, y = Q[1:]
        front[y] = -1
        back[x] = -1

    elif Q[0] == 3:
        x = Q[1]
        while front[x] != -1:
            x = front[x]
        ans = []
        while x != -1:
            ans.append(x)
            x = back[x]
        print(len(ans), *ans)
