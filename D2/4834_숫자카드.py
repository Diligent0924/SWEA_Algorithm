from collections import Counter
for test_case in range(1, int(input())+1):
    N = int(input())
    list_a = Counter([int(i) for i in str(input())])
    max_a, result = 0, []
    for i in list_a:
        max_a = max(max_a, list_a[i])
    for i in list_a:
        if list_a[i] == max_a:
            result.append(i)
    print(f'#{test_case} {max(result)} {max_a}')