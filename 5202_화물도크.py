'''

3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24
'''

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        start, end = map(int, input().split())
        arr.append((start, end))
    arr.sort(key=lambda x: x[1])
    print(arr)

    count = 0
    E = 0

    for start, end in arr:
        if start >= E:
            count += 1
            E = end
    print(f"#{test_case} {count}")