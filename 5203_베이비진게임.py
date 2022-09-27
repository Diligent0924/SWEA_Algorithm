T = int(input())
def babygin_1():
    global break_i
    if len(player_1) >= 3:
        for j in range(len(player_1)):
            if player_1.count(player_1[j]) >= 3:
                print(f'#{test_case} 1')
                break_i = True
                return
            if player_1[j] + 1 in player_1 and player_1[j] + 2 in player_1:
                print(f'#{test_case} 1')
                break_i = True
                return

def babygin_2():
    global break_i
    if len(player_2) >= 3:
        for j in range(len(player_2)):
            if player_2.count(player_2[j]) >= 3:
                print(f'#{test_case} 2')
                break_i = True
                return
            if player_2[j] + 1 in player_2 and player_2[j] + 2 in player_2:
                print(f'#{test_case} 2')
                break_i = True
                return


for test_case in range(1, T+1):
    cards = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    break_i = False
    for i in range(12):
        if i % 2 == 0:
            player_1.append(cards[i])
            babygin_1()
            if break_i:
                break
        else:
            player_2.append(cards[i])
            babygin_2()
            if break_i:
                break
    print(player_1, player_2)

    if not break_i:
        print(f'#{test_case} 0')