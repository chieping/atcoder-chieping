from sys import stdin
N, W = map(int, stdin.readline().split())

for i in range(1002):
    if W * i > N:
        print(i-1)
        break
