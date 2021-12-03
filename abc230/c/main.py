N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

# G = [['.'] * (N+1) for i in range(N+1)]

a = max(1-A, 1-B)
b = min(N-A, N-B)
c = max(1-A, B-N)
d = min(N-A, B-1)


for i in range(P, Q+1):
# for i in range(1, N+1):
    # ans = ['.'] * (S-R+2)
    # ans = ['.'] * N
    j1 = -1
    j2 = -1
    if (A+a) <= i <= (A+b):
        j = B + (i - A) - 1
        # if 0 <= j <= (S-R+1):
            # ans[j] = '#'
        j1 = j
    if (A+c) <= i <= (A+d):
        j = B - (i - A) - 1
        # if 0 <= j <= (S-R+1):
            # ans[j] = '#'
        j2 = j
    # print('j1:', j1, 'j2:', j2)
    for i in range(R-1, S):
        if i == j1 or i == j2:
            print('#', end='')
        else:
            print('.', end='')
    print()
    # print(''.join(ans[R-1:S:]))
    # print(''.join(ans[::]))
