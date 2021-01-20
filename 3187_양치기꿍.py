import copy

def CountVnK(x, y):
    global countK, countV, saveK, saveV
    if Field[y][x] == '#' or Visited[y][x]:
        return
    xx = [0, 0, -1, 1]
    yy = [-1, 1, 0, 0]
    for m in range(4):
        newx = x + xx[m]
        newy = y + yy[m]
        if 0 < newx < C and 0 < newy < R:
            if Field[newy][newx] == 'k':
                countK += 1
            elif Field[newy][newx] == 'v':
                countV += 1
        Visited[newy][newx] = 1
        CountVnK(newy, newx)


R, C = map(int, input().split(' '))
Field = []
for r in range(R):
    row = input()
    RR = []
    for c in range(C):
        RR.append(row[c])
    Field.append(copy.deepcopy(RR))

# for __ in range(R):
#     print(Field[__])

Visited = [[0]*C for __ in range(R)]
saveK, saveV = 0, 0

for r in range(R):
    for c in range(C):
        if Field[r][c] != '#' and not Visited[r][c]:
            countK, countV = 0, 0
            if Field[r][c] == 'k':
                countK += 1
            elif Field[r][c] == 'v':
                countV += 1

            CountVnK(c, r)
            Visited[r][c] = 1
            if countK > countV:
                saveK += countK
            else:
                saveV += countV

print(saveK, saveV)

