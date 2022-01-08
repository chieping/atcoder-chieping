N = int(input())
N2 = 2*N
ans = 0
x = 1
while x*x <= N2:
    if N2 % x == 0:
        if abs(N2//x-x+1)%2 == 0:
            ans += 2
    x += 1
print(ans)
