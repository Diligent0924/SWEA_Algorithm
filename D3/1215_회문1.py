for test_case in range(1,11):
    N = int(input())
    graph = [list(map(str, input())) for _ in range(8)]
    graph_T = list(map(list,zip(*graph)))
    result = 0 
    for i in graph:
        count_a = 0
        while 8 >= count_a+N:
            if i[count_a:count_a+N] == i[count_a:count_a+N][::-1]:
                result += 1
            count_a += 1
            
    for i in graph_T:
        count_a = 0
        while 8 >= count_a+N:
            if i[count_a:count_a+N] == i[count_a:count_a+N][::-1]:
                result += 1
            count_a += 1
    print(f'#{test_case} {result}')
            
    