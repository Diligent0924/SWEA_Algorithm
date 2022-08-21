T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    direction = 0
    i,j = 0, -1 # i => 세로, j => 가로
    for number in range(1,N*N+1):
        # print(i,j)
        # print(arr)        
        if (0 <= i + dy[direction%4] < N and 0 <= j + dx[direction%4] < N):
            if arr[i + dy[direction%4]][j + dx[direction%4]] != 0: # 안쪽에서 충돌되는 부분에서 오래걸렸다.
                direction += 1
                i = i + dy[direction%4]
                j = j + dx[direction%4]
                arr[i][j] = number
                continue
            else:
                i = i + dy[direction%4]
                j = j + dx[direction%4]
                arr[i][j] = number
        else:
            print(1)
            direction += 1
            i = i + dy[direction%4]
            j = j + dx[direction%4]
            arr[i][j] = number
    print(f'#{test_case}')
    for i in arr:
        print(*i)