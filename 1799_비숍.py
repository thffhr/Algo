def Set(x, y, cnt):
    if 0 <= x < N and 0 <= y < N:
        for a in range(y):
            for b in range(x):
                Map[a][b] = 0
        for c in range(y, N):
            for d in range(x, N):
                Map[c][d] = 0
        for e in range(y, N):
            for f in range(x):
                if Map[e][f] < 0:
                    return
        for g in range(y):
            for h in range(x, N):
                if Map[g][h] < 0:
                    return
        Map[y][x] = -1
        Set()

N = int(input())
Map = []
max_cnt = 0
for i in range(N):
    Map.append(list(map(int, input().split(' '))))

