N = int(input())
A = [list(map(int, list(input()))) for _ in range(N)]

# print(A)
dxdy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

ans = []

for i in range(N):
    for j in range(N):
        for k in range(8):
            tmp = []
            for l in range(N):
                xi = (i+(dxdy[k][0]*l))%N
                yi = (j+(dxdy[k][1]*l))%N
                # print(xi, yi)
                tmp.append(A[xi][yi])
            ans = max(ans, tmp)

print(*ans, sep='')