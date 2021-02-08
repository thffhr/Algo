# import sys
# sys.setrecursionlimit(100000)

def SafeZone(x, y):
    Visited[y][x] = 1
    for k in range(4):
        new_x = x + Xx[k]
        new_y = y + Yy[k]
        if 0 <= new_x < N and 0 <= new_y < N and not Visited[new_y][new_x] and not Check[new_y][new_x]:
            SafeZone(new_x, new_y)

N = int(input())
Check = [[0]*N for __ in range(N)]
H_Info = []
for _ in range(N):
    H_Info.append(list(map(int, input().split(' '))))

num_lst = [0]
for i in range(N):
    for j in range(N):
        if H_Info[i][j] not in num_lst:
            num_lst.append(H_Info[i][j])

Xx = [0 , 1, 0, -1]
Yy = [1, 0, -1, 0]
max_safe = 0
num_lst.sort()
for num in num_lst:
    for i in range(N):
        for j in range(N):
            if H_Info[i][j] <= num:
                Check[i][j] = 1
    Visited = [[0] * N for ___ in range(N)]
    cnt = 0
    for n in range(N):
        for m in range(N):
            if not Check[n][m] and not Visited[n][m]:
                SafeZone(m, n)
                cnt += 1
    if max_safe < cnt:
        max_safe = cnt

print(max_safe)