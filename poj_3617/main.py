N = int(input())
S = [input().strip() for i in range(N)]
S = ''.join(S)
T = []

for i in range(N):
    Sr = S[::-1]
    
    # 先頭の方が辞書順で小さい
    if S < Sr:
        T.append(S[0])
        S = S[1:]
    else:
        T.append(S[-1])
        S = S[:-1]

print(''.join(T))
