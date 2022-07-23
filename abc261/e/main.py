# WA
N, C = map(int, input().split())
X = C
T = [0] * N
A = [0] * N
XOR = []
for i in range(N):
    T[i], A[i] = map(int, input().split())
    if T[i] == 3:
        XOR.append(i)

for i in range(N):
    kakutei = [False] * 31

    for j in XOR:
        if j <= i:
            X ^= A[j]
        else:
            break

    for j in range(i, -1, -1):
        if j+1 < N and j+1 < i and T[j+1] == 3:
            # xor逆再生
            for k in range(30):
                if kakutei[k]:
                    continue
                if 1<<k & a:
                    X ^= 1<<k
        # 逆から操作を適用していく
        t, a = T[j], A[j]
        if t == 1:
            # and
            for k in range(30):
                if kakutei[k]:
                    continue
                if 1<<k & ~a:
                    kakutei[k] = True
                    X &= ~(1<<k)

        elif t == 2:
            # or
            for k in range(30):
                if kakutei[k]:
                    continue
                if 1<<k & a:
                    kakutei[k] = True
                    X |= 1<<k
    print(X)
