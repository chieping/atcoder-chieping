N = int(input())
D = list(map(int, input().split()))
D.sort()
cmin = D[N//2-1]
cmax = D[N//2]
print(cmax - cmin)
