import sys
readline = sys.stdin.readline
N = int(readline())
N2 = 2*N
A = [[0] * N2 for _ in range(N2)]
for i in range(N2-1):
    a = list(reversed(list(map(int, readline().split()))))
    for j in range(i+1, N2):
        A[i][j] = a.pop()

ans = 0
def calc(dancer, score):
    if len(dancer) == 0:
        global ans
        ans = max(ans, score)
        return
    first = dancer[0]
    for i in range(1, len(dancer)):
        other = dancer[i]
        calc(dancer[1:i] + dancer[i+1:], score ^ A[first][other])

calc(list(range(N2)), 0)
print(ans)