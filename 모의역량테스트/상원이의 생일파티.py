def solution():
    count = 0
    visited = [0] * (N+1)
    visited[1] = 1
    for x in rel[1]: # 상원이의 직접적인 친구들을 구한다.
        if not visited[x]:
            count += 1
            visited[x] = 1
    
        for y in rel[x]:
            if not visited[y]:
                count += 1
                visited[y] = 1            
    return count

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    rel = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        rel[a].append(b)
        rel[b].append(a)
    
    print(f"#{test_case} {solution()}")