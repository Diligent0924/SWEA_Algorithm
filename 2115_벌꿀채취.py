'''
벌통 크기 => N => 최대 10
반드시 2개여야 하며 중복되면 안된다. => 모든 경우의 수를 생각해볼까?

'''
def subset(bee):
    global M, C
    max_count = 0
    for i in range(1<<M):
        count = 0
        temp = []
        for j in range(M):
            if i & (1<<j):
                temp.append(bee[j])
        # temp의 합이 C보다 작을 경우에 각각을 제곱해서 확인한다.
        if sum(temp) <= C:
            for h in temp:
                count += h**2
            max_count = max(max_count, count)
    return max_count


def solution(number):
    global temp, result
    if number == 2:
        value_1 = subset(temp[0])
        value_2 = subset(temp[1])
        # print(f"temp : {temp} value_1 : {value_1} value_2 : {value_2}")
        value = value_1 + value_2
        result = max(value, result)
        return
    else:
        for i in range(N):
            for j in range(N-(M-1)):
                break_i = False
                for h in range(M):
                    if visited[i][j+h]:
                        break_i = True
                        break
                if break_i:
                    continue
                else:
                    for h in range(M):
                        visited[i][j+h] = 1
                    temp.append(graph[i][j:j+M])
                    solution(number+1)
                    temp.remove(graph[i][j:j+M])
                    for h in range(M):
                        visited[i][j+h] = 0

T = int(input())
for test_case in range(1, T+1):
    N, M, C = map(int, input().split()) # N: 정사각형 크기, M: 벌꿀채취의 크기, C: 최대 꿀의 양
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    temp = [] # 안에 넣는거
    result = 0
    solution(0)
    print(f"#{test_case} {result}")
