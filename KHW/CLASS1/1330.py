
while True:
    try:
        a, b = map(int, input().split())
        if -10000 <= a <= 10000 and -10000 <= b <= 10000:
            break
        else:
            print("다시 입력하세요")
    except ValueError:
        print("다시 입력하세요")

if a == b:
    print("==")
elif a > b:
    print(">")
elif a < b:
    print("<")
