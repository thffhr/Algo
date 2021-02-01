C, R = map(int, input().split(' '))
K = int(input())
Seat = [[0]*C for _ in range(R)]

Xx = [0, 1, 0, -1]
Yy = [1, 0, -1, 0]
i = x = y = 0
for k in range(K):
    Seat[y][x] = 1
    new_x = x + Xx[i % 4]
    new_y = y + Yy[i % 4]
    if 0 <= new_x < C and 0 <= new_y < R and not Seat[new_y][new_x]:
        pass
    else:
        i += 1
    x += Xx[i % 4]
    y += Yy[i % 4]
if K > C*R:
    print(0)
else:
    print(x - Xx[i % 4] + 1, y - Yy[i % 4] + 1)