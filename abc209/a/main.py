A, B = map(int, input().split())

ans = 0
if A <= B:
    ans = B-A+1

print(ans)
