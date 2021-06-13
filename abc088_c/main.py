A = []

for _ in range(0, 3):
    A.append(list(map(int, input().split())))


for i in range(0, 2):
    t0 = A[i][0] - A[i + 1][0]
    t1 = A[i][1] - A[i + 1][1]
    t2 = A[i][2] - A[i + 1][2]

    if not(t0 == t1 and t1 == t2):
        print("No")
        exit()

for j in range(0, 2):
    t0 = A[0][j] - A[0][j + 1]
    t1 = A[1][j] - A[1][j + 1]
    t2 = A[2][j] - A[2][j + 1]

    if not(t0 == t1 and t1 == t2):
        print("No")
        exit()

print("Yes")
