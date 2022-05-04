N, T = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
P.append([10000, 1]) # 番兵
ans = min(c for c, t in P if t <= T)
print('TLE' if ans == 10000 else ans)
