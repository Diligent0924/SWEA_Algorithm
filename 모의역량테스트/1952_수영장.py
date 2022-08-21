# import sys
# sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    price = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    # 월별 price 가격
    price_list = [0] * 12
    # 일일권과 월간권에서 각 month별로 뭐가 더 큰지 확인
    for i in range(12):
        day = arr[i] * price[0]
        month = price[1]
        if arr[i] == 0:
            continue
        else:
            if day > month:
                price_list[i] = month
            else:
                price_list[i] = day
    # 분기권와 위를 비교해서 높은것을 확인하기
    branch_list = []
    for i in range(10):
        if price_list[i] + price_list[i+1] + price_list[i+2] >= price[2]:
            branch_list.append([i,i+1,i+2])
    if price_list[10] + price_list[11] > price[2]:
        branch_list.append([10,11])
    if price_list[11] > price[2]:
        branch_list.append([11])
    # print(price_list)
    print(branch_list)
    i = -1 # 첫번째 인덱스
    branch_result = 100000000 # 가장 작은것을 위한 변수
    last_count = 0
    last_number = 0
    while i < len(branch_list)-1:
        count = 1
        copy_price_list = price_list
        i += 1
        # branch_list에서 분기가 들어갈만한 인덱스에 값을 넣는다.
        print(f'first_ {last_number}')
        for a in branch_list[i]:
            copy_price_list[a] = price[2]
            last_number = a
        print(f'second_ {last_number}')
        j = i # i = 0 이면 j는 i+1부터 서칭해야하므로
        # 앞과 뒤의 index를 확인하면서 copy에 넣는 방법
        while j < len(branch_list)-1:
            j += 1
            print(f'branch {branch_list[j][0]} {last_number}')
            if branch_list[j][0] > last_number:
                print(f'branch pass {branch_list[j][0]} {last_number}')
                count += 1
                for b in branch_list[j]:
                    copy_price_list[b] = price[2]
                    last_number = b
                print(f'last_number {last_number}')
                continue
        print(f'copy_price_list {copy_price_list}')
        # 전체 copy한 것 중에서 가장 작은 값을 확인하기
        if branch_result > sum(copy_price_list):
            branch_result = sum(copy_price_list)
            price_list = copy_price_list
            last_count = count

    result = 0
    for i in price_list:
        if i != price[2]:
            result += i
    result += price[2] * last_count
    
    # if result > price[3]:
    #     print(price[3])
    # else:
    #     print(result)
    print(price_list)
    print(last_count)
    print(result)
    print("------end-------")