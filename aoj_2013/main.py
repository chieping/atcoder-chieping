def parse(s):
    h,m,s = map(int, s.split(':'))
    return h*3600+m*60+s

def solve(n):
    imos = [0] * 86405
    for i in range(n):
        t1, t2 = map(parse, input().split())
        imos[t1] += 1
        imos[t2] -= 1
    for i in range(1, len(imos)):
        imos[i] += imos[i-1]
    print(max(imos))

while True:
    n = int(input())
    if n > 0:
        solve(n)
    else:
        break
