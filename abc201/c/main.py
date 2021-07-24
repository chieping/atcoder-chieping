S = input()
ans = 10000
for i in range(10000):
    s = "%04d" % i
    for j in range(10):
        if S[j] == 'o' and str(j) not in s:
            ans -= 1
            break
        if S[j] == 'x' and str(j) in s:
            ans -= 1
            break
print(ans)
