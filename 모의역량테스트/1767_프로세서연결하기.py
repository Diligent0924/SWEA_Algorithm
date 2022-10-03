def permutation(root):
    global temp, total
    # print(f'root:{root}, total:{total} result:{result}')
    if root == count:
        print('---------------------------')
        print(result, total)
        return
    else:
        for direction in core_direction:
            possible = True
            if direction == 'None':
                continue
            elif direction == 'up':
                for i in range(temp[root][0]):
                    if graph[i][temp[root][1]]: # 1이든 2든 만난다면
                        possible = False # possible이 False이면 다음 root로 못넘어가게한다.
                        break # 현재 하는 부분을 그만 둔다.
                    else:
                        total += 1
                        graph[i][temp[root][1]] = 2 # 0 ~ 해당 세로길이까지를 2로 둔다.
            elif direction == 'down':
                for i in range(N-1,temp[root][0],-1):
                    if graph[i][temp[root][1]]:
                        possible = False
                        break
                    else:
                        total += 1
                        graph[i][temp[root][1]] = 2
            elif direction == 'left':
                for j in range(temp[root][0]):
                    if graph[temp[root][0]][j]:
                        possible = False
                        break
                    else:
                        total += 1
                        graph[temp[root][0]][j] = 2
            elif direction == 'right':
                for j in range(N-1,temp[root][0],-1):
                    if graph[temp[root][0]][j]:
                        possible = False
                        break
                    else:
                        total += 1
                        graph[temp[root][0]][j] = 2
                        
            if possible:
                result[root] = direction
                permutation(root+1)
            if not possible:
                continue
            
            if direction == 'None':
                continue
            elif direction == 'up':
                for i in range(temp[root][0]):
                    if graph[i][temp[root][1]] == 2:
                        total -= 1
                        graph[i][temp[root][1]] = 0 
            elif direction == 'down':
                for i in range(N-1,temp[root][0],-1):
                    if graph[i][temp[root][1]] == 2:
                        total -= 1
                        graph[i][temp[root][1]] = 0
            elif direction == 'left':
                for j in range(temp[root][0]):
                    if graph[temp[root][0]][j] == 2:
                        total -= 1
                        graph[temp[root][0]][j] = 0
            elif direction == 'right':
                for j in range(N-1,temp[root][0],-1):
                    if graph[temp[root][0]][j] == 2:
                        total -= 1
                        graph[temp[root][0]][j] = 0
            

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 가운데 코어 수를 확인하기 위한 조건
    count = 0 
    temp = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if graph[i][j] == 1:
                count += 1
                temp.append((i,j))

    # 방향 제시
    core_direction = ['None','up','down','left','right']
    total = 0
    print(temp)
    result = [0] * count
    permutation(0)