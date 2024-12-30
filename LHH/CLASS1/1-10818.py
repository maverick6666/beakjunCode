x=input()
n=list(map(int,input().split()))
max=n[0]
min=n[0]
for i in range(len(n)):
    if(max<n[i]):
        max=n[i]
    if(min>n[i]):
        min=n[i]
print(min,max)
