def solution(arr):
    # 가로 / 세로로 확인
    for i in range(9):
        list_a = []
        list_b = []
        for j in range(9):
            list_a.append(arr[i][j])
            list_b.append(arr[j][i])
        list_a.sort()
        list_b.sort()
        if list_a != [1,2,3,4,5,6,7,8,9]:
            return False
        if list_b != [1,2,3,4,5,6,7,8,9]:
            return False
    # 3*3으로 확인할 경우
    for i in range(0,9,3):
        for j in range(0,9,3):
            # 결과값 확인하기 위한 리스트
            list_c = []
            # 3*3 박스 만들기
            for a in range(i,i+3):
                for b in range(j,j+3):
                    list_c.append(arr[a][b])
            list_c.sort()
            if list_c != [1,2,3,4,5,6,7,8,9]:
                return False
    return True
            
    
    
T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = solution(arr)
    if result:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')