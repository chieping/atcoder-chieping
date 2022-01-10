from sys import stdin
A, B = map(int, stdin.readline().split())
lim = 2 * A + 100
print(lim-B)
