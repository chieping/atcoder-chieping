N, M = map(int, input().split())
X = list(map(int, input().split()))
# どの区間をスキップできるか？という問題と言い換えたとき、
# N-1区間をスキップできる。
# 区間の大きい方からN-1区間をスキップすると考えて計算する。
if N >= M:
    print(0)
    exit()
X.sort()
Y = [abs(X[i+1] - X[i]) for i in range(M-1)]
Y.sort()
print(sum(Y[:M-1-N+1]))