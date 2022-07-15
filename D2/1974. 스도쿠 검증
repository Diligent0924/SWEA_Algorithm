# 가로줄 1~9 확인 / 세로줄 1~9 확인 / 3*3 박스 안에 1~9 확인
for test_case in range(1, int(input()) + 1):
    graph = [list(map(int,input().split())) for i in range(9)]
    graph_T = list(map(list,zip(*graph)))
    list_a = [1,2,3,4,5,6,7,8,9]
    break_i = False
    #가로
    for i in graph:
        if break_i == True:
            break
        i = sorted(i)
        for a,b in zip(i, list_a):
            if a != b:
                break_i = True
                print("#{0} 0".format(test_case))
                break
   #세로              
    for i in graph_T:
        if break_i == True:
            break
        i = sorted(i)
        for a,b in zip(i, list_a):
            if a != b:
                break_i = True
                print("#{0} 0".format(test_case))
                break
   #3*3
    list_b = [(0,3),(3,6),(6,9)]
    square = []
    for i in list_b:
        if break_i == True:
            break
        for j in range(i[0],i[1]):
            for h in range(i[0],i[1]):
                square.append(graph[j][h])
        square = sorted(square)
        for a,b in zip(square, list_a):
            if a!=b:
                break_i = True
                print("#{0} 0".format(test_case))
                break
        square = []
                
    if break_i == False:
        print("#{0} 1".format(test_case))
