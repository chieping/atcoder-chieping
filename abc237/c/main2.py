S = input()
l = 0
r = len(S)-1

while l < r and S[l] == 'a' and S[r] == 'a':
    l += 1
    r -= 1
while l < r and S[r] == 'a':
    r -= 1
while l < r and S[l] == S[r]:
    l += 1
    r -= 1

print('Yes' if l >= r else 'No')
