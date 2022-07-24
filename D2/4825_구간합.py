for test_case in range(1,int(input())+1):
    a, b = map(int,input().split())
    list_a = list(map(int,input().split()))
    max_a, min_a = 0, 1000000
    for i in range(len(list_a)-b+1):
        list_b = list_a[i:i+b]
        max_a = max(max_a, sum(list_b))
        min_a = min(min_a, sum(list_b))
    print(f'#{test_case} {max_a - min_a}')
