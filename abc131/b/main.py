N, L = map(int, input().split())
R = L+N-1
if R <= 0:
    eat = R
elif L >= 0:
    eat = L
else:
    eat = 0
print(L*N+((N-1)*N//2) - eat)