import sys
readline = sys.stdin.readline
a = int(readline())
b = int(readline())
n = int(readline())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

lcm = (a*b) // gcd(a, b)
i = 1
while lcm * i < n:
    i += 1
print(lcm*i)
