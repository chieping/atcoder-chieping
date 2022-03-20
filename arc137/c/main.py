import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
if A[-1]-A[-2] > 1:
    print('Alice')
else:
    if A[-1] % 2 == (N-1) % 2:
        print('Bob')
    else:
        print('Alice')