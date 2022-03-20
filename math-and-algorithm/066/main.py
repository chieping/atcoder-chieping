N, K = map(int, input().split())
ALL = N**3
rem = 0
for a in range(1, N+1):
    for b in range(max(1, a-(K-1)), min(a+(K-1), N) + 1):
        for c in range(max(1, a-(K-1)), min(a+(K-1), N) + 1):
            if abs(b - c) <= K - 1:
                rem += 1
print(ALL - rem)
