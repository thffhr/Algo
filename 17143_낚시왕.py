R, C, M = map(int, input().split(' '))
Shark = [list(map(int, input().split(' '))) for _ in range(M)]
for mm in range(M):
    Shark[mm].append(1)
aws = 0
for c in range(1, C+1):
    idx = -1
    minR = R
    for m in range(len(Shark)):
        if Shark[m][1] == c and minR >= Shark[m][0] and Shark[m][5]:
            minR = Shark[m][0]
            idx = m
    if idx >= 0:
        aws += Shark[idx][4]
        Shark.pop(idx)
    for m in range(len(Shark)):
        if Shark[m][5]:
            if Shark[m][3] < 3:
                num = (R-1)*2
            else:
                num = (C-1)*2
            ms = Shark[m][2] // num
            while ms > 0:
                ms -= 1
                if Shark[m][3] == 1:
                    if Shark[m][0] <= 1:
                        Shark[m][0] += 1
                        Shark[m][3] = 2
                    else:
                        Shark[m][0] -= 1
                elif Shark[m][3] == 2:
                    if Shark[m][0] >= R:
                        Shark[m][0] -= 1
                        Shark[m][3] = 1
                    else:
                        Shark[m][0] += 1
                elif Shark[m][3] == 3:
                    if Shark[m][1] >= C:
                        Shark[m][1] -= 1
                        Shark[m][3] = 4
                    else:
                        Shark[m][1] += 1
                else:
                    if Shark[m][1] <= 1:
                        Shark[m][1] += 1
                        Shark[m][3] = 3
                    else:
                        Shark[m][1] -= 1

    for m1 in range(len(Shark)):
        Check_idx = [m1]
        Check_size = [Shark[m1][4]]
        for m2 in range(len(Shark)):
            if m1 != m2:
                if Shark[m1][0] == Shark[m2][0] and Shark[m1][1] == Shark[m2][1]:
                    Check_idx.append(m2)
                    Check_size.append(Shark[m2][4])
        Check_idx.pop(Check_size.index(max(Check_size)))
        for check in range(len(Check_idx)):
            Shark[Check_idx[check]][5] = 0
print(aws)
