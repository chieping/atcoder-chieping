N, A, B = map(int, input().split())

if A <= B:
    print(max(0, N - A + 1))
    exit()

N = N - (A-1)
if N < 0:
    print(0)
    exit()
ans = N//A * B
mod = N % A
ans += min(mod, B)
print(ans)
