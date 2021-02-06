def FindArr(i, j):
    m = 0
    arr = []
    for t in range(j, N):
        if Tile[j]+m == Tile[t]:
            arr.append(Tile[t])
            m += i
    if len(arr) >= 3:
        return arr
    else:
        return []


N = int(input())
Tile = list(map(int, input().split(' ')))
max_sum = num_sum = 0
for i in range(N):
    for j in range(N):
        aws = FindArr(i, j)
        if aws:
            num_sum = sum(aws)
        if max_sum < num_sum:
            max_sum = num_sum
print(max_sum)


# def FindArr(i, j, n, depth):
#     for k in range(j, N):
#         if Check[i][k] == n:
#             lst.append(Tile[i])
#             FindArr(k, k, n, depth+1)
#             break
#     FindArr(i+1, i+1, n, depth)
#     if depth >= 3:
#         lst.append(Tile[i])
#     if 1 <= len(lst) < 3:
#         lst.pop()
#     return
#
# # def FindArr(i, j, n, depth):
# #     if Check[i][j] == n:
# #         lst.append(Tile[i])
# #         for k in range(N):
# #             if Check[j][k]:
# #                 FindArr(j, k, n, depth+1)
# #                 break
# #     elif 0 <= j+1 < N:
# #         FindArr(i, j+1, n, depth)
# #     elif 0 <= i+1 < N:
# #         FindArr(i+1, j, n, depth)
# #     else:
# #         if depth >= 3: # 여기가 이상하다...
# #             lst.append(Tile[i])
# #         elif lst:
# #             lst.pop()
# #         return
#
#
# N = int(input())
# Tile = list(map(int, input().split(' ')))
# Check = [[0]*N for _ in range(N)]
#
# for i in range(N):
#     for j in range(N):
#         if i != j and Tile[j] - Tile[i] > 0:
#             Check[i][j] = Tile[j] - Tile[i]
#
# max_num = 0
# for n in range(1, N):
#     lst = []
#     FindArr(0, 0, n, 1)
#     num_sum = sum(lst)
#     if max_num < num_sum:
#         max_num = num_sum
# print(max_num)
#
