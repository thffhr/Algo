def Check(x, y, lst):
    for v in range(1, N+1):
        for k in range(4):
            new_x = (Xx[k] * v) + x
            new_y = (Yy[k] * v) + y
            if 0 <= new_x < N and 0 <= new_y < N:
                if [new_y, new_x] in lst:
                    return False
    return True

def Set(depth, idx, lst, set_lst):
    global max_num
    if depth >= N:
        return
    for s in range(idx, len(lst)):
        if Check(lst[s][1], lst[s][0], set_lst):
            set_lst.append(lst[s])
            Set(depth + 1, s + 1, lst, set_lst)
            set_lst.pop()
    if max_num < len(set_lst):
        max_num = len(set_lst)
    return


# 왼위 오위 왼아 오아
Xx = [-1, 1, -1, 1]
Yy = [-1, -1, 1, 1]

N = int(input())
Map = []
Visited = []
for _ in range(N):
    Map.append(list(map(int, input().split(' '))))
    Visited.append([0]*N)

Black = []
White = []
for i in range(N):
    for j in range(N):
        if Map[i][j]:
            if (i + j)%2:
                White.append([i, j])
            else:
                Black.append([i, j])
        Map[i][j] = 0

max_num = 0
Set(0, 0, White, [])
w_max = max_num

max_num = 0
Set(0, 0, Black, [])
b_max = max_num

print(w_max+b_max)