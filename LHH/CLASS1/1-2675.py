n=int(input())
for i in range(n):
    r,s=input().split()
    for i in range(len(s)):
        print(int(r)*s[i],end="")
    print()