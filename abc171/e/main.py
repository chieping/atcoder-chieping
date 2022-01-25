# WIP
from pprint import pprint
import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))

li = list(zip(*list(bin(a)[2:].zfill(40)[::-1] for a in A)))
parity = [i.count('1') for i in li]
print(li)