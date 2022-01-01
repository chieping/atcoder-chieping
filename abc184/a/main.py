from sys import stdin
a, b = map(int, stdin.readline().split())
c, d = map(int, stdin.readline().split())
ans = a*d - b*c
print(ans)
