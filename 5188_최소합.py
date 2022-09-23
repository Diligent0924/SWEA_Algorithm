def solution(i, j, count):
    global graph, result
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    else:
        if i == N-1 and j == N-1:
            count = count + graph[i][j]
            result = min(result, count)
            return
        else:
            solution(i, j+1, count+graph[i][j])
            solution(i+1, j, count+graph[i][j])

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    result = 1000000000
    solution(0,0,0)
    print(f"#{test_case} {result}")