S, P = map(int, input().split())

for n in range(1, 10**6+1):
    m, r = divmod(P, n)
    if r == 0 and n + m == S:
        print('Yes')
        exit()
print('No')