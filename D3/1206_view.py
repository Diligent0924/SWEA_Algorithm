from collections import deque
for test_case in range(10):
    N = int(input())
    list_a = list(map(int, input().split()))
    diff_a = deque([list_a[0],list_a[1]]) # 처음 2개의 경우 미리 집어넣기(이 리스트로 앞/뒤 2칸씩 비교)
    max_a,count = 0, 0
    for i in range(N):
        if (len(diff_a) == 5 or i == N-2 or i ==N-1): # 끝날 때에는 5개가 아니므로 예외처리
            diff_a.popleft()
        if i not in (N-2,N-1): # N-2부터는 i+2의 인덱스가 없으므로 예외처리
            diff_a.append(list_a[i+2])
        max_a = sorted(diff_a)[-2] # diff_a라는 5개를 sort해서 2번째 min값 찾기
        if list_a[i] == max(diff_a): # 만약 해당 i의 값이 최대라면 count하기
            count += list_a[i] - max_a
    print(f'#{test_case+1} {count}')