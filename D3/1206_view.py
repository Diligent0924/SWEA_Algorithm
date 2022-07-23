from collections import deque
for test_case in range(10):
    N = int(input())
    list_a = list(map(int, input().split()))
    diff_a = deque([list_a[0],list_a[1]])
    max_a,count = 0, 0
    for i in range(N):
        if (len(diff_a) == 5 or i == N-2 or i ==N-1):
            diff_a.popleft()
        if i not in (N-2,N-1):
            diff_a.append(list_a[i+2])
        max_a = sorted(diff_a)[-2]
        if list_a[i] == max(diff_a):
            count += list_a[i] - max_a
    print(f'#{test_case+1} {count}')