def FindBingo(Check):
    global Bingo
    # 가로 빙고 찾기
    cnt2 = 0
    for i in range(5):
        cnt1 = 0
        for j in range(5):
            if int(Check[i][j]):
                cnt1 += 1
        if cnt1 == 5:
            Bingo += 1
        if int(Check[i][i]):
            cnt2 += 1
    if cnt2 == 5:
        Bingo += 1
    return

Chulsu = [list(map(int, input().split())) for _ in range(5)]
MC = []
for _ in range(5):
    MC += list(map(int, input().split()))
Check = [[0] * 5 for _ in range(5)]
Bingo = k = result = 0

while Bingo < 3 and k < 25:
    Bingo = 0
    v_Check = []
    for n in range(5):
        for m in range(5):
            if MC[k] == Chulsu[n][m]:
                Check[n][m] = 1
                break
    for m in range(4, -1, -1):
        v = ''
        for n in range(5):
            v += str(Check[n][m])
        v_Check.append(v)

    FindBingo(Check)
    FindBingo(v_Check)
    if Bingo >= 3:
        result = k+1
        break
    k += 1

print(result)