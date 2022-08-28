'''
버스 정류장 : 1 ~ 1000번
모든 버스 : A번 => B번 운행
일반 버스 : A => B사이의 모든 구간에서 정차
급행 버스 : 짝수 => A ~ B 짝수 번호에만 정차, 홀수인 경우 반대
광역 버스 : A짝수 => 4의 배수 / A 홀수 => 3의 배수 but 10의 배수는 X
'''

T = int(input())
for test_case in range(1, T+1):
    bus_stop = [0] * 1001 # 인덱스로 문제를 풀어본 것이 도움이 되었다.
    N = int(input())
    for _ in range(N):
        bus_type, A, B = map(int,input().split())
        # 1 => 일반버스, 2=> 급행, 3 => 광역
        if bus_type == 1:
            for i in range(A, B+1):
                bus_stop[i] += 1
        elif bus_type == 2:
            for i in range(A, B+1, 2):
                bus_stop[i] += 1
        elif bus_type == 3:
            if A % 2 == 0:
                for i in range(A, B+1):
                    if i % 4 == 0:
                        bus_stop[i] += 1
            else:
                for i in range(A, B+1):
                    if i % 3 == 0 and i % 10 != 0: # 숫자에 혼돈이 있었다. => 이런 조건들이 잘 이루어졌는지 다시 한번 확인해야할거 같다.
                        bus_stop[i] += 1

    print(f'#{test_case} {max(bus_stop)}')