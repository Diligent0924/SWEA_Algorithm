def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2] # 가운데 있는 것을 pivot으로 두고 시작한다.
    less_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            less_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(less_arr) + equal_arr + quick_sort(greater_arr)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = quick_sort(arr)
    print(f"#{test_case} {result[N//2]}")