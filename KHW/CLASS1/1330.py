
while True:
    a, b = input().split()

    if (a < -10000 or a > 10000):
        print("다시 입력하세요")
    elif (b < -10000 or b > 10000):
        print("다시 입력하세요")
    else:
        break

if a == b:
    print("==")
elif a > b:
    print(">")
elif a < b:
    print("<")
