
N = int(input())

arr = [list(map(int, input().split())) for i in range(N)]

arr.sort(key= lambda x: -x[0]-x[1])

ans = 0

for i in range(N):
    a, b = arr[i]

for i, (a, b) in enumerate(arr):

    if i % 2 == 0:
        ans += a
    else:
        ans -= b

print(ans)
