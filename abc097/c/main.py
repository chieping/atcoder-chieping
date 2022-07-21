S = input()
N = len(S)
K = int(input())
INF = "z" * 6
sub_set = set()
ans = [INF] * 5

for i in range(N):
    for j in range(i+1, N+1):
        if j - i > 5:
            break
        subs = S[i:j]
        for k in range(5):
            if subs not in sub_set and subs < ans[k]:
                ans.insert(k, subs)
                sub_set.add(subs)
                break
        ans = ans[:5]
print(ans[K-1])