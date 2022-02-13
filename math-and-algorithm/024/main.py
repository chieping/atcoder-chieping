N = int(input())
T = [map(int, input().split()) for _ in range(N)]
print(sum(q/p for p, q in T))