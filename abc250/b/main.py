N, A, B = map(int, input().split())

line1 = ((('.' * B) + ('#' * B)) * N)[:N*B]
line2 = ((('#' * B) + ('.' * B)) * N)[:N*B]

flag = 0
for i in range(N):
    if flag == 0:
        for j in range(A):
            print(line1)
        flag = abs(flag - 1)
    elif flag == 1:
        for j in range(A):
            print(line2)
        flag = abs(flag - 1)
