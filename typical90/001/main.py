N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split())) + [L]

def check(i):
    last = 0
    k = K
    for a in A:
        if a-last >= i:
            if k == 0:
                return True
            k -= 1
            last = a
    return False

l = 0
r = L
while r-l > 1:
    m = (l+r) // 2
    if check(m):
        l = m
    else:
        r = m
print(l)
