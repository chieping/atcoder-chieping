MOD = 10**9+7
N = int(input())
A = list(map(int, input().split()))
A.sort()
if N % 2:
    B = [0]
    for i in range(2, N, 2):
        B.append(i)
        B.append(i)
    if A != B:
        print(0)
    else:
        print(pow(2, (N-1)//2, MOD))
else:
    B = []
    for i in range(1, N, 2):
        B.append(i)
        B.append(i)
    if A != B:
        print(0)
    else:
        print(pow(2, N//2, MOD))
