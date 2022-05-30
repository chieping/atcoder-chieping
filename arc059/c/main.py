N = int(input())
A = list(map(int, input().split()))
ans = min(sum((n-a)**2 for a in A) for n in range(-100, 101))
print(ans)
