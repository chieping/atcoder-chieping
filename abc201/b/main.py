N = int(input())

Q = []

for i in range(N):
    s, t = input().split()
    t = int(t)
    Q.append((t, s))

Q.sort()

print(Q[N-2][1])
