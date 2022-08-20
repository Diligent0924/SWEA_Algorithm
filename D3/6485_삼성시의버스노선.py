'''
문제에서 버스정류장의 개수가 이미 나와있다. => 꼼꼼히 확인
문제에 변수라고 판단되면 위의 주석부분에 미리미리 넣어놓자.
'''
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    # 버스가 지나가는 장소
    bus = [list(map(int,input().split())) for _ in range(N)]
    
    P = int(input()) # 버스정류장 수
    bus_stop = [int(input()) for _ in range(P)]
    bus_count = [0] * 5000 # 문제를 꼼꼼하게 읽어야할거 같다.
    for i in bus:
        for j in range(i[0],i[1]+1):
            bus_count[j-1] += 1

    result = []
    for i in bus_stop:
        result.append(bus_count[i-1])
    print(f'#{test_case} {" ".join(map(str,result))}')