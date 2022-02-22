N, K, M = map(int, input().split())
A = list(map(int, input().split()))
ans = max(0, M*N - sum(A))
print(ans if ans <= K else -1)