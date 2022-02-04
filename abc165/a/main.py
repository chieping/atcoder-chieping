import sys
readline = sys.stdin.readline
K = int(readline())
A, B = map(int, readline().split())

d, m = divmod(A, K)
if m == 0 or (d+1)*K <= B:
    print('OK')
else:
    print('NG')