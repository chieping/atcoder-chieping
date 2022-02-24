N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7
# 桁ごとに独立に考えてもよい
# k桁目の和は、0と1の組み合わせのとき2^kが足されることになるので、
# k桁目が0であるときにx、1であるときにyとすると、
# x * y * 2^k となる
# それを各桁ごとに計算する
ans = 0
for i in range(60):
    x = sum(a>>i&1 for a in A)
    ans += x*(N-x)*pow(2, i, MOD)
    ans %= MOD
print(ans)
