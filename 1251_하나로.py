def find_set(x):
    while x != p[x]:  # 대표원소가 아니면 (인덱스랑 해당 값이 다르면)
        x = p[x]  # x가 가리키는 정점으로 이동
    return x


T = int(input())
for test_case in range(1, T+1):
    V = int(input())
    x_arr = list(map(int, input().split()))
    y_arr = list(map(int, input().split()))
    point = []
    for x, y in zip(x_arr, y_arr):
        point.append((x,y))
    tax = float(input())
    rel = []
    # print(point)
    for i in range(V-1):
        for j in range(1, V):
            rel.append((tax * (abs(point[i][0]-point[j][0]) + abs(point[i][1]-point[j][1])) ** 2, i ,j))
    
    print(rel)

    rel.sort()  # 가중치 기준 오름차순 정렬

    p = [i for i in range(V + 1)]  # 대표원소 초기화

    N = V + 1  # 0~V번 까지의 정점
    cnt = 0
    total = 0  # 가중치의 합

    for w, u, v in rel:  # N-1개의 간선 선택 루프
        if find_set(u) != find_set(v):  # 사이클을 형성하지 않으면 선택
            cnt += 1
            total += w  # 가중치의 합
            p[find_set(v)] = find_set(u)  # v의 대표원소를 u의 대표원소로 바꿈
            if cnt == N - 1:
                break
    print(f'#{test_case} {int(total)}')