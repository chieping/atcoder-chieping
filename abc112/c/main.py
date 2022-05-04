N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

for cx in range(101):
    for cy in range(101):
        # cx, cyを中心と仮定したときのchを求める
        # hが0でない座標の値を使って計算する
        p = next(p for p in P if p[2] != 0)
        ch = p[2] + abs(p[0] - cx) + abs(p[1] - cy)
        assert ch != 0

        # ここが中心と考えて矛盾がないか検査する
        if all(max(ch-abs(cx-x)-abs(cy-y), 0)==h for x,y,h in P):
            print(cx, cy, ch)
            exit()
