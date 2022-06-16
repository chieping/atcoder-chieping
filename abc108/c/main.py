N, K = map(int, input().split())

if K % 2:
    # Kが奇数のときはa, b, cそれぞれKの倍数
    print((N//K)**3)
else:
    # Kが偶数のときは
    ans = 0
    # 1. a, b, cそれ ぞれKの倍数である場合
    ans += (N//K)**3
    # 2. a, b, cそれぞれ2/Kの倍数である場合
    ans += (1 + ((N-K//2)//K))**3
    print(ans)
