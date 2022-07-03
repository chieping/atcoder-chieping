K = int(input())
H = 21
M = K
if K >= 60:
    H += 1
    M -= 60
print(f'{H:02}:{M:02}')
