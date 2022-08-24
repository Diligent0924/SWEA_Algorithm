'''

3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''

for test_case in range(1,int(input())+1):
    graph = [[0] * 10 for _ in range(10)]   
    N = int(input())
    list_a = [list(map(int,input().split())) for _ in range(N)]
    for i in list_a:
        for j in range(i[1],i[3]):
            for h in range(i[0],i[2]):
                if graph[j][h] != 0:
                    graph[j][h] = -1
                else:
                    graph[j][h] = i[4]
    count = 0
    for i in graph:
        count += i.count(-1)
    print(count)
    