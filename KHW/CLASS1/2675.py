testcase = int(input())
for i in range(testcase):
    R,S = input().split()

    for i in S:
        print(i*int(R),end='')
    print()