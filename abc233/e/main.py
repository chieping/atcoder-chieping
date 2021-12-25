X = list(map(int, list(input())))
# 累積和
A = []
tmp = 0
for x in X:
    tmp += x
    A.append(tmp)
# 下の桁から順番に確定した数を格納
ans = []
tmp = 0
for a in A[::-1]:
    tmp, mod = divmod(a+tmp, 10)
    ans.append(mod)
if tmp > 0:
    ans.append(tmp)

print(*ans[::-1], sep="")
