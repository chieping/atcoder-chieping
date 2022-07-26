a = int(input())
ansnum = 0
ans = ''
for i in range(1, 1000):
    k = i
    for j in range(26):
        k *= 1000
        if k > a:
            break
        if ansnum < k:
            ansnum = k
            ans = f'{i}{chr(97+j)}'
print(ans)