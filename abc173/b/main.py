from collections import Counter
import sys
N, *S = sys.stdin.readlines()
S = Counter(s.rstrip() for s in S)
for k in 'AC', 'WA', 'TLE', 'RE':
    print(k, 'x', S[k])