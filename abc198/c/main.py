from math import ceil, sqrt

R, X, Y = map(int, input().split())

d = sqrt(X*X + Y*Y)

if d == R:
    print(1)
elif d <= 2*R:
    print(2)
else:
    print(ceil(d / R))
