def find_set(x):
    while x != root[x]:
        x = root[x]
    return x

db = []
for _ in range(M):
    u, v, w = map(int, input().split())
    db.append((w,u,v))

root = [i for i in range(len(db)+1)]
cnt = 0
total = 0
for w, u, v in db:
    if find_set(u) != find_set(v):
        cnt += 1
        total += w
        root[find_set(v)] = find_set(u)
        if cnt == V:
            break
        