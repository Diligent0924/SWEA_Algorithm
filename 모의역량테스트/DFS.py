'''
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6
'''
def dfs(graph, start_node):
    # need_visited : ??, visited : 방문한 곳
    need_visited, visited = [],[]
    need_visited.append(start_node)
    
    while need_visited:
        print(f'graph : {graph}')
        print(f'need_visited : {need_visited}')
        print(f'visited : {visited}')
        
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
        print(f'need_visited_final : {need_visited}')
        print(f'visited_final : {visited}')
    return visited

# 인덱스를 기준으로 푼다.
T = int(input())
for test_case in range(1,T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        # graph[b-1].append(a-1) # 양방향일 경우에만 사용
    S, G = map(int, input().split())
    print(dfs(graph,S-1))