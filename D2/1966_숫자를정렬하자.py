T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    # 해당 arr에서 최대값을 찾는다.
    max_arr = 0
    for i in arr:
        if i > max_arr:
            max_arr = i
    # 최댓값의 +1 만큼까지 index가 필요하므로 저장한다.
    count_list = [0] * (max_arr+1)

    # 해당 인덱스에 +1 을 해서 index-count 관계를 성립시킨다.
    for i in arr:
        count_list[i] = count_list[i] + 1
    
    # count_list 전체를 앞에서부터 확인해서 개수가 1이상이면 result에 넣어준다.
    result = []
    for i in range(max_arr+1):
        while count_list[i] != 0:
            result.append(i)
            count_list[i] -= 1
    print(f'#{test_case}',end=' ')
    print(*result)