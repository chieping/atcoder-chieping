import sys
readline = sys.stdin.readline
N, K = map(int, readline().split())
A = list(map(int, readline().split()))
X = 0
# ループを検出し、2回目にその数を追加したときに、
# ループ回数 x 1ループの追加個数を考える

# ループ検出用配列
B = [0] * N
# 1ループの追加個数
sum1loop = 0
loop_shuuki = 0
calc_loop = False
# 最初に"2"になったら、3になる直前までループの計算をする

while K > 0:
    i = X % N
    if B[i] == 1 and calc_loop == False:
        calc_loop = True
    if calc_loop == True and B[i] == 2:
        calc_loop = False
        d, r = divmod(K, loop_shuuki)
        K = r
        X += sum1loop * d
        continue

    B[i] += 1
    if calc_loop:
        loop_shuuki += 1
        sum1loop += A[i]
    X += A[i]
    K -= 1
print(X)
