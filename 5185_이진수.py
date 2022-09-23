'''
3
4 47FE
5 79E12
8 41DA16CD

'''
tc = int(input())
Dic = {"A" : 10, "B":11, "C" :12, "D" :13, "E" :14, "F" : 15, "G": 16}
for test_case in range(1, tc+1):
    N, M = input().split()
    arr = []
    N = int(N)
    for _ in range(N):
        int_2 = [0, 0, 0, 0]
        if M[_] in Dic:
            number = Dic[M[_]]
        else:
            number = int(M[_])

        for i in range(4):
            if number >= 2**(3-i):
                number -= 2**(3-i)
                int_2[i] = 1

        arr.extend(int_2)
    print(f"#{test_case} {''.join(map(str,arr))}")