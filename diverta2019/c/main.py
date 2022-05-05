N = int(input())
S = [input() for _ in range(N)]
ab_natural = sum(s.count('AB') for s in S)
only_a = 0
only_b = 0
both = 0
for s in S:
    if s[0] == 'B':
        if s[-1] == 'A':
            both += 1
        else:
            only_b += 1
    elif s[-1] == 'A':
        only_a += 1
# bothを使ってABを作る
ab_from_both = 0
if both > 0:
    ab_from_both = both - 1
    # bothを使うとひとつの大きなbothになるのでそれを使う
    if only_a > 0:
        ab_from_both += 1
        only_a -= 1
    if only_b > 0:
        ab_from_both += 1
        only_b -= 1
# 残ったonlyを使ってABを作る
ab_from_only = min(only_a, only_b)
print(ab_natural + ab_from_only + ab_from_both)
