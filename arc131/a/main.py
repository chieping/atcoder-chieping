A = int(input())
B = int(input())

B2 = B // 2
BR = B % 2
if BR:
    ans = 10 * B2 + 5
else:
    ans = B2

ans = str(ans) + '0' + str(A)

print(ans)

