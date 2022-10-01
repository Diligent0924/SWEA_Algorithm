'''
모든 충돌 가능한 경우의 수를 구한 뒤에 시간 순서대로 먼저 일어나는 충돌을 처리한다.
'''
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        arr.append((x,y,d,k))
    
    count = 0
    multicampus = []
    for i in range(N):
        x_1, y_1, d_1 = arr[i]
        distance = [] # (거리, 에너지) 형태의 튜플 생성
        for j in range(N):
            if i == j:
                continue
            x_2, y_2, d_2,  = arr[j]
            if d_1 == 3:
                if x_1 < x_2: # 무조건 x_2가 더 커야함
                    if d_2 == 2 and y_1 == y_2:
                        distance.append((abs(x_2 - x_1) / 2, i, j))
                    elif (d_2 == 0 and y_1 > y_2) or (d_2 == 1 and y_1 < y_2):
                        if abs(x_2 - x_1) == abs(y_2 - y_1):
                            distance.append((abs(x_2 - x_1), i, j))
            elif d_1 == 2:
                if x_1 > x_2:
                    if d_2 == 3 and y_1 == y_2:
                        distance.append((abs(x_2 - x_1) / 2, i, j))
                    elif (d_2 == 0 and y_1 > y_2) or (d_2 == 1 and y_1 < y_2):
                        if abs(x_2 - x_1) == abs(y_2 - y_1):
                            distance.append((abs(x_2 - x_1), i, j))
            elif d_1 == 1:
                if y_1 > y_2:
                    if d_2 == 0 and x_1 == x_2:
                        distance.append((abs(y_2 - y_1) / 2, i, j))
                    elif (d_2 == 2 and x_1 < x_2) or (d_2 == 3 and x_1 > x_2):
                        if abs(x_2 - x_1) == abs(y_2 - y_1):
                            distance.append((abs(y_2 - y_1), i, j))
            elif d_1 == 0:
                if y_1 < y_2:
                    if d_2 == 1 and x_1 == x_2:
                            distance.append((abs(y_2 - y_1) / 2, i, j))
                    elif (d_2 == 2 and x_1 < x_2) or (d_2 == 3 and x_1 > x_2):
                        if abs(x_2 - x_1) == abs(y_2 - y_1):
                            distance.append((abs(y_2 - y_1), i, j))
        
        multicampus.extend(distance)

    multicampus.sort()

    list_a = [0] * N # visited랑 같은 개념
    count = 0
    # multicampus 자체가 시간이 무조건 빠른 순서대로 sort되어있기 때문에 순서대로 넣는게 가능하다.
    for d, i, j in multicampus:
        if not list_a[i] and not list_a[j]: # 
            count += arr[j][3]
            count += arr[i][3]
            list_a[i] = d
            list_a[j] = d
        elif list_a[i] and not list_a[j]:
            if list_a[i] == d:
                count += arr[j][3]
                list_a[j] = d 
        elif not list_a[i] and list_a[j]:
            if list_a[j] == d:
                count += arr[i][3]
                list_a[i] = d 

    print(f'#{test_case} {count}')