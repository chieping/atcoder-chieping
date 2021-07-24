from collections import defaultdict

N, M = input().split()
K = int(M)

INF = K + 1

dp = defaultdict(int)
eq_prod = 1

for i in range(len(N)):
    digit = ord(N[i]) - ord('0')
    nxt = defaultdict(int)

    # less -> less
    for prod, val in dp.items():
        for d in range(10):
            nxt_prod = min(INF, prod * d)
            n
    
