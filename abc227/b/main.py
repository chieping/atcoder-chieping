N = int(input())
S = list(map(int, input().split()))
ans = 0
for s in S:
    found = False
    a = 1
    while found == False and a <= 1000:
        b = 1
        while found == False and b <= 1000:
            if s == 4*a*b + 3*a + 3*b:
                found = True
            b += 1
        a += 1
    if not found:
        ans += 1
print(ans)




