import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
for i in range(Q):
    E = int(input())
    # z = 高さ
    # z = -cos
    z = L/2-(L/2)*math.cos(2*math.pi*E/T)
    # print('z: ', z)

    # y = -sin
    y = -L/2*math.sin(2*math.pi*E/T)
    # print('y: ', y)

    # dist = xy平面での直線距離
    dist = math.sqrt(X**2+(Y-y)**2)
    # print('dist: ', dist)

    # zとdistからatanで求める
    ans = math.atan2(z, dist)
    ans = ans*180/math.pi
    print(ans)
