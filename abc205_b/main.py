N = int(input())
A = list(map(int, input().split()))

if sorted(A) == list(range(1, N + 1)):
    print('Yes')
else:
    print('No')

