# WA
n, m = map(int, input().split())
L = 100001
x = [False] * L
a = list(map(int, input().split()))
for i in a:
    x[i] = True

d = []
for i in range(2, L):
    flag = False
    j = i
    while j < L:
        if x[j]:
            flag = True
        j += i
    if flag:
        d.append(i)

ok = [True] * (m+1)
for i in d:
    j = i
    while j <= m:
        ok[j] = False
        j += i

cnt = 0
for i in range(1, m):
    if ok[i]:
        cnt += 1
print(cnt)
for i in range(1, m):
    if ok[i]:
        print(i) 
