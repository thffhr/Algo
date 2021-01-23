N = int(input())
Paper = []
X = 0
Y = 0
for n in range(N):
    lo = list(map(int, input().split(' ')))
    Paper.append(lo)
    if lo[0] > X:
        X = lo[0]
    if lo[1] > Y:
        Y = lo[1]

X += 11
Y += 11
Board = [[0]*(X) for _ in range(Y)]

for p in range(N):
    for x in range(Paper[p][0], 10+Paper[p][0]):
        for y in range(Paper[p][1], Paper[p][1]+10):
            Board[y][x] = 1

count = 0
for x in range(X):
    for y in range(Y):
        if Board[y][x] == 1:
            count += 1

print(count)