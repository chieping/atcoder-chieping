N = int(input())

# 奇数-> 0
if N % 2 == 1:
    print(0)
    exit()

ans = 0
d = 10
while d <= N:
    ans += N//d
    d *= 5
print(ans)