def self_len(arr):
    count = 0
    for i in arr:
        count += 1
    return count


for test_case in range(1,11):
    N, password = input().split()
    stack =[]
    for i in password:
        if self_len(stack) == 0:
            stack.append(i)
            continue
        
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{test_case} {"".join(stack)}')