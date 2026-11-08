
n,t=map(int,input().split())
a=list(map(int,input().split()))

p=[0]*(n+1)

for i in range(n):
    p[i+1]=p[i]+a[i]

while(t>0):
    l,r=map(int,input().split())
    print(p[r]-p[l-1])
    t-=1
