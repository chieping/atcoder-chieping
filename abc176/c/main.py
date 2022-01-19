import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
A.insert(0, 0)
box_height = 0
ans = 0
for i in range(N):
    if A[i]+box_height > A[i+1]:
        box_height = A[i] + box_height - A[i+1]
        ans += box_height
    else:
        box_height = 0
print(ans)

