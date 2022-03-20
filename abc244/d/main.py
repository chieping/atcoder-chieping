import sys
input = sys.stdin.readline
S = input().split()
T = input().split()
change_cnt = 0
for i in range(3):
    if S[i] != T[i]:
        change_cnt += 1
if change_cnt == 0 or change_cnt == 3:
    print('Yes')
else:
    print('No')