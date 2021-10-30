import heapq
N, K = map(int, input().split())

def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)
def _heappop_max(heap):
    """Maxheap version of a heappop."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup_max(heap, 0)
        return returnitem
    return lastelt

q = []
for i in range(N):
    a, b = map(int, input().split())
    _heappush_max(q, [b, a-b])

ans = 0
while K > 0 and len(q) > 0:
    greatest = _heappop_max(q)
    K -= 1
    ans += greatest[0]
    if len(greatest) == 2:
        _heappush_max(q, [greatest[1]])

print(ans)
