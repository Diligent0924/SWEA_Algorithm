for test_case in range(1, int(input())+1):
    N = int(input())
    list_a = list(map(int, input().split()))
    print(f'#{test_case} {max(list_a) - min(list_a)}')