a, b, c, d = map(int, input().split())

if b*c < a*d:
    print("AOKI")
elif b*c > a*d:
    print("TAKAHASHI")
else:
    print("DRAW")