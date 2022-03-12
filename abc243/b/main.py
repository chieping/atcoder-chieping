from pprint import pprint
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = sum(A[i] == B[i] for i in range(N))

ans2 = len(set(A).intersection(set(B))) - ans1

print(ans1)
print(ans2)