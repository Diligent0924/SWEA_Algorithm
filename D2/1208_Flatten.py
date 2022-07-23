# 가장 높은 곳 => 가장 낮은 곳으로 옮기는 작업 수행
for test_case in range(1, 11):
    N = int(input())
    list_a = list(map(int, input().split()))
    count = 0
    while N > count:
        count += 1
        list_a[list_a.index(max(list_a))] = list_a[list_a.index(max(list_a))] - 1
        list_a[list_a.index(min(list_a))] = list_a[list_a.index(min(list_a))] + 1
    print(list_a)