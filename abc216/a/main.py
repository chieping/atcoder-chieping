xy = input()

x = xy.split('.')[0]
y = int(xy[-1])

if y <= 2:
    s = '-'
elif y <= 6:
    s = ''
else:
    s = '+'

print(x + s)
