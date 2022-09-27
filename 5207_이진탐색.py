def binary_search(start,end):
    global result, count
    while start <= end:
        mid = (start + end) // 2
        if mid >= N: # 인덱스 값을 넘어가면 끝낸다.
            return 
        if result > arr_1[mid]: # start가 움직임 => 0
            if direction[-1] == 0:
                return
            else:
                direction.append(0)
                start = mid + 1
        elif result < arr_1[mid]: # end가 움직임 => 1
            if direction[-1] == 1:
                return
            else:
                direction.append(1)
                end = mid - 1
        else: # mid가 result랑 같으면
            count += 1
            return

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_1.sort()
    arr_2 = list(map(int, input().split()))

    count = 0
    for i in arr_2:
        direction = [3] # 왼쪽을 0으로 오른쪽을 1로 둔다.
        result = i
        binary_search(0, N-1)
    print(f"#{test_case} {count}")
