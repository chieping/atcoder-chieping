T = int(input())
case = [list(map(int, input().split())) for _ in range(T)]

for n2, n3, n4 in case:
    ans = 0
    # 3を2個使うケースを優先して消費する
    tmp = min(n3//2, n4)
    n3 -= tmp*2
    n4 -= tmp
    ans += tmp
    tmp = min(n3//2, n2//2)
    n2 -= tmp*2
    ans += tmp
    # 残った2と4を使って10を作る
    tmp = min(n2, n4//2)
    n4 -= tmp*2
    n2 -= tmp
    ans += tmp
    tmp = min(n2//3, n4)
    n2 -= tmp*3
    ans += tmp
    ans += n2//5
    print(ans)
