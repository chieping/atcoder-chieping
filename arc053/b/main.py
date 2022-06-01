from collections import Counter
S = input()
Len = len(S)
counts = list(Counter(S).values())
chunk_cnt = sum(c % 2 for c in counts)

if chunk_cnt == 0:
    print(Len)
else:
    ans = Len // chunk_cnt
    if ans % 2 == 0:
        ans -= 1
    print(ans)