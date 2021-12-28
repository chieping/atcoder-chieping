from sys import stdin
N, K = stdin.readline().split()
K = int(K)
N = list(map(int, list(N)))

def from8_to9(N):
    ret = []
    tmp = sum(N[-i-1] * 8**i for i in range(len(N)))
    while tmp > 0:
        tmp, mod = divmod(tmp, 9)
        ret.append(mod)
    return ret[::-1] or [0]

for _ in range(K):
    N = from8_to9(N)
    N = [5 if n == 8 else n for n in N]

print(''.join(map(str, N)))
