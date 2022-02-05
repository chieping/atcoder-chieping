from pprint import pprint
import sys
readline = sys.stdin.readline
MOD = 998244353
N = int(readline())

def f(n):
    keta = len(str(n))
    return n - (10**(keta-1)-1)

ans = 0
keta = 1
if N >= 10**keta:
    ans += (10**(keta-1)+(10**(keta)-1))*(10**keta-1)//2
    ans %= MOD
    keta += 1
else:
    ans = sum(range(1, N+1))
    print(ans)
    exit()

while N >= 10**keta:
    # ans += (1+(10**(keta)-1-(10**(keta-1)-1)))*(10**keta)//2
    ans += (1+f(10**keta-1))*(10**keta-10**(keta-1))//2
    ans %= MOD
    keta += 1

# ans += (1+(N-(10**(keta-1)-1)))*(N-10**(keta-1)+1)//2
ans += (1+f(N))*(N-10**(keta-1)+1)//2
ans %= MOD

print(ans)