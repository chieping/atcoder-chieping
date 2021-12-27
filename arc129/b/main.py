N = int(input())
maxL = 0
minR = 10**20
for _ in range(N):
    l, r = map(int, input().split())
    maxL = max(maxL, l)
    minR = min(minR, r)
    print(max((maxL-minR+1)//2, 0))
