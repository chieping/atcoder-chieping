N = int(input())
P = list(map(int, input().split()))
print('YES' if sum(P[i] != i+1 for i in range(N)) <= 2 else 'NO')