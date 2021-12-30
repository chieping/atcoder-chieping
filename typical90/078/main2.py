from sys import stdin
N, M = map(int, stdin.readline().split())
G = [0] * (N+1)
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    G[max(a, b)] += 1
print(len([g for g in G if g == 1]))
