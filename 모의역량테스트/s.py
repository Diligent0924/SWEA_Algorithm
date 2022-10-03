def combination(root):
    if root == 3:
        print(temp)
        return
    else:
        for i in range(root, N):
            if visited[i]:
                continue
            else:
                visited[i] = 1
                temp.append(arr[i])
                combination(root+1)
                temp.remove(arr[i])
                visited[i] = 0

def permutation(root):
    global temp, visited
    if root == N:
        print(temp)
        return
    else:
        for i in range(N):
            if visited[i]:
                continue
            else:
                visited[i] = 1
                temp[root] = arr[i]
                permutation(root+1)
                visited[i] = 0

def subset():
    for i in range(1<<N):
        list_a = []
        for j in range(N):
            if i & (1<<j):
                list_a.append(arr[j])
        print(list_a)


arr = [1,2,3,4]
N = 4
subset()

visited = [0] * (N+1)
temp = [0] * N
permutation(0)

visited = [0] * (N+1)
temp = []
print('-----combination----')
combination(0)