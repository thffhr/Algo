import copy

def Danji(x, y):
    global cnt
    Visited[y][x] = 1
    Xx = [0, 1, 0, -1]
    Yy = [1, 0, -1, 0]
    for i in range(4):
        new_x = x + Xx[i]
        new_y = y + Yy[i]
        if 0 <= new_x < N and 0 <= new_y < N and Map[new_y][new_x] and not Visited[new_y][new_x]:
            Danji(new_x, new_y)
    cnt += 1
    return


N = int(input())
Map = []
Visited = [[0]*N for _ in range(N)]
for n in range(N):
    L = []
    line = input()
    for nn in range(N):
        L.append(int(line[nn]))
    Map.append(copy.deepcopy(L))

cnt = 0
CNT = []
for i in range(N):
    for j in range(N):
        if Map[i][j] and not Visited[i][j]:
            Danji(j, i)
            CNT.append(cnt)
            cnt = 0
CNT.sort()

print(len(CNT))
for c in range(len(CNT)):
    print(CNT[c])