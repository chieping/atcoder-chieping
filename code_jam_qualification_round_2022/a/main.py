N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

for i, [r, c] in enumerate(C, 1):
    print('Case #' + str(i) + ':')
    l1 = ''.join(['-' if i%2 else '+' for i in range(2*c+1)])
    l2 = ''.join(['.' if i%2 else '|' for i in range(2*c+1)])
    print('..' + l1[2:])
    for i in range(r):
        if i == 0:
            print('..' + l2[2:])
        else:
            print(l2)
        print(l1)
