'''
1. 8개의 숫자로 되어있는 것을 찾는다. 단, 가장 빠른 것을 찾는다.
2. 만약 8개의 숫자로 되어있는 것이 맞다면 확인해본다.

사각형 규칙
1. 비율에따라서 정해진다. 이 비율을 어떻게 확인해야하는지 모르겠음...
2. 세로 2000, 가로 500 이하라는 것을 잘 생각하고 풀어야할것 같다.
'''
Dic = {"0001101": 0, "0011001": 1, "0010011" : 2, "0111101" : 3, "0100011" : 4,'0110001':5,"0101111":6,"0111011":7,"0110111":8,"0001011":9}
for i in range(2, 35):
    zero = "000" * i + "11" * i + "0" *i + "1"*i
    one = "00" * i + "11" * i + "00" * i + "1" * i
    two = "00" * i + "1" * i + "00"*i + "11"*i
    three = "0" * i + "1111" * i + "0"*i + "1"*i
    four = "0" * i + "1" * i + "000"*i + "11" * i
    five = "0" * i + "11" * i + "000" * i + "1" * i
    six = "0" * i + "1" * i + "0" * i + "1111" * i
    seven = "0" * i + "111" * i + "0" * i + "11" * i
    eight = "0" * i + "11" * i + "0" * i + "111" * i
    nine = "000" * i + "1" * i + "0"* i + "11" * i
    Dic[zero], Dic[one],Dic[two],Dic[three],Dic[four],Dic[five],Dic[six],Dic[seven],Dic[eight],Dic[nine],= 0,1,2,3,4,5,6,7,8,9

T = int(input())
for test_case in range(1, T+1):
    sero, garo = map(int, input().split())
    scan_list = []
    for _ in range(sero):
        list_a = input().strip()
        list_a = list_a.strip("0")
        if list_a not in scan_list:
            scan_list.append(list_a)
    scan_list.pop(0)
    # print(scan_list)

    new_scan_list = []
    # 0이 두개 이상일 때 분리한다.
    for scan in scan_list:
        new_scan_list.append(scan)
        temp = ''
        for j in range(len(scan)):
            if scan[j] == "0" and scan[j+1] == "0":
                if temp not in new_scan_list and temp != '':
                    new_scan_list.append(temp)
                temp = ''
            elif scan[j] != 0:
                temp += scan[j]
        new_scan_list.append(temp)
    # 0이 한개일때도 분리해보자
    for scan in scan_list:
        temp = ''
        for j in range(len(scan)):
            if scan[j] == "0":
                if temp not in scan_list and temp != '':
                    new_scan_list.append(temp)
                temp = ''
            elif scan[j] != 0:
                temp += scan[j]
        new_scan_list.append(temp)


    new_scan_list = list(set(new_scan_list))
    bin_list = []
    for i in new_scan_list:
        print(i)
        int_2 = bin(int(i, 16))
        int_2 = int_2.replace('0b', '')
        trace = "0" * 100 + int_2
        bin_list.append(trace)

    # print(bin_list)
    result = []
    for bin_number in bin_list:
        for j in range(len(bin_number)):
            i = 0
            while i < 10:
                i += 1
                if bin_number[j:j+(7*i)] in Dic:
                    temp_2 = []
                    while bin_number[j:j+(7*i)] in Dic:
                        temp_2.append(Dic[bin_number[j:j+(7*i)]])
                        j += (7*i)

                    if len(temp_2) == 8 and temp_2 not in result:
                        result.append(temp_2)

    # print(result)

    final = False
    list_a = []
    for number_list in result:
        number = (number_list[0] + number_list[2] + number_list[4] + number_list[6])*3 + number_list[1] + number_list[3] + number_list[5] + number_list[7]
        if number % 10 == 0:
            final = True
            list_a.append(sum(number_list))

    if final:
        print(f'#{test_case} {sum(list_a)}')
    else:
        print(f'#{test_case} 0')

