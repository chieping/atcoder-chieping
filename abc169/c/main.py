from pprint import pprint
import sys
readline = sys.stdin.readline
A, B = readline().split()
A = int(A)
B100 = int(B[:-3] + B[-2:])
print(A*B100 // 100)