n = int(input())
R = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = []
q = int(input())
for _ in [0]*q:
    r, c = map(int, input().split())
    r, c = r-1, c-1
    if R[r] + C[c] > n:
        ans.append('#')
    else:
        ans.append('.')
print(''.join(ans))
