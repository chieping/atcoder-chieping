from itertools import groupby

def run_length(orig):
    """ランレングス圧縮"""
    return [[key,len(list(group))] for key,group in groupby(orig)]

S = run_length(input())
T = run_length(input())

if len(S) != len(T):
    print('No')
    exit()

ans = False
for i in range(len(S)):
    if S[i][0] != T[i][0]: break
    if S[i][1] == 1 and T[i][1] > 1: break
    if S[i][1] > T[i][1]: break
else:
    ans = True
print('Yes' if ans else 'No')
