import sys
import numpy
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]
print(*[int(i) for i in numpy.polydiv(C, A)[0]][::-1])
