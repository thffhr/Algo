# def PaperCut(WH, input_lst, output_lst):
#     last_num = 0
#     for i in range(len(input_lst)):
#         if i:
#             output_lst.append(input_lst[i] - output_lst[-1])
#         else:
#             output_lst.append(input_lst[i])
#         last_num = input_lst[i]
#     output_lst.append(WH - last_num)

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

# W_list = []
# H_list = []

# PaperCut(W, cut_W, W_list)
# PaperCut(H, cut_H, H_list)
# aws = 0
# for m in range(len(W_list)):
#     for k in range(len(H_list)):
#         if W_list[m] * H_list[k] > aws:
#             aws = W_list[m] * H_list[k]
print(awsW*awsH)