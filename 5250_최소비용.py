def bfs():
    queue = [(0,0)]
    visited[0][0] = 0
    while queue:
        # print(f'queue : {queue}')
        i, j = queue.pop(0)
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx = i + dx
            ny = j + dy
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > graph[i][j] and visited[nx][ny] > visited[i][j] + graph[nx][ny] - graph[i][j]+1:
                    visited[nx][ny] = visited[i][j] + graph[nx][ny] - graph[i][j]+1 # 이런부분 조심해야한다.
                    queue.append((nx,ny))
                elif graph[nx][ny] <= graph[i][j] and visited[nx][ny] > visited[i][j] + 1:
                    visited[nx][ny] = visited[i][j] + 1
                    queue.append((nx,ny))
    # print(visited)
    print(f"#{test_case} {visited[N-1][N-1]}")
    return

    

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[1000000] * N for _ in range(N)]
    bfs()
    # print(f"#{test_case} {min_count}")