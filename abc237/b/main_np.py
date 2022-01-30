import numpy as np
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = np.asarray(A).T
for b in B:
    print(*b)
