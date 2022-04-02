from math import sqrt
A, B = map(int, input().split())
C = sqrt(A*A+B*B)
print(A/C, B/C)