A, B = map(int, input().split())

def f(a):
    # x と x + 1 の xor は 1 になる
    # 0から数えて x と x + 1 のペアの数は
    cnt = (a + 1) // 2
    # ペアの数が奇数の場合、1が余る
    fans = cnt % 2
    # ペアにならなかった数がある場合
    if a % 2 == 0:
        fans ^= a
    return fans

print(f(B) ^ f(A - 1))
