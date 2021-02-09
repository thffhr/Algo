def FindPath(x, y, j, i):
    global count
    if x == j and y == i:
        count += 1
        return
    Map[y][x] = 1
    for k in range(2):
        new_x = x + Xx[k]
        new_y = y + Yy[k]
        if x <= new_x <= j and y <= new_y <= i and not Map[new_y][new_x]:
            FindPath(new_x, new_y, j, i)
            Map[new_y][new_x] = 0


N, M, O = map(int, input().split(' '))
Map = [[0]*M for _ in range(N)]
Xx = [1, 0]
Yy = [0, 1]
Ocnt = Ox = Oy = count = cnt1 = cnt2 = 0
if O:
    for a in range(N):
        for b in range(M):
            Ocnt += 1
            if Ocnt == O:
                Ox = b
                Oy = a
                break
    FindPath(0, 0, Ox, Oy)
    cnt1 = count
    count = 0
FindPath(Ox, Oy, M-1, N-1)
cnt2 = count
count = 0

if cnt1:
    aws = cnt1*cnt2
else:
    aws = cnt2

print(aws)

