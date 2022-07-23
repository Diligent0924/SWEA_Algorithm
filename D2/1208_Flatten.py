# 가장 높은 곳 => 가장 낮은 곳으로 옮기는 작업 수행
# 간단하게 풀 수 있는 문제
for test_case in range(1, 11):
    N = int(input())
    list_a = list(map(int, input().split()))
    count = 0
    while N > count:
        count += 1
        list_a[list_a.index(max(list_a))] = list_a[list_a.index(max(list_a))] - 1
        list_a[list_a.index(min(list_a))] = list_a[list_a.index(min(list_a))] + 1
    print(list_a)
    
# 새로 알게 된 것
# list_a.index('')으로 해당 자료의 index를 알 수 있다.
# index로 해당값의 위치를 알고 싶을 떄는 list_a[], 값으로 알고싶을 경우에는 list_a.index('')를 사용한다
# index가 필요할 떄는 enumerate의 사용도 좋은것 같다.