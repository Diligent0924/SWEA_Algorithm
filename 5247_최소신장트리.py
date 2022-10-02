def find_set(x):
    while x != p[x]:  # 대표원소가 아니면 (인덱스랑 해당 값이 다르면)
        x = p[x]  # x가 가리키는 정점으로 이동
    return x


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    edge = []

    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append((w, u, v))

    edge.sort()  # 가중치 기준 오름차순 정렬

    p = [i for i in range(V + 1)]  # 대표원소 초기화

    # N개의 정점이 있으면 사이클이 생기지 않도록 N-1개의 간선을 선택
    # MST에 포함된 간선의 가중치의 합 구하기
    N = V + 1  # 0~V번 까지의 정점
    cnt = 0
    total = 0  # 가중치의 합

    for w, u, v in edge:  # N-1개의 간선 선택 루프
        if find_set(u) != find_set(v):  # 사이클을 형성하지 않으면 선택
            cnt += 1
            total += w  # 가중치의 합
            p[find_set(v)] = find_set(u)  # v의 대표원소를 u의 대표원소로 바꿈
            if cnt == N - 1:
                break
    print(f'#{test_case} {total}')

'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''