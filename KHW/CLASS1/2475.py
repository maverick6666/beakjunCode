while True:
    try:
        a,b,c,d,e=map(int,input().split())

        #각 자리수가 0~9만 들어가게 설정
        if 0<=a <=9 and 0<=b <=9 and 0<=c <=9 and 0<=d <=9 and 0<=e <=9:
            break
        else:
            print("다시 입력하세요")
    except ValueError:
        print("다시 입력하세요")

all = a**2+b**2+c**2+d**2+e**2

print(all % 10)