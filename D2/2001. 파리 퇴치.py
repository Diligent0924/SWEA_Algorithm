T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for i in range(N)]
    factor,result = 0, 0 
    #구현 1
    column_count = 0
    for number in range(N-M+1):
        for h in range(N-M+1):
            for i in range(number,M+number):
                for j in range(h,M+h):
                    factor += graph[i][j]
            result = max(result, factor)   
            factor = 0
    print("#{0} {1}".format(test_case,result))
