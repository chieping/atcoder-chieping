from functools import reduce
N = int(input())
A = list(map(int, input().split()))
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

print(reduce(lambda x, y: x//gcd(x, y)*y, A))