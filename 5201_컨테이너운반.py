T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    N_weight_list = list(map(int, input().split()))
    M_weight_list = list(map(int, input().split()))
    N_weight_list.sort(reverse=True)
    M_weight_list.sort(reverse=True)

    count = 0
    for M_weight in M_weight_list:
        for N_weight in N_weight_list:
            if M_weight >= N_weight:
                # print(N_weight)
                count += N_weight
                N_weight_list.remove(N_weight)
                break
    print(f"#{test_case} {count}")
