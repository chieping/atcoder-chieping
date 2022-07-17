N, X, Y = map(int, input().split())
level = N
red = 1
blue = 0
while level > 1:
    blue += X * red
    red = red
    red += blue
    blue = Y * blue
    level -= 1
print(blue)
