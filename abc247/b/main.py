import sys
input = sys.stdin.readline
N  = int(input())
S = []
T = []
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)

for i in range(N):
    temp1 = 0
    temp2 = 0
    for j in range(N):
        if i != j:
            if S[i] == S[j] or S[i] == T[j]:
                temp1 = 1
            if T[i] == T[j] or T[i] == S[j]:
                temp2 = 1
    if temp1 == 1 and temp2 == 1:
        print('No')
        exit()

print('Yes') 
