from collections import deque
from pprint import pprint
def bfs():
    queue = deque([(0, 0)])
    visited = [[10000000]*N for _ in range(N)]
    visited[0][0] = graph[0][0]
    while queue:
        # print(queue)
        # pprint(visited)
        i, j = queue.popleft()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[i][j] + graph[ni][nj] < visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + graph[ni][nj]
                queue.append((ni, nj))
    return visited[N-1][N-1]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    print(f"#{test_case} {bfs()}")