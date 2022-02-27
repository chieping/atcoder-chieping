from pprint import pprint
import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))

# Aをすべて0にするという問題に読み替える
# なるべく連結を切らさないように、数値を下げていく
