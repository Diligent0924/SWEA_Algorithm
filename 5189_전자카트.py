from itertools import permutations as permu
def permutations(root):
    if root == N-1:
        p_1.append(tuple(new_arr))
        return
    else:
        for i in range(1, N):
            if visited[i]: # 만약 방문했다면 그냥 넘긴다.(같은 숫자면 넘김)
                continue
            new_arr[root] = i
            visited[i] = True
            permutations(root+1)
            visited[i] = False


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [i for i in range(2, N+1)]
    graph = [list(map(int, input().split())) for _ in range(N)]
    result = []
    visited = [0] * N # N만큼만 필요하기 때문에
    new_arr = [0] * (N-1)
    p_1 = []
    permutations(0)
    print(p_1)

    min_count = 100000000000
    for p_list in p_1:
        count = 0
        count += graph[0][p_list[0]]
        for j in range(len(p_list)-1):
            count += graph[p_list[j]][p_list[j+1]]
        count += graph[p_list[-1]][0]
        # print(count)
        min_count = min(min_count, count)
    print(f'#{test_case} {min_count}')