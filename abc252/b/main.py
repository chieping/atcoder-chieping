N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = [b-1 for b in B]
Max = max(A)

ans = False
for i in range(N):
    if A[i] == Max:
        if i in B:
            ans = True

print('Yes' if ans else 'No')