N = int(input())
A = [int(input()) for _ in range(N)]
visited = [False] * N
cnt = 0
i = 0
while not visited[i]:
    visited[i] = True
    cnt += 1
    i = A[i]
    i -= 1
    if i == 1:
        print(cnt)
        exit()
print(-1)
