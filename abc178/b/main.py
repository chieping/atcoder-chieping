import sys
readline = sys.stdin.readline
a, b, c, d = map(int, readline().split())
print(max(a*c, a*d, b*c, b*d))
