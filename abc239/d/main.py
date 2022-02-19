import sys
readline = sys.stdin.readline
A, B, C, D = map(int, readline().split())

def is_prime(n):
    i = 2
    while i*i <= n:
        d, r = divmod(n, i)
        if r == 0:
            return False
        else:
            i += 1
    return True

ans = 'Aoki'
for i in range(A, B+1):
    res = True # 素数にできたらFalseにする
    for j in range(C, D+1):
        if is_prime(i+j):
            res = False
            break
    if res:
        ans = 'Takahashi'
        break
print(ans)