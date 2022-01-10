from collections import Counter
import sys
readline = sys.stdin.readline
S = list(map(int, list(readline()[:-1])))
C = Counter(S)
ans = False
if len(S) == 1:
    ans = S[0] == 8
elif len(S) == 2:
    ans |= (S[0] * 10 + S[1]) % 8 == 0
    ans |= (S[1] * 10 + S[0]) % 8 == 0
else:
    # 下三桁で8の倍数を作れたらYes
    for eight in range(112, 1000, 8):
        R = Counter(list(map(int, list(str(eight)))))
        for n, cnt in R.items():
            if C[n] < cnt:
                break
        else:
            # breakしなかったらOK
            ans |= True
print('Yes' if ans else 'No')
