t = int(input())

for _ in range(t):
    s = input()

    f = ord(s[0])-97
    s = ord(s[1])-97

    ans = f*25+1

    if f < s:
        ans += s - 1
    else:
        ans += s
    print(ans)

