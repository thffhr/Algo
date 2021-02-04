def Count(n, m):
    Visited[n][m] = 1
    for check in range(4):
        new_y = n + Yy[check]
        new_x = m + Xx[check]
        if 0 <= new_y < N and 0 <= new_x < M and Arctic[new_y][new_x] and not Visited[new_y][new_x]:
            Count(n + Yy[check], m + Xx[check])

def Melt(n, m):
    cnt = 0
    for check in range(4):
        new_y = n + Yy[check]
        new_x = m + Xx[check]
        if 0 <= new_y < N and 0 <= new_x < M and not Arctic[new_y][new_x]:
            cnt += 1
    return cnt


N, M = map(int, input().split(' '))
Arctic = []
for _ in range(N):
    Arctic.append(list(map(int, input().split(' '))))
Xx = [0, 1, 0, -1]
Yy = [1, 0, -1, 0]

count = year = 0
while count >= 0:
    count = 0
    Visited = [[0] * M for __ in range(N)]
    for n1 in range(N):
        for m1 in range(M):
            if Arctic[n1][m1] and not Visited[n1][m1]:
                Count(n1, m1)
                count += 1
    if count >= 2:
        break
    for n2 in range(N):
        for m2 in range(M):
            if Arctic[n2][m2]:
                Arctic[n2][m2] -= Melt(n2, m2)
    year += 1

print(year)

