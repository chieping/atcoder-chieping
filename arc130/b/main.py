H, W, C, Q = map(int, input().split())
ans = [0] * C
ques = [map(int, input().split()) for i in range(Q)]
col = H
row = W
used_row = set()
used_col = set()
for t, n, c in ques[::-1]:
    n -= 1
    c -= 1
    if t == 1:
        # 行
        if n not in used_row:
            ans[c] += row
            used_row.add(n)
            col -= 1

    elif t == 2:
        # 列
        if n not in used_col:
            ans[c] += col
            used_col.add(n)
            row -= 1
print(*ans)
