import sys
input = sys.stdin.readline
T = int(input())
C = [list(map(int, input().split())) for _ in range(T)]
INF = 10**18
for c in C:
    ans = INF
    for i in range(3):
        for j in range(i+1, 3):
            if (c[i]-c[j]) % 3:
                continue
            ans = min(ans, max(c[i], c[j]))
    print(ans if ans != INF else -1)
