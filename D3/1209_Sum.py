for test_case in range(1,11):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    graph_T = list(map(list,zip(*graph)))
    max_a = 0
    for i in graph:
        max_a = max(max_a,sum(i))
    for i in graph_T:
        max_a = max(max_a,sum(i))
    
    sum_a, sum_b = 0, 0 
    for i in range(0,100):
        sum_a += graph[i][i]
        sum_b += graph[i][99-i]
    max_a = max(max_a,sum_a,sum_b)
    print(f'#{N} {max_a}')