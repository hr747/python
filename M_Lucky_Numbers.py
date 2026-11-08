a,b=map(int,input().split())
f=False
for i in range(a,b+1):
    if all(c in '47' for c in str(i)):
        print(i,end=" ")
        f=True
if not f:
 print(-1)  
    