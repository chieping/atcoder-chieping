N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
Diff = [0] + [A[i+1]-A[i] for i in range(1, N)] + [0]
ans = sum(map(abs, Diff))
for _ in range(Q):
    L, R, V = map(int, input().split())
    before = abs(Diff[L-1]) + abs(Diff[R])
    # Left
    if L > 1:
        Diff[L-1] += V
    # Right
    if R < N:
        Diff[R] -= V
    after = abs(Diff[L-1]) + abs(Diff[R])
    # 差分のあった区画だけ変動後の値で再計算
    ans += after - before
    print(ans)
