G = [[0 for i in range(101)] for i in range(101)]
result = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):   #가로만큼
        for m in range(y1, y2):    #높이만큼
            if G[j][m] == 0:
                G[j][m] += 1
                result += 1
print(result)
