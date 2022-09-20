
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 한면의 길이
            size = 0
            while True:
                size += 1
                delta_right_down(i, j, 0)
