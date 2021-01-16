def FindMax(start, end, num):
    # 채우기
    for n in range(start, end):
        W[n] = num
    # 왼/오 탐색

W = [0]*1000
max_L = max_H = max_HIdx = 0
min_L = 987654321
N = int(input())
for _ in range(N):
    L, H = map(int, input().split())
    W[L] = H
    if max_L < L:
        max_L = L
    if max_H < H:
        max_H = H
        max_HIdx = L
    if min_L > L:
        min_L = L

FindMax(max_HIdx, max_HIdx+1, max_H)








# N = int(input())
# Info = []
# max_L = max_H = 0
# for _ in range(N):
#     Info.append(list(map(int, input().split(' '))))
#     if max_L < Info[-1][0]:
#         max_L = Info[-1][0]
#     if max_H > Info[-1][1]:
#         max_H = Info[-1][1]
#
# Map = [[0]*(max_L+1) for __ in range(max_H)]
#
# # 기둥 그리기
# for n in range(N):
#     for m in range(Info[n][1]):
#         Map[m][Info[n][0]] = 1
#
# # 공간 채우기


