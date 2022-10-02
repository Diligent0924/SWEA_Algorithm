def dijkstra():
    queue = [(0,0)]
    while queue:
        # print(queue)
        n, w = queue.pop(0) # 뒤로 돌아도 되나?
        if visited[n] > w:
            visited[n] = w
            for x in arr[n]:
                queue.append((x[0],w+x[1]))
    return


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        arr[s].append((e,w))
    print(arr)
    for i in range(1,N+1):
        if arr[i]:
            arr[i].sort(key=lambda x: x[1])
    print(arr)
    visited = [1000000] * (N+1)
    dijkstra()
    print(f"#{test_case} {visited[-1]}")
    