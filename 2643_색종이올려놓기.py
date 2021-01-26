N = int(input())
Paper = []
max_w = max_h = idx = 0
for n in range(N):
    Len = list(map(int, input().split(' ')))
    Paper.append(Len)
    if max_w < Len[0] and max_h < Len[1]:
        max_w = Len[0]
        max_h = Len[0]
        idx = n
Paper.pop(idx)
count = 1
min_w = max_w
min_h = max_h
for i in range(N-1):
