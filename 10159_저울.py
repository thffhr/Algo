def Count(i, lst, hl, depth):
    if depth >= N:
        return
    for j in range(N):
        if hl == 0:
            if Relations[i][j] != 0 and (j + 1) not in lst:
                new_hl = Relations[i][j]
                lst.append(j+1)
                Count(j, lst, new_hl, depth + 1)
        else:
            if Relations[i][j] == hl and (j + 1) not in lst:
                lst.append(j + 1)
                Count(j, lst, hl, depth + 1)
    return len(lst)


N = int(input())
M = int(input())
Check = [[0]*N for _ in range(N)]
Aws = [0]*N
Relations = [[0]*N for _ in range(N)]
for __ in range(M):
    heavy, light = map(int, input().split(' '))
    Relations[heavy - 1][light - 1] = 1
    Relations[light - 1][heavy - 1] = -1

for n in range(N):
    Aws[n] = Count(n, [], 0, 0)

for a in range(N):
    print(N - 1 - Aws[a])