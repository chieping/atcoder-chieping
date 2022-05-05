N = int(input())
X = list(map(int, input().split()))
Xs = list(sorted(X))
c1 = Xs[N//2-1]
c2 = Xs[N//2]
for x in X:
    if x <= c1:
        print(c2)
    else:
        print(c1)