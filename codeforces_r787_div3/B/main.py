t = int(input())

def solve(N, A):
    cur = 10**18
    ans = 0
    for i, a in list(enumerate(A))[::-1]:
        # print('a:', a)
        while cur <= a and a > 0:
            a //= 2
            ans += 1
        if a == 0 and i != 0:
            # print(i)
            print(-1)
            return
        cur = a
        # print('cur:', cur)
    print(ans)


for _ in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)