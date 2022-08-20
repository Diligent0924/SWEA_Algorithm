from cgi import test


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    buy = 0 # 살때의 가격 
    count = 0 # 사는것의 개수
    profit = 0 # 이익
    index = 0 # 최고시점일 때의 index
    while True:
        # 최대값을 찾자
        max_arr = 0
        for i in range(index,N): # 0 ~ N, 
            if arr[i] > max_arr:
                max_arr = arr[i] # 3
        # print(max_arr)  
        # print(buy,count,profit)
        for i in range(index,N): # 0 ~ N
            if arr[i] == max_arr:
                profit += max_arr * count - buy
                buy = 0
                count = 0
                index = i + 1
                break
            else:
                buy += arr[i]  # 최대 하나씩 추가이므로
                count += 1

        if index == N:
            break
    print(f'#{test_case} {profit}')