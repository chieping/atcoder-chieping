N = int(input())
A, B, C = map(int, input().split())
MAX = 10000
ans = 1<<60

for i in range(MAX):
    for j in range(MAX):
        div, mod = divmod(N-A*i-B*j, C)
        if mod == 0 and div >= 0 and ans > i+j+div:
            ans = i+j+div
print(ans)
