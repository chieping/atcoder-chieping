while True:
    R, N = map(int, input().split())
    if R == -1 and N == -1:
        break
    X = list(map(int, input().split()))
    X.sort()

    i = 0
    ans = 0

    while i < N:
        s = X[i]
        while i < N and X[i] <= s + R:
            i += 1
        p = X[i - 1]
        while i < N and X[i] <= p + R:
            i += 1
        ans += 1

    print(ans)
