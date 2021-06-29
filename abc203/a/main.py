f, s, t = map(int, input().split())

if f == s:
    print(t)
elif s == t:
    print(f)
elif f == t:
    print(s)
else:
    print(0)
