from sys import stdin
import numpy as np
H, W = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(H)]
A = np.array(A)
print(np.sum(A-np.min(A)))
