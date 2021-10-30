S = input()
sl = [S[i:] + S[0:i] for i in range(len(S))]
sl.sort()
print(sl[0])
print(sl[-1])
