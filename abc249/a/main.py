a, b, c, d, e, f, x = map(int, input().split())

taka = ([b] * a + [0] * c) * 100
ao = ([e] * d + [0] * f) * 100

ta = sum(taka[:x]) 
aa = sum(ao[:x]) 

if ta > aa:
    print('Takahashi')
elif aa > ta:
    print('Aoki')
else:
    print('Draw')