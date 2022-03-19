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
