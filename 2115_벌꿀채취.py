def backtracking(root):
    global result, temp
    # print(temp)
    if root == M:
        print(temp)
        result.append(temp[:]) # 얕은 복사하는 것
        return
    else:
        for x in range(N):
            for y in range(N):
                if visited[x][y]:
                    continue
                visited[x][y] = 1
                temp[root] = arr[x][y]
                backtracking(root+1)
                visited[x][y] = 0

T = int(input())
for test_case in range(1, T+1):
    N, M, C = map(int,input().split()) # N: 벌통크기, M: 벌통 개수, C: 최대 양
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    temp = [0] * M
    visited = [[0] * N for _ in range(N)]
    backtracking(0)
    print(result)