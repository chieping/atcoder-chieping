N=int(input())
B=[10**6]+list(map(int,input().split()))+[10**6]
print(sum(min(B[i],B[i+1])for i in range(N)))