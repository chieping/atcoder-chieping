N = int(input())
L = [0]*N
R = [0]*N
for i in range(N):
    L[i], R[i] = map(int, input().split())
ans = 0.0

for i in range(N):
    for j in range(i+1, N):
        res = 0
        for k in range(L[i], R[i]+1):
            for l in range(L[j], R[j]+1):
                if k > l:
                    res += 1
        ans += res / ((R[i]-L[i]+1)*(R[j]-L[j]+1))
print(ans)
