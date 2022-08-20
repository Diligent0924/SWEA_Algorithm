'''

'''

T = int(input())
for test_case in range(1,T+1):
    arr = [list(input()) for _ in range(5)]

    max_arr_count = 0
    for i in arr:
        # i의 len값을 찾는다.
        count = 0
        for j in i:
            count += 1
        # len값과 max_arr_count를 비교한다.
        if count > max_arr_count:
            max_arr_count = count

    for i in range(5):
        count = 0
        for j in arr[i]:
            count += 1
        
        if count < max_arr_count:
            arr[i] = arr[i] + [-1] * (max_arr_count - count)
    
    word = ''
    for i in range(max_arr_count):
        for j in range(5):
            if arr[j][i] == -1:
                continue
            else:
                word += arr[j][i]
    print(f'#{test_case} {word}')