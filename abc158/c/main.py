A, B = map(int, input().split())

Amin = A*100 // 8 + (1 if A*100 % 8 else 0)
Amax = (A+1)*100 // 8 + (1 if (A+1)*100 % 8 else 0)
Bmin = B*10
Bmax = (B+1)*10
# print(Amin, Amax, Bmin, Bmax)
ok = set(range(Amin, Amax)).intersection(set(range(Bmin, Bmax)))

if len(ok):
    print(min(ok))
else:
    print(-1) 