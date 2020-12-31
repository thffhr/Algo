N = int(input())
Class = [list(map(int, input().split())) for _ in range(N)]
Class_check = [[0]*N for _ in range(N)]
result = [0]*N

for i in range(5):
    for j in range(N):
        for k in range(j+1, N):
            if Class[j][i] == Class[k][i] and Class_check[j][k] == 0:
                Class_check[j][k] = 1
                Class_check[k][j] = 1

for i in range(N):
    cnt = 0
    for j in range(N):
        if Class_check[i][j]:
            cnt += 1
    result[i] = cnt
banjang = result.index(max(result)) + 1
print(banjang)

# N = int(input())
# Class = [list(map(int, input().split())) for _ in range(N)]
# Cnt_list = [0]*(N+1)
#
# for i in range(5):
#     for j in range(N):
#         if Cnt_list[j+1] == 0:
#             cnt = 0
#             Check_list = [0] * (N + 1)
#             for k in range(j+1, N):
#                 if Class[j][i] == Class[k][i]:
#                     cnt += 1
#                     Check_list[j+1] = True
#                     Check_list[k+1] = True
#             if cnt:
#                 for c in range(N+1):
#                     if Check_list[c]:
#                         Cnt_list[c] += cnt
#
# banjang = Cnt_list.index(max(Cnt_list))
# print(banjang)
