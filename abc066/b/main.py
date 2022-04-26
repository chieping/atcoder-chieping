S = list(input())
N = len(S)
for i in range((N-1)//2, 0, -1):
    if S[:i] == S[i:i+i]:
        print(i+i)
        exit()
