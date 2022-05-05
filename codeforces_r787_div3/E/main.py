t = int(input())

def solve(n, k, s):
    # A = list(map(lambda x: ord(x)-97, s))
    o1 = 0
    br = False
    o2_from = 0
    o2_to = 0
    for i, c in enumerate(s):
        if ord(c)-97 <= k:
            o1 = max(o1, ord(c)-97)
        else:
            br = True
            break
    k -= o1
    if br:
        o2_from = ord(s[i])-97
        o2_to = ord(s[i])-97-k
    # print(o1, i, o2_from, o2_to)
    ans = []
    for c in s:
        if ord(c)-97 <= o1:
            ans.append('a')
        elif ord(c)-97 <= o2_from:
            ans.append(chr(min(97+o2_to, ord(c))))
        else:
            ans.append(c)
    print(''.join(ans))
    
            
            

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    solve(n, k, s)
