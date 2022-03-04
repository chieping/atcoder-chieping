S = input()
N = len(S)
ans = [0]*N
seq = 0
for i in range(N):
    if S[i] == 'R':
        seq +=1
    else:
        ans[i] += seq // 2
        ans[i-1] += (seq+1) // 2
        seq = 0

seq = 0
for j in range(N-1, -1, -1):
    if S[j] == 'L':
        seq += 1
    else:
        ans[j] += seq // 2
        ans[j+1] += (seq+1) // 2
        seq = 0

print(*ans)
