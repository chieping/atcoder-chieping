H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = list(zip(*A))
for b in B:
    print(*b)
