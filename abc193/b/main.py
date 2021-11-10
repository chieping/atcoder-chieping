N = int(input())
shops = [list(map(int, input().split())) for i in range(N)]
buyable_prices = [s[1] for s in shops if s[2] > s[0]]
if len(buyable_prices):
    print(min(buyable_prices))
else:
    print(-1)
