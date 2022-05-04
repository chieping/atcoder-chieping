S = input()
T = input()
start = [-1] * 26
goal = [-1] * 26
base = ord('a')

for i in range(len(S)):
    a = ord(S[i]) - base
    b = ord(T[i]) - base

    if start[a] != -1 or goal[b] != -1:
        if start[a] != b or goal[b] != a:
            print('No')
            exit()
    
    start[a] = b
    goal[b] = a

print('Yes')
