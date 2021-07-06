N = list(map(int, input().split()))

ans = sum(map(lambda x: 7-x, N))

print(ans)
