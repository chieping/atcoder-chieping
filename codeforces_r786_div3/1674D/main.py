import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))[::-1]
    for i in range(0, n, 2):
        if i+1 == n:
            continue
        if A[i] < A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
    
    ans = True
    tmp = A[0]
    for a in A[1:]:
        if a > tmp:
            ans = False
            break
        tmp = a
    print('YES' if ans else 'NO')
