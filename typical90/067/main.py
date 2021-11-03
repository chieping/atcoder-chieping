N, K = map(int, input().split())

def trans_base(n, b1, b2):
    digit = 1
    b10 = 0
    while n > 0:
        q, r = divmod(n, 10)
        b10 += r * digit
        n = q
        digit *= b1
    ret = 0
    digit = 1
    while b10 > 0:
        q, r = divmod(b10, b2)
        ret += r * digit
        b10 = q
        digit *= 10
    return ret

for i in range(K):
    N = trans_base(N, 8, 9)
    N = str(N)
    N = N.replace('8', '5')
    N = int(N)
print(N)
