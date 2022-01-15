import sys
readline = sys.stdin.readline
a, b, c = map(int, list(readline()[:-1]))
print(a*100+b*10+c+b*100+c*10+a+c*100+a*10+b)
