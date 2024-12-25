numlist = [0] * 9

for i in range(9):
    numlist[i] = int(input())

maxNum = max(numlist)
maxIndex = numlist.index(maxNum) + 1

print(maxNum)
print(maxIndex)