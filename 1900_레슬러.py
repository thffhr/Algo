N = int(input())
Player = []
for _ in range(N):
    Player.append(list(map(int, input().split(' '))))
max_num = 0
Count = []
for n1 in range(N):
    cnt = 0
    for n2 in range(N):
        P1 = Player[n1][0]+Player[n2][0]*Player[n1][1]
        P2 = Player[n2][0]+Player[n1][0]*Player[n2][1]
        if P1 > P2:
            cnt += 1
    Count.append(cnt)

for n in range(N):
    aws = Count.index(max(Count))
    print(aws + 1)
    Count[aws] = -1