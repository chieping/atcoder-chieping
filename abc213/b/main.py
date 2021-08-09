N = int(input())
A = list(map(int, input().split()))
A = [(a, i+1) for i,a in enumerate(A)]
A.sort()
print(A[-2][1])
