W, H = map(int, input().split())
MOD = 10**9+7
# 移動しなければならない回数N
N = W - 1 + H - 1
# 答えはnCk でkは W - 1 または H - 1
K = W - 1
# コンビネーションの分母部分は、割り算をするのでなく、
# 逆元を掛ける
# 逆元はフェルマーの小定理を使って求める

def fact(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
        ret %= MOD
    return ret

inv = pow(fact(N-K)*fact(K)%MOD, MOD-2, MOD)
ans = fact(N)*inv%MOD
print(ans)
