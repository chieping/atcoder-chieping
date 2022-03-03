from collections import defaultdict
import heapq
import sys
readline = sys.stdin.readline
N, M = map(int, readline().split())
Bdict = defaultdict(list)
for _ in range(N):
    a, b = map(int, readline().split())
    Bdict[a].append(b)

ans = 0
heap = []
for i in range(1, M+1):
    # i日後にM日になるアルバイトを候補に追加
    for b in Bdict[i]:
        heapq.heappush(heap, -b)
    # 候補の中から最大を採用
    if len(heap):
        ans += -heapq.heappop(heap)

print(ans)
