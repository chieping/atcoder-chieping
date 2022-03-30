# 解説AC
N = int(input())
ans = 0
def f(n):
    return n*(n+1)//2
for i in range(1, N+1):
    ans += i * f(N//i)
print(ans)