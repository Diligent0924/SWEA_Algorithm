N = int(input())
arr = list(map(lambda x: True if x == "1" else False,input().split()))
person = int(input())
for _ in range(person):
    sex, switch = map(int,input().split())
    if sex == 1:
        count = 0
        while True:
            count += 1
            if switch*count <= N:
                arr[switch*count-1] = not arr[switch*count-1]
            else:
                break
    else:
        switch -= 1
        arr[switch] = not arr[switch] # 처음 값을 변경
        left = switch-1 # 왼쪽으로 한칸
        right = switch + 1 # 오른쪽으로 한칸
        while True:
            if 0 <= left < N and 0 <= right < N:
                if arr[left] != arr[right]:
                    break
                else:
                    arr[left] = not arr[left]
                    arr[right] = not arr[right]
                    left -= 1
                    right += 1
            else:
                break
result = list(map(lambda x: 1 if x == True else 0,arr))
for i in range(N):
    if i % 20 == 0 and i != 0:
        print()
    print(result[i], end=' ')