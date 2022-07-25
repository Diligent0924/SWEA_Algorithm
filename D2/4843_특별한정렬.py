from collections import deque
for test_case in range(1, int(input())+1):
    N = int(input())
    list_a = deque(sorted([int(i) for i in input().split()]))
    result = []
    while len(list_a) > 0:
        a = str(list_a.pop())
        b = str(list_a.popleft())
        result.extend([a,b])
        if len(result) == 10:
            break
    print(f'#{test_case} {" ".join(result)}')