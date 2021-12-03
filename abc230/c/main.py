N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
H = Q-P+1
W = S-R+1
ans = [['.'] * W for i in range(H)]
for i in range(H):
    x = i + P
    for j in range(W):
        y = j + R
        if (A - x == B - y) or (-A + x == B - y):
        # if x-y == A-B or x+y == A+B:
            ans[i][j] = '#'

for l in ans:
    print(''.join(l))
