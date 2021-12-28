from sys import stdin
Q = int(stdin.readline())
top = []
bottom = []
for _ in range(Q):
    t, x = map(int, stdin.readline().split())
    if t == 1:
        top.append(x)
    elif t == 2:
        bottom.append(x)
    elif t == 3:
        if len(top) >= x:
            print(top[-x])
        else:
            print(bottom[x-len(top)-1])
