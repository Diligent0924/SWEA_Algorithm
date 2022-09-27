def permutation(root):
    global count, result
    if root == N:
        result = min(result, count)
        return
    else:
        for i in range(N):
            if visited[i]:
                continue
            
            value = graph[root][i]
            visited[i] = 1
            count += value
            if count < result:
                permutation(root+1)
            count -= value
            visited[i] = 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N+1)
    count = 0
    result = 100000000
    permutation(0)
    print(f"#{test_case} {result}")
