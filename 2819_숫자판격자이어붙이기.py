def bfs(start_i, start_j, word):
    global result, count
    if len(word) == 7:
        if word not in result:
            result.append(word)
            count += 1
        return
    else:
        for di , dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni = di + start_i
            nj = dj + start_j
            if 0 <= ni < 4 and 0 <= nj < 4:
                new_word = word + graph[ni][nj]
                bfs(ni, nj, new_word)

T = int(input())
for test_case in range(1, T+1):
    graph = [list(map(str, input().split())) for _ in range(4)]
    result = []
    count = 0
    for i in range(4):
        for j in range(4):
            bfs(i, j, graph[i][j])

    print(f"#{test_case} {count}")

