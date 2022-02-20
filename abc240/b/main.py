from pprint import pprint
import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
print(len(set(A)))