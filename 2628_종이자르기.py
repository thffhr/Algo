def maxNum(WH, cut_lst):
    last = 0
    max_len = 0
    for i in range(len(cut_lst)):
        if max_len < (cut_lst[i] - last):
            max_len = cut_lst[i] - last
        last = cut_lst[i]
    if max_len < (WH - last):
        max_len = WH - last
    return max_len

W, H = map(int, input().split(' '))
N = int(input())
cut_W = []
cut_H = []
for n in range(N):
    WH, LEN = map(int, input().split(' '))
    if WH:
        cut_W.append(LEN)
    else:
        cut_H.append(LEN)

cut_W.sort()
cut_H.sort()

awsW = maxNum(W, cut_W)
awsH = maxNum(H, cut_H)

print(awsW*awsH)