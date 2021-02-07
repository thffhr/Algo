def move(i, j, tf):
    lst = []
    if tf:
        for n in range(4):
            lst.append(Q_Board[n][j])
    else:
        for n in range(4):
            lst.append(Q_Board[i][n])
    cnt = 0
    while lst[0] != A_Board[i][j]:
        num = lst.pop()
        lst.insert(0, num)
        cnt += 1
    return cnt


def checkout():
    for a in range(4):
        for b in range(4):
            if not Check[a][b] and A_Board[a][b] == Q_Board[a][b]:
                Check[a][b] = 1
                Q_Board[a][b] = A_Board[a][b]


A_Board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Q_Board = []
for _ in range(4):
    Q_Board.append(list(map(int, input().split(' '))))
Check = [[0]*4 for __ in range(4)]
checkout()

Aws = []
for i in range(4):
    for j in range(4):
        if not Check[i][j]:
            tf = 0
            ij = i
            if 1 in Check[i]:
                tf = 1
                ij = j
            count = move(i, j, tf)
            Aws.append(str(tf + 1) + ' ' + str(ij + 1) + ' ' + str(count))
            checkout()
            # for o in range(4):
            #     print(Check[o])



print(len(Aws))
for w in range(len(Aws)):
    print(Aws[w])



