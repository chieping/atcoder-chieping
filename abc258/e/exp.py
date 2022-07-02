N = 3
W = [2, 3, 4]
X = 5
a = 0
for i in range(1000):
    a += W[i%N]
    if a >= X:
        print(i, a)
        a = 0

