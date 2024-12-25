a = int(input())

fourX = a % 4
hundredX = a % 100
fourHunX = a % 400

if (fourX == 0 and hundredX != 0) or (fourHunX == 0):
    print("1")
else:
    print("0")
    