N=int(input())
r=range(10)
print('Yes' if max(N==a*b for a in r for b in r) else 'No')