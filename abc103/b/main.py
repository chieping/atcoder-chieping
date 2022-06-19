S = input()
T = input()
N = len(S)
for i in range(N):
    ans = False
    for j in range(N):
        if S[j] != T[(j+i)%N]:
            break
    else:
        ans = True
    if ans:
        print('Yes')
        exit()
print('No')