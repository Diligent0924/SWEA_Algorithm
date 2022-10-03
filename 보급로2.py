def dijkstra(start_i, start_j, end_i, end_j):
    total = 0
    visited = [[0] * N for _ in range(N)] # 방문여부 확인하기
    short_map = [[10000000] * N for _ in range(N)] # 값을 최대로 생각하기
    short_map[start_i][start_j] = 0
    queue = [(start_i, start_j, 0)]
    while queue:
        queue.sort(key=lambda x: x[2], reverse= True)
        i, j, min_a = queue.pop()
        # print(f'i : {i}, j : {j} {short_map}')
        visited[i][j] = 1
        for di, dj in ((0,1),(0,-1),(-1,0),(1,0)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and min_a + graph[ni][nj] < short_map[ni][nj]:
                queue.append((ni, nj, min_a + graph[ni][nj]))
                short_map[ni][nj] = min_a + graph[ni][nj]
                if ni == end_i and nj == end_j: # 가장 빠른 길을 찾았으므로 바로 끝내면 된다.
                    total = short_map[ni][nj]
                    return total
     
    
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(lambda x: int(x) , list(input()))) for _ in range(N)]
    print(f"#{test_case} {dijkstra(0 , 0, N-1, N-1)}")