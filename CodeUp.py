num = int(input("100보다 작은 수를 입력해주세요 : "))
if num < 100:
    a = num//10
    b = num-(a*10)
    if a == 2 and b == 2:
        print(f"십의 자리 : {a}, 일의 자리: {b}")
        print("오늘은 행운이 가득해요!!!")
    elif a == 2 and b != 2:
        print(f"십의 자리 : {a}, 일의 자리: {b}")
        print("오늘의 운세는 보통입니다~ 화이팅!")
    elif a != 2 and b == 2:
        print(f"십의 자리 : {a}, 일의 자리: {b}")
        print("오늘의 운세는 보통입니다~ 화이팅!")
    elif a%2 != 0 and b%2 != 0:
        print(f"십의 자리 : {a}, 일의 자리: {b}")
        print("오늘은 행운이 가득해요!!!")
    elif a%2 != 0 and b%2 == 0 or a%2 == 0 and b%2 != 0:
        print(f"십의 자리 : {a}, 일의 자리: {b}")
        print("오늘의 운세는 보통입니다~ 화이팅!")
    elif a%2 == 0 and b%2 == 0:
        print(f"십의 자리 : {a}, 일의 자리: {b}")
        print("오늘의 운세는 꽝..ㅠ 그래도 킵고잉~")
else:
    print("잘못된 입력입니다.")