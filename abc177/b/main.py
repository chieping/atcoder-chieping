S = input()
T = input()
ans = 10**4
for i in range(len(S)-len(T)+1):
    tmp = 0
    # print('---------')
    for j in range(len(T)):
        # print(S[i+j])
        # print(T[j])
        if S[i+j] != T[j]:
            tmp += 1
    ans = min(ans, tmp)
print(ans)
