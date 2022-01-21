K = int(input())
S = 0
# K回繰り返しても割り切れないときは少なくとも
# どこか2回訪れている数があり、ループしているという
# ことになり、どこまでやっても割り切れないことがわかる
for i in range(1, K+1):
    S = (S*10+7) % K
    if S == 0:
        print(i)
        break
else:
    print(-1)
