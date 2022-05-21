import math
A, B, H, M = map(int, input().split())

# 時針の先端の位置
a_rad = 2 * (H*60 + M) / 720 * math.pi
a_y = math.sin(a_rad) * A
a_x = math.cos(a_rad) * A

# 分針の先端の位置
b_rad = 2 * M / 60 * math.pi
b_y = math.sin(b_rad) * B
b_x = math.cos(b_rad) * B

# 距離を求める
ans = ((a_y - b_y)**2 + (a_x - b_x)**2)**(1/2)
print(ans)
