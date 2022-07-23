for test_case in range(1, int(input()) + 1):
    print("#{0}".format(test_case))
    N = int(input())
    graph = [list(map(str, input().split())) for i in range(N)]
    word_1,word_2,word_3 = '','',''
    for i in range(N):
        for j in range(N):
            word_1 += graph[j][i]
            word_2 += graph[N-i-1][j]
            word_3 += graph[j][N-i-1]
        word_1 = word_1[::-1]
        word_2 = word_2[::-1]
        print("{0} {1} {2}".format(word_1,word_2,word_3))
        word_1,word_2,word_3 = '', '',''
