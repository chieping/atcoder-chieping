S = input()
Slen = len(S)
T = input()
Tlen = len(T)

# 後ろから、TがS'の部分文字列として適用可能か
# 判定し、適用可能であれば適用する
# 他の?はaに変換する
# **↑は嘘解法 **
# 
# ?b??
# ab
# 
# abaaが答えだが、ababとなってしまう。

def f(i):
    ret = list(S)
    ret[i:i+Tlen] = T
    ret = ['a' if c == '?' else c for c in ret]
    return ''.join(ret)

for i in range(Slen-1, -1, -1):
    j = Tlen-1
    while j >= 0:
        if i < 0: break
        if not (S[i] == '?' or S[i] == T[j]):
            break
        i -= 1
        j -= 1
    else:
        ans = f(i+1)
        print(ans)
        exit()
print('UNRESTORABLE')
