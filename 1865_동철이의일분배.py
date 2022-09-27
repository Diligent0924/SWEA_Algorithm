def backtracking(root):
    global result, count
    if count * 100 < result: #뒤에 최대값이 1이기 때문에 현재 해당되는 수에서 확인이 가능하다.
        return
    if root == N:
        result = max(result, count * 100)
        return
    else:
        for i in range(N):
            if visited[i] or graph[root][i] == 0:
                continue
            else:
                visited[i] = 1
                count = count*graph[root][i]/100
                backtracking(root+1)
                count = count/graph[root][i]*100
                visited[i] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = 0
    count = float(1)
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N+1)
    backtracking(0)
    print(f'#{test_case} {result:.6f}')