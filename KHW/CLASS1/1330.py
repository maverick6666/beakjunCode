# 무한 루프 시작
while True:
    try:
        # 두 정수 입력받기
        a, b = map(int, input().split())

        # 입력 값이 범위 내에 있는지 확인
        if -10000 <= a <= 10000 and -10000 <= b <= 10000:
            break  # 조건 만족하면 루프 종료
        else:
            print("다시 입력하세요")  # 범위 외 입력시 재입력 요청
    except ValueError:
        # 숫자가 아닌 값 입력 시 재입력 요청
        print("다시 입력하세요")

# a와 b 비교 후 결과 출력
if a == b:
    print("==")
elif a > b:
    print(">")
elif a < b:
    print("<")