# 解説AC
S = input()
Bcnt = S.count('B')
Len = len(S)
# 初期状態をBが一列に並び、続いてWが残りとして並んでいる、
# という状態だと仮定したとき、
# 最終状態の操作回数は
last_num = (Len-1+Len-Bcnt)*Bcnt//2
# 与えられた状態の操作回数は
init_num = sum(i for i in range(Len) if S[i] == 'B')
# 求める答えは最終状態の操作回数-与えられた状態の操作回数
print(last_num - init_num)