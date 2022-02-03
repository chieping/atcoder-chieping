from collections import defaultdict
X = int(input())
M = defaultdict(int)
ans = []
i = -120
while not ans:
    i5 = i**5
    M[i5] = i
    if X == i5:
        ans = (0, -i)
    elif M[X-i5]:
        ans = (i, -M[X-i5])
    elif M[X+i5]:
        ans = (i, M[X+i5])
    i += 1

print(*ans)
