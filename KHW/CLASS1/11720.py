N = int(input())
numbers = list(map(int,input()))
mul = 0

for i in range(N):
    mul +=  numbers[i]

print(mul)