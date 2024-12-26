testcase = int(input())
for i in range(testcase):
    test = list(map(str,input().split()))
    R = int(test[0])
    S = list(test[1])

for j in range(len(S)):
    P = ''.join(R*S)
    print(P)