'''
상: 1, 하: 2, 좌: 3, 우: 4
'''
def direction_solution(direction):
    if direction == 1:
        new_direction = 2
    elif direction == 2:
        new_direction = 1
    elif direction == 3:
        new_direction = 4
    elif direction == 4:
        new_direction = 3
    return new_direction

delta = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]
def solution(): # 시간이 1시간 지날 때마다 확인하는 함수
    global arr
    temp = []
    while arr:
        s, g, number, direction = arr.pop(0)
        ds = s + delta[direction][0]
        dg = g + delta[direction][1]
        if ds == 0 or ds == N-1 or dg == 0 or dg == N-1: # 끝에 가면
            number = number // 2
            direction = direction_solution(direction)

        temp.append((ds, dg, number, direction))
    # print(f'temp : {temp}')
    # 만약 i,j가 같을 경우를 확인해 봐야 한다.
    index_b = []
    result = []
    for x in range(len(temp)):
        s, g, number, direction = temp[x]
        list_a = [number]
        list_b = [direction]
        for y in range(x+1, len(temp)):
            s_1, g_1, number_1, direction_1 = temp[y]
            if s == s_1 and g == g_1: # 같으면
                list_a.append(number_1)
                list_b.append(direction_1)
        if (s,g) not in index_b:
            index_b.append((s, g))
            result.append((s, g, sum(list_a), list_b[list_a.index(max(list_a))]))
    arr = result
    # print(f'arr : {arr}')

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split()) # N 정사각형 , M : 격리시간 , K : 군집 수
    arr = []
    for _ in range(K):
        s, g ,number, direction = map(int, input().split())
        arr.append((s,g,number,direction))
    print(f'arr:{arr}')
    for _ in range(M): # 시간경과에 따른 것
        solution()

    count = 0
    for a,b,c,d in arr:
        count += c
    print(f'#{test_case} {count}')