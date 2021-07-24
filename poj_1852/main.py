cases = int(input())

for i in range(cases):
    L, n = map(int, input().split())
    A = list(map(int, input().split()))
    minT = 0
    for i in range(n):
        minT = max(minT, min(A[i], L-A[i]))
    
    maxT = 0
    for i in range(n):
        maxT = max(maxT, max(A[i], L-A[i]))

    print(str(minT) + " " + str(maxT))
