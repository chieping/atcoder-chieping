# AtCoder上ではimportできないので提出する際はコードを貼り付ける
# SortedSetはSortedListを利用するので貼り付ける手間が多いのでSortedListを使用した
from sortedcontainers import SortedList

L, Q = map(int, input().split())

st = SortedList([0, L])

for _ in range(Q):
    c, x = map(int, input().split())

    if c == 1:
        st.add(x)
    else:
        i = st.bisect_left(x)
        print(st[i] - st[i-1])
