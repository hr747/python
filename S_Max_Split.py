s=input()
count=0
start=0
arr=[]
for i in range(len(s)):
    if s[i]=='L':
        count+=1
    else:
        count-=1

    if count==0:
        arr.append(s[start:i+1])
        start=i+1
print(len(arr))
for i in arr:
 print(i)
    