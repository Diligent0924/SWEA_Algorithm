for test_case in range(1, int(input())+1):
    a, b = map(int, input().split())
    list_a = list(map(int, input().split()))
    result = []
    for i in range(1,a+1):
        if i not in list_a:
            result.append(str(i))
    print(f'#{test_case} {" ".join(result)}')