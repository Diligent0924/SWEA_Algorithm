def bfs(start_i, start_j):
    global result
    count = 0
    if graph[start_i][start_j] == 1: # 집이 1개일 때와 0개일 때를 잘 생각하면서 풀어야한다. => 이런거 시험에서 안알랴줄듯...
        house = 1
        profit = M
    else:
        house = 0
        profit = 0
    queue_list = [[(start_i, start_j)]]
    visited = [[0] * N for _ in range(N)]
    visited[start_i][start_j] = 1
    while queue_list: # 일부러 순서를 나타내기 위해서 queue_list형태로 나타냈음
        count += 1 # 한번 돌때마다 count를 늘려나가는 방식임.
        queue = queue_list.pop(0) # 제일 앞 리스트(어차피 queue_list는 항상 1개밖에없음)
        list_a = [] # queue_list에 담아줄것
        while queue:
            i, j = queue.pop(0)
            for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    list_a.append((ni, nj)) # 이후에 list_a자체를 queue_list에 넣을 것이기 때문에...
                    # 만약 집이 있다면 profit에 M만큼 추가
                    if graph[ni][nj] == 1:
                        house += 1
                        profit += M

        if profit - cost_list[count] >= 0:
            # print(f"house : {house}")
            result = max(result, house)

        queue_list.append(list_a)
        # visited가 전부 1이면 끝낸다.
        sum_visited = 0
        for visit in visited:
            sum_visited += sum(visit)
        if sum_visited == N*N:
            return


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N : 크기 / M : 집 비용
    graph = [list(map(int,input().split())) for _ in range(N)]

    # 결과값
    result = 1
    # 비용을 미리 list로 정의해둔다. => 이 방법을 사용했기 때문에 queue_list를 사용해야했음.
    cost_list = [1]
    for i in range(1, 2*N+30):
        a = 4 * i
        cost_list.append(cost_list[-1]+a)

    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print(f"#{test_case} {result}")