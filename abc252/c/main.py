N = int(input())
S = [list(map(int, input())) for _ in range(N)]
ans = 10**10
for n in range(10):
    stop = [False] * N
    i = 0
    while not all(stop):
        for j in range(N):
            if not stop[j] and S[j][i%10] == n:
                stop[j] = True
                break
        i += 1
    ans = min(ans, i)



print(ans - 1)