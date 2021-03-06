X, Y = map(int, input().split())
MOD = 10**9+7

# 移動回数: N
N, r = divmod(X+Y, 3)
if r != 0:
    print(0)
    exit()

# N回の移動のうち、X方向へはXN回、Y方向へはXY回移動する
XN = X - N
XY = Y - N

if 0 > XN or 0 > XY:
    print(0)
    exit()

# ansは N C K
K = XN

class Combination:

    def __init__(self, n: int, mod: int) -> None:
        assert n < mod
        self.mod = mod
        self.fact = [0] * (N+1)
        self.inv = [0] * (N+1)
        self.fact_inv = [0] * (N+1)
        self.fact[0:2] = 1, 1
        self.fact_inv[0:2] = 1, 1
        self.inv[1] = 1
        for i in range(2, N+1):
            self.fact[i] = self.fact[i-1] * i % self.mod
            self.inv[i] = self.mod - self.inv[self.mod%i] * (self.mod//i) % self.mod
            self.fact_inv[i] = self.fact_inv[i-1] * self.inv[i] % self.mod

    def c(self, n: int, k: int) -> int:
        if k < 0 or k > n:
            return 0
        return self.fact[n] * (self.fact_inv[k] * self.fact_inv[n-k] % self.mod) % self.mod

C = Combination(N, MOD)
print(C.c(N, K))