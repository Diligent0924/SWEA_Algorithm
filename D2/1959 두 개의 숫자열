from collections import deque 

for i in range(int(input())):
    a, b = map(int,input().split())
    ai = deque(list(map(int,input().split())))
    bi = deque(list(map(int,input().split())))
    result = sum([x*y for x,y in zip(ai,bi)])
    
    if a > b:
        while len(ai) > len(bi):
            bi.appendleft(0)
            result = max(result, sum([x*y for x,y in zip(ai,bi)]))
    else:
        while len(ai) < len(bi):
            ai.appendleft(0)
            result = max(result, sum([x*y for x,y in zip(ai,bi)]))
    print("#{0} {1}".format(i+1,result))
