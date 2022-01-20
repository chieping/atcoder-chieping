X, K, D = list(map(int, input().split()))
X = abs(X)
a = X // D
if K < a:
    print(X - D*K)
else:
    if (K-a) % 2 == 0:
        print(X - a*D)
    else:
        print(abs(X - (a+1)*D))
