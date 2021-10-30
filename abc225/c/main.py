N, M = map(int, input().split())
B = [list(map(int, input().split())) for i in range(N)]
counter = B[0][0]
first_col = (counter-1) % 7
for n in range(N):
    for m in range(M):
        if B[n][m] != counter or first_col + m > 6:
            print('No')
            exit()
        else:
            if m != M-1:
                counter += 1
            else:
                counter += 8-M

print('Yes')
