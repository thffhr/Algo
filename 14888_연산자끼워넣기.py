def cal(lst):
    aws = Numbers[0]
    for c in range(1, N):
        if lst[c - 1] == 0:
            aws += Numbers[c]
        elif lst[c - 1] == 1:
            aws -= Numbers[c]
        elif lst[c - 1] == 2:
            aws *= Numbers[c]
        else:
            if aws < 0:
                aws = -1 * (abs(aws) // Numbers[c])
            else:
                aws //= Numbers[c]
    return aws


def findM(lst, len_cnt):
    global max_num, min_num
    if len(lst) == N-1:
        aws = cal(lst)
        if aws > max_num:
            max_num = aws
        if aws < min_num:
            min_num = aws
        return
    for f in range(len(Calculators)):
        select_num = Calculators.pop(f)
        lst.append(select_num)
        findM(lst, f + 1)
        restore_num = lst.pop()
        Calculators.insert(f, restore_num)


N = int(input())
Numbers = list(map(int, input().split(' ')))
Cal_Info = list(map(int, input().split(' ')))
max_num = -1000000000
min_num = 1000000000
Calculators = []

for i in range(4):
    while Cal_Info[i] > 0:
        Cal_Info[i] -= 1
        Calculators.append(i)

findM([], 0)

print(max_num)
print(min_num)