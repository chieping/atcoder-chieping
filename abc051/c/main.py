sx, sy, tx, ty = map(int, input().split())

dx = abs(tx - sx)
dy = abs(ty - sy)

ans = []
ans += list('U'*dy)
ans += list('R'*dx)
ans += list('D'*dy)
ans += list('L'*(dx+1))
ans += list('U'*(dy+1))
ans += list('R'*(dx+1))
ans += list('DR')
ans += list('D'*(dy+1))
ans += list('L'*(dx+1))
ans += list('U')
print(''.join(ans))