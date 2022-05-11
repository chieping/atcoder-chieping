a, b = map(int, input().split())
ans = list(range(1, a)) + list(range(-1, -b, -1))
if a > b:
    ans.append(a)
else:
    ans.append(-b)
ans.append(0 - sum(ans))
print(*ans)
