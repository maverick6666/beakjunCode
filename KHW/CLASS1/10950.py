testcase = int(input())
num1 = [0] * testcase
num2 = [0] * testcase

for i in range(testcase):
    num1[i],num2[i] = map(int,input().split())

for i in range(testcase):
    print(num1[i] + num2 [i])

