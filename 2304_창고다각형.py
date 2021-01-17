max_L = max_H = max_idx = 0
min_L = 987654321
N = int(input())
Info = []
for _ in range(N):
    L, H = map(int, input().split())
    Info.append([L, H])
    if max_L < L:
        max_L = L
    if max_H < H:
        max_H = H
        max_idx = L
    if min_L > L:
        min_L = L

W = [0]*(max_L+1)
for idx in range(N):
    W[Info[idx][0]] = Info[idx][1]

max_left = 0
for i in range(min_L, max_idx):
    if max_left < W[i]:
        max_left = W[i]
    W[i] = max_left

max_right = 0
for j in range(max_L, max_idx, -1):
    if max_right < W[j]:
        max_right = W[j]
    W[j] = max_right

aws = 0
for add in range(len(W)):
    aws += W[add]

print(aws)