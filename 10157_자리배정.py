def FindXY(x, y, n, aws):
    if n == 0:
        aws = str(x) + ' ' + str(y)
        return
    if aws == '':
        Seat[y][x] = 1
        Xx = [0, 1, 0, -1]
        Yy = [1, 0, -1, 0]
        for i in range(4):
            new_x = x + Xx[i]
            new_y = y + Yy[i]
            if 0 <= new_x < C and 0 <= new_y < R and not Seat[new_y][new_x]:
                FindXY(new_x, new_y, n-1, aws)
    else:
        return

C, R = map(int, input().split(' '))
K = int(input())
Seat = [[0]*C for _ in range(R)]
aws = ''

FindXY(0, 0, K, aws)

if aws == '':
    print(0)
else:
    print(aws)
