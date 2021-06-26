from math import ceil


A, B, C, D = map(int, input().split())

if ((C * D) - B) <= 0:
    print(-1)
else:
    ans = ceil((A / ((C * D) - B)))
    print(ans)
