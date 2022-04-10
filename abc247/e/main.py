from pprint import pprint
import sys
input = sys.stdin.readline
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
l = 0
lastX = -1
lastY = -1
for r in range(N):
    a = A[r]
    if X < a or Y < a:
        l = -1
        lastX = -1
        lastY = -1
        l = r + 1
        continue
    if a == X:
        lastX = r
    if a == Y:
        lastY = r
    if lastX != -1 and lastY != -1:
        ans += (min(lastX, lastY)-l) * (N - max(lastX, lastY))
        l = r + 1
        


print(ans)