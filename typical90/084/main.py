N = int(input())
S = list(input())
only_o = 0
only_x = 0
completed = 0
ans = 0
for s in S:
    if s == 'o':
        completed += only_x
        only_x = 0
        only_o += 1
    elif s == 'x':
        completed += only_o
        only_o = 0
        only_x += 1
    ans += completed
print(ans)
