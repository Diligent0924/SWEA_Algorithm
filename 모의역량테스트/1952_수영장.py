T = int(input())

for test_case in range(1,T+1):
    price = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    # 월별 price 가격
    price_list = [0] * 12
    # 일일권과 월간권에서 각 month별로 뭐가 더 큰지 확인
    for i in range(11):
        day = arr[i] * price[0]
        month = price[1]
        if day > month:
            price_list[i] = day
        else:
            price_list[i] = month
            