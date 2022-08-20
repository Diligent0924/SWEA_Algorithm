'''
N : 퍼즐 크기, K: 특정 길이값, T : 테스트케이스
* 제약사항 : 반드시 K의값이랑 정확하게 맞아야한다.

1시간 반걸렸다...
index Error가 계속 나서 직접 공책에 확인을 해보니 빠르게 할 수 있었다.
Ctrl + C/V할 때 그냥 똑같이 붙여넣는데 변수를 안바꿔줘서 Error가 많이 났다.
다음부터는 제발 복붙할 때 변수나 이런것들 좀 신경써서 생각하자.

'''

T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    count = 0 # 개수를 셀 때 사용
    for i in range(N):
        for j in range(N-K+1):
            if arr[i][j:j+K] == [1] * K:
                if j+K == N:
                    if arr[i][j-1] == 0:
                        count += 1
                    else:
                        continue
                elif j == 0:
                    if arr[i][j+K] == 0:
                        count += 1
                    else:
                        continue
                elif arr[i][j+K] == 0 and arr[i][j-1] == 0:
                    count += 1
    # 가로와 세로를 변경할 때 사용하는 방법
    arr_T = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_T[i][j] = arr[j][i]
            
    for i in range(N):
        for j in range(N-K+1):
            if arr_T[i][j:j+K] == [1] * K:
                if j+K == N:
                    if arr_T[i][j-1] == 0:
                        count += 1
                    else:
                        continue
                elif j == 0:
                    if arr_T[i][j+K] == 0:
                        count += 1
                    else:
                        continue
                elif arr_T[i][j+K] == 0 and arr_T[i][j-1] == 0:
                    count += 1

    print(f'#{test_case} {count}')