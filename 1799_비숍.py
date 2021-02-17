def Set(x, y, cnt, tf):
    if tf:

    else:
        pass



N = int(input())
Map = []
max_cnt = 0
for _ in range(N):
    Map.append(list(map(int, input().split(' '))))

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

for w in range(len(White)):
    Set(White[w][1], White[w][0], 0, True)

for b in range(len(Black)):
    Set(Black[b][1], White[w][0], 0, False)