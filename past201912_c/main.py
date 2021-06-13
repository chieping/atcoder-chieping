import io
import sys
_INPUT = """\
4 18 25 20 9 13
"""
sys.stdin = io.StringIO(_INPUT)

S = list(map(int, input().split()))
S.sort(reverse=True)

print(S[2])

