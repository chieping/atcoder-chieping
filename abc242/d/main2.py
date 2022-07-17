import sys
input = sys.stdin.readline
S = input()
Len = len(S)
Q = int(input())

def to_i(char):
    return ord(char) - 65 # A => 0

def to_c(num):
    return chr(num + 65)

for _ in range(Q):
    t, k = map(int, input().split())
    k -= 1
    # tとkから、該当の文字がSのどの文字由来なのか判定する
    if t <= 60:
        nth = k // 2**t
        k %= 2**t
    else:
        nth = 0
    count1 = '{:b}'.format(k).count('1')
    print(to_c((to_i(S[nth]) + t + count1) % 3))
