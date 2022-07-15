for number in range(int(input())):
    N,K = map(int,input().split()) # N,K
    graph = [list(map(int,input().split())) for i in range(N)]
    result = 0
  	# 가로방향
    for i in graph:
    	count = 0
    	for j in i:
      		if j == 0:
        		if count == K:
          			result += 1
        		count = 0
      		else:
          		count += 1
    	if count == K:
            result += 1
  # 세로방향
    graph_T = list(map(list, zip(*graph)))
    for i in graph_T:
        count = 0
        for j in i:
            if j == 0:
                if count == K:
                    result += 1
                count = 0
            else:
                count += 1
        if count == K:
            result += 1
    print("#{0} {1}".format(number+1, result))
