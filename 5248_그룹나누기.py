'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
'''
def bfs(i):
    global count
    if visited[i]:
        return
    queue = [i]
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = 1
            queue.extend(node_list[node])
    count += 1

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    node_list = [[] for _ in range(N+1)]
    for i in range(1, len(arr),2):
        a,b = arr[i-1], arr[i]
        node_list[a].append(b)
        node_list[b].append(a)
    # print(node_list)
    count = 0
    visited = [0] * (N+1)
    for i in range(1,N+1):
        bfs(i)
    print(f'#{test_case} {count}')