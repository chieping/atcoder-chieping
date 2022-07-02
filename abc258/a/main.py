K = int(input())
h = 21
m = K
if K >= 60:
    h += 1
    m -= 60

print(f'{h}:%02d' % m)

