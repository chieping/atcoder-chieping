T,N=map(int,input().split())
C=[0]*N
for p in [map(int,input().split())for _ in [0]*T]:
	C=list(map(max,zip(C,p)))
	print(sum(C))