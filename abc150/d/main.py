from math import gcd
import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())
A = list(map(int, readline().split()))
B = [a // 2 for a in A]

lcm = 1
for b in B:
    g = gcd(lcm, b)
    lcm = lcm//g*b
# print(lcm)
for b in B:
    if (lcm // b) % 2 == 0:
        print(0)
        exit()

print(((M//lcm)+1)//2)
