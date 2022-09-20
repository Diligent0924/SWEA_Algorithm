T = int(input())
for test_case in range(1, T+1):
    arr = [0] * 13
    N = float(input())
    for i in range(13):
        if N >= 2**(-(i+1)):
            N -= 2**(-(i+1))
            arr[i] = 1

        if N == 0:
            break

    if N > 0:
        print(f'#{test_case} overflow')
    else:
        word = ''.join(map(str, arr))
        print(f'#{test_case} {word.rstrip("0")}')
