'''
제일 앞의 수가 클수록 뒤의 수가 작을수록 크기가 커진다.
제일 앞에 수와 제일 뒤에서부터 확인해서 제일 큰값과 변경
뒤의 수 중에서 최대값이 여러개라면 어떤 위치로 바꿀지 고민해야함 => 통상적으로는 제일 뒤와 바뀌는게 제일 좋지만 32888과 같이 88832같은 경우 생각
'''

T = int(input())
def Selection(start):
    # print(arr)
    global full
    N = len(arr)
    if start == N:
        full = False
        return

    position = start
    count = 0
    for i in range(N-1, start, -1):
        count += 1
        if arr[i] > arr[position]:
            position = i # 원래는 제일앞과 맨뒤에서부터 큰값을 바꿔준다.(기본적으로)
            count = 0
            while start + count < len(arr)-1: # 32888일 경우 88832가 나와야하는데 88823이 나온다. => 단순히 뒤에서부터만 시작하면 Error가 뜬다.
                count += 1
                if arr[i-count] == arr[i] and arr[start] > arr[start+count]: # 32888에서 두번째 8과 바뀌어야하는데 이때 자리수를 확인하는 방법
                    position = i-count
    if position == start:
        Selection(start+1)
    else:
        arr[position], arr[start] = arr[start], arr[position]
        return



for test_case in range(1, T+1):
    number, change = input().split()
    change = int(change)
    arr = [int(i) for i in number]

    for _ in range(change): # 개수만큼 돌린다.
        full = True
        Selection(0)
        if not full:
            count= 1
            for i in arr:
                count = max(count, arr.count(i))
            if count == 1:
                arr[-2], arr[-1] = arr[-1], arr[-2]
    print(f"#{test_case} {''.join(map(str,arr))}")