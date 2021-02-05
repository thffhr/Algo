def FindArr(i, j, n, depth):
    if Check[i][j] == n:
        lst.append(Tile[i])
        for k in range(N):
            if Check[j][k]:
                FindArr(j, k, n, depth+1)
                break
    elif 0 <= j+1 < N:
        FindArr(i, j+1, n, depth)
    elif 0 <= i+1 < N:
        FindArr(i+1, j, n, depth)
    else:
        if depth >= 3: # 여기가 이상하다...
            lst.append(Tile[i])
        elif lst:
            lst.pop()
        return


N = int(input())
Tile = list(map(int, input().split(' ')))
Check = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j and Tile[j] - Tile[i] > 0:
            Check[i][j] = Tile[j] - Tile[i]

max_num = 0
for n in range(1, N):
    lst = []
    FindArr(0, 0, n, 1)
    num_sum = sum(lst)
    if max_num < num_sum:
        max_num = num_sum
print(max_num)
# for i in range(1, N):
#     for j in range(N):
#         if Tile[j] + i in Tile:


# max_sum = 0
# for i in range(1, N):
#     cnt = 0
#     Step = []
#     for j in range(1, N):
#         if Tile[j] - Tile[j-1] == i:
#             cnt += 1
#             if Tile[j] not in Step:
#                 Step.append(Tile[j])
#             if Tile[j-1] not in Step:
#                 Step.append(Tile[j-1])
#         elif cnt < 3:
#             cnt = 0
#             Step = []
#         elif cnt >= 3:
#             break
#     num_sum = sum(Step)
#     if max_sum < num_sum:
#         max_sum = num_sum
#
# print(max_sum)
