from functools import reduce
N = int(input())
V = list(map(int, input().split()))
V.sort()
ans = reduce(lambda x, y: (x+y)/2, V)
print(ans)