N = int(input())
S = input()

def yes():
    print('Yes')
    exit()

def no():
    print('No')
    exit()

if S == S[::-1]:
    yes()

if N == 2:
    if S[0] == S[1]:
        yes()
    else:
        no()
if S[-1] == 'A':
    yes()

if N > 4 and S[0] == 'B':
    yes()

no()