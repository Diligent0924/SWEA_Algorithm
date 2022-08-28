'''
사람 : N명
M초마다 K개의 붕어빵을 만든다.
기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램 작성

구현 방식
1초마다 증가하면서 붕어빵을 만들고 손님이 해다 초에 있을 때 붕어빵이 있는지를 확인하는 방법으로 진행
처음 붕어빵이 만들어지는 초보다 사람이 빨리 왔다면 미리 제거
'''
def solution(second, bung):
    while second < arr[-1]:
        second += 1  # 1초씩 증가한다.
        if second % M == 0:
            bung += K
        # second == arr[0]와 같을 때만 하기
        while second == arr[0]:
            arr.pop(0)
            if bung > 0:
                bung -= 1
            elif bung <= 0:
                return False

            if len(arr) == 0: # 만약 끝까지 갔다면 전부 가능하다고 판단하는 것이기 때문에
                return True


T = int(input())
for test_case in range(1, T+1):
    people, M, K = map(int, input().split()) # people / M : 붕어빵이 만들어지는 시간 / K : 붕어빵 개수
    arr = list(map(int, input().split()))
    arr.sort()

    bung = 0
    second = 0

    if M > arr[0]:
        print(f'#{test_case} Impossible')
        continue
    else:
        a = solution(second, bung)

    if a:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')