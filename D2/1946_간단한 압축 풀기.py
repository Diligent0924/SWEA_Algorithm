for i in range(1, int(input())+1):
    answer = ""
    b = int(input())
    print("#{0}".format(i))
    for j in range(1, b+1):
        c,d = map(str, input().split())
        answer += c * int(d)

    count = 0
    for i in answer:
        print(i, end="")
        count += 1
        if count == 10:
            print("")
            count = 0
    print()
