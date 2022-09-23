def dfs(i,j,direction):
    global answer
    # 만약 범위를 벗어난다면 끝난다.
    if i < 0 or i == N or j < 0 or j == N:
        return

    if i == start_i and j == start_j and complex_list:
        answer = max(answer, len(complex_list))
        return
    if graph[i][j] not in complex_list:
        # complex_list.append(graph[i][j])
        # if direction == 4:
        #     dfs(i+delta[direction][0], j+delta[direction][1], direction)
        # else:
        #     dfs(i+delta[direction][0], j+delta[direction][1], direction)
        #     complex_list.remove(graph[i][j])
        #     complex_list.append(graph[i][j])
        #     dfs(i+delta[direction+1][0], j+delta[direction+1][1], direction+1)
        # complex_list.remove(graph[i][j])

        complex_list.append(graph[i][j])
        if direction == 'north':
            dfs(i-1, j+1, 'north')
        elif direction == 'east':
            dfs(i+1, j+1, 'east')
            complex_list.remove(graph[i][j])
            complex_list.append(graph[i][j])
            dfs(i+1, j-1, 'south')
        elif direction == 'south':
            dfs(i+1, j-1, 'south')
            complex_list.remove(graph[i][j])
            complex_list.append(graph[i][j])
            dfs(i-1, j-1, 'west')
        elif direction == 'west':
            dfs(i-1, j-1, 'west')
            complex_list.remove(graph[i][j])
            complex_list.append(graph[i][j])
            dfs(i-1, j+1, 'north')
        complex_list.remove(graph[i][j])

delta = [[], [1, 1], [1, -1], [-1, -1], [-1, 1]]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int,input().split())) for _ in range(N)]
    answer = -1 # 결과값을 추출
    for i in range(N):
        for j in range(N):
            complex_list = []
            start_i = i
            start_j = j
            dfs(i, j, 'east')
    print(f'#{test_case} {answer}')