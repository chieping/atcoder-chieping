# TLE
def main():
    import sys
    readline = sys.stdin.readline
    write = sys.stdout.write
    N, Q = map(int, readline().split())
    A = list(map(int, readline().split()))
    X = list(map(int, readline().split()))
    ans = []

    for x in X:
        res = 0
        r = 0
        sum_ = 0
        for l in range(N):
            while r < N and sum_ + A[r] <= x:
                sum_ += A[r]
                r += 1
            res += r-l
            if r == l:
                r += 1
            else:
                sum_ -= A[l]
        ans.append(res)
    write('\n'.join(map(str, ans)))
    write('\n')
main()
