s = input()
N = len(s)
K = int(input())
INF = "z" * 6
Set = set()
ans = [INF] * 5

for i in range(N):
    for j in range(i+1, N+1):
        if j - i >= 6:
            break
        ss = s[i:j]
        for k in range(5):
            if ss not in Set and ss < ans[k]:
                ans.insert(k, ss)
                Set.add(ss)
                break
        ans = ans[:5]
print(ans[K-1])