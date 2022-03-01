N = int(input())
A = list(map(int, input().split()))
X = sum(1/a for a in A)
print(1/X)
