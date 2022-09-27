def solution(root):
    global final, count, result
    if root > final:
        return
    if root == final:
        # print(count)
        result = count
        return
    else:
        for i in range(1, bus_stop[root]+1):
            count += 1
            if count < result: # 가지치기
                solution(root+i)
            count -= 1

T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    result = 1000000
    final = arr[0]
    bus_stop = [0] + arr[1:] + [0]
    count = 0
    solution(1)
    print(f'#{test_case} {result-1}')
    
