import sys
input = sys.stdin.readline
N = int(input())
S = set(range(1, 2*N+2))
print(1, flush=True)
S.remove(1)
for _ in range(N):
    Naoki = int(input())
    S.remove(Naoki)
    Ntaka = S.pop()
    print(Ntaka, flush=True)
